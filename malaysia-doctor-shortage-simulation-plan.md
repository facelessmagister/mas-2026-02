# Malaysia Doctor Shortage: Research Synthesis & Simulation Plan

## Executive Summary

Malaysia is caught in a **15-year pendulum swing**:
- **1990-2010**: Expanded from 3 to 30+ medical schools to address shortage
- **2011-2021**: Moratorium + quota (4,820 cap) to address "glut"
- **2024-2026**: Shortage again — 6,417 MOs resigned (2019-2023), housemen dropped from 6,134 (2019) to 3,271 (2023)

The critical insight: the 2016 "glut" was a **budget glut**, not a **service glut**. Government hospitals remained overcrowded, doctors worked extreme hours, and Klinik Kesihatan / specialist queues stayed long. The problem was never too many doctors for the population — it was too many graduates for the government's salary budget and rigid civil service post structure.

---

## Research Synthesis

### Key Facts from CodeBlue / Health DG Sources

| Metric | Value | Source |
|--------|-------|--------|
| Medical schools (2010s) | 30+ (highest per capita globally) | Dr Sean Thum, Dec 2024 |
| Moratorium on new programs | 2011, extended 2016-2021 | MOH / MOHE |
| Annual intake cap (2018) | 4,820 students | Quota policy |
| Peak house officers (2019) | 6,134 | MOH data |
| House officers (2023) | 3,271 | MOH data |
| MO resignations (2019-2023) | 6,417 (~3.5/day) | Dr Sean Thum |
| Specialists exited (2019-2023) | 1,046 | Dr Sean Thum |
| Contract MOs → permanent | 1,086 | Dr Sean Thum |
| Registered doctors (2023) | 74,517 | Health DG, Apr 2026 |
| Doctor-to-population | 2.3 / 1,000 (OECD: 3.9) | World Bank / Health DG |
| Skilled health workers | 6.34 / 1,000 (WHO benchmark: 4.45) | Health DG |
| On-call allowances | Unchanged since 2012 | Dr Sean Thum |
| Budget 2026 threat | RM3b cut requested by Treasury; 10% expected | CodeBlue Apr-May 2026 |

### Root Causes Identified

1. **Fragmented pipeline**: MOHE (education) → JPA (posts/recruitment) → MOH (service delivery) operate in silos. No binding workforce-needs quota. Registration takes months. (Health DG, Apr 2026)

2. **Rigid civil service structure**: Limited permanent posts (jawatan), contract doctors excluded from specialization and benefits, salary uncompetitive vs private sector/overseas.

3. **Brain drain**: 6,417 MOs left public service in 4 years. Private sector reports record earnings. Overseas opportunities (Singapore, Australia, UK, Middle East) pull talent.

4. **Working conditions**: Underfunded, understaffed, overworked, overstretched. Abrupt deployment to remote areas (< 2 weeks notice). On-call allowances frozen since 2012.

5. **Training mismatch**: Hospital-based, specialty-oriented, "knowledge-heavy and competency-light". Limited rural/community exposure. Not aligned with ageing population + NCD burden.

6. **Budget pressure**: Treasury demanding RM3b cuts to Health Ministry 2026 budget. Health workers bracing for "death by a thousand cuts".

### The Trap

The easiest government response — **increase medical student intake** — risks repeating the exact cycle:
- Intake ↑ → graduates ↑ in 5-6 years → housemanship bottleneck → contract system expansion → frustration → brain drain → shortage again in 2035-2040.

Unless the **environment** (posts, pay, working conditions, career pathway) changes in parallel, intake changes alone are oscillatory, not solutions.

---

## Simulation Design

### Engine Choice

**Recommended**: Hybrid ABM + LLM (Pythia-style) or adapted MiroFish-Lite with custom actions. Domain: `malaysia_health_workforce`.

- **Time horizon**: 2026 → 2040 (15 years = one full medical training cycle)
- **Round mapping**: 1 round = 6 months (30 rounds = 15 years)
- **Agent count**: 40-50 (stakeholder archetypes), with quantitative state variables for the underlying population
- **State variables** (quantitative, updated per round by formula):
  - Annual medical graduates
  - Available housemanship posts
  - Permanent posts created
  - Contract-to-permanent conversion rate
  - Brain drain rate (MOs leaving/year)
  - Overseas return rate (Malaysians coming back)
  - Doctor-to-population ratio
  - Public hospital overcrowding index
  - Average doctor workload (hours/week)
  - Klinik Kesihatan waiting time (days)
  - Specialist appointment waiting time (weeks)
  - Medical student interest index (applications per seat)
  - Health budget (% of GDP)
  - Public doctor salary vs private sector ratio
  - Training quality / competency score

### Stakeholder Agents

| Role | Count | Key Concerns |
|------|-------|--------------|
| Medical students / applicants | 6 | Cost, career certainty, specialization pathway, salary |
| House officers | 5 | Post availability, contract vs permanent, workload, bullying |
| Medical officers (MO) | 6 | Permanent post, specialization, pay, working hours, brain drain |
| Specialists | 4 | Private sector pull, public sector conditions, research funding |
| MOH administrators | 4 | Budget constraints, deployment, retention, service delivery |
| JPA administrators | 3 | Civil service rules, post ceilings, salary scales, Treasury pressure |
| MOHE administrators | 3 | School accreditation, intake quotas, graduate quality |
| Private hospital operators | 3 | Profit, hiring from public pool, training partnerships |
| MMA / doctor associations | 3 | Advocacy, Health Services Commission, working conditions |
| Rural clinic staff | 3 | Understaffing, isolation, equipment, career stagnation |
| Urban patients | 4 | Waiting times, specialist access, quality of care |
| Rural patients | 3 | Access, transport, chronic disease burden |
| Treasury / Finance | 2 | Fiscal deficit, health budget cuts, efficiency |

### Action Space (Domain-Specific)

```
INCREASE_INTAKE, DECREASE_INTAKE, MAINTAIN_INTAKE
CREATE_PERMANENT_POSTS, EXPAND_CONTRACT_SYSTEM
CONVERT_CONTRACT_TO_PERMANENT
RAISE_SALARIES, FREEZE_SALARIES, CUT_ALLOWANCES
IMPROVE_WORKING_CONDITIONS, IGNORE_CONDITIONS
ESTABLISH_HEALTH_SERVICES_COMMISSION
STREAMLINE_REGISTRATION, DELAY_REGISTRATION
EXPAND_PRIVATE_PARTNERSHIP, RESTRICT_PRIVATE_HIRING
DEPLOY_TO_RURAL, RESIST_RURAL_DEPLOYMENT
PURSUE_SPECIALIZATION, LEAVE_FOR_PRIVATE, EMIGRATE
RETURN_FROM_OVERSEAS, STAY_OVERSEAS
COMPLAIN_TO_MINISTRY, ORGANISE_PROTEST, PUBLISH_RESEARCH
SUPPORT_POLICY, OPPOSE_POLICY, IGNORE
```

---

## Simulation Scenarios

### SIM-1: Baseline (Status Quo Trajectory)
**Premise**: Government makes no structural changes. Minor tweaks only. Budget cuts proceed.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 (static) |
| Housemanship posts | Grow at +2%/year (minimal) |
| Permanent posts | No net increase |
| Contract system | Continues, limited conversion |
| Salary adjustments | None (on-call still frozen) |
| Budget trend | -10% cut by 2027, flat thereafter |
| Brain drain rate | 1,200 MOs/year (current level) |
| Overseas return | 5%/year of diaspora |
| HSC / pipeline reform | Not implemented |
| Private sector growth | +8%/year hiring |

**Expected outcome**: Gradual worsening of shortage. Doctor-to-population stagnates or falls. Overcrowding and waiting times increase. By 2035, critical shortage in specialist fields.

---

### SIM-2: Intake Surge (Repeat 1990s Mistake)
**Premise**: Government panics and rapidly expands medical school intake to 8,000+/year, opens new schools. No parallel post creation.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 → 8,000 by 2028 (+10%/year) |
| Housemanship posts | Grow at +3%/year (insufficient) |
| Permanent posts | +1%/year (negligible) |
| Contract system | Massively expanded |
| Salary adjustments | None |
| Budget trend | -5% (cuts partially reversed then reimposed) |
| Brain drain rate | 1,500 MOs/year (worsens as frustration grows) |
| Overseas return | 3%/year (worsening conditions deter return) |
| HSC / pipeline reform | Not implemented |
| Private sector growth | +10%/year (absorbs frustrated graduates) |

**Expected outcome**: By 2032-2035, a massive glut of graduates competing for limited posts. Long waits for housemanship. Contract doctor crisis 2.0. By 2038, government imposes moratorium again. Cycle repeats exactly.

---

### SIM-3: Balanced Pipeline (Fix the Structural Mismatch)
**Premise**: Intake increases moderately, but **only in lockstep with verified post creation**. The missing piece from the 1990s.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 → 6,500 by 2030 (tied to post availability) |
| Housemanship posts | Tied 1:1 to graduate projections (+6%/year) |
| Permanent posts | +8%/year (funded by efficiency savings + reprioritization) |
| Contract system | Phased out over 10 years |
| Salary adjustments | +15% by 2028, on-call reindexed |
| Budget trend | Flat in real terms (protected from cuts) |
| Brain drain rate | 800 MOs/year (improves as certainty returns) |
| Overseas return | 12%/year (improved conditions attract returnees) |
| HSC / pipeline reform | Partial (streamlined registration, MOH-JPA coordination) |
| Private sector growth | +6%/year (less poaching as public improves) |

**Expected outcome**: Steady growth in workforce without glut. Doctor-to-population reaches 3.0/1,000 by 2038. Waiting times improve moderately. Risk: requires sustained political will and budget protection.

---

### SIM-4: Environment Reform (Fix Retention & Working Conditions)
**Premise**: Intake stays flat at 4,820. All effort goes to making the profession attractive and sustainable.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 (static) |
| Housemanship posts | +4%/year (targeted expansion) |
| Permanent posts | +10%/year (major conversion drive) |
| Contract system | Abolished by 2032 |
| Salary adjustments | +25% by 2030, on-call reindexed to 2026 levels, hazard pay restored |
| Budget trend | +5% real growth (protected) |
| Brain drain rate | 400 MOs/year (dramatic improvement) |
| Overseas return | 20%/year (Malaysia becomes attractive) |
| HSC / pipeline reform | Full Health Services Commission established 2028 |
| Working conditions | Deployment notice → 3 months, rural incentives enhanced, workload caps |
| Training reform | Competency-based, community exposure, digital literacy |
| Private sector growth | +4%/year (public sector competitiveness reduces poaching) |

**Expected outcome**: Existing workforce retained and expanded through returnees. Doctor-to-population improves to 2.8/1,000 by 2038. Overcrowding reduced. Waiting times cut by 30-40%. Specialist retention improves. Risk: slower absolute growth in numbers; if population grows fast, may still lag.

---

### SIM-5: Balanced Pipeline + Environment Reform (Comprehensive)
**Premise**: Moderate intake increase AND full environment reform. The most comprehensive but politically difficult solution.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 → 6,000 by 2030 (modest, tied to posts) |
| Housemanship posts | Tied to graduate output (+5%/year) |
| Permanent posts | +10%/year (major expansion) |
| Contract system | Phased out by 2032 |
| Salary adjustments | +20% by 2030, full allowance reindexing |
| Budget trend | +8% real growth (major reprioritization) |
| Brain drain rate | 300 MOs/year (near full retention) |
| Overseas return | 25%/year (strong pull factor) |
| HSC / pipeline reform | Full — unified governance, end-to-end workforce planning |
| Working conditions | 3-month deployment notice, rural incentives, workload caps, AI support |
| Training reform | Competency-based, community focus, interprofessional learning |
| Private sector growth | +5%/year (regulated partnership, not poaching) |
| PPP | Government subsidizes training, private sector provides housemanship slots |

**Expected outcome**: Doctor-to-population reaches 3.2/1,000 by 2038 (near OECD). Overcrowding and waiting times halved. Malaysia becomes net importer of medical talent. Sustainable, non-cyclical. Risk: requires massive political capital, budget reallocation, and 10+ year continuity.

---

### SIM-6: Private Sector Integration (Market-Based)
**Premise**: Government stops trying to employ all doctors. Expands public-private partnerships, subsidizes private training, regulates compulsory service.

| Parameter | Value |
|-----------|-------|
| Annual intake | 4,820 → 6,500 (private schools expand with accreditation) |
| Housemanship posts | Public: +2%/year; Private: +15%/year (PPP-funded) |
| Permanent posts | Public: static; Private: major expansion |
| Contract system | Public retains; Private offers direct permanent |
| Salary adjustments | Public: +10%; Private: market rate (already higher) |
| Budget trend | -5% (government offloads training costs to private) |
| Brain drain rate | 600 MOs/year (private sector absorbs many) |
| Overseas return | 15%/year (private sector attractive) |
| HSC / pipeline reform | Light-touch regulation, accreditation focus |
| Compulsory service | 3-year public service required, then free market |
| Private sector growth | +15%/year (major expansion) |
| Universal coverage | Regulated fee structure, government vouchers for poor |

**Expected outcome**: Rapid expansion of total doctor workforce. Private sector handles urban middle-class; public sector focuses on poor and rural. Risk: two-tier system emerges. Rural and poor patients may face access inequality if private sector cherry-picks profitable areas.

---

## Comparative Metrics Table

| Metric | SIM-1 Status Quo | SIM-2 Intake Surge | SIM-3 Balanced | SIM-4 Environment | SIM-5 Comprehensive | SIM-6 Private Integration |
|--------|------------------|-------------------|----------------|-------------------|---------------------|--------------------------|
| **Intake 2030** | 4,820 | 8,000 | 6,500 | 4,820 | 6,000 | 6,500 |
| **Doc/pop 2038** | 2.1 | 2.4 then crash | 3.0 | 2.8 | 3.2 | 3.0 |
| **Glut risk by 2035** | Low | **HIGH** | Low | Low | Low | Low |
| **Brain drain 2030** | 1,200/yr | 1,500/yr | 800/yr | 400/yr | 300/yr | 600/yr |
| **Overseas return 2030** | 5% | 3% | 12% | 20% | 25% | 15% |
| **KK wait time 2038** | 14 days | 12 days | 7 days | 6 days | 4 days | 5 days |
| **Specialist wait 2038** | 12 weeks | 10 weeks | 6 weeks | 5 weeks | 3 weeks | 4 weeks |
| **Workload hrs/week 2038** | 72 | 68 | 58 | 55 | 50 | 52 |
| **Budget trajectory** | -10% | -5% | Flat | +5% | +8% | -5% |
| **Political feasibility** | High | High | Medium | Low | Very Low | Medium |
| **Cycle repeat risk** | Medium (slow) | **HIGH** | Low | Low | Very Low | Medium |

---

## Recommended Simulation Run Order

1. **SIM-1 (Baseline)** — Establish the "do nothing" trajectory. This is the counterfactual against which all others are measured.

2. **SIM-2 (Intake Surge)** — Prove that repeating the 1990s produces the same 2016 glut. Validates the user's hypothesis.

3. **SIM-3 (Balanced Pipeline)** — Tests whether matching intake to posts alone prevents the cycle.

4. **SIM-4 (Environment Reform)** — Tests whether retention/working conditions can solve shortage WITHOUT increasing intake.

5. **SIM-5 (Comprehensive)** — The ideal policy. Tests what happens when both supply and environment are addressed.

6. **SIM-6 (Private Integration)** — Tests market-based alternative. Reveals equity risks.

---

## Key Simulation Events to Inject

| Round | Year | Event |
|-------|------|-------|
| 2 | 2027 | Budget 2027: 10% health cut implemented |
| 4 | 2028 | Election year — health workforce becomes campaign issue |
| 6 | 2030 | World Bank report: Malaysia doctor density stagnant |
| 8 | 2032 | Regional comparison: Singapore reaches 4.0/1,000 |
| 10 | 2034 | Aging population crisis: NCD burden +30% |
| 14 | 2036 | New government — reviews health workforce policy |
| 16 | 2038 | Commonwealth Games / major event strains health system |
| 20 | 2040 | Final assessment round |

---

## Next Steps

1. Select simulation engine (Pythia hybrid ABM recommended for quantitative state tracking)
2. Compile corpus from CodeBlue articles, MOH speeches, World Bank data
3. Seed agent personas with the archetypes above
4. Run SIM-1 and SIM-2 first to validate the engine and establish baseline
5. Iterate on event injection and peer influence layers
6. Generate comparative reports with quantitative trajectory charts
