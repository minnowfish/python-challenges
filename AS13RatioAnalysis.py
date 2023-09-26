def GPM(grossProfit,sales):
    grossProfitMargin = round((grossProfit/sales)*100,2)
    print(f"The gross progit margin is {grossProfitMargin}")
def NPM(netProfit,sales):
    netProfitMargin = round((netProfit/sales)*100,2)
    print(f"The netProfitMargin is {netProfitMargin}")

def check():
    try:
        choice = int(input('''
Which profit margin ratios would you like to use?
    1) Gross Profit Margin (GPM)
    2) Net Profit Margin (NPM)                       
'''))
        if choice != 1 and choice != 2:
            print("Not a valid option")
            return False, 0
    except ValueError:
        print("Not an integer, try again")
        return False, 0
    return True, choice

integer = False
while integer == False:
    integer, choice = check()

if choice == 1:
    grossProfit =  int(input("Input the gross profit: "))
    sales = int(input("Input the amount of sales: "))
    GPM(grossProfit,sales)

else:
    netProfit =  int(input("Input the net profit: "))
    sales = int(input("Input the amount of sales: "))
    NPM(netProfit,sales)
