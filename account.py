account = {
    "account_name": "tim_huza",
    "password": 123,
    "money": 1000
}

def log_in():
    
    print("Log In to your account!")
    print(" ")

    name = input("Enetr your account name: ")
    str_password = input("Enter your password: ")
    
    try:
        password = int(str_password)
    except ValueError:
        print("Password must be a number.")
        return False
    
    if name.lower() == account["account_name"] and password == account["password"]:
         print("You loged in to your account✅")
         return True
    else:
        print("Incorrect account name or password. Try again!")
        return False


def money():
    print(f"You have ${account['money']}. Would you like to put or take money?")
    money_answer = input("Press p to put money. Press t to take money. ")

    if money_answer.lower() == "p":
        print("What amount of money you want to put?")
        putting_money = input("Amount of money should be from $50-$100! ")
        put_money = int(putting_money)

        if put_money >= 50 and put_money <= 500:
            total_money = put_money + account['money']
            print(f"Transaction was successful total money you have is ${total_money} dollars!")
            return True
        
        else:
            print("Amount of money should not be less than $50 and greater than $500.")
            return False 

    elif money_answer.lower() == "t":
        print("What amount of money you want to take?")
        taking_money = input("Amount of money should be from $20-$1000! ")
        
        try:
            take_money = int(taking_money)
        except ValueError:
            print("Must be a number.")
            return False

        if take_money >= 20 and take_money <= 1000:
            if take_money >= account["money"]:
                print("Not enough money to take that sum!")
                return False
            
            else:
                total_money = account['money'] - take_money
                print(f"Transaction was successful total money you have is ${total_money} dollars!")
                return True
            
        else:
            print("Amount of money should not be less than $50 and greater than $500.")
            return False
            
    else:
        print("Invalid try again.")
        return False


if log_in():
    answer = input("Would you like to put or take some cash? (yes/no) ")

    if answer.lower() == 'yes':
        acc_money = money() 
        print(acc_money)

    elif answer.lower() == 'no':
        print("Okay, then have a good day.")

    else:
        print("Invalid input. Please try again.")

else:
    # If login fails, no further actions are taken
    print("You cannot access the cash transaction options without logging in.")
