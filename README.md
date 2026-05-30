# PMP Quiz Study

A self-contained, single-file quiz study app for PMP exam prep, plus the structured
question dataset it runs on.

## Contents

| File | Description |
|------|-------------|
| `quiz.html` | The 200-question quiz app (no build step — open in a browser). |
| `qa_dataset.json` | 200 PMP practice questions: `number`, `question`, `options` (A–E), `correct_answer`, `explanation`. |
| `principles.html` | The 50 Mindset Principles study app — Learn, Flashcards, Quiz, and Mind Map modes. |
| `principles_dataset.json` | 50 PMP mindset principles: `number`, `title`, `category`, `key_point`, `knowledge`, plus a practice `question`/`options`/`correct_answer`/`explanation`. |
| `dnd.html` | The Drag-and-Drop practice app — match items to categories by dragging (or clicking). |
| `dnd_dataset.json` | PMP drag-and-drop questions: `number`, `prompt`, `left_label`, `right_label`, `items` (text→answer), `options`, `explanation`, `video_time`. |
| `200 untra hard transcript.md` | Source transcript for the question dataset. |
| `50 Principles.md` | Source transcript for the principles dataset. |
| `progress.md` | Extraction progress log. |

## 50 Mindset Principles app (`principles.html`)

- **Learn** — all 50 principles grouped by category, with a key idea + explanation, searchable.
- **Flashcards** — two modes: *Principle → meaning* and *Scenario → apply*; flip, shuffle, mark Known / Need-review, review-only filter.
- **Quiz** — one practice question per principle with instant scoring and explanations.
- **Mind Map** — central node → 11 category branches → principle leaves; click a leaf for its key idea.
- Dark/light theme, progress saved to localStorage.

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
