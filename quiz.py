
quiz_starter = input("Do you want to play ? Y/N\n").lower()

def quiz(quiz_starter):
    s0 = 0
    if quiz_starter == 'y':
        # Australia
        ans1 = input(
            "Which country do cities of Perth, Adelade & Brisbane belong to?\n")
        s1 = check_and_increase(
            s0, ans1.lower() == 'australia')

        ans2 = input(
            "What is the romanized Arabic word for \"moon\"?\n")  # Qamar
        s2 = check_and_increase(
            s1, (ans2.lower() == 'qamar'))

        ans3 = input(
            "How many languages are written from right to left?\n")  # 12
        s3 = check_and_increase(s2, ans3 == '12')

        ans4 = input(
            "What is the name of the biggest technology company in South Korea?\n")  # Samsung
        s4 = check_and_increase(
            s3, ans4.lower() == 'samsung')

        ans5 = input(
            "Demolition of the Berlin wall separating East and West Germany began in what year?\n")  # 1989
        finalScore = check_and_increase(s4, ans5 == '1989')

        print("Your total score = ", finalScore, "/5")

        if finalScore == 5:
            print("Well Done!🎉")

        if finalScore == 0:
            print("Hard luck :( .. ", end='')
            quiz_starter = input("Do you want to play again? Y/N\n")
            quiz(quiz_starter)

    else:
        quit()


def check_and_increase(old_score, condition):
    new_score = old_score
    if condition:
        new_score += 1
        print("Good job!")
    else:
        print("Incorrect :(")
    return new_score


quiz(quiz_starter)
