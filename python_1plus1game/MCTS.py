'''
選擇（Selection）：從根節點R開始，連續向下選擇子節點至葉子節點L。下文將給出一種選擇子節點的方法，讓遊戲樹向最佳的方向擴充，這是蒙地卡羅樹搜尋的精要所在。
擴充（Expansion）：除非任意一方的輸贏使得遊戲在L結束，否則建立一個或多個子節點並選取其中一個節點C。
仿真（Simulation）：在從節點C開始，用隨機策略進行遊戲，又稱為playout或者rollout。
反向傳播（Backpropagation）：使用隨機遊戲的結果，更新從C到R的路徑上的節點資訊。
'''
from math import sqrt
import numpy as np
import onePoneGame
import TreeNode
import random
def UCB1(avg_v,N,n):
    if n!=0:
        return avg_v+(sqrt((2*np.log(N))/n))
    else:
        return np.inf

def Rollout(a):
    if a[1][1]==1:
        data=onePoneGame.situation(a[0][0],a[0][1],a[0][2],a[0][3])
    else:
        data=onePoneGame.situation(a[0][2],a[0][3],a[0][0],a[0][1])
        for i in range(len(data)):
            data[i]=[data[i][2],data[i][3],data[i][0],data[i][1]]
    data_terminal=[]
    if a[1][1]==0:    
        r=a[1][1]+1
    else:
        r=a[1][1]-1
    for i in range(len(data)):
        if onePoneGame.judge([data[i][0],data[i][1]],[data[i][2],data[i][3]],1)[0]==0:
            Score=onePoneGame.terminal_score(data[i][0],data[i][1],data[i][2],data[i][3])
            data_terminal.append(((data[i][0],data[i][1],data[i][2],data[i][3]),onePoneGame.judge([data[i][0],data[i][1]],[data[i][2],data[i][3]],r),0,Score[0]))     
    return data_terminal

def Expansion_Simulation_Backpropagation(A,Path_nodes):
    Path_nodes.append([])
    x=len(Path_nodes)-1
    if A.name[1][0]==0:
        for i in range(len(Rollout(A.name))):
            new_tuple=()
            for j in range(len(Rollout(A.name)[i])):
                new_tuple += (Rollout(A.name)[i][j],)
            new_tuple += ((x,i),)
            Path_nodes[x].append(A.add_child(new_tuple))
            def return_path(a):
                if a.parent != None and type(a.parent.name[2]) != str:
                    k=(a.parent.name[0],a.parent.name[1],a.parent.name[2]+1,a.parent.name[3]+Path_nodes[x][i].name[3],a.parent.name[4])
                    a.parent.name=k
                    return(return_path(a.parent))
            return_path(Path_nodes[x][i])
    else:
        None 

def Selection(a,Path_nodes):
    if a.child != {}:
        key_list=[]
        UCB1_list=[]
        
        for key in a.child:
            key_list.append(Path_nodes[key[4][0]][key[4][1]].name)
        for i in range(len(key_list)):
            if key_list[i][2]!=0:
                avg_v=key_list[i][3]/key_list[i][2]
            else:
                avg_v=np.inf
            n=key_list[i][2]
            N=Start.name[2]
            UCB1_list.append(UCB1(avg_v,N,n))
        max_x_i_ucb=0
        if key_list[0][1][1]==0:
            max_x_i_ucb=key_list[UCB1_list.index(max(UCB1_list))]
        else:
            max_x_i_ucb=key_list[UCB1_list.index(min(UCB1_list))]
        if max_x_i_ucb==0:
            print("bug")
            return(a)
        terminal_choce=Path_nodes[max_x_i_ucb[4][0]][max_x_i_ucb[4][1]]
        return(Selection(terminal_choce,Path_nodes))
    else:
        return(a)


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
            UCB1_list.append(UCB1(avg_v,N,n))
        R=R_list[UCB1_list.index(max(UCB1_list))]
        return(R)
    else:
        return("empty")

root = TreeNode.TreeNode("One_P_One") 
Start=root.add_child(((1,1,1,1),(0,1),1,0,(0,0)))
Path_nodes=[[Start]]
Expansion_Simulation_Backpropagation(Start,Path_nodes)
'''
#test
print("File_name():")
x=input()
print("Number of expansions:")

#txt存檔
File = open(x+".txt", 'w')
root.dump_file(File)
File.close()
y=input()
y=int(y)


def dictionary(a):
    dict=a.child
    for name,obj in a.items():
        dict[name]=obj.child
        dictionary(obj)
    return dict
Path_sum=[]
for i in range(len(Path_nodes)):
    Path_sum.append(len(Path_nodes[i]))
save_as_np=np.array(dictionary(root))
np.save(x,save_as_np)
np.save(x+"_PathNumber",Path_sum)'''
