class ATM:
    def __init__(self):
        self.pin = ''
        self.balance = 0

    def menu(self):
        user_input = input("""
        1. Press 1 to create pin 
        2. Press 2 to change pin 
        3. Press 3 to check balance 
        4. Press 4 to withdraw
        5. Anything else to exit 
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()        # ✅ Fixed typo
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        self.pin = input('Enter your pin: ')    # ✅ Store as str, no int()
        print('Pin created successfully')
        self.menu()

    def change_pin(self):
        old_pin = input('Enter your old pin: ')
        if old_pin == self.pin:                 # ✅ Both are str now
            self.pin = input('Enter new pin: ')
            print('Pin changed successfully')
            self.menu()
        else:
            print('Wrong pin, try again')
            self.menu()

    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:                # ✅ Both are str now
            print("Your balance is:", self.balance)
            self.menu()
        else:
            print("Wrong pin, try again")
            self.menu()

    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter amount: "))   # ✅ Convert to int for comparison
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful, please take your cash")
                print("Your balance is:", self.balance)
            else:
                print("Insufficient funds in your account")
            self.menu()
        else:
            print("Wrong pin, please try again")
            self.menu()


obj = ATM()
obj.menu()