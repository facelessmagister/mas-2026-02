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

### SIM-3: Balanced Pipeline (Planned)
**Purpose**: Test whether matching intake to verified post creation prevents the cycle.

| Parameter | Planned Value |
|-----------|---------------|
| Annual intake | 4,820 → 6,500 by 2030 (tied to post availability) |
| Housemanship posts | Tied 1:1 to graduate projections (+6%/year) |
| Permanent posts | +8%/year (funded by efficiency savings) |
| Contract system | Phased out over 10 years |
| Salary adjustments | +15% by 2028, on-call reindexed |
| Budget trend | Flat in real terms (protected from cuts) |
| Brain drain rate | 800 MOs/year (improves as certainty returns) |
| Overseas return | 12%/year |
| HSC / pipeline reform | Partial (streamlined registration, MOH-JPA coordination) |
| Private sector growth | +6%/year (less poaching as public improves) |

**Key assumptions**:
- Intake increases are gated on verified post creation
- Contract system is gradually converted to permanent
- Budget protection clause prevents Treasury cuts
- Working conditions improve moderately
- Student interest stabilizes as career pathway becomes predictable

**Expected outcome**: Steady workforce growth without glut. Doctor/pop reaches 3.0/1,000 by 2038.

---

### SIM-4: Environment Reform (Planned)
**Purpose**: Test whether fixing retention/working conditions solves shortage WITHOUT increasing intake.

| Parameter | Planned Value |
|-----------|---------------|
| Annual intake | 4,820 (static) |
| Housemanship posts | +4%/year |
| Permanent posts | +10%/year (major conversion drive) |
| Contract system | Abolished by 2032 |
| Salary adjustments | +25% by 2030, on-call reindexed, hazard pay restored |
| Budget trend | +5% real growth (protected) |
| Brain drain rate | 400 MOs/year (dramatic improvement) |
| Overseas return | 20%/year |
| HSC / pipeline reform | Full Health Services Commission established 2028 |
| Working conditions | 3-month deployment notice, rural incentives, workload caps |
| Training reform | Competency-based, community exposure, digital literacy |
| Private sector growth | +4%/year (public competitiveness reduces poaching) |

**Key assumptions**:
- Health Services Commission breaks MOHE-JPA-MOH silos
- Massive permanent post expansion funded by efficiency + reprioritization
- Contract abolition removes the single biggest retention barrier
- Salary competitiveness with private sector reduces brain drain
- Returnees come back as Malaysia becomes attractive

**Expected outcome**: Existing workforce retained and expanded through returnees. Doctor/pop 2.8/1,000 by 2038. Overcrowding and waiting times cut by 30–40%.

---

### SIM-5: Comprehensive (Planned)
**Purpose**: The ideal policy — moderate intake increase AND full environment reform.

| Parameter | Planned Value |
|-----------|---------------|
| Annual intake | 4,820 → 6,000 by 2030 (modest, tied to posts) |
| Housemanship posts | Tied to graduate output (+5%/year) |
| Permanent posts | +10%/year (major expansion) |
| Contract system | Phased out by 2032 |
| Salary adjustments | +20% by 2030, full allowance reindexing |
| Budget trend | +8% real growth (major reprioritization) |
| Brain drain rate | 300 MOs/year (near full retention) |
| Overseas return | 25%/year (strong pull factor) |
| HSC / pipeline reform | Full — unified governance, end-to-end workforce planning |
| Working conditions | 3-month notice, rural incentives, workload caps, AI support |
| Training reform | Competency-based, community focus, interprofessional learning |
| Private sector growth | +5%/year (regulated partnership, not poaching) |
| PPP | Government subsidizes training, private sector provides housemanship slots |

**Key assumptions**:
- Political capital and budget reallocation are sustained for 10+ years
- Both supply (intake) and demand (posts/conditions) addressed simultaneously
- Malaysia becomes net importer of medical talent
- System reaches OECD-equivalent density (3.2/1,000) by 2038

**Expected outcome**: Sustainable, non-cyclical. Overcrowding and waiting times halved. Risk: requires massive political continuity.

---

### SIM-6: Private Sector Integration (Planned)
**Purpose**: Test market-based alternative — government stops employing all doctors directly.

| Parameter | Planned Value |
|-----------|---------------|
| Annual intake | 4,820 → 6,500 (private schools expand with accreditation) |
| Housemanship posts | Public: +2%/year; Private: +15%/year (PPP-funded) |
| Permanent posts | Public: static; Private: major expansion |
| Contract system | Public retains; Private offers direct permanent |
| Salary adjustments | Public: +10%; Private: market rate (already higher) |
| Budget trend | −5% (government offloads training costs) |
| Brain drain rate | 600 MOs/year (private sector absorbs many) |
| Overseas return | 15%/year (private sector attractive) |
| HSC / pipeline reform | Light-touch regulation, accreditation focus |
| Compulsory service | 3-year public service required, then free market |
| Private sector growth | +15%/year (major expansion) |
| Universal coverage | Regulated fee structure, government vouchers for poor |

**Key assumptions**:
- Private sector can absorb surplus graduates quickly
- Regulation prevents two-tier system (urban rich vs. rural poor)
- Compulsory service ensures minimum public coverage
- Government vouchers maintain access for poor

**Expected outcome**: Rapid workforce expansion. Risk: equity gap if private sector cherry-picks profitable areas.

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
├── SIM-3/                                 ← planned
├── SIM-4/                                 ← planned
├── SIM-5/                                 ← planned
└── SIM-6/                                 ← planned
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
