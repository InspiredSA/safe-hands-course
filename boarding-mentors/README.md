# Boarding Mentor Essentials

An English-only pilot course based on the supplied Inspired South Africa Boarding Mentors Standards Handbook 2026 (version 1.1, July 2026).

## Status and intended use

The source handbook requires legal, HR, safeguarding, nursing and health-and-safety specialist review before formal adoption. This course is clearly marked as a pilot for leadership review. It does not establish that formal approval has occurred.

The course is learning support, not a live incident reporting channel. Real concerns must use current approved school reporting, medical and emergency procedures. Scenarios are fictional. Learners must not enter real pupil names, private information, live incidents or medical information into their responses.

## Learning and completion

- Eight modules; approximately 75–90 minutes, with extra time to verify local procedures.
- Thirteen fictional scenarios, each with a written response, a decision check and explanatory feedback.
- Eight required written reflections.
- Twenty assessment questions; at least 16 correct (80%) and all six critical answers correct.
- Participant details and completion declarations are required before generating a completion certificate.
- Written responses have a minimum-presence check of 40 characters; they are not automatically graded for quality. Suggested word counts in the reflection prompts support fuller answers.
- Edited scenario responses must be compared with feedback again before the module is complete.
- All assessment attempts are retained in the browser and full answer record.

The threshold is a course design choice, not a source-handbook rule. The certificate records online course completion only. It does not confirm Head of Boarding review, observed competence, professional accreditation or authorisation for unsupervised duty. Local induction, role-specific shadowing and formal competence sign-off remain separate requirements.

## Email and records

Learners enter their own name, work email, school and Head of Boarding email; the recipient is repeated and confirmed by the learner using a trusted school source. The site does not verify that address independently.

Completion provides:

1. A UTF-8 full answer record (.txt), including the learner's written responses, decision choices, feedback, reflections, declarations and assessment history.
2. A named PDF completion certificate, if eligible.
3. An addressed mailto draft and copyable email text.

Opening an email draft does not send email or attach files. The learner downloads the files, manually attaches them to their school email, checks the recipient and attachments, and sends the email themselves. No delivery confirmation is recorded by the site. Do not add credentials or an email API key to a public static site.

## Privacy and storage

All entered details and progress are stored in this browser under the course-specific local-storage key `inspired-boarding-mentors-learning-v1`. There is no external form submission, analytics, automatic email endpoint or central response register. Hosting providers may still record normal hosting traffic. The course and repository are publicly accessible; noindex is advisory, not access control.

Coursework can be downloaded before completion. On a shared computer, learners should download/send records and clear this course's saved work. Clearing affects only this course's key, not other courses or downloaded files. Corrupt or version-mismatched saved records are preserved for backup and require an explicit reset before being replaced. Storage errors are shown visibly.

## Practical reference handbook

The `downloads/` folder contains the reviewed 12-page companion in PDF and editable Word formats. It condenses the learning into an on-duty reference and retains the source-review caveat and local-procedure boundaries. It is not the original full source handbook.

## Build and assets

No build step. Serve this folder with a static HTTP server. Local fonts, Inspired logo assets and the bundled PDF library match the established InspiredSA course assets. Font and library licences are included. Certificate generation uses a canvas image for Unicode rendering and the bundled pdf-lib. The accessible answer record and HTML completion preview provide textual equivalents.

New files are isolated to `/boarding-mentors/`; the existing safeguarding, intimate-care and co-regulation courses are unchanged. Do not publish the original source handbook, private review notes, actual learner records or test exports.

## Validation

The pilot passed 87 deterministic regression checks on 9 October 2026. Coverage includes missing details, recipient checks, required responses, edited-response invalidation, all module gates, 80% threshold, every critical-question failure, retries, attempt history, browser-state reload, corrupt/version-mismatched state, quota failures, certificate identity, Unicode text, HTML escaping, email draft wording, reset confirmation/cancellation and all course routes. JavaScript syntax checks passed. The certificate was rendered with the actual bundled PDF library, local fonts and native canvas; normal and maximum-length names were visually inspected.

These deterministic tests do not replace real browser checks. Live browser QA follows pilot deployment before the link is handed over for review. The source handbook review and final school approval remain separate.
