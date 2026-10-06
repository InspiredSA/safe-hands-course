# Helping Young Children Regulate – Level 1

Inspired ELS staff development · Content version 1.0 · 6 October 2026

A separate, evidence-informed course for adult Early Learning School teachers, teaching assistants and caregivers. The examples focus mainly on ages 2–6 and must be adapted to developmental, communication, cultural and sensory needs. This course adds the `/co-regulation/` path; it does not replace or alter Safe Hands or Intimate Care.

## Purpose and boundaries

Six modules build everyday co-regulation skills: start with connection; make the day easier; respond early; protect safety and reconnect; teach through play; and plan with families and colleagues. The course contains original fictional scenarios, scripts, practice ideas and illustrations.

This is not an Inspired-approved policy, an accredited qualification, a diagnosis or treatment protocol, or safeguarding/first-aid/physical-intervention training. It does not teach or authorise restraint or seclusion. Staff follow current school procedures, local requirements, individual plans and their training limits. A school lead should review local fit before rollout; translations need fluent early-years/safeguarding specialist review. No expert endorsement of this course is implied by citations or video links.

The planned duration is about 60 minutes: 48 minutes for modules and reflections, 10 minutes for the assessment and 2 minutes for acknowledgements. Optional official videos and team practice add time. Actual timing depends on reading and reflection pace and should be checked with a staff pilot.

## Learning and completion

- Six modules with substantive teaching text, one formative scenario check each, a required written response and model feedback
- Three original five-step illustrated explainers with captions, play/pause, previous/next/restart controls and full text transcripts
- An original supportive adult-and-child SVG illustration and an in-the-moment support map
- Three verified official expert video pages, each with a course summary, reflection prompt and accessibility guidance; no automatic third-party video loading
- A 20-question assessment: 16/20 or higher AND every safety-critical question correct
- Safety-critical questions: 6, 9, 10, 11, 12 and 18 (respectively supportive quiet spaces; optional strategies/communication access; immediate danger; medical emergency; restrictive-intervention boundaries; safeguarding)
- Required staff name, work email, school and confirmed Head email; module confirmations and responsibility acknowledgements
- A named certificate of online completion, full-results text file and manually sent email draft addressed to the participant’s confirmed Head
- Optional blank team practice guide, available on screen, as a PDF and through browser print
- English plus clearly marked draft French and Kreol Morisien translations

Written reflections require meaningful input but are not automatically graded. A certificate records online completion, not observed competence, external accreditation, intervention authorisation or school approval. Names are self-entered. Certificate references are generated locally and are not part of a verified central register.

The team guide is an adult-to-adult rehearsal aid. Never provoke or stage a real child’s distress for training. It contains no physical technique and does not confer a practical sign-off.

## Privacy and data handling

Storage key: `inspired-co-regulation-v1`. Certificate prefix: `CR-ONLINE-`.

Participant details, draft/final reflections, language, progress, answers, attempt history and certificate identity remain in the current browser’s local storage. Switching language preserves the same progress and does not translate participant writing. Other courses use separate keys.

There is no backend registration endpoint, analytics, automatic email service or school personnel register. Static hosting providers may keep ordinary access logs. Client-side state is not tamper-proof and must not be treated as a verified staff record. The course saves no real child or incident data by design: all activities explicitly require fictional scenarios.

Downloaded results and the `.eml` draft include the adult’s entered details and reflections. Downloading does not send an email. Open the draft in a compatible email application, check the recipient/content and send manually. If `.eml` editing is unavailable, attach the certificate and results to a fresh email. The app never automatically contacts a Head.

On shared computers, use a private window, download records and close the window. Do not enter children’s details, diagnoses, real incidents or confidential school records. Keep those in approved school systems. Clearing all site data on the shared GitHub Pages origin may also clear progress for other courses; download needed records first.

## Run, edit and deploy

This is a static site. There is no build-time network dependency and no runtime third-party JavaScript/font dependency.

For a local preview, serve the folder with an ordinary static HTTP server. The site uses relative paths for its own assets.

Edit `course-en.json`, `course-extras-en.json` and `ui-en.json`, then update the corresponding `fr` and `mfe` source dictionaries. Keep module IDs, block topology, option order, answer indexes, critical flags, resource URLs and visual-guide IDs aligned. Run:

    python3 tools/assemble.py
    node tools/test-course.cjs

The script validates the main cross-language structure and writes `course-data*.js`, `course-extras.js` and `i18n.js`. `--english-only` exists for interim development only and must never be used for a multilingual production release.

Runtime files: `index.html`, `style.css`, `app.js`, `certificate.js`, `extras.js`, `course-data.js`, `course-data-fr.js`, `course-data-mfe.js`, `course-extras.js`, `i18n.js`, `assets/brand/`, and `vendor/pdf-lib.min.js`. Course provenance is in `course-notes.html` and this README.

The Inspired logo, Roboto/Open Sans fonts and PDF library are reused with their existing licence/source files. New art is original code-native SVG/CSS. Source files are included for maintainability; private QA output and participant data are not published.

## Accessibility

Labelled controls, keyboard-focus indicators, a skip link, status announcements, document-language changes, responsive layouts and print styles are provided. Explainers start paused with no sound; every step is also readable. Reduced-motion preferences remove transitions and pulsing. Essential course learning does not depend on watching an external video. External providers control their own captions, language options and availability; the course includes text alternatives and links to official transcript-bearing pages where available.

Certificate and practice PDFs use rendered text to retain French and Kreol characters. The text-based results download and on-screen content remain the accessible text alternatives. These image-backed PDFs are not claimed to be tagged accessible PDFs.

## Public availability

The GitHub repository and Pages site are public and can be opened or shared by anyone with their address. The `noindex, nofollow` metadata and project-folder robots advisory request reduced search indexing; they are not access controls. No private school procedure, real child record or participant record is committed.

## Evidence and provenance

Sources checked 6 October 2026. Primary guidance comes from England/UK, the United States and Australia. Jurisdiction-specific legal details remain jurisdiction-specific. Research evidence for particular early-years self-regulation programmes is limited and uneven, and co-regulation-specific intervention evidence is still developing. The course is evidence-informed professional learning, not a validated intervention with guaranteed outcomes.

### Module-to-source mapping

- Module 1, Start with connection: eef-regulation, harvard-activities, acecqa-regulation, headstart-communication, ncpmi-calm, dfe-emotions
- Module 2, Make the day easier to manage: ncpmi-visuals, nice-autism, acecqa-regulation, acecqa-discipline
- Module 3, Respond before distress grows: dfe-mental-health, ncpmi-response, dfe-emotions, acecqa-inclusion, ncpmi-calm, acecqa-discipline
- Module 4, Keep everyone safe, then reconnect: acecqa-discipline, safeguarding, ncpmi-calm, acecqa-self-regulation, dfe-mental-health
- Module 5, Teach skills in everyday play: ncpmi-teaching, eef-regulation, harvard-activities, ncpmi-emotions
- Module 6, Build the plan together: headstart-communication, acecqa-self-regulation, nice-autism, dfe-mental-health, safeguarding

The scenarios, scripts, quiz and visual sequences are original teaching examples synthesising the principles. They are not copied provider protocols. Safety boundary language is deliberately conservative and must be applied through current local procedures.

### Official sources

- [Self-regulation and executive function: Early Years Evidence Store](https://educationendowmentfoundation.org.uk/early-years/evidence-store/self-regulation-and-executive-function) — Education Endowment Foundation; England. Defines related regulation skills; supports teaching, modelling, repeated practice and tailoring adult scaffolding to the child and context. Official page or resource content checked on 6 October 2026.
- [Research Agenda: Self-Regulation and Executive Function in the Early Years](https://educationendowmentfoundation.org.uk/projects-and-evaluation/research-agenda-themes-priority-areas/research-agenda-theme-self-regulation-and-executive-function-sref-in-the-early-years) — Education Endowment Foundation; England. Explains the limited and uneven early-years evidence base, including gaps for younger children and co-regulation interventions. Official page or resource content checked on 6 October 2026.
- [Activities Guide: Enhancing and Practicing Executive Function Skills with Children from Infancy to Adolescence](https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/) — Center on the Developing Child at Harvard University; United States. Age-adapted play and interaction provide opportunities to develop executive-function and self-regulation skills. Official page or resource content checked on 6 October 2026.
- [Serve and Return](https://developingchild.harvard.edu/key-concept/serve-and-return/) — Center on the Developing Child at Harvard University; United States. Responsive back-and-forth exchanges with caring adults support early communication and social development. Official page or resource content checked on 6 October 2026.
- [QA5 information sheet: Supporting children to regulate their own behaviour](https://www.acecqa.gov.au/qa5-information-sheet-supporting-children-regulate-their-own-behaviour) — Australian Children’s Education and Care Quality Authority; Australia. Highlights warm relationships, fluctuating capacity, adult regulation, environmental reflection and calm-time skill teaching. Official page or resource content checked on 6 October 2026.
- [QA5 information sheet: Inappropriate discipline](https://www.acecqa.gov.au/qa5-information-sheet-inappropriate-discipline) — Australian Children’s Education and Care Quality Authority; Australia. Distinguishes supported cooling down from punishment and identifies inappropriate discipline. Legal details apply to its Australian framework; this course does not export them as universal law. Official page or resource content checked on 6 October 2026.
- [Element 5.2.2: Self-regulation](https://www.acecqa.gov.au/element-522-self-regulation) — Australian Children’s Education and Care Quality Authority; Australia. Supports emotion communication, conflict resolution, educator reflection and partnership with families and other professionals. Official page or resource content checked on 6 October 2026.
- [Inclusion and inclusive practice](https://www.acecqa.gov.au/latest-news/inclusion-and-inclusive-practice) — Australian Children’s Education and Care Quality Authority; Australia. Describes responsive co-regulation through presence, gentle tone and choices respectful of the child’s pace and needs. Official page or resource content checked on 6 October 2026.
- [Autism spectrum disorder in under 19s: support and management, recommendations 1.1.9 and 1.4](https://www.nice.org.uk/guidance/cg170/chapter/recommendations) — National Institute for Health and Care Excellence; United Kingdom. Recommends attention to communication, sensory environment, predictability, possible health factors and family-informed individual care. Clinical guidance does not authorise educators to diagnose or prescribe. Official page or resource content checked on 6 October 2026.
- [Visual Supports for Routines, Schedules, and Transitions](https://www.challengingbehavior.org/document/visual-supports-for-routines-schedules-and-transitions/) — National Center for Pyramid Model Innovations, University of South Florida; United States. Provides tools for visual schedules, routine cards and first/then supports. Official page or resource content checked on 6 October 2026.
- [Help Us Stay Calm](https://www.challengingbehavior.org/docs/Stay-Calm_Infographic.pdf) — National Center for Pyramid Model Innovations; United States. Encourages adults to regulate themselves, reflect and reconnect before teaching through the interaction. Official page or resource content checked on 6 October 2026.
- [Tips for Responding to Challenging Behavior in Young Children](https://challengingbehavior.org/wp-content/uploads/2025/02/2017-01-PEP-Tips.pdf) — Strain, Joseph, Hemmeter, Barton and Fox; hosted by NCPMI; United States. Response strategies belong alongside intentional prevention and teaching, rather than replacing them. Official page or resource content checked on 6 October 2026.
- [You Got It! Teaching Social and Emotional Skills](https://challengingbehavior.org/docs/YouGotIt_Teaching-Social-Emotional-Skills.pdf) — Fox and Lentini; hosted by NCPMI; United States. Illustrates modelling, practice, specific feedback, games and stories for teaching social-emotional skills. Official page or resource content checked on 6 October 2026.
- [Social Emotional Teaching Strategies: Enhancing Emotional Vocabulary](https://challengingbehavior.org/docs/ttyc/TTYC_A_EnhancingEmotVoc.pdf) — Center on the Social and Emotional Foundations for Early Learning; hosted by NCPMI; United States. Describes feeling vocabulary, adult modelling, role-play and story-based practice as parts of wider social-emotional teaching. Official page or resource content checked on 6 October 2026.
- [Understanding Children’s Behavior as Communication](https://headstart.gov/mental-health/article/understanding-childrens-behavior-communication) — Office of Head Start, Administration for Children and Families; United States. Supports relationship-based family partnership and interpreting behaviour in context for children from birth to five. Official page or resource content checked on 6 October 2026.
- [Strategies for Supporting Self-Regulation: Snapshot Series](https://headstart.gov/mental-health/article/strategies-supporting-self-regulation-snapshot-series) — Office of Head Start / Administration for Children and Families; United States. Introduces adult co-regulation and links age-specific practice resources based on ACF’s Self-Regulation and Toxic Stress reports. Official title and description verified in indexed source results; direct retrieval returned 403. Supplementary reading, not the sole basis for any course claim.
- [Help for early years providers: Emotions](https://help-for-early-years-providers.education.gov.uk/areas-of-learning/personal-social-and-emotional-development/emotions) — Department for Education; England. Supports empathetic emotional coaching, language and visual supports, reflection and family knowledge. Includes an official video transcript. Official page or resource content checked on 6 October 2026.
- [Mental health for early years children](https://help-for-early-years-providers.education.gov.uk/health-and-wellbeing/mental-health-for-early-years-children) — Department for Education, developed with early-years and health professionals; England. Covers individual patterns, changes needing support, family and professional partnership, and safeguarding escalation. Official page or resource content checked on 6 October 2026.
- [Keeping children safe in education 2026: part one – overview for all staff](https://www.gov.uk/government/publications/keeping-children-safe-in-education--2/part-one-overview-for-all-staff) — Department for Education; England. Requires prompt action, local safeguarding routes and records; immediate danger needs emergency response. This England-specific overview complements rather than replaces the full guidance. Use the current equivalent in your jurisdiction. Official page or resource content checked on 6 October 2026.

### Official video pages

- [How-to: 5 Steps for Brain-Building Serve and Return](https://developingchild.harvard.edu/resources/videos/how-to-5-steps-for-brain-building-serve-and-return/) — Center on the Developing Child at Harvard University. The official page provides explanatory text and several language options. This course summary is a text alternative; player captions and availability may vary. Official Harvard page links to its YouTube player. The page and video title were verified; playback was not independently tested.
- [The importance of emotions in the early years foundation stage framework](https://help-for-early-years-providers.education.gov.uk/areas-of-learning/personal-social-and-emotional-development/emotions) — Department for Education, England. A full transcript is available on the official page beneath the Vimeo video. Official DfE page and linked Vimeo player verified. Player title: EYFS Personal, social and emotional development – Emotions.
- [How Children and Adults Can Build Core Capabilities for Life](https://developingchild.harvard.edu/resources/videos/video-building-core-capabilities-life/) — Center on the Developing Child at Harvard University. The official page includes an explanatory text summary and English and Japanese video options. This course summary is also a text alternative. Official Harvard page verifies title and five-minute duration and links to its YouTube player; playback was not independently tested.
