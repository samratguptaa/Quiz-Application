"""
Project 34: Quiz Application
Asks questions and calculates the final score.

Functions:
    ask_question()    - shows one question, takes the answer, checks it
    calculate_score() - computes the final score and percentage
"""

# Each question: text, four options, and the correct option number (1-4)
QUESTIONS = [
    {
        "question": "Which organelle is known as the powerhouse of the cell?",
        "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
        "answer": 2,
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["O2", "CO2", "H2O", "NaCl"],
        "answer": 3,
    },
    {
        "question": "Which Python keyword is used to define a function?",
        "options": ["func", "def", "function", "define"],
        "answer": 2,
    },
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Kolkata", "New Delhi", "Chennai"],
        "answer": 3,
    },
    {
        "question": "Which molecule carries genetic information?",
        "options": ["DNA", "ATP", "Glucose", "Insulin"],
        "answer": 1,
    },
]


def ask_question(number, q):
    """Display one question, read the user's choice and return True if correct."""
    print(f"\nQ{number}. {q['question']}")
    for i, option in enumerate(q["options"], start=1):
        print(f"   {i}. {option}")

    # Keep asking until the user enters a valid option number
    while True:
        choice = input("Your answer (1-4): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(q["options"]):
            choice = int(choice)
            break
        print("Please enter a number between 1 and 4.")

    if choice == q["answer"]:
        print("Correct!")
        return True

    print(f"Wrong! The correct answer is: {q['answer']}. {q['options'][q['answer'] - 1]}")
    return False


def calculate_score(correct, total):
    """Return the percentage score and a feedback message."""
    percentage = (correct / total) * 100
    if percentage == 100:
        remark = "Excellent! Perfect score!"
    elif percentage >= 60:
        remark = "Good job!"
    elif percentage >= 40:
        remark = "Not bad, keep practicing."
    else:
        remark = "Better luck next time."
    return percentage, remark


def main():
    print("=" * 40)
    print("          QUIZ APPLICATION")
    print("=" * 40)

    correct = 0
    for number, q in enumerate(QUESTIONS, start=1):
        if ask_question(number, q):
            correct += 1

    total = len(QUESTIONS)
    percentage, remark = calculate_score(correct, total)

    print("\n" + "=" * 40)
    print(f"Final Score : {correct} / {total}")
    print(f"Percentage  : {percentage:.1f}%")
    print(remark)
    print("=" * 40)


if __name__ == "__main__":
    main()
