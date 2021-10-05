print("")
print("City Bank")
print("")
print("Welcome to City Bank with a Y. Your personalized bank ATM at your hands.")

print("")
config = input("Do you have an account. If no then type 'no' or type 'yes'. :")


if(config == "no"):
    print("Please create an account first.")
    create = input("Type 'create' to start creating. Type 'stop' to stop the banking process. :")

    if(create == "create"):
        name = str(input("enter your name: "))
        age = int(input("enter your age: "))

    if(create == "stop"):
        exit()

    if age<18:
        print("Your age is less than 18. You are not eligible to create an account. ")
        exit()

    else:
        print("You are aged above 17 and are eligible to create an account. Please enter you bank details.")

    age2 = str(age)

    bank = str(input("enter your bank name: "))
    cash = str(input("opening balance: "))

    acc = str(input("enter your card number:"))
    

    print("")
    print("Account of name" + " " + name + ", aged" + " " + age2 + " is created!")
    print("")
    print("Account Details :-")
    print("Bank : " + bank)
    print("Opening Balance : " + cash)
    print("Account Number: " + acc)
    print("")
    print("Thankyou For Choosing City Bank!!!")

    print("")


print("Please Continue...")
cardnumber = input("enter your card number: ")
pin = input("enter your pin: ")
money = int(input("enter opening balance : "))

    

class Atm:
    def __init__(self, card_number, pin):
        self.card = card_number
        self.pin = pin
        


    def withdraw(self, amount):
        new_amount = money - int(amount)
        print("You withdrawed" + " " + str(amount) + "Rs." + "Balance :" + str(new_amount) + "Rs")
        print("")
        print("Please take the reciept and note it down. You will need it to enter the balance next time. Thanks")
        print("")

    def deposit(self, amount):
        
        deposit_amount = money + int(amount)
        print("You deposited" + " " + str(amount) + "Rs." + "Balance :" + str(deposit_amount) + "Rs")
        print("")
        print("Please take the reciept and note it down. You will need it to enter the balance next time. Thanks")
        print("")
    

def main():

    new_user = Atm(cardnumber, pin)

   
    print("Type your banking process :-")

    print("Create A Bank Account")
    print("Withdrawal")
    print("Deposit")
  

    print("")

    
    banking = str(input("enter your banking option:-"))
    print("")

    if(banking == "Create"):

        name = str(input("enter your name: "))
        age = int(input("enter your age: "))

        if age<18:
            print("Your age is less than 18. You are not eligible to create an account. ")
            exit()

        else:
            print("You are aged above 17 and are eligible to create an account. Please enter you bank details.")

        age2 = str(age)

        bank = str(input("enter your bank name: "))
        cash = str(input("opening balance: "))

        acc = str(input("enter your card number:"))
        

        print("")
        print("Account of name" + " " + name + ", aged" + " " + age2 + " is created!")
        print("")
        print("Account Details :-")
        print("Bank : " + bank)
        print("Opening Balance : " + cash)
        print("Account Number: " + acc)
        print("")
        print("Thankyou For Choosing City Bank!!!")

        print("")


    if(banking == "Withdrawal"):
        amount = int(input("Enter the money to withdraw : "))
        new_user.withdraw(amount)

    
    if(banking == "Deposit"):
        amount = int(input("Enter the money to deposit : "))
        new_user.deposit(amount)

   
main()
