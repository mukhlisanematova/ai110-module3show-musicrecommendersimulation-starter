# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This system scores every song in a 20-song catalog against a user taste profile and returns the top-K matches ranked by a weighted point total. It combines categorical preference matching (genre, mood) with continuous audio-feature proximity (energy, valence, tempo, danceability, acousticness) to produce explainable recommendations.

---

## How The System Works

### Song Features

Each song carries 7 scoreable attributes loaded from `data/songs.csv`:

| Feature | Type | Range |
|---|---|---|
| `genre` | categorical | pop, rock, lofi, jazz, metal, blues, … |
| `mood` | categorical | happy, chill, intense, moody, focused, … |
| `energy` | float | 0.0 – 1.0 |
| `tempo_bpm` | float | ~50 – 180 |
| `valence` | float | 0.0 – 1.0 (sad → joyful) |
| `danceability` | float | 0.0 – 1.0 |
| `acousticness` | float | 0.0 – 1.0 |

### User Profile

The user profile is a dictionary of target values for each feature above, for example:

```python
user_prefs = {
    "genre":        "indie pop",
    "mood":         "happy",
    "energy":       0.75,
    "tempo_bpm":    115,
    "valence":      0.78,
    "danceability": 0.80,
    "acousticness": 0.25,
}
```

### Algorithm Recipe — Scoring Logic

Each song is scored against the profile using additive weighted rules. Maximum possible score is **6.75 points**.

| Signal | Weight | Rule |
|---|---|---|
| Genre match | **+2.0** | Exact string match |
| Mood match | **+1.5** | Exact string match |
| Energy proximity | **+1.0** | `1.0 − │user − song│` |
| Valence proximity | **+0.75** | `1.0 − │user − song│` |
| Tempo proximity | **+0.50** | `1.0 − │diff / 200│` (normalized) |
| Danceability proximity | **+0.50** | `1.0 − │user − song│` |
| Acousticness proximity | **+0.50** | `1.0 − │user − song│` |

All songs are scored, sorted descending, and the top K are returned with a plain-language explanation built from the contributing reasons.

### Data Flow

```
User Prefs ──┐
             ├──► score_song() ──► (score, reasons) ──┐
songs.csv ───┘   [× 20 songs]                         ├──► sort ──► Top-K
                                                       │
                                              scored_songs list
```

### Known Biases and Limitations

- **Genre over-weighting:** At 2.0 points, genre dominates. A perfect-audio-match song in the wrong genre will almost always rank below a mediocre same-genre song. This can bury genuinely similar songs that just have a different label (e.g., "indie pop" vs. "pop").
- **Mood label brittleness:** `"relaxed"` and `"chill"` feel similar to a human but score 0 against each other. The system treats mood as a binary hit/miss, not a spectrum.
- **Catalog bias:** The 20-song catalog was hand-authored. Genres the author knows well (pop, lofi) have more songs and more variation, so those users get better recommendations by default.
- **Single-user assumption:** The profile is one fixed dict. There is no history, no feedback loop, and no way to express "I like chill *except* during workouts."
- **No diversity enforcement:** The top-K could return 5 nearly identical songs if the catalog has a cluster. A real system would add a diversity penalty.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

