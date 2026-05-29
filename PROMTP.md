I have a transcript file (transcript.md) of a PMP exam-prep video where an
instructor reads practice questions aloud, lists the answer options, then
explains which option is correct and why.

Read the entire transcript and convert it into a structured Q&A dataset.

TASK
- Extract up to 200 questions (as many as the transcript genuinely supports —
  do not pad, duplicate, or invent questions to reach 200).
- For each question, produce these fields:
    1. number         — sequential question number
    2. question       — the scenario/question text, cleaned of spoken filler
    3. options         — object with keys A, B, C, D
    4. correct_answer — the correct option letter
    5. explanation    — why it's correct (and why others are wrong)

GROUNDING RULES (important)
- The question, correct_answer, and explanation must come ONLY from what the
  instructor actually says in the transcript. Do not add outside PMP knowledge
  or assume answers the transcript doesn't state.
- If the transcript clearly states the options, use them. If the instructor
  only describes the correct answer without giving full distractors, generate
  plausible-but-incorrect distractors to fill A–D, but never alter the stated
  correct answer or its reasoning.
- If a question's correct answer or reasoning isn't clearly stated in the
  transcript, skip it rather than guess. Record skipped/unclear items in the
  progress file.

CLEANUP
- Strip timestamps and the instructor's asides (e.g. "we got 199 more to go",
  "okay okay", "all right") so the question/option text reads cleanly while
  keeping the original meaning intact.

PROGRESS TRACKING
- Create and maintain a progress.md file that you update AS YOU WORK, not just
  at the end. It should contain:
    - A status line (e.g. "In progress" / "Complete")
    - A running count: questions extracted so far / total found / skipped
    - A checklist of transcript sections processed
    - A "Skipped / Unclear" list with the question number and a one-line reason
    - A timestamp of the last update
- Update progress.md after each batch of ~25 questions so I can watch progress.

OUTPUT
- Write the dataset to qa_dataset.json as an array of question objects with the
  fields above. Ensure it is valid, parseable JSON.
- When finished, set progress.md status to "Complete" and print a short
  summary: total extracted, total skipped, and the path to the JSON file.