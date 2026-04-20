"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs
# spotify
# - matrix factorization - comparing libraries, NLP for web, blogs, CNNs - audio models
    # 
def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Full taste profile — enough axes to separate "intense rock" from "chill lofi"
    user_prefs = {
        "genre":        "indie pop",   # primary genre signal (one-hot match)
        "mood":         "happy",       # categorical mood preference
        "energy":       0.75,          # moderately high — energetic but not brutal
        "tempo_bpm":    115,           # mid-to-fast; avoids sleepy ambient AND thrash metal
        "valence":      0.78,          # positive / uplifting feel
        "danceability": 0.80,          # likes groove; discriminates rock vs. pop
        "acousticness": 0.25,          # slight preference for produced sound over raw acoustic
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    width = 60
    print("\n" + "=" * width)
    print("  ** MUSIC RECOMMENDATIONS **")
    print(f"  Profile: {user_prefs['genre']} / {user_prefs['mood']}")
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  #{rank}  {song['title']}  —  {song['artist']}")
        print(f"       Score : {score:.2f}")
        print(f"       Genre : {song['genre']}  |  Mood: {song['mood']}")
        reasons = [r.strip() for r in explanation.split(",")]
        print(f"       Why   : {reasons[0]}")
        for reason in reasons[1:]:
            print(f"               {reason}")

    print("\n" + "=" * width + "\n")


if __name__ == "__main__":
    main()
