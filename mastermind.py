import random

"""
Generates the random code without duplictes
"""
def select_random_num():
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code

"""
Gets the user input
"""
def get_user_input():
    answer = input("Input 4 digit code: ")
    if len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        return get_user_input()
    else:
        return answer

"""
Checks if the code is correct or not an gives feedback
"""
def give_feedback(answer, code):
    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = get_user_input() 

        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1
        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1
        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))

    print('The code was: '+str(code))

"""
Calls all the other functions
"""
def run_game():
    code = select_random_num()
    answer = []
    give_feedback(answer, code)

if __name__ == "__main__":
    run_game()
