import random

def run_game():

    num = []    

    #STEP 1: Guess a code
    while len(num) < 4:
        rand_num = random.randint(1, 8)
        if rand_num not in num:
            num.append(rand_num)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')    
    
    #STEP 2: Get a guess
    turns = 12
    user_num = ''
    while turns > 0:
        user_num = input('Input 4 digit code: ')
        if not user_num.isdigit() or ('0' in user_num or '9' in user_num ) or len(user_num) != 4: #combined all the conditions into a single if statement 
            print('Please enter exactly 4 digits.')
            continue #continue added for the loop to return to the beginning if the "if" statement returns true
        # except EOFError:
        #     print('') 

        #STEP 3: Evaluate input
        correct_digits_in_correct_place = 0
        correct_digits_not_in_correct_place = 0
        for i in range(len(user_num)):
            if int(user_num[i]) == num[i]:
                correct_digits_in_correct_place += 1
            elif int(user_num[i]) in num:
                correct_digits_not_in_correct_place += 1
        print(f'Number of correct digits in correct place:     {correct_digits_in_correct_place}')
        print(f'Number of correct digits not in correct place: {correct_digits_not_in_correct_place}')  
        
        if correct_digits_in_correct_place == 4:
            empty_word = ''
            for i in range(4):
                empty_word += str(num[i])
            print('Congratulations! You are a codebreaker!')
            print(f'The code was: {empty_word}')
            break
        else:
            #STEP 4: Count guesses
            turns -= 1
            print(f'Turns left: {turns}')

if __name__ == "__main__":
    run_game()

