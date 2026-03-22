# RoadWork Roadmap

## Phase 1: Foundation (Months 1-3)
- [RC] FSRS v4 engine implementation in Rust with WebAssembly compilation
- [RC] Core accessibility component library (WCAG 2.2 AA)
- [RC] PostgreSQL schema design — multi-tenant, accommodation-aware
- [RC] Authentication — OAuth2, SAML SSO, LTI 1.3 launch
- [RC] Basic flashcard CRUD — create, review, schedule
- [RC] Screen reader testing framework — automated NVDA/JAWS/VoiceOver
- [RC] ADA Title II 2025 compliance checklist + automated scanner
- [RC] Docker deployment + basic Helm chart
- **Milestone**: Internal alpha with accessibility testing

## Phase 2: LMS Integration (Months 4-6)
- [RC] LTI 1.3 certification — Canvas (primary target)
- [RC] LTI Assignment and Grade Services (AGS) — grade passback
- [RC] LTI Names and Role Provisioning Services (NRPS) — roster sync
- [RC] Deep linking — content selection from within LMS
- [RC] Schoology + Moodle LTI certification
- [RC] Educator content studio — deck builder, bulk import
- [RC] Student accommodation profiles per institution
- [RC] Analytics dashboard v1 — mastery tracking, at-risk alerts
- **Milestone**: Beta with 3 pilot institutions

## Phase 3: Scale (Months 7-9)
- [RC] Mobile apps — React Native, full a11y tree support
- [RC] Offline mode with background sync
- [RC] Multi-modal content — audio, video, interactive sim
- [RC] AI alt-text + auto-captions
- [RC] Content import — Anki, Quizlet, CSV, QTI
- [RC] Multi-language — i18n framework + Spanish, French, Mandarin, Arabic
- [RC] VPAT documentation + Section 508 certification
- [RC] Performance optimization — 10K concurrent users
- **Milestone**: General availability for institutions

## Phase 4: Growth (Months 10-12)
- [RC] Individual plan launch ($9.99/mo)
- [RC] Content marketplace for educator-created decks
- [RC] Parent/guardian portal
- [RC] Google Classroom integration
- [RC] Blackboard LTI 1.3 certification
- [RC] Learning analytics — xAPI + Caliper export
- [RC] API + developer documentation
- [RC] White-label + custom branding for institutions
- **Milestone**: 50 institutions, 10K individual users

## Phase 5: Expansion (Year 2)
- [RC] Adaptive difficulty — AI-driven content sequencing
- [RC] Collaborative review sessions — real-time classroom mode
- [RC] Cognitive accessibility profiles — complexity levels, chunking
- [RC] Research partnerships — efficacy studies with universities
- [RC] Self-hosted marketplace — institution-to-institution content sharing
- [RC] Gamification — accessible streaks, badges, progress trees
- [RC] Enterprise tier — air-gapped, on-premise, dedicated support
- **Milestone**: 500 institutions, 100K learners

## Revenue Targets
| Quarter | Individual MRR | Institutional MRR | Total ARR |
|---------|---------------|-------------------|-----------|
| Q1 Y1   | —             | $5K (pilots)      | $60K      |
| Q2 Y1   | —             | $25K              | $300K     |
| Q3 Y1   | $10K          | $75K              | $1.02M    |
| Q4 Y1   | $30K          | $150K             | $2.16M    |
| Q4 Y2   | $100K         | $500K             | $7.2M     |

## Key Metrics
- **Retention**: 94% long-term via FSRS (target)
- **Accessibility**: 100% WCAG 2.2 AA compliance, 90% AAA
- **Integration**: <15 min LTI setup time
- **Performance**: <200ms p99 review latency
- **Market**: 240M children with disabilities worldwide (TAM)
