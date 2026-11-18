
print("Welcome to the Animal Guessing Game!")
print("You will be asked 5 questions.")
print("You have 3 guesses for each question.")
print("1st guess = 100 points")
print("2nd guess = 65 points")
print("3rd guess = 30 points")
print("Incorrect after 3 guesses = 0 points")

# Store the questions and answers
questions = [
    ("Which animal says meow?", "cat"),
    ("Which animal has a long trunk?", "elephant"),
    ("Which animal is called the king of the jungle?", "lion"),
    ("Which animal gives us milk?", "cow"),
    ("Which animal has a long neck?", "giraffe")
]

# Points for each guess
points = [100, 65, 30]

# Start the game
total_score = 0

for question_number, (question, answer) in enumerate(questions, start=1):
    print(f"\nQuestion {question_number}: {question}")

    for guess_number in range(3):
        guess = input(
            f"Guess {guess_number + 1}: "
        ).strip().lower()

        if guess == answer:
            earned_points = points[guess_number]
            total_score += earned_points

            print("Correct!")
            print(f"You earned {earned_points} points.")
            break
        else:
            print("Incorrect!")

    else:
        print(f"The correct answer was {answer}.")
        print("You earned 0 points.")

# Show the final score
print("\nGame Over!")
print(f"Your total score is {total_score} out of 500 points.")
