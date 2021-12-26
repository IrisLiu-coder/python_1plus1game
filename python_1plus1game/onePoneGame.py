#如果單手等於五則該手歸零
#如果兩隻手皆歸零則輸掉這局比賽
#1.任何數不可單獨與 0 對換，如(3,0)可以變為(1,2)、(2,1)，但不可變為(0,3)
#2.當兩隻手一樣時如(2,2)，只能變為(0,4)、(1,3)、(3,1)、(4,0)，不可變為(2,2)。
#3.但(1,2)變為(2,1)是被允許的。
import random
import csv
players=[[1,1],[1,1]]
def situation(a1,a2,b1,b2):
    r=a1+a2
    data=[]
    if 1<r<5:
        for i in range(r):
            a1_data=i
            a2_data=r-i
            if [a1_data,a2_data,b1,b2] not in data:
                data.append([a1_data,a2_data,b1,b2])
    elif 5<r and r<8:
        for i in range(r-5+1,5):
            a1_data=i
            a2_data=r-i
            if [a1_data,a2_data,b1,b2] not in data:
                data.append([a1_data,a2_data,b1,b2])
    
    if [a1,a2,b1+a1,b2] not in data:
        data.append([a1,a2,b1+a1,b2])
    if [a1,a2,b1,b2+a1] not in data:
        data.append([a1,a2,b1,b2+a1])
    if [a1,a2,b1,b2+a2] not in data:
        data.append([a1,a2,b1,b2+a2])
    if ([a1,a2,b1+a2,b2] not in data):
        data.append([a1,a2,b1+a2,b2])
    if [a1,a2,b1,b2] in data:
        data.remove([a1,a2,b1,b2])
    if a1==0 or a2==0:
        if [0,a1] in data:
            data.remove([0,a1,b1,b2])
        if [a2,0] in data:
            data.remove([a2,0,b1,b2])
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]>=5:
                data[i][j]=0
    return data
def situation_random(a1,a2,b1,b2):
    if (a1,a2)==(0,0) or(b1,b2)==0 or len(situation(a1,a2,b1,b2))-1<=0:
        None        
    else:
        return situation(a1,a2,b1,b2)[random.randint(0,len(situation(a1,a2,b1,b2))-1)]
def judge(A,B,r):
    if sum(B)==0:
        return((2500,r))
    elif sum(A)==0:
        return((1,r)) 
    elif A[0]==1 and A[1]==1 and B[0]==1 and B[1]==1:
        return((0,r))
    else:
        return((0,r))
def exhibit_situation():
    x=()
    for i in range(len(players)):    
        for j in range(len(players[i])):
            x=x+(players[i][j],)
    return(x)
def a_Chapter():
    round=0
    x=0
    Chapter=()
    while x==0:
        [players[round%2][0],players[round%2][1],players[(round+1)%2][0],players[(round+1)%2][1]]=situation_random(players[round%2][0],players[round%2][1],players[(round+1)%2][0],players[(round+1)%2][1])
        x=(judge(players[round%2],players[(round+1)%2],round%2)[0])
        Chapter=Chapter+((exhibit_situation(),judge(players[round%2],players[(round+1)%2],round%2)),)
        round=round+1
    return Chapter
def terminal_score(a,b,c,d):
    if a+b!=0 and c+d!=0:
        player=[[a,b],[c,d]]
        round=0
        x=0
        Chapter=()
        def exhibit_situation():
            x=()
            for i in range(len(player)):    
                for j in range(len(player[i])):
                    x=x+(player[i][j],)
            return(x)
        while x==0:
            if situation_random(player[round%2][0],player[round%2][1],player[(round+1)%2][0],player[(round+1)%2][1])==None:
                break
            [player[round%2][0],player[round%2][1],player[(round+1)%2][0],player[(round+1)%2][1]]=situation_random(player[round%2][0],player[round%2][1],player[(round+1)%2][0],player[(round+1)%2][1])
            x=(judge(player[round%2],player[(round+1)%2],round%2)[0])
            Chapter=Chapter+((exhibit_situation(),judge(player[round%2],player[(round+1)%2],round%2)),)
            round=round+1
        return (Chapter[-1][1])
    elif(a+b==0):
        return((100,1))
    elif(c+d==0):
        return((100,0))
a=0
inp=500
R=[0,0]
with open('output_random.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['test times', 'odds'])
for i in range(inp):
    for j in range(0,10):
        ans=terminal_score(1,1,1,1)
        if sum(ans)==1 or sum(ans)==2501:
            R[1]=R[1]+1
        elif sum(ans)==2500 or sum(ans)==2:
            R[0]=R[0]+1
    persent=(R[0]/(R[0]+R[1]))*100   
    with open('output_random.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([i+1, persent])
    R=[0,0]
print("finish_work!")