class ATM():
    def __init__(self,card,pin):
        self.card=card
        self.pin=pin

    def cashWithdrawl(self):
        print("Withdrawing money")

    def balanceEnquiry(self):
        print("Your balance is 50000")


card=int(input("Card number: "))
pin=int(input("Pin number: "))
atm=ATM(card,pin)

question=int(input("1. Do to want to withdraw the money \n 2. Do you want to see your balance \n"))

if(question==1):
    atm.cashWithdrawl()
elif(question==2):
    atm.balanceEnquiry()
else:
    print("Wrong number")