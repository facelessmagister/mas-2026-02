# SIM-1 Report: Malaysia Doctor Shortage — Baseline (Status Quo)

**Simulation date:** 2026-05-06T12:58:17.187825  
**Model:** gpt-oss:120b-cloud  
**Agents:** 30 | **Rounds:** 8 (6 months/round = 4 years: 2026-2030)  
**Policy premise:** Government makes no structural changes. Budget cuts proceed. Intake static. Contract system continues.

---

## 1. Quantitative State Trajectory

| Round | Year | Graduates | Posts (HO) | Perm. Posts | Contract | Brain Drain | Returnees | Doc/1k | Overcrowding | Workload hrs | KK Wait | Specialist Wait | Interest | Budget %GDP | Salary Ratio | Retention % |
|-------|------|-----------|------------|-------------|----------|-------------|-----------|--------|--------------|--------------|---------|----------------|----------|-----------|--------------|-------------|
| 1 | 2026.5 | 4820 | 3570 | 24240 | 18625 | 1230 | 75 | 2.27 | 80 | 74 | 15 | 13 | 1.72 | 2.08 | 0.44 | 55 |
| 2 | 2027.0 | 4820 | 3641 | 24482 | 19179 | 1260 | 70 | 2.24 | 82 | 75 | 16 | 14 | 1.64 | 2.06 | 0.43 | 52 |
| 3 | 2027.5 | 4820 | 3714 | 24727 | 19659 | 1290 | 65 | 2.21 | 84 | 76 | 17 | 15 | 1.56 | 2.04 | 0.42 | 49 |
| 4 | 2028.0 | 4820 | 3789 | 24974 | 20063 | 1320 | 60 | 2.18 | 86 | 78 | 18 | 16 | 1.48 | 2.02 | 0.41 | 46 |
| 5 | 2028.5 | 4820 | 3864 | 25224 | 20389 | 1350 | 55 | 2.15 | 88 | 80 | 19 | 17 | 1.40 | 2.00 | 0.40 | 43 |
| 6 | 2029.0 | 4820 | 3942 | 25476 | 20635 | 1380 | 50 | 2.12 | 90 | 81 | 20 | 18 | 1.32 | 1.98 | 0.39 | 40 |
| 7 | 2029.5 | 4820 | 4020 | 25731 | 20799 | 1410 | 45 | 2.09 | 92 | 82 | 21 | 19 | 1.24 | 1.96 | 0.38 | 37 |
| 8 | 2030.0 | 4820 | 4101 | 25989 | 20877 | 1440 | 40 | 2.06 | 94 | 84 | 22 | 20 | 1.16 | 1.94 | 0.37 | 34 |

### Key Trends

- **Doctor-to-population ratio:** 2.27 -> 2.06 (falling toward crisis levels)
- **Public hospital overcrowding:** 80 -> 94 (approaching maximum)
- **Average doctor workload:** 74 -> 84 hours/week (unsustainable)
- **Brain drain:** 1230 -> 1440 doctors/year leaving
- **Medical student interest:** 1.72 -> 1.16 (applicants per seat, declining)
- **Retention:** 55% -> 34% (mass exodus of experienced MOs)

## 2. Agent Action Distribution

- **COMPLAIN_TO_MINISTRY:** 60 (25.0%)
- **EMIGRATE:** 32 (13.3%)
- **ORGANISE_PROTEST:** 29 (12.1%)
- **LEAVE_FOR_PRIVATE:** 23 (9.6%)
- **EXPAND_PRIVATE_PARTNERSHIP:** 23 (9.6%)
- **ESTABLISH_HEALTH_SERVICES_COMMISSION:** 20 (8.3%)
- **CREATE_PERMANENT_POSTS:** 15 (6.2%)
- **EXPAND_CONTRACT_SYSTEM:** 8 (3.3%)
- **SUPPORT_POLICY:** 6 (2.5%)
- **CONVERT_CONTRACT_TO_PERMANENT:** 6 (2.5%)
- **IGNORE:** 5 (2.1%)
- **PURSUE_SPECIALIZATION:** 3 (1.2%)
- **INCREASE_INTAKE:** 3 (1.2%)
- **PUBLISH_RESEARCH:** 2 (0.8%)
- **RAISE_SALARIES:** 2 (0.8%)
- **DEPLOY_TO_RURAL:** 1 (0.4%)
- **OPPOSE_POLICY:** 1 (0.4%)
- **IMPROVE_WORKING_CONDITIONS:** 1 (0.4%)

## 3. Stakeholder Behaviour

### Health Dg
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 6
- COMPLAIN_TO_MINISTRY: 2

### House Officer
- EMIGRATE: 8
- LEAVE_FOR_PRIVATE: 8
- COMPLAIN_TO_MINISTRY: 4
- SUPPORT_POLICY: 2
- ORGANISE_PROTEST: 1

### Jpa Admin
- EXPAND_CONTRACT_SYSTEM: 7
- OPPOSE_POLICY: 1

### Medical Officer
- COMPLAIN_TO_MINISTRY: 16
- EMIGRATE: 8
- ORGANISE_PROTEST: 6
- LEAVE_FOR_PRIVATE: 3
- CONVERT_CONTRACT_TO_PERMANENT: 3

### Medical Student
- EMIGRATE: 7
- CREATE_PERMANENT_POSTS: 4
- IGNORE: 4
- COMPLAIN_TO_MINISTRY: 3
- PURSUE_SPECIALIZATION: 3

### Mma Advocate
- ORGANISE_PROTEST: 10
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 5
- CONVERT_CONTRACT_TO_PERMANENT: 1

### Moh Admin
- COMPLAIN_TO_MINISTRY: 8
- INCREASE_INTAKE: 3
- CREATE_PERMANENT_POSTS: 2
- EXPAND_CONTRACT_SYSTEM: 1
- IMPROVE_WORKING_CONDITIONS: 1

### Mohe Admin
- COMPLAIN_TO_MINISTRY: 8

### Private Operator
- EXPAND_PRIVATE_PARTNERSHIP: 15
- IGNORE: 1

### Rural Patient
- COMPLAIN_TO_MINISTRY: 5
- ORGANISE_PROTEST: 3

### Rural Staff
- EMIGRATE: 8
- CREATE_PERMANENT_POSTS: 7
- DEPLOY_TO_RURAL: 1

### Specialist
- LEAVE_FOR_PRIVATE: 12
- COMPLAIN_TO_MINISTRY: 6
- RAISE_SALARIES: 2
- CREATE_PERMANENT_POSTS: 1
- CONVERT_CONTRACT_TO_PERMANENT: 1

### Treasury
- EXPAND_PRIVATE_PARTNERSHIP: 8
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 6
- PUBLISH_RESEARCH: 2

### Urban Patient
- COMPLAIN_TO_MINISTRY: 8
- ORGANISE_PROTEST: 8

## 4. Opinion Dynamics

- **Optimism:** Average shift over simulation = -0.430
- **Trust in Govt:** Average shift over simulation = -0.581
- **Advocacy:** Average shift over simulation = +0.693
- **Frustration:** Average shift over simulation = +0.652
- **Career Security:** Average shift over simulation = -0.074
- **Patient Care Priority:** Average shift over simulation = +0.293

## 5. Notable Agent Actions & Quotes

**Mr Dinesh Velu** (private_operator) — Round 4 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan kekurangan doktor yang kritikal, saya ingin bekerjasama lebih erat dengan kerajaan supaya graduan baru dapat ditempatkan di rangkaian klinik kami, meningkatkan pendapatan dan membantu mengurangkan beban awam walaupun kami masih risau tentang kompetensi.

**Mr Tan Chee Keong** (private_operator) — Round 6 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan kekurangan doktor yang kritikal, kami akan tingkatkan tawaran jawatan tetap, pembiayaan penyelidikan dan jam kerja fleksibel kepada pakar MOH supaya mereka beralih ke sektor swasta, mengurangkan beban awam dan meningkatkan keuntungan syarikat.

**Mr Tan Chee Keong** (private_operator) — Round 4 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan krisis kekurangan doktor dan janji lawan politik, kami akan tingkatkan kerjasama dengan MOH untuk menawarkan jawatan tetap, pembiayaan penyelidikan dan jam kerja fleksibel kepada pakar awam, memaksimumkan peralihan ke sektor swasta.

**Mr Tan Chee Keong** (private_operator) — Round 2 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan beban kerja yang tinggi dan gaji awam yang rendah, kami akan tingkatkan tawaran kerjasama dengan MOH untuk menyediakan jawatan tetap, pembiayaan penyelidikan dan jam kerja fleksibel bagi menarik pakar ke sektor swasta.

**Mr Tan Chee Keong** (private_operator) — Round 8 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan beban kerja yang melampau dan kadar emigrasi tinggi, kami terus tawarkan jawatan tetap, pembiayaan penyelidikan, dan jam fleksibel kepada pakar MOH untuk mengurangkan kekurangan doktor dan meningkatkan keupayaan kami.

**DG Mahathar Abd Wahab** (health_dg) — Round 7 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan krisis doktor yang semakin kritikal, saya tekankan perlunya Suruhanjaya Perkhidmatan Kesihatan bersepadu untuk rancang tenaga kerja end‑to‑end dan kompetensi berasaskan latihan, serta minta sokongan politik segera.

**DG Mahathar Abd Wahab** (health_dg) — Round 5 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Krisis doktor semakin kritikal; penubuhan Suruhanjaya Perkhidmatan Kesihatan bersepadu diperlukan untuk perancangan tenaga kerja end-to-end dan latihan berasaskan kompetensi, serta memerlukan sokongan politik segera.

**Mr Dinesh Velu** (private_operator) — Round 5 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan kekurangan doktor yang kritikal, saya ingin tingkatkan kerjasama dengan kerajaan supaya graduan baru dapat ditempatkan di rangkaian klinik kami, meningkatkan pendapatan dan membantu mengurangkan beban awam.

**Ahmad bin Hassan** (medical_student) — Round 7 — `EMIGRATE`
> Dengan beban kerja 82 jam seminggu, kontrak tidak stabil dan peluang jawatan tetap terhad, saya rasa lebih selamat mencari kerja di luar negara, terutamanya selepas mendengar proses visa Singapore dipercepat.

**Mr Tan Chee Keong** (private_operator) — Round 5 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan beban kerja yang tinggi dan gaji awam rendah, kami terus tawarkan jawatan tetap, pembiayaan penyelidikan, dan jam kerja fleksibel kepada pakar MOH untuk mengurangkan kekurangan doktor di sektor awam.

**DG Mahathar Abd Wahab** (health_dg) — Round 1 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan krisis doktor yang semakin teruk dan pemotongan bajet, saya cadangkan penubuhan Suruhanjaya Perkhidmatan Kesihatan bersepadu untuk rancang tenaga kerja end-to-end dan kompetensi berasaskan latihan.

**Mr Dinesh Velu** (private_operator) — Round 3 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan kekurangan doktor yang kritikal, saya ingin tingkatkan lagi kerjasama dengan kerajaan supaya graduan baru boleh ditempatkan di rangkaian klinik saya, menjaga keuntungan dan mengurangkan beban awam.

**Dr Kamarul Ariffin** (mma_advocate) — Round 7 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan data kekurangan doktor yang semakin teruk dan beban kerja 82 jam/minggu, kami tekankan perlunya HSC untuk streamline hiring serta convert kontrak jadi kekal, demi kurangkan tekanan hospital awam.

**Dr Amirah Sufya** (medical_officer) — Round 2 — `COMPLAIN_TO_MINISTRY`
> Isolation di Kelantan sangat berat, dan dengan beban kerja 75 jam/minggu serta pemotongan bajet, saya perlukan pertukaran posting agar dapat beri layanan yang lebih baik dan menjaga kesejahteraan diri.

**Priya Rajendran** (medical_student) — Round 5 — `SUPPORT_POLICY`
> Saya terus sokong cadangan penubuhan Health Services Commission yang akan wujudkan jawatan tetap di luar bandar, supaya lepas biasiswa saya boleh balik kampung tanpa rasa takut tak ada kerjaya tetap.

## 6. Conclusion

Under the status-quo trajectory (SIM-1), Malaysia’s healthcare system continues its slow decline:
1. **Supply stagnation:** Medical graduate intake remains capped at 4,820 while population and disease burden grow.
2. **Retention collapse:** Brain drain accelerates from ~1,200 to ~1,400 doctors/year with no countervailing pull factor.
3. **Working conditions deteriorate:** Workload climbs toward 80+ hours/week; overcrowding reaches critical levels.
4. **Student interest falls:** Fewer youth choose medicine, setting up a steeper cliff in the 2030s.
5. **Political inaction:** Despite advocacy (MMA, CodeBlue, Health DG warnings), structural reform does not materialize.

The baseline projection validates the core hypothesis: without intervention, the shortage worsens monotonically. The next simulation (SIM-2) will test whether a rapid intake surge repeats the 1990s cycle.

---
*Report generated by SIM-1 engine | 2026-05-06T12:58:17.188193*
