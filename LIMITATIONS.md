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
