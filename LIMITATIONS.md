# Known Limitations & Things to Revisit

A running list of caveats across the three PMP study apps, so we can navigate/fix them later.
Last updated: 2026-05-30.

---

## General (all datasets)
- **Wording is paraphrased, not verbatim.** Questions/options were cleaned from auto-generated
  video transcripts and a PDF. Meaning is preserved, but text is not word-for-word.
- **Answers reflect the instructor (Andrew Ramdayal), not independent PMI doctrine.** Where the
  instructor says "best of four," that judgment is carried over as-is.
- **Some distractor options were reconstructed** where the source audio/PDF was garbled.
- **Sources:** transcripts are auto-captioned (occasional mis-hearings, e.g., "dorcy" = dormancy,
  "drop bonus" = dropped baton).

## 1) 200 Ultra-Hard Q&A (`qa_dataset.json` / `quiz.html`)
- **Video timestamps are approximate.** Only ~112 of 200 matched the transcript exactly; the rest
  are interpolated. Links land *within* the right question's segment, but early ones can be ~1–2 min
  into the discussion rather than at the first word. Source video: `1sWpc6765AI`.
- Multi-select items (e.g., Q16, 91, 104, 125, 140, 158, 179) store the answer as e.g. `"B, E"` and
  may include an `E` option — confirm the UI renders/scores these as intended.

## 2) 50 Mindset Principles (`principles_dataset.json` / `principles.html`)
- **Video timestamps:** principle start times are accurate (anchored to chapter markers, e.g.
  Principle 1 = 3:15); the per-question fallbacks are interpolated. Source video: `-u0rO-YQr9c`.
- A few principle titles/`key_point`s are our summaries, not the instructor's exact phrasing.
- Principle 82's source audio said "D" but the reasoning points to the "meet with stakeholders"
  option — recorded per the reasoning. Double-check if revisiting.

## 3) 100 Drag-and-Drop (`dnd_dataset.json` / `dnd.html`)
- **Extraction was rocky.** The PDF isn't cleanly parseable; content was recovered via coordinate
  parsing + transcript. Q90–100 were initially mis-extracted and corrected. **Worth a full
  re-read/spot-check of Q41–100 against the PDF for exact label spelling.** Source video: `K7J4WGbR9Ig`.
- **"By elimination" hybrids** (mirror the source, but conceptually debatable):
  - Q63 — "Iterative / Incremental Development" → Hybrid (it's normally agile; sorted to hybrid
    because Burn Down=Agile and Scope Baseline=Traditional take the other slots).
  - Q64 — "Balanced Team Structure" → Hybrid.
  - Q98 — "Continuous Stakeholder Engagement" → Hybrid (arguably "All").
- **Video timestamps:** only ~24 of 100 announcements matched; the rest are interpolated (coarser
  than the other two apps).
- **Reusable chips:** the engine lets a chip be placed in multiple slots (needed for Q19-style
  2-bucket sorts). For 1-to-1 matching questions, users could place duplicates; "Check" still flags
  them. Consider a per-question "consume chip" mode later.
- **UI is HTML5 drag + click-to-place.** Native drag may be fiddly on some touch devices; the
  click-to-place fallback is the reliable path. Not yet tested on mobile.
- Q19 (predictive vs agile) is a 10-item, 2-option sort — verify it reads clearly in the UI.

## 4) 150 PMBOK 7 — David McLachlan (`pmbok7_dataset.json` / `pmbok7.html`)
- Extracted from the spoken transcript ("150 PMBOK 7 by David McLachlan.md", video `Zht0-j03NfQ`).
  Questions, options, answers and explanations are paraphrased from the narration and grounded only
  in the transcript — **not** copied from the PMBOK 7 guide itself. PMBOK page citations that appear
  in explanations are the ones the instructor read aloud.
- **Video timestamps are accurate.** `video_time` is read directly from the per-line `M:SS` (and
  `H:MM:SS`) markers at the point each scenario begins, so links should land within a few seconds.
  Note: this is a long (~7-hour) video, so later questions have large timestamps.
- The transcript's chapter heading for the eleventh block is mislabeled "110-120"; those ten are
  numbered **111–120** consistently in the dataset (1–150 with no gaps/dups, verified).
- Extraction was fanned out across 15 parallel passes (10 questions each), then re-assembled and
  validated (every `correct_answer` maps to an existing option; all 150 present). A few answers where
  the instructor was ambiguous reflect the option he leaned toward.

## 5) 110 Drag & Drop — David McLachlan (`dnd2_dataset.json` / `dnd2.html`)
- Extracted from the spoken transcript ("110 DND by David McLachlan.md", video `wwNUBe21jtM`). There is
  no source PDF — items, terms, answers and explanations are paraphrased from the narration, grounded
  only in the transcript. PMBOK / Process Groups / Agile Practice Guide page citations are the ones the
  instructor read aloud.
- **111 questions, not 110:** the video ends with an explicit "bonus question 11" (a Myers-Briggs match),
  so the dataset has the 110 main questions plus that bonus = 111. The page is titled "110 (+1 bonus)".
- `video_time` is read from the per-line `M:SS` / `H:MM:SS` markers at each question's start (this is a
  ~2.5-hour video). One timestamp on the scope/quality question was auto-corrected during assembly
  (a stray value past the outro → its true 2:26:48 start).
- Each question is 1-to-1 matching (options count = items count), so the engine runs in "consume" mode:
  a placed chip is removed from the pool. Extracted via 11 parallel passes (one per section), then
  re-assembled and validated (every item's answer exists in its options; 0 issues).

## 6) 200 Agile PMP — David McLachlan (`agile_dataset.json` / `agile.html`)
- Extracted from the spoken transcript ("200 AGILE PMP.md", video `tNIHysh2ZW4`). Questions, options,
  answers and explanations are paraphrased from the narration, grounded only in the transcript.
- **195 questions, not 200:** the video is titled "200 Agile" but the instructor ends Section 28 after
  the genuine last question ("we're out of questions, we completed all of these"). After removing 3
  duplicate re-extractions at a chunk boundary (confirmed identical text/options/timestamps), the set
  contains **195 distinct questions**, numbered 1–195 with no gaps. The page keeps the "200 Agile" name.
- `video_time` is read from the per-line `M:SS` / `H:MM:SS` markers (this is a ~6.8-hour video); the
  full timeline is monotonic after dedup. Extracted via 20 parallel windowed passes, then de-duplicated,
  re-sorted, renumbered and validated (every answer maps to an option; 0 issues).
- Some questions reuse a common intro stem (e.g. the Agile Manifesto "in 2001 a group of individuals…")
  across different sub-questions — these are distinct questions with different options/answers, kept as-is.

## 7) Process Groups Practice Guide knowledge page (`processgroups_dataset.json` / `processgroups.html`)
- A KNOWLEDGE page (not a quiz), distilled from David McLachlan's mind-map walkthrough video
  (`b5X3Z6X56uk`) of the PMI Process Groups Practice Guide (formerly PMBOK 6). 8 sections / 52 subsections.
- Bullet points are concise paraphrases of the instructor's spoken explanation — meaning preserved,
  not verbatim, and not copied from the PMI guide itself.
- Each section and subsection has a `video_time` read from the per-line `M:SS` markers (minutes run
  past 59 in this ~62-min video); Watch links jump to that spot. Inner subsection timestamps are
  approximate to where the instructor begins that topic.
- Extracted via 8 parallel section passes, then assembled and validated (0 issues).

## 8) PMBOK 7 Body of Knowledge page (`pmbok7guide_dataset.json` / `pmbok7guide.html`)
- A KNOWLEDGE page (not a quiz), distilled from David McLachlan's PMBOK 7th Edition walkthrough video
  (`2gmCr40uT4U`). Structure: the 12 Principles, 8 Performance Domains, Tailoring, and Models/Methods/
  Artifacts — 13 sections / 94 subsections.
- Bullet points are concise paraphrases of the narration (meaning preserved, not verbatim, not copied
  from the PMI guide). Each section/subsection `video_time` comes from the per-line `M:SS` markers
  (minutes run past 59 in this ~61-min video); Watch links jump to that spot.
- Extracted via 13 parallel section passes, then assembled and validated (0 issues). Reuses the same
  generic knowledge-page renderer as the Process Groups page.

## 9) PMBOK 8 — All 40 Processes page (`pmbok8guide_dataset.json` / `pmbok8guide.html`)
- A KNOWLEDGE page (not a quiz), distilled from David McLachlan's PMBOK 8th Edition walkthrough video
  (`LcZvGRTJnLo`). PMBOK 8 returns to process groups; the page maps all 40 processes across the 5 groups
  (Initiating 2, Planning 19, Executing 8, Monitoring & Controlling 10, Closing 1), each with
  Inputs / Tools & Techniques / Outputs subsections.
- The 40th process ("Close the Project or Phase") has no standalone heading in the transcript — the
  instructor transitions inline (~1:12:02); captured correctly so the count is the full 40.
- Bullets are concise paraphrases of the narration (not verbatim, not copied from the PMI guide). Each
  process `video_time` comes from the per-line `M:SS`/`H:MM:SS` markers; Watch links jump to that spot.
- Process titles/group assignments follow the instructor's order; PMBOK 8 is draft/exposure material
  (the instructor notes it appears in the PMP exam from July 2026), so names may be refined by PMI.
- Extracted via 8 parallel block passes, assembled, grouped, and validated (40 processes, monotonic
  timestamps, 0 issues).

## 10) 100 Waterfall PMP — David McLachlan (`waterfall_dataset.json` / `waterfall.html`)
- Extracted from the spoken transcript ("100 Waterfall PMP Questions and Answers.md", video `xIH-u81XCxM`,
  drawn from PMBOK 6 / predictive). Questions, options, answers and explanations are paraphrased from the
  narration and grounded only in the transcript.
- 100 questions, clean 10-per-chapter structure; extracted via 10 parallel passes, assembled and validated
  (every answer maps to an option; 1–100 with no gaps/dups; 0 issues).
- `video_time` is read from the per-line `M:SS` markers (this is a long ~4.8-hour video). Two minor
  timestamp dips at the Q60 and Q71 chapter boundaries are harmless (distinct questions; links still land
  in the right segment).

## 11) 63 Project Management Tools page (`tools_dataset.json` / `tools.html`)
- A KNOWLEDGE page (not a quiz), distilled from David McLachlan's "63 Project Management Tools" video
  (`vi0drXKr7PM`), which walks the tools through an example project (PetBuddy) from initiation to risk.
- Organised into 11 phase sections; **64 distinct tool entries** are presented (the video is titled "63"
  — the page keeps that name; the heading count came out at 64, likely a one-off split in the source).
- Each tool has 2-4 paraphrased bullets and a `video_time` from the per-line `M:SS` markers (Watch links
  jump to that tool). Tool timeline verified monotonic; extracted via 11 parallel phase passes, validated
  (0 issues). Bullets are faithful paraphrases, not verbatim PMI text.

## 12) Exam simulator — ECO-weighted, multi-bank (`exam.html`)
- The simulator now mixes questions from all four multiple-choice banks (qa_dataset, pmbok7_dataset,
  agile_dataset, waterfall_dataset) and samples them weighted to the PMI ECO domain ratio
  (People 42% / Process 50% / Business Environment 8%). After a test it stores the result in
  localStorage (`pmp_exam_history`, last 20) and shows a per-domain accuracy breakdown vs the ECO target.
- Each question carries an `eco_domain` field added to the four datasets. **These domain tags are
  heuristic** — assigned by an LLM pass over the question + correct answer, not by PMI. Overall pool
  skews Process-heavy (People 187 / Process 420 / Business Environment 38 of 645), so the Business
  Environment pool (38) caps very large Business-Environment-heavy selections; the sampler fills any
  shortfall from other domains. Treat the domain match as study guidance, not an official score.

## Tooling / process notes
- During the DnD build, the sandbox intermittently ate/garbled tool stdout, which caused a failed
  silent append and a mis-extraction before they were caught and fixed. If we do another large
  extraction, prefer: build datasets via a Python script (load/modify/write + assertions) rather
  than large text edits, and gate commits on an assertion so bad data can't be published.

## Nice-to-have backlog (not bugs)
- Verbatim "source_lines" / transcript references per item for traceability.
- Rename repo subfolder `pmp prep` → `pmp-prep` for a cleaner Pages URL (currently `%20`).
- Mobile/touch QA pass on `dnd.html`.
- Cross-link or unify the 3 apps' shared UI (theme, video-link helper) into one shared snippet.
