def sum( a, b, c):
    return a+b+c

def pb(xstate,zstate):
    zero='x' if xstate[0] else ('0' if zstate[0] else 0)
    one='x' if xstate[1] else ('0' if zstate[1] else 1)
    two='x' if xstate[2] else ('0' if zstate[2] else 2)
    three='x' if xstate[3] else ('0' if zstate[3] else 3)
    four='x' if xstate[4] else ('0' if zstate[4] else 4)
    five='x' if xstate[5] else ('0' if zstate[5] else 5)
    six='x' if xstate[6] else ('0' if zstate[6] else 6)
    seven='x' if xstate[7] else ('0' if zstate[7] else 7)
    eight='x' if xstate[8] else ('0' if zstate[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print("---|---|----")
    print(f" {three} | {four} | {five} ")
    print("---|---|----")
    print(f" {six} | {seven} | {eight} ")

def checkwin(xstate,zstate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6]]
    for w in wins:
        if(sum(xstate[w[0]],xstate[w[1]],xstate[w[2]])==3):
            print("X won the game !")
            return 1
        if(sum(zstate[w[0]],zstate[w[1]],zstate[w[2]])==3):
            print("0 won the game !")
            return 0
    return -1

xstate=[0,0,0,0,0,0,0,0,0]
zstate=[0,0,0,0,0,0,0,0,0]
print("welcome!")
turn=1
pb(xstate,zstate)
while(True):
    if(turn == 1):
        print("X's chance")
        v=int(input("enter a value : "))
        xstate[v]=1
    else:
        print("0's chance")
        v=int(input("enter a value : "))
        zstate[v]=1
    pb(xstate,zstate)
    m=checkwin(xstate,zstate)
    if(m!=-1):
        print("match over.")
        break
    turn = 1-turn