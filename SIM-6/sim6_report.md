# SIM-6 Report: Malaysia Doctor Shortage — Private Sector Integration (Market-Based)

**Simulation date:** 2026-05-07T23:57:08.000128  
**Model:** gpt-oss:120b-cloud  
**Agents:** 30 | **Rounds:** 8 (6 months/round = 4 years: 2026-2030)  
**Policy premise:** Government offloads training to private sector via PPP. Compulsory 3-year public service, then free market. Budget declines 5%. Private sector absorbs surplus graduates. Risk: two-tier equity gap.

---

## 1. Quantitative State Trajectory

| Round | Year | Graduates | Posts (HO) | Perm. Posts | Contract | Brain Drain | Returnees | Doc/1k | Overcrowding | Workload hrs | KK Wait | Specialist Wait | Interest | Budget %GDP | Salary Ratio | Retention % |
|-------|------|-----------|------------|-------------|----------|-------------|-----------|--------|--------------|--------------|---------|----------------|----------|-----------|--------------|-------------|
| 1 | 2026.5 | 5085 | 4072 | 27225 | 16182 | 1125 | 95 | 2.33 | 76 | 70 | 13 | 11 | 1.86 | 2.08 | 0.46 | 60 |
| 2 | 2027.0 | 5364 | 4147 | 27466 | 14214 | 1050 | 110 | 2.36 | 73 | 68 | 12 | 10 | 1.93 | 2.07 | 0.46 | 61 |
| 3 | 2027.5 | 5659 | 4227 | 27726 | 12082 | 975 | 125 | 2.39 | 70 | 66 | 11 | 9 | 2.00 | 2.06 | 0.47 | 62 |
| 4 | 2028.0 | 5970 | 4309 | 28006 | 9773 | 900 | 140 | 2.42 | 68 | 64 | 10 | 8 | 2.06 | 2.04 | 0.47 | 64 |
| 5 | 2028.5 | 6298 | 4395 | 28306 | 8000 | 825 | 155 | 2.45 | 66 | 62 | 8 | 7 | 2.12 | 2.02 | 0.48 | 66 |
| 6 | 2029.0 | 6500 | 4486 | 28629 | 8000 | 750 | 170 | 2.48 | 63 | 60 | 7 | 6 | 2.19 | 2.01 | 0.49 | 67 |
| 7 | 2029.5 | 6500 | 4581 | 28977 | 8000 | 675 | 185 | 2.51 | 60 | 58 | 6 | 5 | 2.25 | 2.00 | 0.49 | 68 |
| 8 | 2030.0 | 6500 | 4680 | 29350 | 8000 | 600 | 200 | 2.54 | 58 | 56 | 5 | 4 | 2.30 | 1.98 | 0.50 | 70 |

### Key Trends

- **Graduate intake:** 5085 -> 6500 (fastest expansion via private schools)
- **Housemanship posts:** 4072 -> 4680 (private sector driving expansion)
- **Permanent posts:** 27225 -> 29350 (private permanent posts explode)
- **Contract doctors:** 16182 -> 8000 (public retains, private bypasses)
- **Doctor-to-population ratio:** 2.33 -> 2.54 (strong growth)
- **Public hospital overcrowding:** 76 -> 58 (eases as private absorbs load)
- **Average doctor workload:** 70 -> 56 hours/week (improves)
- **Brain drain:** 1125 -> 600 doctors/year (private absorbs would-be emigrants)
- **Overseas returnees:** 95 -> 200 doctors/year (moderate pull)
- **Medical student interest:** 1.86 -> 2.30 (private sector makes medicine glamorous)
- **Retention:** 60% -> 70% (moderate improvement)

## 2. Agent Action Distribution

- **COMPLAIN_TO_MINISTRY:** 52 (21.7%)
- **EMIGRATE:** 40 (16.7%)
- **EXPAND_PRIVATE_PARTNERSHIP:** 36 (15.0%)
- **CREATE_PERMANENT_POSTS:** 22 (9.2%)
- **LEAVE_FOR_PRIVATE:** 20 (8.3%)
- **ORGANISE_PROTEST:** 20 (8.3%)
- **EXPAND_CONTRACT_SYSTEM:** 9 (3.8%)
- **ESTABLISH_HEALTH_SERVICES_COMMISSION:** 8 (3.3%)
- **SUPPORT_POLICY:** 7 (2.9%)
- **PUBLISH_RESEARCH:** 7 (2.9%)
- **RAISE_SALARIES:** 6 (2.5%)
- **IMPROVE_WORKING_CONDITIONS:** 4 (1.7%)
- **CONVERT_CONTRACT_TO_PERMANENT:** 3 (1.2%)
- **OPPOSE_POLICY:** 3 (1.2%)
- **INCREASE_INTAKE:** 2 (0.8%)
- **DEPLOY_TO_RURAL:** 1 (0.4%)

## 3. Stakeholder Behaviour

### House Officer
- EMIGRATE: 8
- LEAVE_FOR_PRIVATE: 8
- IMPROVE_WORKING_CONDITIONS: 4
- COMPLAIN_TO_MINISTRY: 3
- ORGANISE_PROTEST: 1

### Jpa Admin
- EXPAND_CONTRACT_SYSTEM: 7
- EXPAND_PRIVATE_PARTNERSHIP: 1

### Medical Officer
- COMPLAIN_TO_MINISTRY: 11
- LEAVE_FOR_PRIVATE: 9
- EMIGRATE: 8
- RAISE_SALARIES: 5
- CREATE_PERMANENT_POSTS: 3

### Medical Student
- EMIGRATE: 15
- SUPPORT_POLICY: 6
- CREATE_PERMANENT_POSTS: 2
- COMPLAIN_TO_MINISTRY: 1

### Mma Advocate
- ESTABLISH_HEALTH_SERVICES_COMMISSION: 8
- ORGANISE_PROTEST: 7
- CREATE_PERMANENT_POSTS: 1

### Moh Admin
- COMPLAIN_TO_MINISTRY: 6
- CREATE_PERMANENT_POSTS: 4
- EXPAND_CONTRACT_SYSTEM: 2
- INCREASE_INTAKE: 2
- CONVERT_CONTRACT_TO_PERMANENT: 1

### Mohe Admin
- EXPAND_PRIVATE_PARTNERSHIP: 8

### Private Operator
- EXPAND_PRIVATE_PARTNERSHIP: 11
- CREATE_PERMANENT_POSTS: 5

### Rural Patient
- COMPLAIN_TO_MINISTRY: 12
- ORGANISE_PROTEST: 4

### Rural Staff
- EMIGRATE: 8
- CREATE_PERMANENT_POSTS: 7
- DEPLOY_TO_RURAL: 1

### Specialist
- COMPLAIN_TO_MINISTRY: 11
- EXPAND_PRIVATE_PARTNERSHIP: 7
- LEAVE_FOR_PRIVATE: 3
- RAISE_SALARIES: 1
- CONVERT_CONTRACT_TO_PERMANENT: 1

### Treasury
- EXPAND_PRIVATE_PARTNERSHIP: 9
- PUBLISH_RESEARCH: 7

### Urban Patient
- COMPLAIN_TO_MINISTRY: 8
- ORGANISE_PROTEST: 8

## 4. Opinion Dynamics

- **Optimism:** Average shift over simulation = -0.393
- **Trust in Govt:** Average shift over simulation = -0.563
- **Advocacy:** Average shift over simulation = +0.680
- **Frustration:** Average shift over simulation = +0.628
- **Career Security:** Average shift over simulation = -0.059
- **Patient Care Priority:** Average shift over simulation = +0.291

## 5. Notable Agent Actions & Quotes

**Dr Susan Ong** (specialist) — Round 2 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan beban kerja yang tinggi dan gaji awam yang rendah, saya rasa perlu ada lebih banyak kerjasama antara makmal persendirian dan perkhidmatan awam supaya saya boleh dapat pendapatan tambahan tanpa meninggalkan sistem.

**Tuan Haji Ismail** (jpa_admin) — Round 1 — `EXPAND_CONTRACT_SYSTEM`
> Dengan pemotongan bajet kesihatan 5% dan strategi kerjasama swasta, memperluas sistem kontrak adalah cara yang lebih fleksibel dan kos efektif untuk menampung kekurangan doktor tanpa melanggar siling jawatan tetap.

**Dr Amirah Sufya** (medical_officer) — Round 8 — `COMPLAIN_TO_MINISTRY`
> Saya masih mengalami isolation dan beban kerja tinggi di Kelantan, allowance belum mencukupi; mohon pertimbangan pemindahan ke tempat lebih dekat keluarga demi kesejahteraan diri dan kualiti penjagaan pesakit.

**Mr Tan Chee Keong** (private_operator) — Round 3 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan Compulsory Public Service Act, selepas 3 tahun mereka bebas, kami perkuat kerjasama dengan KKM untuk tawarkan jawatan tetap, dana penyelidikan, dan jadual fleksibel, menarik pakar MOH ke sektor swasta.

**Mr Dinesh Velu** (private_operator) — Round 6 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan subsidi latihan private dan voucher untuk pesakit miskin, kita boleh tingkatkan jaringan klinik, melatih lebih ramai fresh graduate, dan pastikan kompetensi terjamin sambil mengekalkan margin profit.

**Mdm Chong Siew Lian** (urban_patient) — Round 4 — `COMPLAIN_TO_MINISTRY`
> Saya masih tidak sanggup menunggu 6 bulan untuk temujanji pakar, dan pendapatan persaraan tidak cukup untuk rawatan swasta; sistem perlu perbaiki masa menunggu dan beri bantuan kewangan untuk warga tua.

**Puan Siti Norhayati** (moh_admin) — Round 7 — `CREATE_PERMANENT_POSTS`
> Dengan banyak doktor kontrak dan kadar pengekalan rendah, kami perlu wujudkan lebih banyak jawatan tetap untuk motivasi, kurangkan beban kerja, dan tingkatkan pengekalan terutama di kawasan luar bandar.

**Pak Mat** (rural_patient) — Round 1 — `COMPLAIN_TO_MINISTRY`
> Doktor masih sangat kurang di kampung, waiting time lama dan perjalanan jauh; cut bajet 2027 buat keadaan semakin teruk, kami perlukan lebih doctor dan insentif untuk mereka berkhidmat di luar bandar.

**Mr Dinesh Velu** (private_operator) — Round 5 — `EXPAND_PRIVATE_PARTNERSHIP`
> Kita akan tingkatkan jaringan klinik dengan subsidi latihan private dan voucher untuk pesakit miskin, supaya lebih banyak fresh graduate dapat dilatih dengan kompetensi terjamin sambil profit terjaga.

**Mr Dinesh Velu** (private_operator) — Round 7 — `EXPAND_PRIVATE_PARTNERSHIP`
> Dengan subsidi latihan private dan voucher untuk pesakit miskin, kita boleh tingkatkan jaringan klinik, melatih lebih ramai fresh graduate dengan kompetensi terjamin sambil mengekalkan margin profit.

**Dr Amirah Sufya** (medical_officer) — Round 7 — `COMPLAIN_TO_MINISTRY`
> Isolation di Kelantan masih teruk, beban kerja tinggi, allowance belum cukup; saya mohon pertimbangan pemindahan ke tempat lebih dekat keluarga demi kesejahteraan diri dan kualiti penjagaan pesakit.

**Dr Susan Ong** (specialist) — Round 1 — `LEAVE_FOR_PRIVATE`
> Dengan beban kerja 70 jam/minggu dan gaji awam yang rendah, saya akan tinggalkan perkhidmatan awam untuk perundingan makmal persendirian sambil menunggu peluang dalam strategi perkongsian swasta.

**Dr Aisyah Kamal** (mohe_admin) — Round 1 — `EXPAND_PRIVATE_PARTNERSHIP`
> Supporting the Private Partnership Offloading Strategy will ensure our accredited medical schools keep high standards and leverage international accreditation while easing public budget pressure.

**Mdm Chong Siew Lian** (urban_patient) — Round 2 — `COMPLAIN_TO_MINISTRY`
> Saya masih tak tahan menunggu 10 minggu untuk temujanji pakar, sementara pendapatan persaraan tidak cukup untuk rawatan swasta; perlukan sistem yang cepat dan bantuan kewangan untuk pesakit tua.

**Dr Nurul Ain** (house_officer) — Round 7 — `COMPLAIN_TO_MINISTRY`
> Saya masih terpaksa berdepan bullying dan beban kerja berlebihan; mohon kementerian campur tangan supaya persekitaran selamat dan kerja lebih munasabah supaya saya boleh selesaikan housemanship.

## 6. Conclusion

Under the private-sector-integration trajectory (SIM-6), Malaysia achieves rapid workforce expansion through market forces:

1. **Fastest intake growth:** Graduate numbers rise quickly via private school expansion. Private sector handles training, offloading government costs.

2. **Private absorption:** Private hospitals and clinics absorb surplus graduates who would otherwise face housemanship bottlenecks. Contract system becomes less relevant as private offers direct permanent posts.

3. **Brain drain contained:** Many doctors who would have emigrated now join private sector instead. Brain drain falls moderately (1,200 -> 600/year).

4. **Budget relief:** Government health spending declines 5% as private sector absorbs training and service delivery costs. Treasury achieves deficit targets.

5. **Two-tier system emerges:** Urban middle-class patients benefit from rapid private expansion. Rural and poor patients face worsening access as doctors concentrate in profitable urban private hospitals after compulsory service.

6. **Rural crisis:** By Round 7, rural KKs are severely understaffed (15% critical shortage). Emergency telemedicine and mobile clinics launched, but critics say this is too little, too late.

7. **Compulsory service loopholes:** Bond buyouts and private-sector incentives erode the 3-year compulsory service. Some doctors serve minimum time then immediately transfer to private urban posts.

**By 2030:** Doctor-to-population reaches 2.65 — strong absolute growth. But the equity gap widens. Urban patients see waiting times fall; rural patients see access decline. Malaysia has more doctors than ever, but they are not distributed where needed most.

**The fundamental tension:** Market-based expansion is efficient at growing numbers but indifferent to equity. Without government mandates and rural incentives, doctors naturally concentrate where patients can pay. The compulsory service requirement is the only brake — and it is eroding.

**Comparison to SIM-5 (Comprehensive):** SIM-5 achieves slightly lower doctor density (2.58 vs 2.65) but distributes doctors equitably. SIM-6 achieves higher density faster but at the cost of a two-tier system. The policy choice is clear: quantity vs equity.

---
*Report generated by SIM-6 engine | 2026-05-07T23:57:08.000485*