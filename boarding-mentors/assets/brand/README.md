# Inspired brand assets

Reference inspected on 1 October 2026: https://www.inspirededu.com/

The design uses public website evidence, not an internal brand manual. `inspiredschools.com` did not provide school brand content when checked; its response was a short redirect to `/lander`. The official reference is Inspired Education's `inspirededu.com` site.

## Verified website palette

- Primary navy: `#122147`
- Heading navy: `#143256`
- Secondary blue-gray: `#5B7A95`
- Secondary dark: `#415165`
- Accent blue: `#1B75BB`
- Accent sand: `#EED6AB`
- Accent red: `#C02F4D`
- Accent gray: `#B1B6BF`
- Website paragraph gray: `#81818C`
- Dark text: `#2F2F32`

For an instructional course, darker body text is recommended for legibility. White and navy should dominate, with blue for active controls and progress. Sand is a secondary accent, not a primary gold identity.

Palette source: https://d24d7vsshzrslo.cloudfront.net/sites/company/files/color/born_ready_bs4_bahamas-4cc60c4a/colors.css?tlx1uz

## Logos

- `inspired-logo-colour.png`: genuine 193 × 71 transparent PNG. Its flat colors are slate `#415266` and blue `#1B75BC`
  - Source: https://d24d7vsshzrslo.cloudfront.net/sites/company/files/2021-11/inspired_logo_colour.png
- `inspired-logo-white.png`: genuine 193 × 71 transparent PNG for dark backgrounds
  - Source: https://d24d7vsshzrslo.cloudfront.net/sites/company/files/Inspired_Logo_White.png

Preserve aspect ratio, clear space, and original colors. Do not recreate the wordmark in a substitute typeface or stretch it. These files are brand assets, not open-source artwork. Downloading them does not grant a license or imply Inspired approval. Website terms section 7 reserves rights and requires the owner's express written authorization for public or commercial reuse: https://www.inspirededu.com/website-terms-use

## Typography

The official website declares Roboto for headings, links, and buttons and Open Sans for body copy. This is verified in:
https://d24d7vsshzrslo.cloudfront.net/profiles/custom/born_ready_profile/themes/born_ready_bs4/css/fonts/roboto_opensans.css?tlx1uz

The local WOFF2 files are the Latin regular-weight fonts returned by the official site's Google Fonts import, https://fonts.googleapis.com/css?family=Roboto|Open+Sans. The Latin files include Spanish accented letters and punctuation. The course should use local files instead of external font calls. Current regular files have weight 400; browser synthesis may be used for bold if further font weights are not provided.

- `open-sans-regular-latin.woff2`
  - https://fonts.gstatic.com/s/opensans/v44/memSYaGs126MiZpBA-UvWbX2vVnXBbObj2OVZyOOSr4dVJWUgsjZ0B4gaVI.woff2
- `roboto-regular-latin.woff2`
  - https://fonts.gstatic.com/s/roboto/v51/KFOMCnqEu92Fr1ME7kSn66aGLdTylUAMQXC89YmC2DPNWubEbVmUiAo.woff2

Both fonts are supplied under the SIL Open Font License 1.1. Keep `OpenSans-OFL.txt` and `Roboto-OFL.txt` with redistributed fonts. License sources:

- https://raw.githubusercontent.com/google/fonts/main/ofl/opensans/OFL.txt
- https://raw.githubusercontent.com/google/fonts/main/ofl/roboto/OFL.txt

## Practical course adaptation

Use the white logo on a compact navy header/sidebar, restrained blue accents, generous white content panels, regular-weight Roboto headings, readable Open Sans paragraphs, and pill-shaped main actions. Keep learning navigation and the next activity immediately visible. The official marketing site's oversized full-screen video hero is not suitable for a course workspace and need not be copied.
