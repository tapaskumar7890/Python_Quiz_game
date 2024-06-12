def print_logo():
    print(r"""
 ____        _   _                  ____        _             
|  _ \ _   _| |_| |__   ___  _ __  / \ \  __ _| |_ __ _ _ __  
| |_) | | | | __| '_ \ / _ \| '_ \/ _ \ \/ _` | __/ _` | '_ \ 
|  __/| |_| | |_| | | | (_) | | | / ___ \ (_| | || (_| | | | |
|_|    \__, |\__|_| |_|\___/|_| |_/_/   \_\__,_|\__\__,_|_| |_|
       |___/                                                  
    """)

def print_welcome():
    print("""
    -----------------------------------
             WELCOME TO THE QUIZ
    -----------------------------------
    Test your knowledge with our fun quiz game!
    Answer the questions by selecting the correct option.
    -----------------------------------
    """)

def print_results(score, guesses, answers):
    print("---------------------------")
    print("          RESULTS          ")
    print("---------------------------")

    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")

    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")

    print()

    score = int(score / len(questions) * 100)

    print(f"Your score is: {score}%")

questions = [
    "How many elements are in the periodic table?:",
    "Which animal lays the largest eggs?:",
    "What is the most abundant gas in Earth's atmosphere?:",
    "How many bones are in the human body?:",
    "Which planet in the solar system is the hottest?:"
]

options = [
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
]

answers = ["C", "D", "A", "A", "B"]

def main():
    guesses = []
    score = 0
    question_num = 0
    
    print_logo()
    print_welcome()

    for question in questions:
        print("-------")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print_results(score, guesses, answers)

if __name__ == "__main__":
    main()