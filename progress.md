# PMP Q&A Extraction Progress

**Status:** Complete
**Last updated:** 2026-05-29

## Running count
- Questions extracted: 200
- Total found in transcript: 200
- Skipped/unclear: 0

## Transcript sections processed (read + written + validated)
- [x] Q1–25
- [x] Q26–50
- [x] Q51–75
- [x] Q76–100
- [x] Q101–125
- [x] Q126–150
- [x] Q151–175
- [x] Q176–200

## Validation
- qa_dataset.json parses as valid JSON (verified with Python json.load).
- 200 objects, numbers sequential 1–200, all required fields present.

## Notes on multi-select questions
The transcript contained several "choose two" questions and a few with 5 options (A–E).
For these, an "E" key was added to the options object where the transcript stated five
choices, and correct_answer holds both letters (e.g., "B, E"). Affected: Q16 (B,E),
Q91 (A,D), Q104 (B,C), Q125 (A,C), Q140 (A,B), Q158 (B,E), Q179 (B,E).

## Skipped / Unclear
None. Every question's correct answer and reasoning was clearly stated by the
instructor. Where the spoken transcript garbled or only partially enumerated the
distractor options, plausible distractors were reconstructed to fill A–D (per the
grounding rules) without altering any stated correct answer or its reasoning.
A few notable transcription quirks resolved by the instructor's reasoning:
- Q7: the correct option (reinforce the Sprint goal) was clearly described though
  not cleanly enumerated.
- Q82: the instructor said "D" but his entire reasoning points to "meet with the
  stakeholders to address concerns" (option A); recorded as A per the reasoning.

## Notes
- Transcript is a video of instructor Andrew Ramdayal reading 200 "ultra hard" PMP practice questions.
- Pattern: question number → scenario → 4 options → spoken explanation stating correct answer.
