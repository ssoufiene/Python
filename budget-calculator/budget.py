class Category:
    withdrawls=[]
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.a = ''
        self.total=[]
    def deposit(self, amount, description=''):
        x = {"amount": amount, "description": description}
        self.ledger.append(x)
        self.total.append(amount)

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == False:
            return False
        else:
            y = {"amount": -(amount), "description": description}
            self.ledger.append(y)
            self.total.append(-amount)
            self.withdrawls.append(amount)
            return True

    def get_balance(self):
        balance=sum(self.total)
        return balance

    def transfer(self, amount, bcategory):
        n = self.name
        if self.check_funds(amount) == True:
            self.withdraw(amount, description=f"Transfer to {bcategory.name}")
            bcategory.deposit(amount, description=f'Transfer from {n}')

            return True
        else:
            return False
    def percentage(self):
        wit=0

        for i in self.total:
            if i<0:
                wit+=i

        percent=(-wit/sum(self.withdrawls))*100
        if percent>10:
         if percent%10==0:
                return percent
         elif percent%10>5:
            return (int(percent/10)+1)*10
         else:
            return int(percent)
        else:
            return 1

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        x = (self.name.center(30, '*'))
        for i in self.ledger:
            s = list(i.values())
            first = s[1][:23]
            second = f'{s[0]:.2f}'
            third = second[:7].rjust(30 - len(first))
            self.a = f'{self.a}{first}{third}\n'
        return f'{x}\n{self.a}Total: {self.get_balance()}'
def fon(places):
    max_len = max([len(place) for place in places])
    for i, place in enumerate(places):
     if len(place) < max_len:
            places[i] = place.ljust(max_len)
    a=''
    for i in range(max_len):
      if i<max_len -1 :
            a=a+f'     {"  ".join([place[i] for place in places])}  \n'
      else :
             a=a+f'     {"  ".join([place[i] for place in places])}  '
    return a
def create_spend_chart(cat_lst):
        newlst=[]
        new2=[]
        new3=[]

        for i in cat_lst:
            new2.append(i.percentage())
            newlst.append(i.name)
            slash=10*'-'
        for j in range(11):
            bull=' '
            for i in new2 :
                if (i/10)>=j:
                    incr='o'
                else :
                    incr=' '
                bull=bull+incr+'  '
            new3.append(bull)
        return (f'Percentage spent by category\n100|{new3[10]}\n 90|{new3[9]}\n 80|{new3[8]}\n 70|{new3[7]}\n 60|{new3[6]}\n 50|{new3[5]}\n 40|{new3[4]}\n 30|{new3[3]}\n 20|{new3[2]}\n 10|{new3[1]}\n  0|{new3[0]}\n    {slash}\n{fon(newlst)}')
