# mas-2026-02: Malaysia Healthcare Workforce Policy Simulation

**Project repository for multi-agent simulation of Malaysia's cyclical doctor shortage crisis.**

---

## Purpose

Malaysia's medical workforce has oscillated between shortage and glut for 30 years:

- **1990s**: Shortage → expanded medical schools (3 → 30+)
- **2011**: Glut → moratorium on new programs + intake cap (4,820)
- **2024–2026**: Shortage again → 6,417 MOs resigned (2019–2023), housemen fell from 6,134 → 3,271

The critical insight: the 2016 "glut" was a **budget glut** (too many graduates for rigid civil service posts), not a **service glut** (hospitals remained overcrowded, queues stayed long). Simply increasing medical student intake risks repeating the exact pendulum.

This project uses **multi-agent LLM-driven simulation** to:
1. **Validate the prediction engine** against known historical dynamics
2. **Compare policy scenarios** to find sustainable, non-cyclical solutions
3. **Retain agent personas** for post-simulation interviews to assess realism

---

## Engine Architecture

- **Core**: Pure-Python async kernel, stdlib-only (no external dependencies)
- **LLM**: `gpt-oss:120b-cloud` via local Ollama gateway (OpenAI-compatible API)
- **Concurrency**: 2 agents at a time (conservative, avoids gateway overload)
- **Rounds**: 8 rounds = 4 years (2026–2030), 6 months per round
- **Agents**: 30 stakeholder archetypes with distinct personas, influence levels, and reaction speeds
- **State tracking**: 16 quantitative variables updated deterministically per round
- **Opinion dynamics**: 6-dimensional vectors per agent (optimism, trust, advocacy, frustration, career security, patient care priority)
- **Memory**: Agents retain per-round action summaries across the simulation
- **Interview**: Post-sim conversational interviews load full persona + memories + final opinion state

---

## Simulations

### SIM-1: Baseline (Status Quo)
**Purpose**: Validate engine against "do nothing" trajectory. Establish counterfactual.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 (static) |
| Housemanship posts | +2%/year (minimal) |
| Permanent posts | +1%/year (negligible) |
| Contract system | Continues, limited conversion |
| Salary adjustments | None (on-call still frozen) |
| Budget trend | −10% cut by 2027, flat thereafter |
| Brain drain rate | 1,200 → 1,440 MOs/year |
| Overseas return | 80 → 40/year (deterred) |
| HSC / pipeline reform | Not implemented |
| Private sector growth | +8%/year hiring |

**Key assumptions**:
- Government makes no structural changes despite crisis warnings
- Treasury continues fiscal consolidation, health is not protected
- Contract doctors remain excluded from specialization and benefits
- Student interest declines as profession reputation worsens
- Brain drain accelerates linearly as working conditions stagnate

**Outcome**: Doctor/pop ratio falls from 2.30 → 2.06. Overcrowding 78 → 94. Retention collapses 58% → 34%. Shortage worsens monotonically.

---

### SIM-2: Intake Surge (Repeat 1990s Mistake)
**Purpose**: Prove that rapid intake expansion without post creation recreates the exact cycle.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 → 8,000 by 2028 (+10%/year) |
| Housemanship posts | +3%/year (insufficient) |
| Permanent posts | +1%/year (negligible) |
| Contract system | Massively expanded to absorb overflow |
| Salary adjustments | None |
| Budget trend | −5% then flat |
| Brain drain rate | 1,200 → 1,900 MOs/year |
| Overseas return | 50 → 20/year |
| HSC / pipeline reform | Not implemented |
| Private sector growth | +10%/year (absorbs frustrated graduates) |

**Key assumptions**:
- Government panics and opens 5 new medical schools
- MOHE expands intake aggressively; JPA does not create posts
- Contract system balloons to absorb graduates who cannot get housemanship
- Initial student interest spike (shortage panic) followed by crash (glut reality)
- Training quality degrades as system is flooded with trainees
- Brain drain accelerates as contract frustration peaks

**Outcome**: By 2030, 14,265 unemployed graduates, 713-month housemanship waitlist, 37,447 contract doctors, retention 20%. System poised for moratorium by 2032–2035.

---

### SIM-3: Balanced Pipeline (Complete)
**Purpose**: Test whether matching intake to verified post creation prevents the cycle.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 → 6,000 by 2030 (tied to post availability) |
| Housemanship posts | Tied 1:1 to graduate projections |
| Permanent posts | +8%/year |
| Contract system | Phased out over 8 years |
| Salary adjustments | +15% by 2028 |
| Budget trend | Flat in real terms (protected) |
| Brain drain rate | 1,200 → 800 MOs/year |
| Overseas return | 80 → 200/year |
| HSC / pipeline reform | Partial (streamlined registration, MOHE-JPA coordination) |
| Private sector growth | +6%/year |

**Outcome**: Graduate-post matching eliminates glut. Doctor/pop reaches 2.62 by 2030. Overcrowding falls to 50. Retention rises to 72%. Contract doctors drop from 18,000 to 3,900. Sustainable, but slower retention than SIM-4.

---

### SIM-4: Environment Reform (Complete)
**Purpose**: Test whether fixing retention/working conditions solves shortage WITHOUT increasing intake.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 (static) |
| Housemanship posts | +4%/year |
| Permanent posts | +10%/year |
| Contract system | Abolished by 2030 |
| Salary adjustments | +25% by 2030, on-call reindexed |
| Budget trend | +5% real growth |
| Brain drain rate | 1,200 → 400 MOs/year |
| Overseas return | 80 → 280/year |
| HSC / pipeline reform | Full Health Services Commission by 2028 |
| Working conditions | 3-month notice, rural incentives, workload caps |

**Outcome**: Existing workforce retained and expanded through returnees. Doctor/pop 2.55 by 2030. Brain drain halved, returnees tripled. Overcrowding falls to 58. Retention reaches 78%. Contract abolition removes single biggest barrier. System becomes attractive despite static intake.

---

### SIM-5: Comprehensive (Complete)
**Purpose**: The ideal policy — moderate intake increase AND full environment reform.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 → 6,000 by 2030 |
| Housemanship posts | +5%/year (tied to graduate output) |
| Permanent posts | +10%/year |
| Contract system | Abolished |
| Salary adjustments | +20% by 2030 |
| Budget trend | +8% real growth |
| Brain drain rate | 1,200 → 304 MOs/year |
| Overseas return | 80 → 296/year |
| HSC / pipeline reform | Full — unified governance |
| Working conditions | 3-month notice, AI support, rural incentives, workload caps |

**Outcome**: Fastest, most sustainable improvement. Doctor/pop reaches 2.58 by 2030. Retention hits 82%. Brain drain near full retention. Returnees quadruple. Overcrowding falls to 50. Intake and retention addressed simultaneously — the pendulum is broken.

---

### SIM-6: Private Sector Integration (Complete)
**Purpose**: Test market-based alternative — government offloads training to private sector via PPP.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 → 6,500 by 2030 (private schools expand with accreditation) |
| Housemanship posts | Public: +2%/year; Private: +15%/year |
| Permanent posts | Public: static; Private: major expansion |
| Contract system | Public retains; Private offers direct permanent |
| Salary adjustments | Public: +10%; Private: market rate |
| Budget trend | −5% |
| Brain drain rate | 1,200 → 600 MOs/year |
| Overseas return | 80 → 200/year |
| HSC / pipeline reform | Light-touch regulation, accreditation focus |
| Compulsory service | 3-year public service required, then free market |
| Private sector growth | +15%/year |

**Outcome**: Fastest absolute workforce growth. Doctor/pop reaches 2.54 by 2030. Private sector absorbs surplus graduates, reducing brain drain. But **two-tier system emerges**: urban patients benefit; rural patients face worsening access as doctors concentrate in profitable urban private posts after compulsory service. By Round 7, 15% of rural KKs critically understaffed. Market-based expansion is efficient at growing numbers but indifferent to equity.

**Risk realized**: Equity gap widens significantly. Malaysia has more doctors than ever, but they are not distributed where needed most.

---

## Validation Methodology

### Phase 1: Engine Validation (Complete)

| Test | Evidence | Status |
|------|----------|--------|
| Policy divergence | SIM-1 vs SIM-2 produce quantitatively distinct futures | ✓ Pass |
| JSON validity | 97.9–100% parseable agent responses | ✓ Pass |
| Stakeholder differentiation | Roles maintain consistent, scenario-appropriate signatures | ✓ Pass |
| Opinion dynamics | 6D vectors shift plausibly per scenario | ✓ Pass |
| Event awareness | Agents reference budget cuts, elections, visas, HSC | ✓ Pass |
| Nonlinear dynamics | SIM-2 shows boom-then-bust student interest | ✓ Pass |
| Memory retention | Agents reference previous-round actions in reasoning | ✓ Pass |

### Phase 2: Realism Testing (In Progress)

Two post-simulation interviews were conducted per simulation. The interview tool loads:
- Full persona (name, role, age, stance)
- All simulation memories
- Final 6D opinion vector
- Temporal context (which policy the agent survived)

Agents respond in character with Malaysian English/Malay phrasing, reference specific simulation events, and display emotionally grounded reasoning. **Note**: the project maintainer has a vested interest in healthcare workforce policy; independent realism assessment by neutral observers is encouraged.

---

## Repository Structure

```
mas-2026-02/
├── README.md                              ← this file
├── malaysia-doctor-shortage-simulation-plan.md   ← research synthesis + full sim design
├── SIM-1/
│   ├── sim1_engine.py                     ← standalone simulation engine
│   ├── sim1_interview.py                  ← post-sim interview tool
│   ├── sim1_log.jsonl                     ← 240 agent actions (8 rounds)
│   ├── sim1_state.json                    ← quantitative trajectory
│   ├── sim1_personas.json                 ← interview-ready personas + memories
│   └── sim1_report.md                     ← structured markdown report
├── SIM-2/
│   ├── sim2_engine.py
│   ├── sim2_interview.py
│   ├── sim2_log.jsonl
│   ├── sim2_state.json
│   ├── sim2_personas.json
│   └── sim2_report.md
├── SIM-3/                                 ← complete: Balanced Pipeline (Match Intake to Posts)
│   ├── sim3_engine.py
│   ├── sim3_interview.py
│   ├── sim3_log.jsonl
│   ├── sim3_state.json
│   ├── sim3_personas.json
│   └── sim3_report.md
├── SIM-4/                                 ← complete: Environment Reform (Fix Retention)
│   ├── sim4_engine.py
│   ├── sim4_interview.py
│   ├── sim4_log.jsonl
│   ├── sim4_state.json
│   ├── sim4_personas.json
│   └── sim4_report.md
├── SIM-5/                                 ← complete: Comprehensive (Balanced + Environment)
│   ├── sim5_engine.py
│   ├── sim5_interview.py
│   ├── sim5_log.jsonl                     ← 240 agent actions
│   ├── sim5_state.json                     ← quantitative trajectory
│   ├── sim5_personas.json                  ← interview-ready personas
│   └── sim5_report.md                      ← structured report
└── SIM-6/                                 ← complete: Private Sector Integration (Market-Based)
    ├── sim6_engine.py
    ├── sim6_interview.py
    ├── sim6_log.jsonl                      ← 240 agent actions
    ├── sim6_state.json                      ← quantitative trajectory
    ├── sim6_personas.json                   ← interview-ready personas
    └── sim6_report.md                       ← structured report
```

---

## Running Simulations

Requirements:
- Python 3.11+
- Local Ollama gateway at `localhost:11434` with `gpt-oss:120b-cloud` model
- No pip packages required (stdlib only)

```bash
cd SIM-1
python3 sim1_engine.py        # ~11 minutes for 30 agents × 8 rounds
python3 sim1_interview.py --agent "Dr Lim Kah Wai"
python3 sim1_interview.py --list
```

---

## Key Quantitative Variables Tracked

| Variable | Unit | SIM-1 End (2030) | SIM-2 End (2030) |
|----------|------|------------------|------------------|
| Annual graduates | count | 4,820 | 8,000 |
| Housemanship posts | count | 4,101 | 4,434 |
| Permanent posts | count | 25,989 | 25,989 |
| Contract doctors | count | 20,877 | 37,447 |
| Brain drain | /year | 1,440 | 1,900 |
| Overseas returnees | /year | 40 | 20 |
| Doctor-to-population | /1,000 | 2.06 | 2.15 |
| Overcrowding index | 0–100 | 94 | 100 |
| Workload | hrs/week | 84 | 92 |
| KK waiting time | days | 22 | 24 |
| Specialist waiting time | weeks | 20 | 22 |
| Student interest | applicants/seat | 1.16 | 0.80 |
| Health budget | % GDP | 1.94 | 1.80 |
| Salary ratio (public/private) | ratio | 0.37 | 0.33 |
| Retention (>3 years) | % | 34 | 20 |
| HO waitlist (SIM-2 only) | months | N/A | 713 |
| Unemployed graduates (SIM-2 only) | count | N/A | 14,265 |

---

## Ethical Notes

- This is a **policy simulation**, not a forecasting model. It explores stakeholder reactions under stylized assumptions.
- Quantitative state variables are formula-driven, not emergent from agent interactions. Population-scale dynamics require ABM substrate integration.
- Agent personas are synthetic composites based on public reporting (CodeBlue, parliamentary statements, MMA advocacy). They do not represent real individuals.
- The project maintainer is a medical student with a vested interest in workforce policy. Results should be interpreted as exploratory, not authoritative.

---

## License

MIT — research and policy use encouraged. Attribution requested.
