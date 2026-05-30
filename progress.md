# PMP Q&A Extraction Progress

## Status: COMPLETE
- 200 Ultra-Hard questions: 200 / 200 → qa_dataset.json
- 50 Mindset Principles: 50 / 50 → principles_dataset.json
- 100 Drag-and-Drop: 100 / 100 → dnd_dataset.json
- 150 PMBOK 7 (David McLachlan): 150 / 150 → pmbok7_dataset.json

## Notes
- Sources:
  - "200 untra hard transcript.md" (video 1sWpc6765AI)
  - "50 Principles.md" (video -u0rO-YQr9c)
  - "100 pmp dnd.md" + TIA PDF (video K7J4WGbR9Ig)
  - "150 PMBOK 7 by David McLachlan.md" (video Zht0-j03NfQ)
- Each Q&A entry: number, question, options (A-D, sometimes E), correct_answer, explanation, video_time
- Questions grounded strictly in transcript content
- Multi-select questions stored with comma-separated answers (e.g., "B, E")
- Distractors generated only when instructor gave just the correct answer
- video_time = seconds from the transcript's M:SS markers (PMBOK 7 set parsed directly from per-line timestamps)

## Apps built
- index.html — study hub linking all apps
- quiz.html — 200-question study UI
- pmbok7.html — 150 PMBOK 7 scenario questions (David McLachlan)
- principles.html — 50 mindset principles
- dnd.html — 100 drag-and-drop questions
- eco.html — Examination Content Outline
- exam.html — Pearson VUE-style simulator
