import random

MAX_BET=100
MIN_BET=1
MAX_LINES = 3

ROWS=3
COLS=3

symbol_count={
    "A":5,
    "B":5,
    "C":5,
    "D":5
}

symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}




def check_win(columns,lines,bet,values):
    win=0
    wl=[]
    for line in range(lines):
        s=columns[0][line]
        for column in columns:
            stc=column[line]
            if s!=stc:
                break
        else:
            win+=values[s]*bet
            wl.append(line+1)   
    
    return win,wl
            
                
    
    
def glms(rows,cols,symbols):
    all_sym=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_sym.append(symbol)
            
    columns=[]
    
    for _ in range(cols):
        
        column=[]
        cur_sym=all_sym[:]
        
        for _ in range(rows):
            v=random.choice(cur_sym)
            cur_sym.remove(v)
            column.append(v)
        columns.append(column)
    
    return columns
        
def print_sm(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate (columns):
            if i!=len(columns)-1:    
                print(col[row],end=" | ")
            else:
                print(col[row],end ="")
                
        print()
        
        
def deposit():
    while True:
        a=input("what would you like to deposite? $")
        if a.isdigit():
            a=int(a)
            if(a>0):
                break
            else:
                print("amount must be greater than zero")
        
        else:
            print("enter a number!")
            
    return a

def gnol():
    while True:
        l=input("Enter the number of lines you want to bet on(1-"+str(MAX_LINES)+")?")     
        if l.isdigit():
            l=int(l)
            if 1<=l<=MAX_LINES:
                break
            else:
                print("Eneter valid number")
        
        else:
            print("enter a number!")
            
    return l

def get_bet():
    while True:
        a=input("what would you like to bet on each line? $")
        if a.isdigit():
            a=int(a)
            if MIN_BET<=a<=MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}.")
        
        else:
            print("enter a number!")
            
    return a

def game(b):
    l=gnol()
    while True:
        bet=get_bet()
        tb=bet*l
        
        if tb>b:
            print(f"you dont have enough amount ot bet , your cuurrent balance is ${b}")
        else:
            break
        
    print(f"you are betting ${bet} on {l}.Total bets is equal to ${tb}")
    
    s=glms(ROWS,COLS,symbol_count)
    print_sm(s)
    win,wl=check_win(s,l,tb,symbol_value)
    print(f"you won ${win} at", *wl)
    return win-tb

def main():
    b=deposit()
    while True:
        print(f"current balance is ${b}")
        s=input("press enter to play (q to quit)")
        if(s== "q"):
            break
        b+=game(b)
    print(f"you left with ${b}")
    
main()