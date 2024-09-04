import random
import time

def spin_row():
    symbols = ["🔔", "🍉", "🍒", "💎", "⭐"]
    # results = []
    # for symbol in range (3):
    #     results.append(random.choice(symbols))
    # return results
    return [random.choice(symbols) for _ in range(3)]
    ## list comprehension

def display(row):
    time.sleep(0.5)
    print ("***************")
    time.sleep(1)
    for i in range(3):
        print (row[i])
        time.sleep(1)
    print ("***************\n")
    time.sleep(0.5)
    
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        global icon
        icon = ""
        global multiplier
        multiplier = 0
        if row[0] == "🍒":
            icon = "cherries"
            multiplier = 2
            return bet * 2
        elif row[0] == "🍉":
            icon = "watermelons"
            multiplier = 3
            return bet * 3
        elif row[0] == "🔔":
            icon = "bells"
            multiplier = 5
            return bet * 5
        elif row[0] == "⭐":
            icon = "stars"
            multiplier = 7
            return bet * 7
        elif row[0] == "💎":
            icon = "diamonds"
            multiplier = 15
            return bet * 15
    return 0

def main():
    balance = 100
    print("--------------------------------------")
    print ("Welcome to the Python Slot Machine!")
    print ("Symbols: 🔔 🍉 🍒 💎 ⭐")
    print("--------------------------------------")
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = input("Place your bet: $")
        
        if not bet.isdigit():
            ##checks if the input is a number/digit string and returns boolean
            print ("Please enter a valid number.")
            continue
            ## moves to next iteration
            
        bet = int(bet)
        
        if bet > balance:
            print ("Insufficient funds.")
            continue
        elif bet <= 0:
            print ("Bet must be more than $0.")
            continue
        
        balance -= bet
        
        row = spin_row()
        print ("Spinning...\n")
        time.sleep(1)
        display(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print (f"You got 3 {icon} which is a multiplier of {multiplier}x!")
            print (f"You won ${payout}!")
        else:
            print ("No winnings gained.")
            
        balance += payout
        
        play_again = input("Would you like to spin again? (y/n): ").lower()
        
        if play_again != "y":
            break
    
    print (f"Game over. You ended with a balance of ${balance}.")
    
if __name__ =="__main__":
    main()
