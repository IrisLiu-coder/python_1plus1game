import TreeNode
import onePoneGame
import numpy as np
'''game_01=onePoneGame.a_Chapter()
root = TreeNode.TreeNode(((1,1,1,1),(0,1))) # root name is ''
counter=[root]
for i in range(len(game_01)):
    counter.append((game_01[i],i))
    counter[i+1]=counter[i].add_child(game_01[i])
for (key,value) in root.child.items():
    print(key,":",value)
def cld(dict):
    for (key,value) in dict.items():
        print(key,":",end="")
        return cld(value)
cld(root.child)
root.dump()
dct= {}
np.save('file.npy', dct)
new_dict = np.load('file.npy', allow_pickle='TRUE')
print(new_dict)
root = TreeNode.TreeNode('test') # root name is ''
a1 = root.add_child("a1")
a1.add_child('b1')
a1.add_child('b2')
a2 = root.add_child('a2')
b3 = a2.add_child('b3')
c1=b3.add_child((1,1))
c2=c1.add_child((0,0))
for key,value in root.items():
    root.child[key]=key.child
root.dump()
print('test items()')
for name, obj in a1.items():
    print(name, obj)
    print(obj.name)
    # b1 TreeNode(b1)
    # b2 TreeNode(b2)


print('test operator "in"')
print("b2 is a1's child = %s" % ('b2' in a1))
    # b2 is a1's child = True


print('test del_child()')
a1.del_child('b2')
root.dump()
print("b2 is a1's child = %s" % ('b2' in a1))
    # (root)
    #  |- a1
    #      |- b1
    #  |- a2
    #      |- b3
    #          |- c1
    # b2 is a1's child = False

print('test find_child()')
obj = root.find_child('a2 b3 c1')
print(obj)
    # TreeNode(c1)

print('test find_child() with create')
obj = root.find_child('a1 b1 c2 b1 e1 f1', create=True)
print(obj)
root.dump()
    # TreeNode(f1)
    # (root)
    # |- a1
    #     |- b1
    #         |- c2
    #             |- b1
    #                 |- e1
    #                     |- f1
    # |- a2
    #     |- b3
    #         |- c1

print('test attr path')
obj_list=c2.path
print(obj_list)
# a1 b1 c2 b1 e1 f1
c2.path_revise("a")
root.dump()
print(c2.child)'''
import TreeNode
import numpy as np
import onePoneGame
print("One Plus One game random test=>")
print("input your file name(.npy):")
x=input()
data_file=np.load(x+".npy",allow_pickle='True')#讀取資料檔案
data_PathNum=np.load(x+"_PathNumber.npy",allow_pickle='True').tolist()
Path_nodes=[]
for i in range(len(data_PathNum)):
    Path_nodes.append([])
    for j in range(data_PathNum[i]):
        Path_nodes[i].append(j)
root=TreeNode.TreeNode("OnePOne_Data")
for key in data_file.item():
    Start=root.add_child(key)
    data=(data_file.item()[key])
Path_nodes[0][0]=Start
def turn_Tree(A,data):
    for key,value in data.items():
        Path_nodes[key[4][0]][key[4][1]]=A.add_child(key)
        turn_Tree(Path_nodes[key[4][0]][key[4][1]],value)
turn_Tree(Start,data)
root.dump()