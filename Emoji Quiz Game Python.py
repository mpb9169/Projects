#Emoji Quiz Game Python

import random

emoji_quiz = {
    "🎈🤡🚂": "It",
    "🌍🦍🗽": "King Kong",
    "🦖🦕🌴": "Jurassic Park",
    "🚢💑🧊": "Titanic",
    "🦇🏙️🃏": "The Dark Knight"
}

score = 0
questions = list(emoji_quiz.items())
random.shuffle(questions)

print("🎉 Welcome to the Emoji Movie Quiz! 🎬")
for emoji_hint, answer in questions:
    print(f"\nGuess the movie from this emoji clue:\n{emoji_hint}")
    guess = input("Your answer: ").strip()

    if guess.lower() == answer.lower():
        print("✅ Correct! 🎉")
        score += 1
    else:
        print(f"❌ Nope! The correct answer was: {answer}")

print(f"\nGame Over! Your score: {score}/{len(questions)}")
