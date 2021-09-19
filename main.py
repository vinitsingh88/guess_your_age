from datetime import date
print("Hello. I am NICK. I am here to help you find your Age and Birth year")
while True:

    while True:
        user_age = int(input("Enter your Age or year of Birth : \n"))
        data_dict = ""
        data = ""
        ab= date.today()
        current_year = ab.year
        if 1850<=user_age<=current_year:
            print("It seems that you have entered your birth year.")
            confirmation = input("If the number entered is your Birth year then press 'y' key for yes,  else press 'n'?(Y/N) : ")

            if confirmation.capitalize() == "Y":
                a = date.today()
                current_year = a.year
                current_age = a.year - user_age
                if current_age == 1:
                    print(f"-------------------your are now {current_age} year old")
                else:
                    print(f"-------------------You are now {current_age} years old")
                print("lets move on with that.")
                data = "yrs"
                data_dict = user_age
                break
            elif confirmation.capitalize() == "N":
                print("Please Enter again")
                continue
            else:
                print("It seems you entered something wrong ! PLEASE TRY AGAIN !")
                continue
        elif 0<user_age<150:
            print("It seems that you have entered your age.")
            confirmation = input("If the number entered is your Age then press 'y' key for yes,  else press 'n'?(Y/N) : ")

            if confirmation.capitalize() == "Y":
                a = date.today()
                current_year = a.year
                print(f"-------------------You were born in the year {current_year - user_age}")
                print("So lets move on with that.")
                data = "age"
                data_dict = user_age
                break
            elif confirmation.capitalize() == "N":
                print("Please Enter again")
                continue
            else:
                print("Something Went Wrong, Please check the input you provided and try again......")
                continue

    while True:
        b=date.today()
        current_year = b.year
        turn100 = input("Do you want me to guess in which year you will turn 100?(Y/N) : ")
        if turn100.capitalize() == "Y":
            if data == "yrs":
                yrs100 = data_dict + 100
                print(f"-------------------In year {yrs100} you will turn 100 years old")
            elif data == "age":
                age100 = 100 - user_age
                yrs100 = current_year + age100
                print(f"-------------------In year {yrs100} you will turn 100 years old")
            break
        elif turn100.capitalize() == "N":
            print("No problem, Thankyou for visiting !")
            exit(0)
        else:
            print("It seems you entered something wrong ! PLEASE TRY AGAIN !")
            continue

    while True:
        what_year = input("Do you want me to guess in which year you will turn what?(Y/N) : ")
        if what_year.capitalize() == "Y":
            if data == "yrs":
                future_age = int(input("Enter a year and I will guess your age in that year : "))
                if future_age<=user_age:
                    print("-------------------You have entered a year previous to your birth year")
                    continue
                guess_age = future_age - user_age
                if future_age<current_year:
                    if guess_age==1:
                        print(f"-------------------In {future_age} you were {guess_age} year old")
                    else:
                        print(f"-------------------In {future_age} you were {guess_age} years old")
                else:
                    print(f"-------------------In {future_age} you will be {guess_age} years old")
            elif data == "age":
                future_age = int(input("Enter a age and I will guess the year when you will turn into that age : "))
                guess_age = current_year + (future_age - user_age)
                if future_age<user_age:
                    print(f"-------------------In {guess_age} you were {future_age} years old")
                else:
                    print(f"-------------------In {guess_age} you will be {future_age} years old")
            break
        elif what_year.capitalize() == "N":
            print("No problem, Thank you for visiting !")
            exit(0)
        else:
            print("It seems you typed something wrong ! PLEASE TRY AGAIN !")
            continue

    cont_game = input("Do you want to contiune the age game?(Y/N) : ")
    if cont_game.capitalize() == "Y":
        print("There you go....")
        continue
    elif cont_game.capitalize() == "N":
        print("Thankyou for visiting....!")
        break