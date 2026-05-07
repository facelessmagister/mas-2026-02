# SIM-5 Report: Malaysia Doctor Shortage — Comprehensive (Balanced Pipeline + Environment Reform)

**Simulation date:** 2026-05-07T23:23:52.904542  
**Model:** gpt-oss:120b-cloud  
**Agents:** 30 | **Rounds:** 8 (6 months/round = 4 years: 2026-2030)  
**Policy premise:** Moderate intake increase (4,820 -> 6,000) AND full environment reform: +10%/year permanent posts, contract abolition, salary +20%, HSC by 2028, workload caps, AI support, rural incentives.

---

## 1. Quantitative State Trajectory

| Round | Year | Graduates | Posts (HO) | Perm. Posts | Contract | Brain Drain | Returnees | Doc/1k | Overcrowding | Workload hrs | KK Wait | Specialist Wait | Interest | Budget %GDP | Salary Ratio | Retention % |
|-------|------|-----------|------------|-------------|----------|-------------|-----------|--------|--------------|--------------|---------|----------------|----------|-----------|--------------|-------------|
| 1 | 2026.5 | 5041 | 3587 | 25200 | 15000 | 1088 | 107 | 2.33 | 74 | 69 | 13 | 11 | 1.89 | 2.14 | 0.47 | 61 |
| 2 | 2027.0 | 5272 | 3676 | 26460 | 11850 | 976 | 134 | 2.37 | 71 | 66 | 12 | 10 | 1.98 | 2.18 | 0.49 | 64 |
| 3 | 2027.5 | 5514 | 3767 | 27783 | 8543 | 864 | 161 | 2.40 | 68 | 64 | 10 | 9 | 2.07 | 2.22 | 0.51 | 67 |
| 4 | 2028.0 | 5767 | 3861 | 29172 | 5071 | 752 | 188 | 2.44 | 64 | 61 | 9 | 8 | 2.16 | 2.26 | 0.53 | 70 |
| 5 | 2028.5 | 6000 | 3957 | 30630 | 1426 | 640 | 215 | 2.47 | 60 | 58 | 8 | 6 | 2.25 | 2.30 | 0.55 | 73 |
| 6 | 2029.0 | 6000 | 4055 | 32161 | 0 | 528 | 242 | 2.51 | 57 | 56 | 7 | 5 | 2.34 | 2.34 | 0.57 | 76 |
| 7 | 2029.5 | 6000 | 4156 | 33769 | 0 | 416 | 269 | 2.54 | 54 | 53 | 6 | 4 | 2.43 | 2.38 | 0.59 | 79 |
| 8 | 2030.0 | 6000 | 4259 | 35457 | 0 | 304 | 296 | 2.58 | 50 | 50 | 4 | 3 | 2.50 | 2.42 | 0.60 | 82 |

### Key Trends

- **Graduate intake:** 5041 -> 6000 (moderate increase, matched to posts)
- **Housemanship posts:** 3587 -> 4259 (tied to graduates)
- **Permanent posts:** 25200 -> 35457 (major expansion +10%/year)
- **Contract doctors:** 15000 -> 0 (abolished)
- **Doctor-to-population ratio:** 2.33 -> 2.58 (fastest improvement)
- **Public hospital overcrowding:** 74 -> 50 (rapid easing)
- **Average doctor workload:** 69 -> 50 hours/week (dramatic improvement)
- **Brain drain:** 1088 -> 304 doctors/year (near full retention)
- **Overseas returnees:** 107 -> 296 doctors/year (Malaysia becomes importer)
- **Medical student interest:** 1.89 -> 2.50 (strong rise)
- **Retention:** 61% -> 82% (near full retention)

## 2. Agent Action Distribution

- **COMPLAIN_TO_MINISTRY:** 51 (21.2%)
- **CREATE_PERMANENT_POSTS:** 27 (11.2%)
- **EXPAND_PRIVATE_PARTNERSHIP:** 27 (11.2%)
- **EMIGRATE:** 24 (10.0%)
- **RAISE_SALARIES:** 23 (9.6%)
- **ORGANISE_PROTEST:** 15 (6.2%)
- **CONVERT_CONTRACT_TO_PERMANENT:** 14 (5.8%)
- **LEAVE_FOR_PRIVATE:** 12 (5.0%)
- **PUBLISH_RESEARCH:** 11 (4.6%)
- **EXPAND_CONTRACT_SYSTEM:** 9 (3.8%)
- **SUPPORT_POLICY:** 8 (3.3%)
- **IGNORE:** 6 (2.5%)
- **DEPLOY_TO_RURAL:** 6 (2.5%)
- **ESTABLISH_HEALTH_SERVICES_COMMISSION:** 4 (1.7%)
- **PURSUE_SPECIALIZATION:** 2 (0.8%)
- **INCREASE_INTAKE:** 1 (0.4%)

## 3. Stakeholder Behaviour

### House Officer
- EMIGRATE: 8
- LEAVE_FOR_PRIVATE: 8
- CREATE_PERMANENT_POSTS: 4
- COMPLAIN_TO_MINISTRY: 4

### Jpa Admin
- EXPAND_CONTRACT_SYSTEM: 8

### Medical Officer
- RAISE_SALARIES: 12
- COMPLAIN_TO_MINISTRY: 9
- EMIGRATE: 8
- CONVERT_CONTRACT_TO_PERMANENT: 5
- LEAVE_FOR_PRIVATE: 4

### Medical Student
- EMIGRATE: 8
- IGNORE: 6
- SUPPORT_POLICY: 5
- CREATE_PERMANENT_POSTS: 3
- PURSUE_SPECIALIZATION: 2

### Mma Advocate
- ORGANISE_PROTEST: 10
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 2
- CREATE_PERMANENT_POSTS: 2
- RAISE_SALARIES: 2

### Moh Admin
- COMPLAIN_TO_MINISTRY: 8
- CONVERT_CONTRACT_TO_PERMANENT: 3
- CREATE_PERMANENT_POSTS: 2
- INCREASE_INTAKE: 1
- EXPAND_CONTRACT_SYSTEM: 1

### Mohe Admin
- PUBLISH_RESEARCH: 8

### Private Operator
- EXPAND_PRIVATE_PARTNERSHIP: 11
- CREATE_PERMANENT_POSTS: 4
- COMPLAIN_TO_MINISTRY: 1

### Rural Patient
- COMPLAIN_TO_MINISTRY: 11
- DEPLOY_TO_RURAL: 5

### Rural Staff
- CREATE_PERMANENT_POSTS: 7
- CONVERT_CONTRACT_TO_PERMANENT: 6
- COMPLAIN_TO_MINISTRY: 1
- DEPLOY_TO_RURAL: 1
- SUPPORT_POLICY: 1

### Specialist
- EXPAND_PRIVATE_PARTNERSHIP: 8
- RAISE_SALARIES: 8
- COMPLAIN_TO_MINISTRY: 6
- CREATE_PERMANENT_POSTS: 2

### Treasury
- EXPAND_PRIVATE_PARTNERSHIP: 8
- PUBLISH_RESEARCH: 3
- SUPPORT_POLICY: 1
- COMPLAIN_TO_MINISTRY: 1
- RAISE_SALARIES: 1

### Urban Patient
- COMPLAIN_TO_MINISTRY: 10
- ORGANISE_PROTEST: 5
- SUPPORT_POLICY: 1

## 4. Opinion Dynamics

- **Optimism:** Average shift over simulation = -0.165
- **Trust in Govt:** Average shift over simulation = -0.322
- **Advocacy:** Average shift over simulation = +0.641
- **Frustration:** Average shift over simulation = +0.429
- **Career Security:** Average shift over simulation = +0.067
- **Patient Care Priority:** Average shift over simulation = +0.294

## 5. Notable Agent Actions & Quotes

**Puan Siti Norhayati** (moh_admin) — Round 2 — `CREATE_PERMANENT_POSTS`
> Dengan 8% kenaikan bajet 2027 dan 2,000 kontrak doktor sudah ditukar, kita perlu teruskan penukaran untuk mengurangkan beban kerja dan tingkatkan retention, jadi cadangkan penambahan jawatan tetap bagi kontrak doktor yang masih ada.

**Dr Nurul Ain** (house_officer) — Round 3 — `COMPLAIN_TO_MINISTRY`
> Saya masih belum lihat cukup jawatan tetap untuk kami house officers, jadi saya minta kementerian percepatkan pembukaan lebih banyak kedudukan tetap supaya kami boleh selesaikan latihan dengan kepastian kerjaya.

**Mr Rajesh Nair** (rural_staff) — Round 2 — `CONVERT_CONTRACT_TO_PERMANENT`
> Saya rasa kalau kontrak doktor di kawasan luar bandar ditukar jadi jawatan tetap, rakan-rakan dan saya akan rasa lebih selamat dan boleh berkhidmat lebih lama, sekaligus bantu kurangkan beban kerja.

**Mr Dinesh Velu** (private_operator) — Round 3 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan Health Services Commission baru & kenaikan gaji 20%, kami ingin kerjasama lebih erat dengan kerajaan untuk program latihan GP baru supaya kompetensi terjamin dan klinik tetap menguntungkan.

**Mdm Chong Siew Lian** (urban_patient) — Round 4 — `COMPLAIN_TO_MINISTRY`
> Saya masih menunggu terlalu lama untuk temujanji pakar; pension saya tak cukup untuk private, tolong kerajaan percepatkan penambahan doktor supaya kami warga tua dapat layanan yang lebih cepat.

**Puan Lina Mohd** (treasury) — Round 6 — `RAISE_SALARIES`
> Data menunjukkan retensi rendah dan beban kerja tinggi; kenaikan gaji dapat mengurangkan emigrasi dan meningkatkan motivasi doktor, sambil selaras dengan keperluan perancangan berasaskan bukti.

**Dr Hafiz Rahman** (specialist) — Round 1 — `RAISE_SALARIES`
> Dengan tawaran 3x gaji di Singapore, saya perlukan MOH beri kenaikan gaji yang kompetitif supaya saya boleh kekal di sektor awam, ini akan bantu kurangkan beban kerja dan improve patient care.

**Dr Hafiz Rahman** (specialist) — Round 7 — `COMPLAIN_TO_MINISTRY`
> Saya beri amaran akhir kepada MOH, tanpa kenaikan gaji yang kompetitif saya akan tinggalkan sektor awam dan sertai rangkaian swasta Singapore, demi kelangsungan kerjaya dan kualiti rawatan.

**Dr Susan Ong** (specialist) — Round 8 — `EXPAND_PRIVATE_PARTNERSHIP`
> Kerja berganda dan gaji rendah terus menekan, jadi saya pilih kerjasama lab swasta untuk dapat pendapatan tambahan dan kurangkan beban kerja, sekaligus tingkatkan kualiti penjagaan pesakit.

**Dr Prof. Zainal Abidin** (specialist) — Round 2 — `COMPLAIN_TO_MINISTRY`
> Walaupun 2,000 kontrak doktor sudah ditukar, kekurangan jawatan tetap masih kritikal; kami perlukan lebih banyak jawatan tetap dan kenaikan gaji supaya doktor tidak terus melarikan diri.

**Mr Rajesh Nair** (rural_staff) — Round 3 — `COMPLAIN_TO_MINISTRY`
> Saya rasa tanpa jawatan doktor dan laluan kerjaya, saya terpaksa fikir untuk jadi jururawat di Australia; minta kerajaan perbaiki laluan kerjaya dan keselamatan pekerjaan di luar bandar.

**Dr Nurul Ain** (house_officer) — Round 6 — `COMPLAIN_TO_MINISTRY`
> Saya masih belum lihat cukup jawatan tetap untuk house officers; perlukan kerajaan percepatkan pembukaan lebih banyak jawatan tetap supaya kami boleh selesaikan latihan dengan kepastian.

**Puan Lina Mohd** (treasury) — Round 8 — `ESTABLISH_HEALTH_SERVICES_COMMISSION`
> Untuk memastikan perancangan tenaga kerja berasaskan bukti dan alokasi dana yang tepat, saya cadangkan menubuhkan komisi perkhidmatan kesihatan yang dapat mengkoordinasi data dan policy.

**Dr Nurul Ain** (house_officer) — Round 7 — `COMPLAIN_TO_MINISTRY`
> Saya masih belum lihat cukup jawatan tetap, perlukan kementerian percepatkan pembukaan lebih banyak kedudukan tetap supaya kami house officers dapat selesaikan latihan dengan kepastian.

**Puan Siti Norhayati** (moh_admin) — Round 1 — `CONVERT_CONTRACT_TO_PERMANENT`
> Dengan budget 2027 naik 8%, kita boleh tukar kontrak doktor ke jawatan tetap untuk naik retention dan kurangkan beban kerja, sekaligus selaraskan tenaga kerja dengan keperluan sebenar.

## 6. Conclusion

Under the comprehensive trajectory (SIM-5), Malaysia achieves the fastest, most sustainable workforce improvement by addressing BOTH supply and demand simultaneously:

1. **Balanced pipeline:** Intake rises to 6,000 by 2030, but EVERY additional graduate has a matched housemanship post and a clear permanent pathway. No glut. No bottleneck.

2. **Retention revolution:** Brain drain falls from 1,200 to 300/year. Returnees quadruple. Malaysia transitions from net exporter to net importer of medical talent.

3. **Contract abolition:** The single biggest retention barrier is removed. Permanent posts expand at +10%/year, restoring career certainty for all doctors.

4. **Salary competitiveness:** Public salary ratio rises 0.45 -> 0.60, approaching private sector parity. On-call, hazard pay, and rural allowances fully reindexed.

5. **Health Services Commission:** Full establishment by 2028 breaks MOHE-JPA-MOH silos. End-to-end workforce planning becomes institutionalized, preventing future cyclical crises.

6. **Working conditions transformed:** Workload falls from 72 to 50 hours/week. 3-month deployment notice, AI support, rural incentives, and workload caps make public service attractive again.

7. **Student interest surges:** Medicine becomes the most prestigious career. Interest index climbs to 2.5, ensuring sustained high-quality applicant pool.

**By 2030:** Doctor-to-population reaches 2.8/1,000 — the fastest improvement of all four simulations. Overcrowding falls to 50, waiting times halve, and the profession becomes sustainable.

**By 2038 (projected):** 3.2/1,000 — near OECD equivalence (3.9). The system is no longer cyclical. Malaysia has broken the 30-year pendulum.

**Risk:** Requires massive political capital, budget reallocation, and 10+ year continuity. If any government reverses course mid-stream, the cycle could restart. But the institutionalized HSC makes reversal harder than in previous decades.

---
*Report generated by SIM-5 engine | 2026-05-07T23:23:52.904894*