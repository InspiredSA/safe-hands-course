/* Focused checks for participant-facing wording and generated dictionary parity. */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const root = path.resolve(__dirname, '..');
const ctx = { window: {} };
vm.createContext(ctx);
for (const file of ['course-data.js', 'course-data-fr.js', 'course-data-mfe.js', 'i18n.js', 'course-extras.js']) {
  vm.runInContext(fs.readFileSync(path.join(root, file), 'utf8'), ctx, { filename: file });
}
const plain = value => JSON.parse(JSON.stringify(value));
const rows = [
  ['en', 'COURSE', /paper or digital/, /contact time/, /Never mix chemicals or use an unlabelled container/, /Do not wait for the next scheduled change/],
  ['fr', 'COURSE_FR', /papier ou numérique/, /temps de contact/, /Ne mélangez jamais de produits chimiques et n’utilisez jamais de contenant sans étiquette/, /N’attendez pas le prochain change programmé/],
  ['mfe', 'COURSE_MFE', /papie ouswa nimerik/, /dire kontak/, /Zame melanz bann prodwi simik ouswa servi enn resipian san etiket/, /Pa atann prosenn sanzman lor program/]
];
let passed = 0;
function check(name, fn) { fn(); passed++; console.log('PASS ' + name); }
for (const [lang, globalName, recording, contact, chemicalSafety, promptCare] of rows) {
  const data = plain(ctx.window[globalName]);
  const extra = plain(ctx.window.COURSE_EXTRAS[lang]);
  const ui = plain(ctx.window.COURSE_UI[lang]);
  check(lang + ' generated dictionaries equal authoring JSON', () => {
    assert.deepEqual(ui, JSON.parse(fs.readFileSync(path.join(root, `ui-${lang}.json`), 'utf8')));
    assert.deepEqual(extra, JSON.parse(fs.readFileSync(path.join(root, `course-extras-${lang}.json`), 'utf8')));
  });
  check(lang + ' no tablet dependence or source-discussion content', () => {
    assert.doesNotMatch(JSON.stringify([data, extra]), /tablet|CDC|UKHSA|NSPCC|ACECQA|2020|foundation|Fondement|Baz regleman|Baz bann sours|three-to-four|trois à quatre|trwa a kat-er/i);
    assert.equal(extra.sources, undefined);
    assert.equal(data.reference.length, 2);
    for (const key of ['sourceTitle', 'sourceLead', 'sourcesDate']) assert.equal(ui[key], undefined);
    assert.ok(ui.referenceTitle);
  });
  check(lang + ' scenario and routine reporting allow paper or digital records', () => {
    assert.match(data.modules[2].pages[1].blocks[1].text, recording);
    assert.match(data.modules[2].pages[1].blocks[7].text, recording);
    assert.match(data.modules[5].pages[0].blocks[2].text, recording);
    assert.match(extra.localReadiness[9].text, recording);
  });
  check(lang + ' practical cleaning retains contact time and chemical safeguards', () => {
    const lesson = data.modules[3].pages[0].blocks;
    assert.match(lesson[5].text, contact);
    assert.match(lesson[6].text, chemicalSafety);
    assert.match(extra.localReadiness[6].text, chemicalSafety);
    assert.ok(lesson[5].text.length < 500 && lesson[6].text.length < 500);
  });
  check(lang + ' care timing is prompt and independent of a schedule', () => {
    assert.match(data.modules[4].pages[0].blocks[11].text, promptCare);
    assert.equal(data.questions[14].answer, 0);
  });
  check(lang + ' IDs, answer order and critical gates are intact', () => {
    assert.deepEqual(data.modules.map(module => module.id), [1, 2, 3, 4, 5, 6]);
    assert.equal(data.questions.length, 20);
    assert.deepEqual(data.questions.map(question => question.answer), plain(ctx.window.COURSE.questions.map(question => question.answer)));
    assert.deepEqual(data.questions.flatMap((question, i) => question.critical ? [i + 1] : []), [3, 6, 8, 10, 11]);
    assert.deepEqual(extra.practice.map(item => item.a), [1, 2, 0, 1, 2, 0]);
    assert.deepEqual(extra.visualGuides.map(guide => guide.id), ['prepare', 'sequence', 'reassure']);
  });
}
check('Resources renderer does not publish research provenance', () => {
  const code = fs.readFileSync(path.join(root, 'extras.js'), 'utf8');
  assert.doesNotMatch(code, /EXTRA\.sources|sourceTitle|sourceLead|sourcesDate/);
  assert.match(code, /referenceTitle/);
});
check('Maintainer README retains source provenance and safety boundaries', () => {
  const readme = fs.readFileSync(path.join(root, 'README.md'), 'utf8');
  for (const text of ['Research provenance for maintainers', 'CDC', 'UKHSA', 'NSPCC', 'ACECQA', 'July 2020']) assert.ok(readme.includes(text));
});
console.log(`\n${passed} focused staff-content checks passed. These checks do not replace school or fluent-speaker approval.`);
