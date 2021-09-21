def val():
    # inputs
    shares = float(input("Shares: "))
    eps = float(input("Owner Earnings: "))
    cash = float(input("Cash: "))
    debt = float(input("Debt: "))
    growth_rate = float(input("10 Year Expected Growth Rate: "))
    perpetual_growth_rate = float(input("Perpetual Growth Rate: "))
    discount_rate = float(input("Discount Rate: "))
    
    #calculations
    
    eps = eps / shares
    cash = cash / shares
    debt = debt / shares
    growth_rate = growth_rate / 100
    perpetual_growth_rate = perpetual_growth_rate / 100
    discount_rate = discount_rate / 100

    counter = 0
    npv = 0
    while counter < 10:
        npv += (eps * (1 + growth_rate)) / ((1 + discount_rate) ** (counter + 1))
        eps = eps * (1 + (growth_rate))
        counter += 1
    
    npv += (1 / ((1 + discount_rate) ** 10)) * (eps / (discount_rate - perpetual_growth_rate)) + cash - debt
    
    return npv


def main():
    run = True
    while run:
        print(val())        

if __name__ == "__main__":
    main()