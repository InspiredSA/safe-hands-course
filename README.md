# Safe Hands Safe Children – Level 1

A one-hour English/French/Kreol Morisien Early Years safeguarding pilot course for Inspired Education teachers and teaching assistants.

Live course: https://inspiredsa.github.io/safe-hands-course/ (existing project site).

## What is included

- Five modules, quick checks and written reflections.
- Required full name, work email, school and Head's email, with recipient confirmation.
- A 20-question assessment requiring at least 16 correct answers and all five critical questions correct.
- Automatic eligibility for a downloadable, named PDF pilot completion certificate after every module, reflection and acknowledgement is completed.
- Full results download with answers, feedback, reflections, acknowledgement and attempt history.
- A prepared email file addressed to the Head, copied to the participant, with full results and a certificate attachment when eligible.

Written responses are ungraded reflections in this pilot. Certificate references are generated locally and are not entries in a central verification register. Names are self-entered. Completion does not certify practical restraint competence.

## Publish on GitHub Pages

1. Create a repository such as `safe-hands-course` in the desired GitHub account. GitHub Free supports Pages from public repositories. Select a private repository only if your plan supports Pages for it.
2. Upload the contents of this folder, including the `vendor` folder, into the repository root. Upload the extracted files, not the ZIP itself. `index.html` must be at the root.
3. Open the repository's **Settings**, then **Pages**.
4. Under **Build and deployment**, select **Deploy from a branch**. Select `main` and `/(root)`, then save.
5. Wait for GitHub's Pages deployment to complete and open the exact URL shown in Settings. In the InspiredSA account, a repository named `safe-hands-course` would normally publish at `https://inspiredsa.github.io/safe-hands-course/`. That URL is illustrative until the repository and Pages deployment exist.
6. Test the published site on a phone and computer, including the required details, certificate download and prepared email. Moving to a different domain does not transfer browser-saved progress.

A school-owned custom domain can be configured later through GitHub Pages and the organisation's DNS administrator.

## Data and email delivery status

This version stores drafts, personal details, progress and results in the participant's browser only. It does not send them to a central register. A participant should download their records before clearing browser data or moving devices. On a shared device, use a private browsing window, download the results and close the window when finished. For records already saved in an ordinary window, use the browser’s site-data controls to remove the saved data after downloading it.

Automatic email delivery is NOT connected. Download email for Head creates a local `.eml` file; it does not send an email. The participant must open it in a compatible email application, check the recipient and send it. If the email application does not allow editing the prepared file, attach the full results and certificate to a new message instead.

For fully automatic delivery, connect a school-controlled server-side email service. Keep sending credentials off this public site. Validate and verify approved recipient addresses, calculate results on the server, handle retries without duplicate messages, and record delivery status. A suggested Resend connection has not yet been confirmed. GitHub Pages alone does not run a server-side email process.

## Before wider rollout

Confirm current approved policy versions, resolve the flagged restraint-policy distinction, add each school's contacts and local reporting procedures, and pilot the planned timing. Do not report real safeguarding incidents or include real children's information in training responses.

## Files

The site uses relative asset paths and requires no build step. `index.html`, `style.css`, `app.js`, `certificate.js`, `i18n.js`, `course-data.js`, `course-data-fr.js`, `course-data-mfe.js`, `assets/brand/` and `vendor/pdf-lib.min.js` make up the course. The bundled PDF library licence is included in `vendor`.

## Validation completed

On 1 October 2026, the bilingual edition passed the existing 47-check regression suite and 60 independent bilingual/source/logic checks. Coverage included exact requested content removals; English/French schema and answer-index parity; every participant route; language switching and browser-storage migration; unsubmitted profile, reflection and checkbox drafts; translated validation; participant validation; module and reflection requirements; acknowledgements; the 80% threshold and each critical-question failure; stable certificate references; HTML escaping; full results; French PDF metadata; UTF-8 prepared-email contents; async output language capture; and file-save fallback links.

PDF container generation used the actual bundled library with a stubbed drawing canvas. JavaScript syntax checks passed. A local headless-browser run was attempted but this execution environment prevented Chromium from opening local sockets, so it did not run. These automated checks do not establish visual rendering or browser download behavior. Final hosted-browser QA remains required, including French accented text in the PDF, phone-sized layout, refresh and back/forward navigation, certificate/results downloads and prepared email. No emails were sent during testing.

The participant navigation no longer exposes owner review notes, the old review-storage footer or the reset control. Safeguarding contacts remain available on narrow screens. Data-handling information remains in the participant form and results workflow.

## Public availability and search indexing

The HTML includes `noindex, nofollow`, and a `robots.txt` crawler advisory is included. These are requests to compliant crawlers, not authentication or privacy controls. A project-site `robots.txt` is below the host root and may not be consulted by crawlers; the HTML robots directive is the page-level safeguard. A public GitHub repository and public Pages site can still be accessed, copied and shared by anyone with the address. Do not add real incident reports or staff/child records to this repository.

The application has no external submission, analytics or email endpoint, and all scripts are bundled locally. Ordinary hosting traffic can still be logged by the hosting provider. Participant-entered details remain in browser storage until the participant clears the site's data; downloaded reports and email drafts contain their entered details.

## Official hosting references

- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Multilingual implementation (version 2.3)

The persistent English / Français / Kreol Morisien selector changes the document language, navigation, lessons, activities, assessment, feedback, acknowledgements, participant form, validation, contacts, dates and downloadable results/certificate/email. Participant-entered text is preserved verbatim. Existing participant storage uses the same key, so deploying this edition on the same origin preserves prior records. Language, profile drafts, responses, quiz answers and activity-tab state survive a refresh. Certificate identity is independent of display language.

`i18n.js` holds keyed interface strings in matching English/French/Kreol Morisien dictionaries. `course-data-fr.js` and `course-data-mfe.js` mirror the English content structure, IDs and correct-answer indexes. The language code for Kreol Morisien is `mfe`; its dates use explicit translated month names and a 24-hour time format because browsers do not consistently support that locale. Section roles use the canonical English structure rather than matching translated display words. Download generation captures the chosen language at the start so switching language cannot mix an in-progress PDF or email. The certificate is rasterized on a canvas using locally bundled fonts, preserving accented characters without PDF standard-font encoding limitations.

The course uses the official Inspired logo, Roboto/Open Sans typefaces and the navy/blue palette verified from Inspired’s website. Font licences and sources are in `assets/brand/README.md`. No external font or analytics requests are needed. The header’s “Pilot edition” badge has been removed as requested; the existing pilot completion and competence caveats remain elsewhere.

The course is titled “Safe Hands Safe Children – Level 1” in English and “Des mains bienveillantes, des enfants en sécurité – Niveau 1” in French. This display-name change does not alter the project URL, local-storage key, participant progress or certificate references.

## Kreol Morisien translation review

Kreol Morisien is available as a complete third course-language option, including lessons, activities, assessment, feedback, interface, participant validation, contacts and downloadable records. This translation is a draft awaiting review by a fluent Kreol Morisien speaker familiar with safeguarding. Availability is not approval or a claim of translation accuracy. A localized review notice appears on every Kreol Morisien screen, in printed summaries and full results/prepared email, and a shorter warning appears on the Kreol Morisien certificate. If wording is unclear, check the English/French version and the school's approved current policy. The school should complete a safeguarding and terminology review before relying on this version for wider training.

Switching languages never translates participant-written responses and does not reset details, drafts, module progress, answer selections, attempt history, acknowledgements or existing certificate references. New certificates carry version 2.3; previously issued locally saved certificates keep their existing identity and version. Course content is selected explicitly for each language with no English content fallback for Kreol Morisien. The completion threshold, all five critical-question gates and local-only privacy model are unchanged.

## Kreol Morisien validation completed

On 1 October 2026, the third-language implementation passed 83 dedicated multilingual checks, all 47 baseline regression checks and all 70 current bilingual regression checks (200 total). Coverage includes three-way language switching; full course/UI schema, question, critical-flag and interpolation parity; every route and activity; persistent and printed review notices; explicit Kreol month formatting; unchanged participant input and certificate identity; stored draft/answer migration; translated validation; completion gates; full results; PDF metadata; UTF-8 prepared email; captured async export language; no certificate on failed completion; and no added external data transport. JavaScript syntax checks pass for every application/data file.

The actual certificate drawing code was also rendered with native canvas, the bundled fonts/logo and bundled PDF library, and visually inspected: the Kreol title, accented participant data, localized date, original caveats and review notice fit without clipping. This native-canvas check does not establish browser download behavior. Local Chromium startup was attempted again and blocked by the environment's socket restrictions before any page actions. Hosted-browser checks are still needed for real switching, responsive layout, refresh/back/forward, print and downloadable output. The translation itself still requires the stated fluent-speaker review.
