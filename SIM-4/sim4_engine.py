#!/usr/bin/env python3
"""
SIM-4: Malaysia Doctor Shortage — Environment Reform (Fix Retention & Working Conditions)
Standalone script using ONLY Python stdlib + asyncio.

Domain: malaysia_health_workforce
Rounds: 8 (2026–2030, 6 months per round)
Agents: 30 stakeholder archetypes
Model: gpt-oss:120b-cloud (via Ollama gateway, OpenAI-compatible API)

Policy premise: Intake stays flat at 4,820. All effort goes to making the profession
attractive and sustainable. Massive permanent post expansion (+10%/year). Contract
system abolished by 2032. Salary +25% by 2030. Full Health Services Commission by
2028. Working conditions transformed (3-month notice, rural incentives, workload caps).

Outputs:
- sim4_log.jsonl          — per-round agent actions
- sim4_state.json         — quantitative state trajectory
- sim4_personas.json      — agent personas for post-sim interviews
- sim4_report.md          — structured markdown report
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import random
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
MODEL_NAME = "gpt-oss:120b-cloud"
BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"
MAX_CONCURRENT = 2
ROUNDS = 8
AGENTS_COUNT = 30
SEED = 42

OUT_DIR = Path("/root/projects/mas-2026-02/SIM-4")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Domain action space
# ---------------------------------------------------------------------------
ACTIONS = [
    "INCREASE_INTAKE", "DECREASE_INTAKE", "MAINTAIN_INTAKE",
    "CREATE_PERMANENT_POSTS", "EXPAND_CONTRACT_SYSTEM", "CONVERT_CONTRACT_TO_PERMANENT",
    "RAISE_SALARIES", "FREEZE_SALARIES", "IMPROVE_WORKING_CONDITIONS", "IGNORE_CONDITIONS",
    "ESTABLISH_HEALTH_SERVICES_COMMISSION", "STREAMLINE_REGISTRATION",
    "EXPAND_PRIVATE_PARTNERSHIP", "DEPLOY_TO_RURAL",
    "PURSUE_SPECIALIZATION", "LEAVE_FOR_PRIVATE", "EMIGRATE", "RETURN_FROM_OVERSEAS",
    "COMPLAIN_TO_MINISTRY", "ORGANISE_PROTEST", "PUBLISH_RESEARCH",
    "SUPPORT_POLICY", "OPPOSE_POLICY", "IGNORE",
]

# ---------------------------------------------------------------------------
# Agent archetypes for Malaysia health workforce
# ---------------------------------------------------------------------------
ARCHETYPES: List[Dict[str, Any]] = [
    {"role": "medical_student", "name": "Ahmad bin Hassan", "age": 22, "stance": "Anxious about job prospects and contract system. Still committed to medicine but exploring overseas options after graduation.", "influence": 3, "reaction_speed": "medium"},
    {"role": "medical_student", "name": "Li Wei Ling", "age": 23, "stance": "Top of class. Applying for UK specialist training after housemanship. Views Malaysian public system as limiting.", "influence": 4, "reaction_speed": "fast"},
    {"role": "medical_student", "name": "Priya Rajendran", "age": 21, "stance": "Rural origin. Wants to return to serve kampung but fears no permanent post. Considering MOH scholarship bond.", "influence": 3, "reaction_speed": "medium"},
    {"role": "house_officer", "name": "Dr Syed Al-Farabi", "age": 25, "stance": "Burned out after 3 months. 80-hour weeks, no mentorship. Already applying to Singapore hospitals.", "influence": 4, "reaction_speed": "fast"},
    {"role": "house_officer", "name": "Dr Nurul Ain", "age": 24, "stance": "Determined to complete housemanship despite bullying culture. Hopes for permanent post but uncertainty is crushing.", "influence": 3, "reaction_speed": "medium"},
    {"role": "house_officer", "name": "Dr Arjun Krishnan", "age": 25, "stance": "Frustrated by 8-month wait for housemanship post after graduation. Lost critical skills during gap. Now considering private GP path.", "influence": 3, "reaction_speed": "medium"},
    {"role": "medical_officer", "name": "Dr Lim Kah Wai", "age": 28, "stance": "5-year contract with no conversion path. Specialization blocked. Preparing emigration papers for Australia.", "influence": 5, "reaction_speed": "fast"},
    {"role": "medical_officer", "name": "Dr Amirah Sufya", "age": 29, "stance": "Accepted rural posting in Kelantan. Better rural allowance but isolation is severe. Considering transfer request.", "influence": 4, "reaction_speed": "medium"},
    {"role": "medical_officer", "name": "Dr Ravi Chandran", "age": 30, "stance": "Serving in busy district hospital. Sees system failures daily. Active in MMA WhatsApp groups advocating for reform.", "influence": 6, "reaction_speed": "fast"},
    {"role": "medical_officer", "name": "Dr Farah Nabila", "age": 27, "stance": "Recently married, planning children. Contract uncertainty means no maternity security. Looking at private hospital HR policies.", "influence": 4, "reaction_speed": "medium"},
    {"role": "medical_officer", "name": "Dr Wong Mei Fong", "age": 32, "stance": "Veteran MO. Survived multiple epidemics. Loyal to public service but dignity eroded by frozen allowances and budget cuts.", "influence": 5, "reaction_speed": "slow"},
    {"role": "specialist", "name": "Dr Prof. Zainal Abidin", "age": 48, "stance": "Head of department. Watching talent leave daily. Submitted memo to DG on retention crisis. Skeptical government will act.", "influence": 8, "reaction_speed": "medium"},
    {"role": "specialist", "name": "Dr Susan Ong", "age": 45, "stance": "Pathologist. Double workload since 3 colleagues emigrated. Considering private lab consultancy to supplement income.", "influence": 6, "reaction_speed": "medium"},
    {"role": "specialist", "name": "Dr Hafiz Rahman", "age": 42, "stance": "Orthopaedic surgeon. Recruited by Singapore chain with 3x salary. Giving MOH until December to counter-offer.", "influence": 7, "reaction_speed": "fast"},
    {"role": "moh_admin", "name": "Encik Rahimudin", "age": 52, "stance": "MOH HR director. Knows the numbers are dire. Cannot create posts without JPA approval. Treasury keeps reducing budget.", "influence": 7, "reaction_speed": "slow"},
    {"role": "moh_admin", "name": "Puan Siti Norhayati", "age": 45, "stance": "MOH planning division. Frustrated by MOHE not aligning intake to workforce needs. Proposed data-sharing system rejected.", "influence": 6, "reaction_speed": "medium"},
    {"role": "jpa_admin", "name": "Tuan Haji Ismail", "age": 55, "stance": "JPA senior director. Bound by civil service rules and post ceilings. Health is not the only sector screaming for posts.", "influence": 8, "reaction_speed": "slow"},
    {"role": "mohe_admin", "name": "Dr Aisyah Kamal", "age": 50, "stance": "MOHE accreditation director. Defends medical school quality. Points to international accreditation. Avoids intake discussions.", "influence": 5, "reaction_speed": "medium"},
    {"role": "private_operator", "name": "Mr Tan Chee Keong", "age": 58, "stance": "CEO of private hospital chain. Poaching MOH specialists aggressively. Offers permanent posts + research funding + flexible hours.", "influence": 7, "reaction_speed": "medium"},
    {"role": "private_operator", "name": "Mr Dinesh Velu", "age": 44, "stance": "Private clinic network owner. Hiring fresh graduates as GPs with minimal supervision. Profitable but worried about competency.", "influence": 5, "reaction_speed": "fast"},
    {"role": "mma_advocate", "name": "Dr Kamarul Ariffin", "age": 38, "stance": "MMA president. Campaigning for Health Services Commission. Organized CodeBlue letter campaign. Media-savvy and relentless.", "influence": 7, "reaction_speed": "fast"},
    {"role": "mma_advocate", "name": "Dr Sarah Abdullah", "age": 35, "stance": "MMA youth wing leader. Uses TikTok to expose junior doctor conditions. Went viral multiple times. Government sees her as threat.", "influence": 6, "reaction_speed": "fast"},
    {"role": "rural_staff", "name": "Dr Rosmah Jali", "age": 33, "stance": "KK serving 5,000 patients with 2 doctors. No specialist referral for 200km. Treating everything from dengue to depression.", "influence": 4, "reaction_speed": "medium"},
    {"role": "rural_staff", "name": "Mr Rajesh Nair", "age": 29, "stance": "Medical assistant in Sabah interior. Does doctor work without doctor title. No advancement pathway. Considering nursing in Australia.", "influence": 3, "reaction_speed": "medium"},
    {"role": "urban_patient", "name": "Mdm Chong Siew Lian", "age": 62, "stance": "Hypertension + diabetes. Specialist appointment took 6 months. Considering private but pension cannot cover.", "influence": 3, "reaction_speed": "slow"},
    {"role": "urban_patient", "name": "Mr Khairul Anwar", "age": 45, "stance": "Father of 3. Took son to GH emergency — 8-hour wait. Now pays for private insurance he can barely afford.", "influence": 4, "reaction_speed": "fast"},
    {"role": "rural_patient", "name": "Makcik Rokiah", "age": 71, "stance": "Lives in Pahang interior. Travel 3 hours to nearest clinic. No transport. Depends on unlicensed bomoh for chronic pain.", "influence": 2, "reaction_speed": "slow"},
    {"role": "treasury", "name": "Encik Azman Hakim", "age": 50, "stance": "Treasury undersecretary. Mandated to reduce fiscal deficit. Health cuts are painful but necessary. Suggests privatization.", "influence": 9, "reaction_speed": "slow"},
    {"role": "treasury", "name": "Puan Lina Mohd", "age": 42, "stance": "Treasury health desk. Secretly sympathetic to MOH but powerless against macro targets. Wants evidence-based workforce planning.", "influence": 5, "reaction_speed": "medium"},
    {"role": "health_dg", "name": "DG Mahathar Abd Wahab", "age": 58, "stance": "Advocating for end-to-end workforce planning and unified Health Services Commission. Pushing for competency-based training. Needs political backing.", "influence": 9, "reaction_speed": "medium"},
]

# ---------------------------------------------------------------------------
# Simulation prompt template
# ---------------------------------------------------------------------------
SIM_PROMPT_TEMPLATE = """\
You are a simulation agent representing a stakeholder in the Malaysian healthcare workforce system.

TEMPORAL CONTEXT: It is {year}. You are participating in a policy simulation about Malaysia's doctor shortage crisis.
Base your decision ONLY on your persona, the current environment state, recent events, and your simulation memories.

Your role: {role}
Name: {name}, Age: {age}
Persona stance: {stance}
Influence: {influence}/10 | Reaction speed: {reaction_speed}

Current healthcare system state (quantitative):
- Annual medical graduates: {graduates}
- Available housemanship posts: {housemanship_posts}
- Permanent civil service posts: {permanent_posts}
- Contract doctors in service: {contract_doctors}
- Doctors emigrating per year: {brain_drain}
- Overseas doctors returning per year: {returnees}
- Doctor-to-population ratio: {doc_ratio}
- Public hospital overcrowding index (0-100): {overcrowding}
- Average doctor workload: {workload} hours/week
- Klinik Kesihatan waiting time: {kk_wait} days
- Specialist appointment wait: {specialist_wait} weeks
- Medical student interest index (applicants per seat): {interest}
- Health budget (% of GDP): {health_budget}
- Public salary vs private ratio: {salary_ratio}
- Retention rate (% MOs staying >3 years): {retention}

Recent events / timeline:
{timeline}

Recent memories from previous rounds:
{memories_text}

Available actions:
{actions_list}

Respond with STRICT JSON only (no markdown, no commentary):
{{
  "action": "<ACTION>",
  "content": "<brief explanation of your reasoning in 1-2 sentences, Malay/English mixed is acceptable as spoken in Malaysia>",
  "target_agent": "<name of another agent you are reacting to, or null>",
  "opinion_shift": [dx1, dx2, dx3, dx4, dx5, dx6]
}}

Opinion_shift dimensions (range [-0.2, 0.2]):
[optimism_about_system, trust_in_government, advocacy_for_reform, frustration_level, career_security, patient_care_priority]
"""

# ---------------------------------------------------------------------------
# State variables (initial values for 2026)
# ---------------------------------------------------------------------------
STATE_0 = {
    "year": 2026.0,
    "graduates": 4820,
    "housemanship_posts": 3500,
    "permanent_posts": 24000,
    "contract_doctors": 18000,
    "brain_drain": 1200,
    "returnees": 80,
    "doc_ratio": 2.3,
    "overcrowding": 78,
    "workload": 72,
    "kk_wait": 14,
    "specialist_wait": 12,
    "interest": 1.8,
    "health_budget": 2.1,
    "salary_ratio": 0.45,
    "retention": 58,
}

# ---------------------------------------------------------------------------
# State update formulas (SIM-4: Environment Reform — fix retention, flat intake)
# ---------------------------------------------------------------------------
def update_state(state: Dict[str, float], round_num: int) -> Dict[str, float]:
    s = dict(state)
    s["year"] = 2026.0 + round_num * 0.5

    # Intake: FLAT at 4,820 (no increase)
    s["graduates"] = 4820

    # Housemanship posts: +4%/year (targeted expansion to clear backlog)
    s["housemanship_posts"] = int(s["housemanship_posts"] * 1.02)

    # Permanent posts: +5%/round = +10%/year (massive conversion drive)
    prev_permanent = s["permanent_posts"]
    s["permanent_posts"] = int(s["permanent_posts"] * 1.05)
    new_permanent = s["permanent_posts"] - prev_permanent

    # Contract system: aggressively abolished. Convert 3x new permanent rate
    conversion = int(new_permanent * 3.0)
    s["contract_doctors"] = max(0, s["contract_doctors"] - conversion)

    # Brain drain: dramatically improves (better conditions, certainty)
    s["brain_drain"] = max(400, 1200 - round_num * 100)

    # Returnees: strong pull factor (Malaysia becomes attractive)
    s["returnees"] = min(300, 80 + round_num * 25)

    # Doc ratio: improves from returnees + retention, not intake
    s["doc_ratio"] = min(2.6, 2.3 + round_num * 0.025)

    # Overcrowding: eases as workload drops + returnees join
    s["overcrowding"] = max(55, 78 - round_num * 3)

    # Workload: improves dramatically with workload caps, more staff
    s["workload"] = max(52, 72 - round_num * 2.5)

    # Waiting times: improve significantly
    s["kk_wait"] = max(5, 14 - round_num * 1.1)
    s["specialist_wait"] = max(4, 12 - round_num * 1.0)

    # Interest: rises as medicine becomes attractive again
    s["interest"] = min(2.5, 1.8 + round_num * 0.08)

    # Budget: +2.5%/round = +5% real growth (protected + reprioritized)
    s["health_budget"] = min(2.5, 2.1 + round_num * 0.025)

    # Salary ratio: +25% by 2030 (~+3.1%/round)
    s["salary_ratio"] = min(0.58, 0.45 + round_num * 0.02)

    # Retention: dramatic improvement
    s["retention"] = min(78, 58 + round_num * 2.5)

    return s

# ---------------------------------------------------------------------------
# Event timeline
# ---------------------------------------------------------------------------
EVENTS: Dict[int, str] = {
    1: "Budget 2027: Health budget receives +5% real increase. Treasury accepts evidence that retention saves more than replacement costs. On-call allowance reindexing pilot announced.",
    2: "Government launches 'Contract Abolition Roadmap': 5,000 contract doctors converted to permanent in Wave 1. 3-month deployment notice policy implemented. MMA declares conditional support.",
    3: "Health Services Commission Bill tabled in Parliament. Unifies MOHE-JPA-MOH governance. Opposition supports. Medical student applications rise 15%.",
    4: "Election 2028: Health workforce reform becomes bipartisan consensus. No party campaigns against HSC or contract abolition. Private sector hiring slows as public becomes competitive.",
    5: "Post-election: New government accelerates contract abolition. Salary adjustment (+25% by 2030) passes cabinet. Hazard pay restored for infectious disease duty.",
    6: "World Bank report: Malaysia 'most improved' in health workforce retention in Southeast Asia. 180 doctors returned from UK/Australia/Singapore in past 12 months.",
    7: "Singapore hospitals report difficulty recruiting Malaysian doctors — public sector salaries now competitive, working conditions better. Malaysian doctors cite 'dignity restored'.",
}

# ---------------------------------------------------------------------------
# Async LLM client using stdlib urllib
# ---------------------------------------------------------------------------
async def llm_chat(messages: List[Dict[str, str]], temperature: float = 0.7, max_tokens: int = 2048) -> str:
    url = f"{BASE_URL}/chat/completions"
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    def _call():
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = json.loads(resp.read().decode("utf-8"))
                choice = body["choices"][0]["message"]
                content = choice.get("content") or ""
                if not content.strip():
                    content = choice.get("reasoning_content") or choice.get("reasoning") or ""
                return content
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")[:500]
            logger.error("HTTP %s: %s", e.code, err_body)
            return '{"action":"IGNORE","content":"HTTP error","target_agent":null,"opinion_shift":[0,0,0,0,0,0]}'
        except Exception as exc:
            logger.error("LLM request failed: %s", exc)
            return '{"action":"IGNORE","content":"Request failed","target_agent":null,"opinion_shift":[0,0,0,0,0,0]}'

    return await asyncio.to_thread(_call)

# ---------------------------------------------------------------------------
# Agent representation
# ---------------------------------------------------------------------------
class Agent:
    def __init__(self, idx: int, archetype: Dict[str, Any]):
        self.idx = idx
        self.agent_id = f"agent_{idx:04d}"
        self.role = archetype["role"]
        self.name = archetype["name"]
        self.age = archetype["age"]
        self.stance = archetype["stance"]
        self.influence = archetype["influence"]
        self.reaction_speed = archetype["reaction_speed"]
        self.opinion = [0.0] * 6
        self.memories: List[str] = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "role": self.role,
            "name": self.name,
            "age": self.age,
            "stance": self.stance,
            "influence": self.influence,
            "reaction_speed": self.reaction_speed,
            "opinion": self.opinion,
            "memories": self.memories,
        }

# ---------------------------------------------------------------------------
# Prompt builder
# ---------------------------------------------------------------------------
def build_prompt(agent: Agent, state: Dict[str, float], round_num: int, timeline: str, observations: str = "") -> str:
    memories_text = "\n".join(f"- {m}" for m in agent.memories[-5:]) if agent.memories else "(none)"
    event_text = EVENTS.get(round_num, "No major external events this round.")
    full_timeline = f"{event_text}\n{timeline}\n{observations}".strip()

    return SIM_PROMPT_TEMPLATE.format(
        year=int(state["year"]),
        role=agent.role,
        name=agent.name,
        age=agent.age,
        stance=agent.stance,
        influence=agent.influence,
        reaction_speed=agent.reaction_speed,
        graduates=int(state["graduates"]),
        housemanship_posts=int(state["housemanship_posts"]),
        permanent_posts=int(state["permanent_posts"]),
        contract_doctors=int(state["contract_doctors"]),
        brain_drain=int(state["brain_drain"]),
        returnees=int(state["returnees"]),
        doc_ratio=round(state["doc_ratio"], 2),
        overcrowding=int(state["overcrowding"]),
        workload=int(state["workload"]),
        kk_wait=int(state["kk_wait"]),
        specialist_wait=int(state["specialist_wait"]),
        interest=round(state["interest"], 2),
        health_budget=round(state["health_budget"], 2),
        salary_ratio=round(state["salary_ratio"], 2),
        retention=int(state["retention"]),
        timeline=full_timeline,
        memories_text=memories_text,
        actions_list=", ".join(ACTIONS),
    )

# ---------------------------------------------------------------------------
# JSON parser
# ---------------------------------------------------------------------------
def parse_action(raw: str) -> Dict[str, Any]:
    text = raw.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            action = parsed.get("action", "IGNORE")
            if action not in ACTIONS:
                action = "IGNORE"
            content = str(parsed.get("content", ""))[:500]
            target = parsed.get("target_agent") or None
            shift = parsed.get("opinion_shift", [0.0]*6)
            if not isinstance(shift, list) or len(shift) != 6:
                shift = [0.0]*6
            shift = [max(-0.2, min(0.2, float(v))) for v in shift[:6]]
            return {"action": action, "content": content, "target_agent": target, "opinion_shift": shift}
    except json.JSONDecodeError:
        pass
    return {"action": "IGNORE", "content": f"Parse error: {raw[:200]}", "target_agent": None, "opinion_shift": [0.0]*6}

# ---------------------------------------------------------------------------
# Single agent turn
# ---------------------------------------------------------------------------
async def agent_turn(agent: Agent, state: Dict[str, float], round_num: int, timeline: str, semaphore: asyncio.Semaphore) -> Dict[str, Any]:
    async with semaphore:
        prompt = build_prompt(agent, state, round_num, timeline)
        messages = [
            {"role": "system", "content": "You are a simulation agent. Respond ONLY with valid JSON."},
            {"role": "user", "content": prompt},
        ]
        raw = await llm_chat(messages, temperature=0.7, max_tokens=2048)
        result = parse_action(raw)

        for i, delta in enumerate(result["opinion_shift"]):
            agent.opinion[i] = round(max(-1.0, min(1.0, agent.opinion[i] + delta)), 3)

        memory = f"Round {round_num}: {result['action']} — {result['content'][:200]}"
        agent.memories.append(memory)

        return {
            "round": round_num,
            "agent_id": agent.agent_id,
            "role": agent.role,
            "name": agent.name,
            "action": result["action"],
            "content": result["content"],
            "target_agent": result["target_agent"],
            "opinion_shift": result["opinion_shift"],
            "opinion": agent.opinion.copy(),
        }

# ---------------------------------------------------------------------------
# Run simulation
# ---------------------------------------------------------------------------
async def run_simulation(agents: List[Agent]) -> tuple[List[Dict], List[Dict]]:
    state = dict(STATE_0)
    log_entries: List[Dict] = []
    state_trajectory: List[Dict] = []
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    for r in range(1, ROUNDS + 1):
        logger.info("=== ROUND %d / %d (Year %.1f) ===", r, ROUNDS, state["year"])
        state = update_state(state, r)
        state_trajectory.append(dict(state, round=r))

        timeline = f"Environment reform underway: retention {state['retention']}%, contracts {state['contract_doctors']:.0f}, salaries rising."
        if r > 1:
            prev_actions = [e for e in log_entries if e["round"] == r - 1]
            action_counts = {}
            for e in prev_actions:
                action_counts[e["action"]] = action_counts.get(e["action"], 0) + 1
            top = sorted(action_counts.items(), key=lambda x: x[1], reverse=True)[:3]
            timeline = "Last round prominent actions: " + ", ".join(f"{a}({c})" for a, c in top)

        tasks = [agent_turn(a, state, r, timeline, semaphore) for a in agents]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for res in results:
            if isinstance(res, Exception):
                logger.error("Agent exception: %s", res)
                continue
            log_entries.append(res)
            print(f"  [{res['round']:02d}] {res['name'][:25]:25s} -> {res['action']}")

        checkpoint = {"round": r, "state": state, "entries": [e for e in log_entries if e["round"] == r]}
        (OUT_DIR / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2, ensure_ascii=False), encoding="utf-8")

    return log_entries, state_trajectory

# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_report(agents: List[Agent], log_entries: List[Dict], state_trajectory: List[Dict]) -> str:
    lines = [
        "# SIM-4 Report: Malaysia Doctor Shortage — Environment Reform (Fix Retention & Working Conditions)",
        "",
        f"**Simulation date:** {datetime.now().isoformat()}  ",
        f"**Model:** {MODEL_NAME}  ",
        f"**Agents:** {len(agents)} | **Rounds:** {ROUNDS} (6 months/round = 4 years: 2026-2030)  ",
        "**Policy premise:** Intake stays flat at 4,820. All effort on retention: +10%/year permanent posts, contract abolition, salary +25%, HSC by 2028, workload caps.",
        "",
        "---",
        "",
        "## 1. Quantitative State Trajectory",
        "",
        "| Round | Year | Graduates | Posts (HO) | Perm. Posts | Contract | Brain Drain | Returnees | Doc/1k | Overcrowding | Workload hrs | KK Wait | Specialist Wait | Interest | Budget %GDP | Salary Ratio | Retention % |",
        "|-------|------|-----------|------------|-------------|----------|-------------|-----------|--------|--------------|--------------|---------|----------------|----------|-----------|--------------|-------------|",
    ]
    for s in state_trajectory:
        lines.append(
            f"| {s['round']} | {s['year']:.1f} | {s['graduates']} | {s['housemanship_posts']:.0f} | "
            f"{s['permanent_posts']:.0f} | {s['contract_doctors']:.0f} | {s['brain_drain']:.0f} | "
            f"{s['returnees']:.0f} | {s['doc_ratio']:.2f} | {s['overcrowding']:.0f} | {s['workload']:.0f} | "
            f"{s['kk_wait']:.0f} | {s['specialist_wait']:.0f} | {s['interest']:.2f} | "
            f"{s['health_budget']:.2f} | {s['salary_ratio']:.2f} | {s['retention']:.0f} |"
        )

    lines.extend(["", "### Key Trends", ""])
    s0 = state_trajectory[0]
    s_last = state_trajectory[-1]
    lines.append(f"- **Graduate intake:** {s0['graduates']} -> {s_last['graduates']} (FLAT — no increase)")
    lines.append(f"- **Housemanship posts:** {s0['housemanship_posts']:.0f} -> {s_last['housemanship_posts']:.0f} (modest expansion)")
    lines.append(f"- **Permanent posts:** {s0['permanent_posts']:.0f} -> {s_last['permanent_posts']:.0f} (major expansion +10%/year)")
    lines.append(f"- **Contract doctors:** {s0['contract_doctors']:.0f} -> {s_last['contract_doctors']:.0f} (abolished)")
    lines.append(f"- **Doctor-to-population ratio:** {s0['doc_ratio']:.2f} -> {s_last['doc_ratio']:.2f} (improving via retention)")
    lines.append(f"- **Public hospital overcrowding:** {s0['overcrowding']:.0f} -> {s_last['overcrowding']:.0f} (easing)")
    lines.append(f"- **Average doctor workload:** {s0['workload']:.0f} -> {s_last['workload']:.0f} hours/week (dramatic improvement)")
    lines.append(f"- **Brain drain:** {s0['brain_drain']:.0f} -> {s_last['brain_drain']:.0f} doctors/year (halved)")
    lines.append(f"- **Overseas returnees:** {s0['returnees']:.0f} -> {s_last['returnees']:.0f} doctors/year (tripled)")
    lines.append(f"- **Medical student interest:** {s0['interest']:.2f} -> {s_last['interest']:.2f} (rising)")
    lines.append(f"- **Retention:** {s0['retention']:.0f}% -> {s_last['retention']:.0f}% (dramatic improvement)")
    lines.append("")

    lines.extend(["## 2. Agent Action Distribution", ""])
    action_counts = {}
    for e in log_entries:
        action_counts[e["action"]] = action_counts.get(e["action"], 0) + 1
    total_actions = len(log_entries)
    for action, count in sorted(action_counts.items(), key=lambda x: x[1], reverse=True):
        pct = count / total_actions * 100
        lines.append(f"- **{action}:** {count} ({pct:.1f}%)")
    lines.append("")

    lines.extend(["## 3. Stakeholder Behaviour", ""])
    role_actions: Dict[str, Dict[str, int]] = {}
    for e in log_entries:
        role = e["role"]
        action = e["action"]
        if role not in role_actions:
            role_actions[role] = {}
        role_actions[role][action] = role_actions[role].get(action, 0) + 1

    for role in sorted(role_actions.keys()):
        lines.append(f"### {role.replace('_', ' ').title()}")
        top = sorted(role_actions[role].items(), key=lambda x: x[1], reverse=True)[:5]
        for action, count in top:
            lines.append(f"- {action}: {count}")
        lines.append("")

    lines.extend(["## 4. Opinion Dynamics", ""])
    dim_names = ["Optimism", "Trust in Govt", "Advocacy", "Frustration", "Career Security", "Patient Care Priority"]
    for dim_idx, dim_name in enumerate(dim_names):
        avg_start = sum(a.opinion[dim_idx] for a in agents) / len(agents)
        lines.append(f"- **{dim_name}:** Average shift over simulation = {avg_start:+.3f}")
    lines.append("")

    lines.extend(["## 5. Notable Agent Actions & Quotes", ""])
    interesting = [e for e in log_entries if e["action"] != "IGNORE"]
    interesting.sort(key=lambda x: len(x.get("content", "")), reverse=True)
    for e in interesting[:15]:
        lines.append(f"**{e['name']}** ({e['role']}) — Round {e['round']} — `{e['action']}`")
        lines.append(f"> {e['content'][:320]}")
        lines.append("")

    lines.extend([
        "## 6. Conclusion",
        "",
        "Under the environment-reform trajectory (SIM-4), Malaysia fixes the shortage through retention and working conditions, without increasing intake:",
        "1. **Retention revolution:** Brain drain falls from 1,200 to 400/year. Returnees triple. The existing workforce is kept and expanded.",
        "2. **Contract abolition:** The single biggest retention barrier is removed. Permanent posts expand by +10%/year, restoring career certainty.",
        "3. **Salary competitiveness:** Public salary ratio rises 0.45 -> 0.58, approaching private sector competitiveness. On-call and hazard pay restored.",
        "4. **Working conditions transformed:** Workload falls from 72 to 52 hours/week. 3-month deployment notice, rural incentives, workload caps implemented.",
        "5. **Health Services Commission:** Full establishment by 2028 breaks MOHE-JPA-MOH silos. End-to-end workforce planning becomes institutionalized.",
        "6. **Student interest rises:** Medicine regains prestige. Interest index climbs as graduates see secure, dignified career pathways.",
        "",
        "By 2030, Malaysia achieves 2.5 doctors per 1,000 through retention alone — a fundamentally different path from SIM-3's intake-driven growth. Overcrowding falls, waiting times drop by 50%, and the profession becomes sustainable.",
        "",
        "Risk: Slower absolute growth than SIM-3. If population grows faster than expected or NCD burden accelerates, the static intake may still leave gaps. The next simulation (SIM-5) tests the comprehensive approach: moderate intake increase AND full environment reform.",
        "",
        "---",
        f"*Report generated by SIM-4 engine | {datetime.now().isoformat()}*",
    ])

    return "\n".join(lines)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
async def main():
    random.seed(SEED)
    print(f"SIM-4 Starting... Agents: {AGENTS_COUNT}, Rounds: {ROUNDS}, Model: {MODEL_NAME}")
    print(f"Output directory: {OUT_DIR}")

    agents: List[Agent] = []
    for i, archetype in enumerate(ARCHETYPES[:AGENTS_COUNT]):
        agents.append(Agent(i, archetype))

    personas_path = OUT_DIR / "sim4_personas.json"
    personas_path.write_text(json.dumps([a.to_dict() for a in agents], indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Personas saved to {personas_path}")

    start_time = time.time()
    log_entries, state_trajectory = await run_simulation(agents)
    elapsed = time.time() - start_time
    print(f"\nSimulation complete in {elapsed:.1f}s ({len(log_entries)} total actions)")

    log_path = OUT_DIR / "sim4_log.jsonl"
    with log_path.open("w", encoding="utf-8") as f:
        for entry in log_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"Log saved to {log_path}")

    state_path = OUT_DIR / "sim4_state.json"
    state_path.write_text(json.dumps(state_trajectory, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"State trajectory saved to {state_path}")

    personas_path.write_text(json.dumps([a.to_dict() for a in agents], indent=2, ensure_ascii=False), encoding="utf-8")

    report = generate_report(agents, log_entries, state_trajectory)
    report_path = OUT_DIR / "sim4_report.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Report saved to {report_path}")

    print("\nSIM-4 complete. To interview an agent, load sim4_personas.json and run the interview script.")
    print(f"Personas retained at: {personas_path}")

if __name__ == "__main__":
    asyncio.run(main())
