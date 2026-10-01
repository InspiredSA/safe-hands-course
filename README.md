# Safe Hands Safe Children

A one-hour Early Years safeguarding pilot course for Inspired Education teachers and teaching assistants.

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

The site uses relative asset paths and requires no build step. `index.html`, `style.css`, `app.js`, `certificate.js`, `course-data.js` and `vendor/pdf-lib.min.js` make up the course. The bundled PDF library licence is included in `vendor`.

## Validation completed

On 1 October 2026, 41 automated source and logic checks passed against this edition. Coverage included participant validation, module and reflection requirements, acknowledgements, the 80% threshold, each critical-question failure at 19/20, stable certificate references, browser-storage save/restore with a test double, HTML escaping, complete results, PDF container generation and prepared-email contents. PDF generation used the actual bundled PDF library with a stubbed drawing canvas; this does not establish visual rendering or browser download behavior.

JavaScript syntax checks also passed. Interactive browser testing of the final hosted URL remains required, including a phone-sized layout, refresh and back/forward navigation, certificate/results downloads and the prepared email. No emails were sent during testing.

The learner navigation no longer exposes owner review notes, the old review-storage footer or the reset control. Safeguarding contacts remain available on narrow screens. Data-handling information remains in the participant form and results workflow.

## Public availability and search indexing

The HTML includes `noindex, nofollow`, and a `robots.txt` crawler advisory is included. These are requests to compliant crawlers, not authentication or privacy controls. A project-site `robots.txt` is below the host root and may not be consulted by crawlers; the HTML robots directive is the page-level safeguard. A public GitHub repository and public Pages site can still be accessed, copied and shared by anyone with the address. Do not add real incident reports or staff/child records to this repository.

The application has no external submission, analytics or email endpoint, and all scripts are bundled locally. Ordinary hosting traffic can still be logged by the hosting provider. Learner-entered details remain in browser storage until the learner clears the site's data; downloaded reports and email drafts contain their entered details.

## Official hosting references

- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
