# ==========================================
#         PYTHON QUIZ APPLICATION
# ==========================================

# Quiz Questions
questions = [
    {
        "question": "1. Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C", "D. Java"],
        "answer": "B"
    },
    {
        "question": "2. Who developed Python?",
        "options": [
            "A. Dennis Ritchie",
            "B. James Gosling",
            "C. Guido van Rossum",
            "D. Charles Babbage"
        ],
        "answer": "C"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /* */", "D. @"],
        "answer": "B"
    },
    {
        "question": "4. Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. display()", "D. output()"],
        "answer": "B"
    },
    {
        "question": "5. Which data type is used to store whole numbers?",
        "options": ["A. float", "B. str", "C. int", "D. bool"],
        "answer": "C"
    }
]


# Function to display instructions
def instructions():
    print("\n========== INSTRUCTIONS ==========")
    print("1. The quiz contains 5 questions.")
    print("2. Each question has 4 options.")
    print("3. Enter A, B, C or D to answer.")
    print("4. Each correct answer gives 1 mark.")
    print("5. There is no negative marking.")
    print("==================================")


# Function to start the quiz
def start_quiz():

    score = 0
    user_answers = []

    print("\n========== QUIZ STARTED ==========")

    for q in questions:

        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid choice! Please enter A, B, C or D.")
            answer = input("Enter your answer: ").strip().upper()

        if answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct answer:", q["answer"])

        user_answers.append({
            "question": q["question"],
            "your_answer": answer,
            "correct_answer": q["answer"]
        })

    # Calculate percentage
    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    # Display results
    print("\n========== QUIZ RESULT ==========")
    print("Total Questions:", total_questions)
    print("Correct Answers:", score)
    print("Incorrect Answers:", total_questions - score)
    print("Your Score:", score, "/", total_questions)
    print("Percentage:", percentage, "%")

    # Review answers
    print("\n========== ANSWER REVIEW ==========")

    for item in user_answers:
        print("\n", item["question"])
        print("Your Answer:", item["your_answer"])
        print("Correct Answer:", item["correct_answer"])

    print("\n===================================")


# Main application
def main():

    while True:

        print("\n================================")
        print("      WELCOME TO PYTHON QUIZ")
        print("================================")
        print("1. Start Quiz")
        print("2. Instructions")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            instructions()

        elif choice == "3":
            print("\nThank you for using Python Quiz!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")


# Run the application
if __name__ == "__main__":
    main()
