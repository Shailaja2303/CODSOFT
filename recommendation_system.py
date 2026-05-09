movies = {
    "action": ["Avengers", "John Wick", "Mad Max"],
    "comedy": ["Mr. Bean", "Jumanji", "The Mask"],
    "horror": ["Conjuring", "Annabelle", "Insidious"],
    "romance": ["Titanic", "The Notebook", "La La Land"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

print("\n=== Movie Recommendation System ===\n")

user_genre = input("Enter your favorite movie genre: ").lower()

if user_genre in movies:

    print("\nRecommended Movies:\n")

    for movie in movies[user_genre]:
        print("⭐", movie)

else:
    print("\nSorry! Genre not found.")