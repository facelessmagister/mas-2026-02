# SIM-3 Report: Malaysia Doctor Shortage — Balanced Pipeline (Intake Matched to Posts)

**Simulation date:** 2026-05-06T15:39:28.897652  
**Model:** gpt-oss:120b-cloud  
**Agents:** 30 | **Rounds:** 8 (6 months/round = 4 years: 2026-2030)  
**Policy premise:** Intake rises moderately (4,820 -> 6,500) ONLY in lockstep with verified post creation. Contract system phased out. Salary +15%. Budget protected.

---

## 1. Quantitative State Trajectory

| Round | Year | Graduates | Posts (HO) | Perm. Posts | Contract | Brain Drain | Returnees | Doc/1k | Overcrowding | Workload hrs | KK Wait | Specialist Wait | Interest | Budget %GDP | Salary Ratio | Retention % |
|-------|------|-----------|------------|-------------|----------|-------------|-----------|--------|--------------|--------------|---------|----------------|----------|-----------|--------------|-------------|
| 1 | 2026.5 | 5133 | 3762 | 24960 | 15600 | 1150 | 95 | 2.33 | 76 | 70 | 13 | 11 | 1.75 | 2.10 | 0.47 | 60 |
| 2 | 2027.0 | 5466 | 4044 | 25958 | 13105 | 1100 | 110 | 2.36 | 73 | 68 | 12 | 10 | 1.70 | 2.10 | 0.49 | 62 |
| 3 | 2027.5 | 5821 | 4347 | 26996 | 10510 | 1050 | 125 | 2.39 | 70 | 67 | 11 | 10 | 1.76 | 2.10 | 0.50 | 63 |
| 4 | 2028.0 | 6199 | 4673 | 28075 | 7813 | 1000 | 140 | 2.42 | 68 | 65 | 10 | 9 | 1.82 | 2.10 | 0.52 | 65 |
| 5 | 2028.5 | 6500 | 5023 | 29198 | 5006 | 950 | 155 | 2.45 | 66 | 63 | 10 | 8 | 1.88 | 2.10 | 0.54 | 67 |
| 6 | 2029.0 | 6500 | 5399 | 30365 | 5000 | 900 | 170 | 2.48 | 63 | 61 | 9 | 7 | 1.94 | 2.10 | 0.55 | 69 |
| 7 | 2029.5 | 6500 | 5803 | 31579 | 5000 | 850 | 185 | 2.51 | 60 | 59 | 8 | 6 | 2.00 | 2.10 | 0.55 | 71 |
| 8 | 2030.0 | 6500 | 6238 | 32842 | 5000 | 800 | 200 | 2.54 | 58 | 58 | 7 | 6 | 2.06 | 2.10 | 0.55 | 72 |

### Key Trends

- **Graduate intake:** 5133 -> 6500 (measured expansion)
- **Housemanship posts:** 3762 -> 6238 (matched to graduates)
- **Permanent posts:** 24960 -> 32842 (major expansion)
- **Contract doctors:** 15600 -> 5000 (phased out)
- **Doctor-to-population ratio:** 2.33 -> 2.54 (steady improvement)
- **Public hospital overcrowding:** 76 -> 58 (easing)
- **Average doctor workload:** 70 -> 58 hours/week (improving)
- **Brain drain:** 1150 -> 800 doctors/year (declining)
- **Overseas returnees:** 95 -> 200 doctors/year (rising)
- **Medical student interest:** 1.75 -> 2.06 (recovering)
- **Retention:** 60% -> 72% (improving)

## 2. Agent Action Distribution

- **EMIGRATE:** 30 (12.5%)
- **COMPLAIN_TO_MINISTRY:** 30 (12.5%)
- **EXPAND_PRIVATE_PARTNERSHIP:** 30 (12.5%)
- **CREATE_PERMANENT_POSTS:** 22 (9.2%)
- **ESTABLISH_HEALTH_SERVICES_COMMISSION:** 22 (9.2%)
- **LEAVE_FOR_PRIVATE:** 16 (6.7%)
- **EXPAND_CONTRACT_SYSTEM:** 15 (6.2%)
- **ORGANISE_PROTEST:** 12 (5.0%)
- **CONVERT_CONTRACT_TO_PERMANENT:** 11 (4.6%)
- **RAISE_SALARIES:** 11 (4.6%)
- **SUPPORT_POLICY:** 10 (4.2%)
- **DEPLOY_TO_RURAL:** 9 (3.8%)
- **OPPOSE_POLICY:** 8 (3.3%)
- **PURSUE_SPECIALIZATION:** 6 (2.5%)
- **IMPROVE_WORKING_CONDITIONS:** 3 (1.2%)
- **IGNORE:** 2 (0.8%)
- **PUBLISH_RESEARCH:** 1 (0.4%)
- **DECREASE_INTAKE:** 1 (0.4%)
- **INCREASE_INTAKE:** 1 (0.4%)

## 3. Stakeholder Behaviour

### Health Dg
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 6
- CONVERT_CONTRACT_TO_PERMANENT: 1
- CREATE_PERMANENT_POSTS: 1

### House Officer
- EMIGRATE: 8
- LEAVE_FOR_PRIVATE: 8
- CREATE_PERMANENT_POSTS: 3
- COMPLAIN_TO_MINISTRY: 2
- SUPPORT_POLICY: 2

### Jpa Admin
- EXPAND_CONTRACT_SYSTEM: 8

### Medical Officer
- COMPLAIN_TO_MINISTRY: 9
- RAISE_SALARIES: 9
- EMIGRATE: 8
- CONVERT_CONTRACT_TO_PERMANENT: 7
- CREATE_PERMANENT_POSTS: 3

### Medical Student
- SUPPORT_POLICY: 8
- EMIGRATE: 6
- PURSUE_SPECIALIZATION: 6
- COMPLAIN_TO_MINISTRY: 2
- IGNORE: 2

### Mma Advocate
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 9
- ORGANISE_PROTEST: 7

### Moh Admin
- EXPAND_CONTRACT_SYSTEM: 6
- CREATE_PERMANENT_POSTS: 4
- COMPLAIN_TO_MINISTRY: 3
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 2
- DECREASE_INTAKE: 1

### Mohe Admin
- OPPOSE_POLICY: 8

### Private Operator
- EXPAND_PRIVATE_PARTNERSHIP: 14
- CREATE_PERMANENT_POSTS: 2

### Rural Patient
- DEPLOY_TO_RURAL: 8

### Rural Staff
- EMIGRATE: 8
- CREATE_PERMANENT_POSTS: 4
- CONVERT_CONTRACT_TO_PERMANENT: 2
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 1
- DEPLOY_TO_RURAL: 1

### Specialist
- EXPAND_PRIVATE_PARTNERSHIP: 8
- LEAVE_FOR_PRIVATE: 5
- CREATE_PERMANENT_POSTS: 4
- COMPLAIN_TO_MINISTRY: 3
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 2

### Treasury
- EXPAND_PRIVATE_PARTNERSHIP: 8
- IMPROVE_WORKING_CONDITIONS: 3
- PUBLISH_RESEARCH: 1
- CREATE_PERMANENT_POSTS: 1
- INCREASE_INTAKE: 1

### Urban Patient
- COMPLAIN_TO_MINISTRY: 11
- ORGANISE_PROTEST: 4
- RAISE_SALARIES: 1

## 4. Opinion Dynamics

- **Optimism:** Average shift over simulation = -0.168
- **Trust in Govt:** Average shift over simulation = -0.275
- **Advocacy:** Average shift over simulation = +0.574
- **Frustration:** Average shift over simulation = +0.355
- **Career Security:** Average shift over simulation = +0.042
- **Patient Care Priority:** Average shift over simulation = +0.272

## 5. Notable Agent Actions & Quotes

**DG Mahathar Abd Wahab** (health_dg) — Round 8 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan data shortage yang semakin kritikal, saya tekankan penubuhan Health Services Commission untuk koordinasi end-to-end workforce planning dan competency‑based training, supaya kita dapat atasi shortage dan tingkatkan retention.

**DG Mahathar Abd Wahab** (health_dg) — Round 3 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan graduate-to-post matching inisiatif berjalan, kita perlu koordinasi end-to-end workforce planning dan competency‑based training; Health Services Commission akan selesaikan shortage dan improve patient care.

**DG Mahathar Abd Wahab** (health_dg) — Round 6 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan data kekurangan doktor dan tekanan kerja, saya tekankan penubuhan Health Services Commission untuk koordinasi end‑to‑end workforce planning dan competency‑based training, supaya sistem lebih terintegrasi.

**DG Mahathar Abd Wahab** (health_dg) — Round 1 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan budget kesihatan terjamin, saya push penubuhan Health Services Commission untuk koordinasi end-to-end workforce planning dan competency‑based training, agar kita dapat atasi shortage dan overload doktor.

**Mr Khairul Anwar** (urban_patient) — Round 3 — `COMPLAIN_TO_MINISTRY`
> Terima kasih, tapi 8 jam menunggu di GH tak boleh diterima; insurans private mahal buat keluarga saya tertekan. Kerajaan perlu percepat kenaikan gaji doktor dan tingkatkan intake supaya layanan lebih cepat.

**Dr Rosmah Jali** (rural_staff) — Round 3 — `CREATE_PERMANENT_POSTS`
> Need lebih banyak jawatan tetap di klinik desa supaya beban kerja dapat dikurangkan dan rujukan specialist dipercepatkan; walaupun 1,500 kontrak dijadikan tetap, masih jauh kurang untuk 5,000 pesakit kami.

**Dr Hafiz Rahman** (specialist) — Round 3 — `LEAVE_FOR_PRIVATE`
> Saya sudah beri MOH sampai Disember untuk counter‑offer, tapi tanpa kenaikan gaji dan kondisi kerja yang lebih baik, saya akan terpaksa tinggalkan sektor awam ke rangkaian Singapore yang tawarkan 3x gaji.

**DG Mahathar Abd Wahab** (health_dg) — Round 4 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan sokongan bipartisan selepas pilihan raya 2028, saya menegaskan perlunya Health Services Commission untuk koordinasi end-to-end workforce planning dan competency‑based training demi atasi shortage.

**Dr Kamarul Ariffin** (mma_advocate) — Round 3 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Walaupun 1,500 kontrak doktor kini ditukar, masih ada keperluan kritikal untuk komisen bebas yang boleh selesaikan isu pengambilan, pengekalan, dan beban kerja doktor demi rawatan pesakit yang selamat.

**Puan Lina Mohd** (treasury) — Round 3 — `IMPROVE_WORKING_CONDITIONS`
> Meningkatkan kondisi kerja seperti jadual fleksibel, cuti yang lebih teratur, dan sokongan mental dapat meningkatkan retention tanpa beban fiskal besar, selaras dengan keperluan bukti dan target makro.

**Dr Rosmah Jali** (rural_staff) — Round 4 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan sokongan dua pihak selepas pilihan raya 2028, saya rasa penubuhan Suruhanjaya Perkhidmatan Kesihatan boleh selesaikan isu kekurangan doktor tetap di klinik desa dan mempercepat rujukan pakar.

**Dr Hafiz Rahman** (specialist) — Round 5 — `COMPLAIN_TO_MINISTRY`
> Walaupun ada kenaikan gaji 15% dalam rangka belanjawan, masih jauh daripada tawaran 3x di Singapore; saya perlukan kenaikan lebih signifikan dan penambahbaikan beban kerja sebelum membuat keputusan.

**Mr Tan Chee Keong** (private_operator) — Round 8 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan beban kerja tinggi dan gaji awam masih rendah, kami akan tingkatkan lagi tawaran post tetap, dana penyelidikan, dan jam kerja fleksibel untuk tarik lebih banyak pakar MOH ke sektor swasta.

**Mr Tan Chee Keong** (private_operator) — Round 6 — `CREATE_PERMANENT_POSTS`
> Beban kerja tinggi dan gaji awam rendah memaksa pakar MOH berpindah; kami akan tambah lagi post tetap dengan dana penyelidikan dan jam fleksibel untuk tarik lebih banyak doktor ke sektor swasta.

**Puan Siti Norhayati** (moh_admin) — Round 2 — `CREATE_PERMANENT_POSTS`
> Dengan intake naik ke 5,800 dan housemanship post tambahan, kita perlukan lebih banyak kedudukan tetap supaya graduan tidak terperangkap dalam sistem kontrak dan beban kerja dapat dikurangkan.

## 6. Conclusion

Under the balanced pipeline trajectory (SIM-3), Malaysia makes steady, non-cyclical progress:
1. **Measured intake expansion:** Medical graduates rise from 4,820 to 6,500, but each increase is gated on verified post creation.
2. **Post-graduate matching:** Housemanship posts grow from 3,500 to ~6,000, eliminating the bottleneck that produced the 2016 glut.
3. **Contract system phased out:** Permanent posts expand (+8%/year), converting contract doctors and restoring career certainty.
4. **Retention improves:** Brain drain falls from 1,200 to ~800/year. Overseas returnees rise as career pathways become predictable.
5. **Working conditions ease:** Workload falls from 72 to ~58 hours/week. Overcrowding eases toward sustainable levels.
6. **Student interest recovers:** After initial reform uncertainty, interest rebounds as medicine regains reputation as a secure career.

By 2030, Malaysia has avoided the boom-bust pendulum. The system is on a credible trajectory toward 3.0 doctors per 1,000 population by 2038. The key lesson: **intake changes are safe IF AND ONLY IF post creation, working conditions, and career pathways are reformed in parallel.**

Risk: This requires sustained political will. A change of government could freeze post creation while intake continues, recreating the structural mismatch. The next simulation (SIM-4) tests whether fixing retention and working conditions alone — without increasing intake — can also resolve the shortage.

---
*Report generated by SIM-3 engine | 2026-05-06T15:39:28.898044*