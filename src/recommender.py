from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # +2.0 for genre match
    if song.get("genre") == user_prefs.get("genre"):
        score += 2.0
        reasons.append(f"genre match ({song['genre']})")

    # +1.5 for mood match
    if song.get("mood") == user_prefs.get("mood"):
        score += 1.5
        reasons.append(f"mood match ({song['mood']})")

    # +1.0 × proximity for energy (0–1 scale)
    if "energy" in user_prefs and "energy" in song:
        energy_sim = 1.0 - abs(float(user_prefs["energy"]) - float(song["energy"]))
        score += 1.0 * energy_sim
        reasons.append(f"energy similarity {energy_sim:.2f}")

    # +0.75 × proximity for valence (0–1 scale)
    if "valence" in user_prefs and "valence" in song:
        valence_sim = 1.0 - abs(float(user_prefs["valence"]) - float(song["valence"]))
        score += 0.75 * valence_sim
        reasons.append(f"valence similarity {valence_sim:.2f}")

    # +0.5 × proximity for tempo (normalized over 200 bpm range)
    if "tempo_bpm" in user_prefs and "tempo_bpm" in song:
        tempo_sim = 1.0 - min(abs(float(user_prefs["tempo_bpm"]) - float(song["tempo_bpm"])) / 200.0, 1.0)
        score += 0.5 * tempo_sim
        reasons.append(f"tempo similarity {tempo_sim:.2f}")

    # +0.5 × proximity for danceability (0–1 scale)
    if "danceability" in user_prefs and "danceability" in song:
        dance_sim = 1.0 - abs(float(user_prefs["danceability"]) - float(song["danceability"]))
        score += 0.5 * dance_sim
        reasons.append(f"danceability similarity {dance_sim:.2f}")

    # +0.5 × proximity for acousticness (0–1 scale)
    if "acousticness" in user_prefs and "acousticness" in song:
        acoustic_sim = 1.0 - abs(float(user_prefs["acousticness"]) - float(song["acousticness"]))
        score += 0.5 * acoustic_sim
        reasons.append(f"acousticness similarity {acoustic_sim:.2f}")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
