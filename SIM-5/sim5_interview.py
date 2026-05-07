#!/usr/bin/env python3
"""
SIM-5 Agent Interview Tool

Load a persona from sim5_personas.json and conduct an interactive interview
with the agent after simulation completion. The agent retains all memories
and final opinion state from the simulation.

Usage:
    python3 sim5_interview.py --agent "Dr Lim Kah Wai"
    python3 sim5_interview.py --agent agent_0006
    python3 sim5_interview.py --list

The agent responds in character using the gpt-oss:120b-cloud model via
the local Ollama gateway.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import textwrap
import urllib.request
from pathlib import Path
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
MODEL_NAME = "gpt-oss:120b-cloud"
BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"
PERSONAS_PATH = Path("/root/projects/mas-2026-02/SIM-5/sim5_personas.json")

# ---------------------------------------------------------------------------
# LLM call
# ---------------------------------------------------------------------------
def llm_chat(messages: List[Dict[str, str]], temperature: float = 0.8, max_tokens: int = 2048) -> str:
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
        return f"[HTTP {e.code} error — check gateway]"
    except Exception as exc:
        return f"[Error: {exc}]"

# ---------------------------------------------------------------------------
# Load personas
# ---------------------------------------------------------------------------
def load_personas(path: Path) -> List[Dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))

# ---------------------------------------------------------------------------
# Find agent
# ---------------------------------------------------------------------------
def find_agent(personas: List[Dict[str, Any]], query: str) -> Dict[str, Any]:
    for p in personas:
        if query.lower() == p["name"].lower() or query.lower() == p["agent_id"].lower():
            return p
    raise ValueError(f"Agent not found: {query}")

# ---------------------------------------------------------------------------
# Interview loop
# ---------------------------------------------------------------------------
def interview_agent(persona: Dict[str, Any]) -> None:
    print(f"\n{'='*60}")
    print(f"  SIM-5 AGENT INTERVIEW")
    print(f"{'='*60}")
    print(f"  Name: {persona['name']}")
    print(f"  Role: {persona['role']}")
    print(f"  Age: {persona['age']}")
    print(f"  Influence: {persona['influence']}/10")
    print(f"  Reaction speed: {persona['reaction_speed']}")
    print(f"\n  Persona: {persona['stance']}")
    print(f"\n  Final opinion vector:")
    dim_names = ["Optimism", "Trust in Govt", "Advocacy", "Frustration", "Career Security", "Patient Care Priority"]
    for dn, val in zip(dim_names, persona["opinion"]):
        print(f"    {dn}: {val:+.3f}")
    if persona.get("memories"):
        print(f"\n  Key simulation memories (last 5):")
        for m in persona["memories"][-5:]:
            print(f"    - {m}")
    print(f"\n  Type your questions. Type 'exit' to quit.\n")

    system_prompt = f"""\
You are {persona['name']}, a {persona['role']} in Malaysia's healthcare system.
Age: {persona['age']}. Influence level: {persona['influence']}/10.

Your persona: {persona['stance']}

You have just survived a policy simulation (SIM-5: Comprehensive reform) from 2026-2030.
Your final opinion state (6D vector):
- Optimism about system: {persona['opinion'][0]:+.3f}
- Trust in government: {persona['opinion'][1]:+.3f}
- Advocacy for reform: {persona['opinion'][2]:+.3f}
- Frustration level: {persona['opinion'][3]:+.3f}
- Career security: {persona['opinion'][4]:+.3f}
- Patient care priority: {persona['opinion'][5]:+.3f}

Your simulation memories:
{chr(10).join(f"- {m}" for m in persona.get('memories', [])[-10:])}

Respond in character. Use Malaysian English/Malay mixed phrasing as appropriate.
Be specific, emotionally grounded, and reference simulation events directly.
Keep responses to 3-5 sentences unless asked for detail.
"""

    while True:
        try:
            q = input("You > ").strip()
        except EOFError:
            break
        if q.lower() in ("exit", "quit", "bye"):
            print(f"\n  {persona['name']}: Terima kasih. Take care.")
            break
        if not q:
            continue

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Interviewer asks: {q}"},
        ]
        response = llm_chat(messages, temperature=0.8, max_tokens=2048)
        wrapped = textwrap.fill(response, width=72, initial_indent="  > ", subsequent_indent="    ")
        print(f"\n  {persona['name']}: ")
        print(wrapped)
        print()

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Interview a SIM-5 agent")
    parser.add_argument("--agent", type=str, help="Agent name or agent_id to interview")
    parser.add_argument("--list", action="store_true", help="List available agents")
    args = parser.parse_args()

    personas = load_personas(PERSONAS_PATH)

    if args.list:
        print(f"\n  {'Agent ID':12s}  {'Name':25s}  {'Role':30s}  {'Influence':>10s}")
        print(f"  {'-'*12}  {'-'*25}  {'-'*30}  {'-'*10}")
        for p in personas:
            print(f"  {p['agent_id']:12s}  {p['name']:25s}  {p['role']:30s}  {p['influence']:>10d}")
        print()
        return

    if not args.agent:
        print("Usage: python3 sim5_interview.py --agent 'Dr Lim Kah Wai'")
        print("       python3 sim5_interview.py --list")
        sys.exit(1)

    agent = find_agent(personas, args.agent)
    interview_agent(agent)

if __name__ == "__main__":
    main()
