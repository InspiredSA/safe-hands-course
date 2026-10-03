# Intimate Care and Nappy Changing – Level 1

Version 1.0 · review edition · Inspired Education Early Years staff development

A separate companion to the existing Safe Hands course. This folder is self-contained. It uses a separate storage key and certificate-reference prefix; publishing it under `intimate-care/` does not alter the original course or its saved progress.

## Scope and approval status

This approximately one-hour online course is internationally informed, drawing on the supplied Inspired Intimate Care and Nappy Policy template and CDC, UKHSA, NSPCC and ACECQA guidance. It is not a universal international standard, external accreditation or a replacement for a current school-approved procedure. Current Inspired policy status, local law, care plans, supervision, staffing, products, cleaning, permissions, reporting contacts and observer arrangements need school approval before rollout.

French and Kreol Morisien are complete draft translations requiring fluent-speaker review by someone familiar with intimate care and safeguarding. Review notices appear in the interface and downloads. Availability does not establish translation approval.

Online completion records knowledge and reflection only. Practical competence and permission to undertake care independently require separate school induction, suitable supervision, observation and school authorisation. The downloadable practical checklist is blank and is never automatically marked passed by the application.

## Included

- Six modules: respect and reassurance; station preparation; changing routine; clean and reset; individual care; record and report
- Six quick checks, six required fictional reflections and model feedback
- Twenty-question assessment: at least 16 correct plus all five critical questions (3, 6, 8, 10 and 11) correct
- Required staff name, work email, school and confirmed Head email for downloadable records
- Separate acknowledgements and named certificate of online completion
- Three original SVG/CSS illustrated explainers with play/pause, previous/next/restart controls, visible captions and full transcripts
- A separate 25-criterion school practical observation checklist, available on screen, as a blank PDF and through browser print
- Local-readiness checklist, source notes and unfilled school contact routes
- Full results text download, online-completion PDF and prepared email file for manual sharing with the Head
- English, French and Kreol Morisien, with unchanged participant-entered responses when switching languages

The illustrations show abstract plans, supplies, hygiene boundaries and communication cues. They are not filmed expert demonstrations and do not teach a lifting or clinical technique. No children, exposed bodies, real incidents or identifiable child records are included. Actual practical demonstration should use a suitable training doll or other approved materials and a trained school observer.

## Run and publish

No build, server application or external runtime dependency is required. Serve the folder through a static HTTP server or publish the entire folder under the existing GitHub Pages repository's `intimate-care/` path. All asset and script references are relative.

Example local preview: `python3 -m http.server 8765 --directory .`

Files required at runtime:

- `index.html`, `style.css`, `app.js`, `certificate.js`, `extras.js`
- `course-data.js`, `course-data-fr.js`, `course-data-mfe.js`
- `i18n.js`, `course-extras.js`
- `assets/brand/` and `vendor/pdf-lib.min.js`

The `ui-*.json` and `course-extras-*.json` files are readable source dictionaries used to assemble their JavaScript equivalents. Update the JSON sources and run `python3 tools/assemble.py` to regenerate the bundles when changing them. Preserve block topology, question option order, correct-answer indexes, critical flags, module IDs and visual-guide IDs across languages.

The existing Inspired logo, bundled Roboto/Open Sans fonts and PDF library are reused with their source and licence files. No fonts, analytics or scripts are requested from third parties at runtime.

## Completion and data handling

`localStorage` key: `inspired-intimate-care-v1`

Certificate prefix: `IC-ONLINE-`; course version: `1.0`

Personal details, drafts, saved responses, language, module state, answers, attempt history and certificate identity are stored in the participant's browser. A language change does not reset their work or translate their writing. Course identity and certificate identity remain separate from the existing Safe Hands course.

There is no central registration or delivery endpoint. Names are self-entered. Locally generated certificate references are not entries in a verified register. Client-side course records are not tamper-proof or a formal personnel system.

The full results download and prepared `.eml` contain entered staff details and reflections. The prepared email is addressed to the confirmed Head and copied to the participant; it is NOT sent by this application. Participants must open it in a compatible email client, review it and send manually. If the client cannot edit `.eml`, attach the results and certificate to a fresh email instead.

Do not enter real incidents, children's details, medical records or confidential school information. On shared computers, use a private window, download records and close the window afterward. Existing browser-stored data can be removed through browser site-data controls after downloading records. Removing site data for the shared hosting origin can also remove the separate Safe Hands course's storage, so download both course records first.

The practical checklist is deliberately not an online collection form. The school completes and retains its observation record in its approved secure system. The online course does not store an observer's decision or authorise practical care.

## Accessibility and motion

The interface includes labelled form controls, keyboard-focus styles, a skip link, status announcements, document language changes, responsive layouts and print styles. Explainers start paused, can be stepped through manually and expose the complete transcript. Reduced-motion preferences disable decorative pulsing and transitions. No sound or auto-playing video is used.

## Public availability

`noindex, nofollow` in HTML and the bundled crawler advisory request that compliant search engines do not index the page. They are not access controls. A public repository or Pages site remains viewable and shareable by anyone with its address. A project-folder `robots.txt` is not a host-root robots file. Hosting providers can log normal traffic even though the application does not submit participant records.

## Validation

See the separate QA handoff for exact test results and any remaining browser limitations. Tests use fictional identities only. An automated or native-canvas check does not establish clinical approval, translation correctness, practical competence or actual hosted browser download behaviour.

Before rollout, the school should check the approved local procedure against every lesson, assessment and visual script, have French/Kreol terminology reviewed, trial timing, test phone and desktop access and downloads, and assign the competent practical observer.
