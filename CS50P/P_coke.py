total_amt = 0

accepted_coins = [5, 10, 25]

while total_amt < 50:
    coin = int(input("Enter coin (5, 10, 25)"))
    
    if coin == 50:
        total_amt = coin
        break
    
    elif coin in accepted_coins:
        total_amt += coin
        print(f"Amount Due {50 - total_amt}")
        
    else:
        print(f"Amount Due: {50 - total_amt}") 
        
change = total_amt - 50

print(f"Change Owed {change}")