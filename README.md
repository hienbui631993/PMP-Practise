# PMP Quiz Study

A self-contained, single-file quiz study app for PMP exam prep, plus the structured
question dataset it runs on.

## Contents

| File | Description |
|------|-------------|
| `quiz.html` | The quiz app (no build step — open in a browser). |
| `qa_dataset.json` | 200 PMP practice questions: `number`, `question`, `options` (A–E), `correct_answer`, `explanation`. |
| `200 untra hard transcript.md` | Source transcript the dataset was extracted from. |
| `progress.md` | Extraction progress log. |

## Features

- Display Q&A with A–D (and E for multi-select) options
- Stores your answer and **time spent per question** (localStorage)
- Next / Prev, Clear Answer, Show Answer, Jump to #
- **Question list** with short text + status colors
- **Results summary** (answered, correct, accuracy, time)
- **Shuffle mode**
- **Dark / light theme** toggle
- **Instant feedback** toggle (show correct answer immediately or not)
- **Random practice sets** of 15 / 50 / 180 questions, timed or untimed
- 30-minute study reminder pop-up
- Export results to CSV

## Run

The app needs a static server so it can `fetch` the JSON (browsers block local
file reads when opened directly):

```bash
python -m http.server 8000
# then open http://localhost:8000/quiz.html
```

Alternatively, just open `quiz.html` and use the file picker to load
`qa_dataset.json` manually.
