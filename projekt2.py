"""
projekt2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Janovec
email: petr.janovec@seznam.cz
discord: Djolefola
"""
import random 
import sys
import time

del_char = "-"
del_len = 40
delimiter = del_char * del_len
bulls = 0
cows = 0
retry = 1 
char_n = 0
tries = 0
tries_list = []


while retry == 1:
    
    digits = random.sample(range(10), 10)

    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    random_dig = digits[:4]
    rnd_num = ''.join(map(str, random_dig))

    tries = 0

    if int(len(tries_list)) == 0:
        print(f"Hi there!\n{delimiter}\nI've generated a 4 digit number for you, it does not start with zero and doesn't contain duplicite characters.\nLet's play a bulls and cows game.\n{delimiter}\nEnter a number:\n{delimiter}")
    else:
        print(f"OK! Let's go for another round. This is your game nr.{int(len(tries_list))+1}")
        print(delimiter)
    
    guess = input(">>>")
    start_time = time.time()
   
    while guess != rnd_num:
        
        correct_input = 0
        while correct_input == 0:
            if len(guess) != 4:
                correct_input = 0
                guess = input("Number must have four digits. Try again\n>>> ")
            elif len(set(guess)) != 4:
                correct_input = 0
                guess = input("Your number contains duplicite characters. Try again\n>>>") 
            elif guess[0] == '0':
                correct_input = 0
                guess = input("Your number starts with zero. Try again\n>>>") 
            elif not guess.isdigit():
                guess = input ("Your number is not a number :) Try again\n>>>")
            else:
                correct_input = 1

        char_n = 0 
        bulls = 0
        cows = 0
        for char in guess:
            if char == rnd_num[char_n]:
                bulls += 1 
            elif char in rnd_num and char != rnd_num[char_n]:
                cows += 1
            char_n += 1
        tries += 1
        print(f"Try nr.{tries}: {bulls} Bull{'s' if bulls > 1 or bulls == 0 else ''}, {cows} Cow{'s' if cows > 1 or cows == 0 else ''}")
        print(delimiter)
        guess = input(">>>")
    tries += 1
    try_time = int(time.time() - start_time) 
    tries_list.append((tries, try_time))

    avg_try = int(sum(item[0] for item in tries_list) / int(len(tries_list)))
    avg_time = int(sum(item[1] for item in tries_list) / int(len(tries_list)))

    if tries < avg_try: 
        txt_tries = "less than"
    elif avg_try == tries: 
        txt_tries = "equal to" 
    else: 
        txt_tries = "more than"

    if try_time < avg_time: 
        txt_time = "faster than"
    elif try_time == tries: 
        txt_time = "same as" 
    else: 
        txt_time = "slower than"

    if len(tries_list) == 1:
        print(f"Correct! You got the number in {tries} guesses! Time taken: {try_time}s.")
    else:
        print(f"Correct! You got correct number in {tries} guesses! That's {txt_tries} your current average({avg_try}).")
        print(f"Time taken: {try_time}s, it's {txt_time} your current average ({avg_time}s).")

    print(delimiter)
    if input("You wanna try it again? Press 'y' and enter. If not press any key and enter, the program will close: ").lower() == "y":
        retry = 1
        print(delimiter)
    else:
        retry = 0
        print(delimiter)

print(f"Thank for your game! You played {len(tries_list)} turns. The lowest nr of tries: {min(item[0] for item in tries_list)}. The fastest game was {int(min(item[1] for item in tries_list))}seconds long.")
print(f"Your average nr. of tries : {avg_try}, avg. time to solve: {avg_time} seconds.")
print(delimiter)
print ("Game will close in 20 seconds")

for sec in range(20,0,-1):
    sys.stdout.write(str(sec)+' ')
    sys.stdout.flush()
    time.sleep(1)
quit() 