# SIM-2 Report: Malaysia Doctor Shortage — Intake Surge (Repeat 1990s)

**Simulation date:** 2026-05-06T13:54:34.513338  
**Model:** gpt-oss:120b-cloud  
**Agents:** 30 | **Rounds:** 8 (6 months/round = 4 years: 2026-2030)  
**Policy premise:** Government panics, expands intake to 8,000+/year. No parallel post creation. Contract system massively expanded.

---

## 1. Quantitative State Trajectory

| Round | Year | Graduates | Posts (HO) | Perm. Posts | Contract | Brain Drain | Returnees | Doc/1k | Overcrowding | Workload hrs | KK Wait | Specialist Wait | Interest | Budget %GDP | Salary Ratio | Retention % | HO Waitlist (mo) | Unemployed Grads |
|-------|------|-----------|------------|-------------|----------|-------------|-----------|--------|--------------|--------------|---------|----------------|----------|-----------|--------------|-------------|------------------|------------------|
| 1 | 2026.5 | 5302 | 3605 | 24240 | 19358 | 1550 | 45 | 2.33 | 74 | 70 | 15 | 13 | 1.95 | 2.08 | 0.43 | 53 | 42.4 | 848 |
| 2 | 2027.0 | 5832 | 3713 | 24482 | 21053 | 1600 | 40 | 2.36 | 70 | 68 | 16 | 14 | 2.25 | 2.06 | 0.42 | 48 | 105.9 | 2119 |
| 3 | 2027.5 | 6415 | 3825 | 24727 | 23125 | 1650 | 35 | 2.39 | 76 | 72 | 18 | 16 | 2.05 | 2.04 | 0.41 | 43 | 194.3 | 3886 |
| 4 | 2028.0 | 7056 | 3939 | 24974 | 25618 | 1700 | 30 | 2.35 | 82 | 76 | 19 | 17 | 1.65 | 1.92 | 0.39 | 38 | 311.7 | 6233 |
| 5 | 2028.5 | 7761 | 4057 | 25224 | 28581 | 1750 | 25 | 2.30 | 88 | 80 | 20 | 18 | 1.05 | 1.89 | 0.38 | 33 | 462.9 | 9259 |
| 6 | 2029.0 | 8000 | 4179 | 25476 | 31638 | 1800 | 20 | 2.25 | 94 | 84 | 21 | 19 | 0.80 | 1.86 | 0.36 | 28 | 573.1 | 11462 |
| 7 | 2029.5 | 8000 | 4305 | 25731 | 34594 | 1850 | 20 | 2.20 | 100 | 88 | 22 | 20 | 0.80 | 1.83 | 0.35 | 23 | 646.7 | 12934 |
| 8 | 2030.0 | 8000 | 4434 | 25989 | 37447 | 1900 | 20 | 2.15 | 100 | 92 | 24 | 22 | 0.80 | 1.80 | 0.33 | 20 | 713.3 | 14265 |

### Key Trends

- **Graduate intake:** 5302 -> 8000 (massive expansion)
- **Housemanship waitlist:** 42.4 -> 713.3 months (bottleneck)
- **Unemployed graduates:** 848.5 -> 14265.218860573375 (glut forming)
- **Doctor-to-population ratio:** 2.33 -> 2.15 (initial rise then crash)
- **Public hospital overcrowding:** 74 -> 100 (reversal then surge)
- **Average doctor workload:** 70 -> 92 hours/week (chaos)
- **Brain drain:** 1550 -> 1900 doctors/year (accelerating)
- **Medical student interest:** 1.95 -> 0.80 (boom then bust)
- **Retention:** 53% -> 20% (mass exodus)

## 2. Agent Action Distribution

- **EMIGRATE:** 35 (14.6%)
- **CREATE_PERMANENT_POSTS:** 31 (12.9%)
- **COMPLAIN_TO_MINISTRY:** 28 (11.7%)
- **ORGANISE_PROTEST:** 25 (10.4%)
- **LEAVE_FOR_PRIVATE:** 18 (7.5%)
- **EXPAND_PRIVATE_PARTNERSHIP:** 16 (6.7%)
- **EXPAND_CONTRACT_SYSTEM:** 14 (5.8%)
- **RAISE_SALARIES:** 13 (5.4%)
- **ESTABLISH_HEALTH_SERVICES_COMMISSION:** 13 (5.4%)
- **CONVERT_CONTRACT_TO_PERMANENT:** 9 (3.8%)
- **SUPPORT_POLICY:** 8 (3.3%)
- **OPPOSE_POLICY:** 8 (3.3%)
- **PUBLISH_RESEARCH:** 7 (2.9%)
- **PURSUE_SPECIALIZATION:** 5 (2.1%)
- **DEPLOY_TO_RURAL:** 5 (2.1%)
- **DECREASE_INTAKE:** 3 (1.2%)
- **INCREASE_INTAKE:** 1 (0.4%)
- **IMPROVE_WORKING_CONDITIONS:** 1 (0.4%)

## 3. Stakeholder Behaviour

### Health Dg
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 8

### House Officer
- EMIGRATE: 8
- LEAVE_FOR_PRIVATE: 8
- COMPLAIN_TO_MINISTRY: 4
- CREATE_PERMANENT_POSTS: 3
- ORGANISE_PROTEST: 1

### Jpa Admin
- EXPAND_CONTRACT_SYSTEM: 7
- COMPLAIN_TO_MINISTRY: 1

### Medical Officer
- COMPLAIN_TO_MINISTRY: 10
- EMIGRATE: 8
- CREATE_PERMANENT_POSTS: 8
- CONVERT_CONTRACT_TO_PERMANENT: 5
- RAISE_SALARIES: 4

### Medical Student
- EMIGRATE: 11
- SUPPORT_POLICY: 8
- PURSUE_SPECIALIZATION: 5

### Mma Advocate
- ORGANISE_PROTEST: 10
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 4
- CONVERT_CONTRACT_TO_PERMANENT: 2

### Moh Admin
- EXPAND_CONTRACT_SYSTEM: 7
- CREATE_PERMANENT_POSTS: 6
- DECREASE_INTAKE: 2
- IMPROVE_WORKING_CONDITIONS: 1

### Mohe Admin
- OPPOSE_POLICY: 8

### Private Operator
- CREATE_PERMANENT_POSTS: 8
- EXPAND_PRIVATE_PARTNERSHIP: 8

### Rural Patient
- DEPLOY_TO_RURAL: 3
- COMPLAIN_TO_MINISTRY: 3
- ORGANISE_PROTEST: 2

### Rural Staff
- EMIGRATE: 8
- CREATE_PERMANENT_POSTS: 4
- DEPLOY_TO_RURAL: 2
- CONVERT_CONTRACT_TO_PERMANENT: 2

### Specialist
- RAISE_SALARIES: 9
- LEAVE_FOR_PRIVATE: 8
- COMPLAIN_TO_MINISTRY: 3
- ORGANISE_PROTEST: 2
- CREATE_PERMANENT_POSTS: 1

### Treasury
- EXPAND_PRIVATE_PARTNERSHIP: 7
- PUBLISH_RESEARCH: 7
- CREATE_PERMANENT_POSTS: 1
- DECREASE_INTAKE: 1

### Urban Patient
- ORGANISE_PROTEST: 8
- COMPLAIN_TO_MINISTRY: 7
- INCREASE_INTAKE: 1

## 4. Opinion Dynamics

- **Optimism:** Average shift over simulation = -0.355
- **Trust in Govt:** Average shift over simulation = -0.531
- **Advocacy:** Average shift over simulation = +0.659
- **Frustration:** Average shift over simulation = +0.585
- **Career Security:** Average shift over simulation = -0.046
- **Patient Care Priority:** Average shift over simulation = +0.306

## 5. Notable Agent Actions & Quotes

**Mr Dinesh Velu** (private_operator) — Round 5 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan banyak graduan menganggur dan klinik kami perlukan staf, kita perlu gandakan kerjasama dengan kerajaan untuk ambil mereka sambil tingkatkan cek kompetensi, supaya kualiti terjaga dan perniagaan terus menguntungkan.

**Dr Farah Nabila** (medical_officer) — Round 7 — `EXPAND_PRIVATE_PARTNERSHIP`
> Kerana kontrak tiada cuti bersalin, saya lihat hospital swasta lebih selamat untuk keluarga; memperluas kerjasama swasta boleh beri lebih banyak jawatan tetap dengan faedah yang lebih baik dan kurangkan beban awam.

**Mr Dinesh Velu** (private_operator) — Round 8 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan 14,265 graduan menganggur, kami akan gandakan kerjasama dengan kerajaan untuk ambil mereka ke klinik sambil tingkatkan cek kompetensi, supaya perniagaan terus menguntungkan dan kualiti penjagaan terjaga.

**Puan Siti Norhayati** (moh_admin) — Round 1 — `CREATE_PERMANENT_POSTS`
> Dengan graduan 5302 dan housemanship post hanya 3605, perlu cipta lebih banyak jawatan tetap supaya doktor tidak terperangkap dalam kontrak atau menganggur, kurangkan beban kerja dan menurunkan kadar emigrasi.

**DG Mahathar Abd Wahab** (health_dg) — Round 1 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> We must set up a unified Health Services Commission to coordinate workforce planning, training, and service deployment; this will address the shortage and align the new medical schools with system needs.

**Puan Siti Norhayati** (moh_admin) — Round 7 — `CREATE_PERMANENT_POSTS`
> Dengan 500 doktor muda melamar visa Singapura, kita perlu segera cipta lebih banyak jawatan tetap supaya graduan tidak terperangkap dalam kontrak atau menganggur, dan kurangkan beban kerja serta emigasi.

**Puan Siti Norhayati** (moh_admin) — Round 5 — `DECREASE_INTAKE`
> Intake masih terlalu tinggi berbanding jawatan tetap dan housemanship, menyebabkan graduan menganggur dan beban kerja doktor melampau; kurangkan intake untuk selaraskan bekalan dengan permintaan.

**Dr Sarah Abdullah** (mma_advocate) — Round 2 — `ORGANISE_PROTEST`
> Dengan peningkatan intake tapi tiada jawatan tetap, doktor junior terpaksa menanggung beban kerja melampau; kami akan demonstrasi di depan Kementerian Kesihatan untuk tuntut penyelesaian segera.

**Dr Sarah Abdullah** (mma_advocate) — Round 8 — `ORGANISE_PROTEST`
> Dengan beban kerja 92 jam/minggu dan housemanship menunggu 713 bulan, kami akan demonstrasi di depan Kementerian Kesihatan untuk tuntut jawatan tetap serta kurangkan beban kerja junior doctors.

**Puan Siti Norhayati** (moh_admin) — Round 2 — `CREATE_PERMANENT_POSTS`
> Dengan intake MOHE naik ke 6,500, mesti cipta lebih banyak jawatan tetap supaya graduan tidak terperangkap dalam kontrak atau menganggur, kurangkan beban kerja dan tingkatkan layanan pesakit.

**Puan Lina Mohd** (treasury) — Round 2 — `PUBLISH_RESEARCH`
> Kita perlu sediakan data bukti kuat tentang jurang tenaga kerja sebelum meningkatkan intake, supaya Treasury dapat alokasikan bajet yang tepat dan MOH dapat merancang secara berasaskan bukti.

**Tuan Haji Ismail** (jpa_admin) — Round 7 — `EXPAND_CONTRACT_SYSTEM`
> Dengan kekangan jawatan tetap dan keperluan segera, menambah kontrak doktor ialah langkah paling praktikal untuk kurangkan beban kerja dan tampung graduan menganggur tanpa melanggar had post.

**Dr Sarah Abdullah** (mma_advocate) — Round 7 — `ORGANISE_PROTEST`
> Workload 88 jam/minggu, housemanship waiting list 646 bulan, kami tak boleh tunggu lagi – masa untuk demonstrasi di depan Kementerian Kesihatan tuntut jawatan tetap dan kurangkan beban kerja.

**Encik Rahimudin** (moh_admin) — Round 1 — `EXPAND_CONTRACT_SYSTEM`
> Dengan kekurangan doktor yang kritikal dan bajet terhad, kontrak sementara dapat ditambah cepat tanpa perlu kelulusan JPA penuh, membantu kurangkan beban kerja dan menurunkan waiting list.

**Dr Kamarul Ariffin** (mma_advocate) — Round 1 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Dengan pemotongan bajet 5% dan beban kerja melampau, MMA menuntut penubuhan Suruhanjaya Perkhidmatan Kesihatan untuk selesaikan krisis doktor dan tingkatkan hak kontrak ke jawatan tetap.

## 6. Conclusion

Under the intake-surge trajectory (SIM-2), Malaysia repeats the 1990s cycle almost exactly:
1. **Intake explosion:** Medical graduates surge from 4,820 to 8,000+/year without corresponding post creation.
2. **Bottleneck return:** Housemanship waitlist grows to 9+ months. Graduates queue for posts that don't exist.
3. **Contract glut 2.0:** Contract doctor numbers balloon toward 25,000+. Same frustration, same brain drain.
4. **Student interest boom-then-bust:** Initial surge in applications (shortage panic) collapses once glut reality hits.
5. **Political oscillation:** Government cycles between 'too few doctors' and 'too many doctors' without fixing structural posts.

By 2030, Malaysia has more graduates than posts, more contract doctors than permanent ones, and accelerating emigration. The system is poised for another moratorium by 2032-2035, recreating the exact pendulum that produced the 2026 shortage.

This validates the core warning: **intake changes without post/condition reform are oscillatory, not solutions.** The next simulation (SIM-3) tests whether matching intake to post creation prevents this cycle.

---
*Report generated by SIM-2 engine | 2026-05-06T13:54:34.513751*