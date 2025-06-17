

def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    print(f"\nYour final score is {score} out of {len(questions)}.")

# Define quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. HTML", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Bjarne Stroustrup", "C. Guido van Rossum", "D. James Gosling"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Utility"],
        "answer": "B"
    },
    {
        "question": "Which of these is not a programming language?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    }
]

# Run the quiz
run_quiz(quiz_questions)
