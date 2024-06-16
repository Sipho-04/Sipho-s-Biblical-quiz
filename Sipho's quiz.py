import random

# Define the questions, options, and correct answers
quiz_data = [
    {
        "question": "How many missionary journeys did Paul have?",
        "options": ["A) Three", "B) Five", "C) Two", "D) None of the above"],
        "answer": "A"
    },
    {
        "question": "Who replaced Judas Iscariot to balance the twelve?",
        "options": ["A) Paul", "B) Matthias", "C) Joseph called Barsabas", "D) Peter"],
        "answer": "C"
    },
    {
        "question": "What miracle should people seek according to Jesus?",
        "options": ["A) Walking on water", "B) Of Jonah", "C) Feeding 5000 people", "D) Of Moses at the red sea"],
        "answer": "B"
    },
    {
        "question": "Who wrote the book of Acts?",
        "options": ["A) Luke", "B) The apostles", "C) Paul", "D) John Mark"],
        "answer": "A"
    },
    {
        "question": "Who was the first king of Israel?",
        "options": ["A) David", "B) Herod", "C) Solomon", "D) Saul"],
        "answer": "D"
    }
]

def run_quiz():
    print("Welcome to Sipho's Biblical Quiz!\n")
    score = 0
    random.shuffle(quiz_data)  # Shuffle the questions for randomness

    for i, q in enumerate(quiz_data):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your final score is {score} out of {len(quiz_data)}.")

# Run the quiz
if __name__ == "__main__":
    run_quiz()