import random

start = input("Enter the start of the range :\n")
top = input("Enter the top of the range :\n")

def guess(start, top):
    guesses = 0
    if top.isdecimal() and start.isdecimal() or (start.lstrip('-').isdecimal() and top.isdecimal()):
        if int(top) <= int(start):
            print("The vlaues of start should be less than the end")
        else:
            random_num = random.randint(int(start), int(top))
            while True:
                guesses += 1
                ans = input("Make a guess\n")
                if ans.isdecimal() or ans.lstrip('-').isdecimal():
                    if int(ans) == random_num:
                        print(
                            "You've got it right!\nYou've got the answer in ", guesses, "guesses")
                        break
                    else:
                        print("You've got it wrong :(")
                else:
                    print("Please Enter a number")

    else:
        print("Please try again and Enter a number")


guess(start, top)
