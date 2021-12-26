from os import close
import TreeNode
import numpy as np
import random
import MCTS
import csv
import onePoneGame
import time
test = TreeNode.TreeNode("One_P_One") 
Start=test.add_child(((1,1,1,1),(0,1),1,0,(0,0)))
Path_nodes=[[Start]]
MCTS.Expansion_Simulation_Backpropagation(Start,Path_nodes)
for i in range(10):
    MCTS.Expansion_Simulation_Backpropagation(MCTS.Selection(Start,Path_nodes),Path_nodes)
def random_fight(s):
        R_list=[]
        if Path_nodes[s[4][0]][s[4][1]].child !={}:
            for key,value in Path_nodes[s[4][0]][s[4][1]].child.items():
                R_list.append(key)
            R=R_list[random.randint(0,len(R_list)-1)]
            return(R)
        else:
            return("empty")
def UCB1_fight(s):
    R_list=[]
    UCB1_list=[]
    if Path_nodes[s[4][0]][s[4][1]].child !={}:
        for key,value in Path_nodes[s[4][0]][s[4][1]].child.items():
            R_list.append(key)
            if key[2]!=0:
                avg_v=key[3]/key[2]
            else:
                avg_v=np.inf
            n=key[2]
            N=Start.name[2]
            UCB1_list.append(MCTS.UCB1(avg_v,N,n))
        R=R_list[UCB1_list.index(max(UCB1_list))]
        return(R)
    else:
        return("empty")
def Simulation(S,a,x=0):
    a=a%2
    result=None
    if S[1][0]==0 or Path_nodes[S[4][0]][S[4][0]].child=={}:
        if a==1:
            if random_fight(S)=="empty":
                x=(onePoneGame.terminal_score(S[0][2],S[0][3],S[0][0],S[0][1]))
            else:
                result=random_fight(S)
        if a==0:
            if UCB1_fight(S)=="empty":
                x=(onePoneGame.terminal_score(S[0][0],S[0][1],S[0][2],S[0][3]))
            else:
                result=UCB1_fight(S)
        if result!=None:
            return(Simulation(result,a+1))
        else:
            return x       
    else:
        return(onePoneGame.terminal_score(S[0][0],S[0][1],S[0][2],S[0][3]))
def choose(a): 
    if a==0:
        S=Path_nodes[0][0].name
    if a==1:
        S_list=[]
        for key,value in Path_nodes[0][0].child.items():
            S_list.append(key)
        S=S_list[random.randint(0,len(S_list-1))]    
    return Simulation(S,a)
a=0
inp=500
R=[0,0]
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['expansion times', 'odds'])
for i in range(inp):
    MCTS.Expansion_Simulation_Backpropagation(MCTS.Selection(Start,Path_nodes),Path_nodes)
    for j in range(0,10):
        final=choose(0)
        if sum(final)==1 or sum(final)==2501:
            R[1]=R[1]+1
        elif sum(final)==2500 or sum(final)==2:
            R[0]=R[0]+1
    persent=(R[0]/(R[0]+R[1]))*100   
    with open('output.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([i+1, persent])
    R=[0,0]
print("finish_work!")