import random

print("*********Good Day*********")
print("Welcome to the Lazy Developer Black Jack Game")
input("PRESS ENTER TO GET STARTED \n")

def random_number():
    return random.randrange(1, 11)

# player = {}

first_num = random_number()
second_num = random_number()
sum = first_num + second_num

def start_game(final_sum):
    print("you've picked two cards \n")
    print("your cards are %d and %d, which sums up to  \t %d \n" %
            (first_num, second_num, sum))

    while final_sum <= 20:

            print("⚠️If 'NO' is selcted, only 50%" " of your stake will be returned⚠️ \n")
            selected_option = input(
                "your number is lesser 21 will you like to pick another card (Y)YES (N)NO \n").lower()

            if selected_option == "y":
                extra_num = random_number()
                final_sum = final_sum + extra_num

                print("your new number is %d, which sums up to \t %d \n" %
                    (extra_num, final_sum))

            elif selected_option == "n":
                print("Thank for playing, your 50% " "cash back was Succefull \n")
                exit()

            else:
                print("You've selected an invalid option!")

    if final_sum == 21:
        print("%d!😲 you got Black Jack" % final_sum)
        print(("🎉🎉🎉you've won the game! congratulations🎉🎉🎉").upper())

    else:
        print("%d is greater than 21" % final_sum)
        print("😥😥😥You've lost the game! please try again😥😥😥")

start_game(sum)