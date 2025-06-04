# Python quiz game with multiple choice questions

questions = ("How many continents are there?",
             "What is the capital of India?",
             "Which country is known as the Land of the Rising Sun?",
             "What is the largest ocean on Earth?",
             "Which planet is known as the Red Planet?")

options = (("1. Five", "2. Six", "3. Seven", "4. Eight"),
              ("1. New Delhi", "2. Mumbai", "3. Kolkata", "4. Chennai"),
              ("1. China", "2. Japan", "3. South Korea", "4. Thailand"),
              ("1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Pacific Ocean"),
              ("1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"))
answers = ("3", "1", "2", "4", "2")
guesses = []
score = 0
question_numb = 0


# for option in options:
#     print("Option:",option)

for question in questions:
    print("------------------------------------")
    print(question)
    for option in options[question_numb]:
        print(option)
    guess  = input("Enter (1,2,3,4):").upper()
    guesses.append(guess)
    if guess == answers[question_numb]:
        score +=1
        print("The answer is CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_numb]} is the correct answer!")
    question_numb += 1

print("------------------------------------")
print("            RESULTS"                 )
print("------------------------------------")

print("answers: ", end="")

for answer in answers:
    print(answer, end = " ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end = " ")
print()

score = (score / len(questions) * 100)

print(f"Your score is: {score}")