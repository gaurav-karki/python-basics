# -----------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("---------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter:(A, B, C or D) : ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

# -----------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!!")
        return 1
    else:
        print("Incorrect!!")
        return 0


# -----------------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("Results")
    print("---------------------------")
    print("Answers: ", end='')
    for i in questions:
        print(questions.get(i), end=' | ')
    print()
    print("Guesses: ", end='')
    for i in guesses:
        print(i, end=' | ')
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")
# -----------------------------------
def play_again():
    response = input("Do you want to play_again(yes/no or y/n):")
    response.upper()
    if response == "yes":
        return True
    else:
        return False

questions = {'In which district is Fungfung waterfall?': 'B',
             'How many heritage of nepal is listed in world heritage site?': 'A',
             'Which is the first magazine in the nepali language?': 'C',
             'what is the surname of monika maam': 'C'}
options = [['A. Kathmandu', 'B. Nuwakot', 'C. Dhadging', 'D. Makawanpur'],
           ['A. 10', 'B. 7', 'C. 6 ', 'D. 8'],
           ['A. Kantipur patrika', 'B. Gorkha patrika', 'C. Gorkha india life patrika', 'D. Raj patrika'],
           ['A.karki', 'B. subedi', 'C.regmi', 'D.lama']]
new_game()
while play_again():
    new_game()
print("Bye!!!")