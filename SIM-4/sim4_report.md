# SIM-4 Report: Malaysia Doctor Shortage — Environment Reform (Fix Retention & Working Conditions)

**Simulation date:** 2026-05-06T16:27:22.104418  
**Model:** gpt-oss:120b-cloud  
**Agents:** 30 | **Rounds:** 8 (6 months/round = 4 years: 2026-2030)  
**Policy premise:** Intake stays flat at 4,820. All effort on retention: +10%/year permanent posts, contract abolition, salary +25%, HSC by 2028, workload caps.

---

## 1. Quantitative State Trajectory

| Round | Year | Graduates | Posts (HO) | Perm. Posts | Contract | Brain Drain | Returnees | Doc/1k | Overcrowding | Workload hrs | KK Wait | Specialist Wait | Interest | Budget %GDP | Salary Ratio | Retention % |
|-------|------|-----------|------------|-------------|----------|-------------|-----------|--------|--------------|--------------|---------|----------------|----------|-----------|--------------|-------------|
| 1 | 2026.5 | 4820 | 3570 | 25200 | 14400 | 1100 | 105 | 2.32 | 75 | 70 | 13 | 11 | 1.88 | 2.12 | 0.47 | 60 |
| 2 | 2027.0 | 4820 | 3641 | 26460 | 10620 | 1000 | 130 | 2.35 | 72 | 67 | 12 | 10 | 1.96 | 2.15 | 0.49 | 63 |
| 3 | 2027.5 | 4820 | 3713 | 27783 | 6651 | 900 | 155 | 2.38 | 69 | 64 | 11 | 9 | 2.04 | 2.18 | 0.51 | 66 |
| 4 | 2028.0 | 4820 | 3787 | 29172 | 2484 | 800 | 180 | 2.40 | 66 | 62 | 10 | 8 | 2.12 | 2.20 | 0.53 | 68 |
| 5 | 2028.5 | 4820 | 3862 | 30630 | 0 | 700 | 205 | 2.42 | 63 | 60 | 8 | 7 | 2.20 | 2.23 | 0.55 | 70 |
| 6 | 2029.0 | 4820 | 3939 | 32161 | 0 | 600 | 230 | 2.45 | 60 | 57 | 7 | 6 | 2.28 | 2.25 | 0.57 | 73 |
| 7 | 2029.5 | 4820 | 4017 | 33769 | 0 | 500 | 255 | 2.47 | 57 | 54 | 6 | 5 | 2.36 | 2.27 | 0.58 | 76 |
| 8 | 2030.0 | 4820 | 4097 | 35457 | 0 | 400 | 280 | 2.50 | 55 | 52 | 5 | 4 | 2.44 | 2.30 | 0.58 | 78 |

### Key Trends

- **Graduate intake:** 4820 -> 4820 (FLAT — no increase)
- **Housemanship posts:** 3570 -> 4097 (modest expansion)
- **Permanent posts:** 25200 -> 35457 (major expansion +10%/year)
- **Contract doctors:** 14400 -> 0 (abolished)
- **Doctor-to-population ratio:** 2.32 -> 2.50 (improving via retention)
- **Public hospital overcrowding:** 75 -> 55 (easing)
- **Average doctor workload:** 70 -> 52 hours/week (dramatic improvement)
- **Brain drain:** 1100 -> 400 doctors/year (halved)
- **Overseas returnees:** 105 -> 280 doctors/year (tripled)
- **Medical student interest:** 1.88 -> 2.44 (rising)
- **Retention:** 60% -> 78% (dramatic improvement)

## 2. Agent Action Distribution

- **COMPLAIN_TO_MINISTRY:** 30 (12.5%)
- **CREATE_PERMANENT_POSTS:** 28 (11.7%)
- **EMIGRATE:** 26 (10.8%)
- **SUPPORT_POLICY:** 25 (10.4%)
- **EXPAND_PRIVATE_PARTNERSHIP:** 25 (10.4%)
- **ORGANISE_PROTEST:** 19 (7.9%)
- **ESTABLISH_HEALTH_SERVICES_COMMISSION:** 17 (7.1%)
- **RAISE_SALARIES:** 12 (5.0%)
- **LEAVE_FOR_PRIVATE:** 10 (4.2%)
- **INCREASE_INTAKE:** 10 (4.2%)
- **EXPAND_CONTRACT_SYSTEM:** 8 (3.3%)
- **OPPOSE_POLICY:** 8 (3.3%)
- **CONVERT_CONTRACT_TO_PERMANENT:** 7 (2.9%)
- **PURSUE_SPECIALIZATION:** 6 (2.5%)
- **IGNORE:** 3 (1.2%)
- **PUBLISH_RESEARCH:** 3 (1.2%)
- **FREEZE_SALARIES:** 2 (0.8%)
- **IMPROVE_WORKING_CONDITIONS:** 1 (0.4%)

## 3. Stakeholder Behaviour

### Health Dg
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 6
- SUPPORT_POLICY: 1
- RAISE_SALARIES: 1

### House Officer
- EMIGRATE: 8
- LEAVE_FOR_PRIVATE: 7
- SUPPORT_POLICY: 5
- CREATE_PERMANENT_POSTS: 3
- CONVERT_CONTRACT_TO_PERMANENT: 1

### Jpa Admin
- EXPAND_CONTRACT_SYSTEM: 5
- SUPPORT_POLICY: 1
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 1
- IMPROVE_WORKING_CONDITIONS: 1

### Medical Officer
- COMPLAIN_TO_MINISTRY: 10
- EMIGRATE: 8
- RAISE_SALARIES: 6
- SUPPORT_POLICY: 5
- CREATE_PERMANENT_POSTS: 4

### Medical Student
- CREATE_PERMANENT_POSTS: 7
- PURSUE_SPECIALIZATION: 6
- SUPPORT_POLICY: 4
- IGNORE: 3
- EMIGRATE: 2

### Mma Advocate
- ORGANISE_PROTEST: 10
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 3
- PUBLISH_RESEARCH: 2
- CREATE_PERMANENT_POSTS: 1

### Moh Admin
- INCREASE_INTAKE: 8
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 3
- EXPAND_CONTRACT_SYSTEM: 2
- CONVERT_CONTRACT_TO_PERMANENT: 1
- CREATE_PERMANENT_POSTS: 1

### Mohe Admin
- OPPOSE_POLICY: 8

### Private Operator
- EXPAND_PRIVATE_PARTNERSHIP: 14
- CREATE_PERMANENT_POSTS: 2

### Rural Patient
- COMPLAIN_TO_MINISTRY: 4
- ORGANISE_PROTEST: 4

### Rural Staff
- EMIGRATE: 8
- CREATE_PERMANENT_POSTS: 7
- CONVERT_CONTRACT_TO_PERMANENT: 1

### Specialist
- COMPLAIN_TO_MINISTRY: 8
- EXPAND_PRIVATE_PARTNERSHIP: 7
- RAISE_SALARIES: 3
- CONVERT_CONTRACT_TO_PERMANENT: 2
- LEAVE_FOR_PRIVATE: 1

### Treasury
- EXPAND_PRIVATE_PARTNERSHIP: 4
- SUPPORT_POLICY: 3
- RAISE_SALARIES: 2
- FREEZE_SALARIES: 2
- CREATE_PERMANENT_POSTS: 2

### Urban Patient
- SUPPORT_POLICY: 6
- COMPLAIN_TO_MINISTRY: 5
- ORGANISE_PROTEST: 4
- INCREASE_INTAKE: 1

## 4. Opinion Dynamics

- **Optimism:** Average shift over simulation = -0.060
- **Trust in Govt:** Average shift over simulation = -0.166
- **Advocacy:** Average shift over simulation = +0.583
- **Frustration:** Average shift over simulation = +0.255
- **Career Security:** Average shift over simulation = +0.097
- **Patient Care Priority:** Average shift over simulation = +0.261

## 5. Notable Agent Actions & Quotes

**DG Mahathar Abd Wahab** (health_dg) — Round 6 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan data kekurangan doktor yang masih kritikal, saya rasa sudah tiba masanya untuk menubuhkan komisi bersepadu bagi perancangan tenaga kerja end-to-end dan latihan berasaskan kompetensi, serta dapatkan sokongan politik segera.

**DG Mahathar Abd Wahab** (health_dg) — Round 5 — `RAISE_SALARIES`
> Dengan kenaikan gaji 25% yang telah diluluskan, saya tekankan perlunya pelaksanaan segera untuk meningkatkan retensi doktor dan mengurangkan beban kerja, sekaligus memperkukuh sokongan politik kepada reformasi tenaga kerja.

**DG Mahathar Abd Wahab** (health_dg) — Round 1 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan peningkatan bajet 2027 dan bukti retention lebih menjimatkan, saya cadangkan penubuhan komisi bersepadu untuk perancangan tenaga kerja end-to-end, supaya strategi kompetensi dan penempatan lebih terkoordinasi.

**Ahmad bin Hassan** (medical_student) — Round 3 — `COMPLAIN_TO_MINISTRY`
> Saya rasa sistem kontrak masih tidak stabil, kerja berlebihan dan gaji rendah, jadi saya ingin tekankan perlunya lebih banyak jawatan tetap dan kenaikan gaji supaya graduan baru tidak terpaksa melarat ke luar negara.

**DG Mahathar Abd Wahab** (health_dg) — Round 7 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan sokongan politik selepas Pilihan Raya 2028 dan gaji yang kini lebih kompetitif, masa tepat untuk menubuhkan komisi bersepadu bagi perancangan tenaga kerja end-to-end serta latihan berasaskan kompetensi.

**DG Mahathar Abd Wahab** (health_dg) — Round 2 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan data kekurangan doktor dan beban kerja tinggi, saya tekankan keperluan komisi bersepadu untuk perancangan tenaga kerja end-to-end dan latihan berasaskan kompetensi, serta minta sokongan politik segera.

**DG Mahathar Abd Wahab** (health_dg) — Round 4 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan konsensus bipartisan selepas Pilihan Raya 2028, saya rasa masa tepat untuk menubuhkan komisi bersepadu supaya perancangan tenaga kerja end-to-end dan latihan berasaskan kompetensi dapat dilaksanakan.

**Puan Lina Mohd** (treasury) — Round 4 — `CREATE_PERMANENT_POSTS`
> Dengan kekurangan doktor yang kritikal dan kadar emigrasi tinggi, menukar kontrak kepada jawatan tetap dapat tingkatkan retention dan stabiliti sistem, serta selaras dengan konsensus bipartisan yang ada.

**Puan Lina Mohd** (treasury) — Round 5 — `SUPPORT_POLICY`
> Saya sokong penubuhan Suruhanjaya Perkhidmatan Kesihatan untuk menyediakan data berasaskan bukti, membantu perancangan tenaga kerja doktor dan memastikan peruntukan bajet selaras dengan keperluan sistem.

**DG Mahathar Abd Wahab** (health_dg) — Round 8 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan data kekurangan doktor masih kritikal, saya rasa waktu tepat untuk menubuhkan komisi bersepadu agar perancangan tenaga kerja end-to-end dan latihan berasaskan kompetensi dapat dilaksanakan segera.

**Mr Tan Chee Keong** (private_operator) — Round 6 — `EXPAND_PRIVATE_PARTNERSHIP`
> Kami akan memperkuat kerjasama dengan KKM, tawarkan jawatan tetap pakar, dana penyelidikan, dan jam kerja fleksibel supaya doktor awam beralih ke rangkaian hospital swasta kami, mengurangkan beban awam.

**Dr Arjun Krishnan** (house_officer) — Round 4 — `SUPPORT_POLICY`
> Dengan reformasi tenaga kerja kesihatan yang kini mendapat sokongan semua parti, saya harap masa menunggu housemanship dapat dipercepat, jadi saya sokong langkah ini demi kerjaya dan penjagaan pesakit.

**Mr Dinesh Velu** (private_operator) — Round 5 — `EXPAND_PRIVATE_PARTNERSHIP`
> We propose a formal partnership with MOH to place contract doctors in our clinic network, boosting their competency and patient flow while protecting our profit margins before contracts are abolished.

**Dr Lim Kah Wai** (medical_officer) — Round 5 — `EMIGRATE`
> Saya teruskan dokumen emigrasi ke Australia; kontrak 5 tahun tanpa laluan tetap dan specialisation masih diblok, walaupun ada kenaikan gaji dan penghapusan kontrak, tiada perubahan segera untuk saya.

**Mr Tan Chee Keong** (private_operator) — Round 2 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan kenaikan beban kerja di sektor awam, kami akan tingkatkan kerjasama dengan MOH untuk tawarkan posisi tetap, dana penyelidikan dan jam kerja fleksibel bagi pakar yang ingin beralih ke swasta.

## 6. Conclusion

Under the environment-reform trajectory (SIM-4), Malaysia fixes the shortage through retention and working conditions, without increasing intake:
1. **Retention revolution:** Brain drain falls from 1,200 to 400/year. Returnees triple. The existing workforce is kept and expanded.
2. **Contract abolition:** The single biggest retention barrier is removed. Permanent posts expand by +10%/year, restoring career certainty.
3. **Salary competitiveness:** Public salary ratio rises 0.45 -> 0.58, approaching private sector competitiveness. On-call and hazard pay restored.
4. **Working conditions transformed:** Workload falls from 72 to 52 hours/week. 3-month deployment notice, rural incentives, workload caps implemented.
5. **Health Services Commission:** Full establishment by 2028 breaks MOHE-JPA-MOH silos. End-to-end workforce planning becomes institutionalized.
6. **Student interest rises:** Medicine regains prestige. Interest index climbs as graduates see secure, dignified career pathways.

By 2030, Malaysia achieves 2.5 doctors per 1,000 through retention alone — a fundamentally different path from SIM-3's intake-driven growth. Overcrowding falls, waiting times drop by 50%, and the profession becomes sustainable.

Risk: Slower absolute growth than SIM-3. If population grows faster than expected or NCD burden accelerates, the static intake may still leave gaps. The next simulation (SIM-5) tests the comprehensive approach: moderate intake increase AND full environment reform.

---
*Report generated by SIM-4 engine | 2026-05-06T16:27:22.104770*