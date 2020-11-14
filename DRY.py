class ATM:
    def __init__(self , balance , bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list=[]

    def name_of_the_bank(self):
        print(self.bank_name)

    def get(self,request):
        result = self.balance - request

        notes = [100, 50, 10, 5 ]
        for note in notes:
            while request >= note:
                request -= note
                print("give ", note)
        else:
            if request > 0 :
               print("give " , request)


    def withdraw(self, request):
        self.name_of_the_bank()
        result = self.balance
        if request > self.balance:
            print("There is no enough money in ATM ")
        elif request <= 0:
            print("your request shouldn't be a negative number ")
        else:
            self.withdrawals_list.append(request)
            result = self.balance - request
            self.get(request)
        return result

    def show_withdrawals_list(self):
        for withdrawal in self.withdrawals_list :
            print(withdrawal)


atm1 = ATM(500 , "salam bank")
atm1.balance = atm1.withdraw(300)
print("ATM balance is", atm1.balance)

atm2 = ATM(600 , "baraka bank")
atm2.balance = atm2.withdraw(322)
print("ATM balance is", atm2.balance)

atm1.balance = atm1.withdraw(58)
print("ATM balance is", atm1.balance)
atm2.balance = atm2.withdraw(120)
print("ATM balance is", atm2.balance)


atm1.balance = atm1.withdraw(300)
print("ATM balance is", atm1.balance)
atm2.balance = atm2.withdraw(-322)
print("ATM balance is", atm2.balance)

print( "with_drawals for atm1 :")
atm1.show_withdrawals_list()
print( "with_drawals for atm2 :")
atm2.show_withdrawals_list()
