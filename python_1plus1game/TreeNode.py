from __future__ import unicode_literals
from __future__ import division, print_function, with_statement
from typing import Type

class TreeNode(object):
    """The basic node of tree structure"""
    def __init__(self, name, parent=None):
        super(TreeNode, self).__init__()
        self.name = name
        self.parent = parent
        self.child = {}

    def __contains__(self, item):
        return item in self.child

    def __len__(self):
        """return number of children node"""
        return len(self.child)
#    def __bool__(self, item):
#        """always return True for exist node"""
#        return True
    @property
    def path(self):
        """return path string (from root to current node)"""
        if self.parent:
            return (str(self.parent.path)+ " "+str(self.name))
        else:
            return self.name

    def get_child(self, name, defval=None):
        """get a child node of current node"""
        return self.child.get(name, defval)

    def add_child(self, name, obj=None):
        """add a child node to current node"""
        if obj and not isinstance(obj, TreeNode):
            raise ValueError('TreeNode only add another TreeNode obj as child')
        if obj is None:
            obj = TreeNode(name)
        obj.parent = self
        self.child[name] = obj
        return obj

    def del_child(self, name):
        """remove a child node from current node"""
        if name in self.child:
            del self.child[name]

    def find_child(self, path, create=False):
        """find child node by path/name, return None if not found"""
        # convert path to a list if input is a string
        path = path if isinstance(path, list) else path.split()
        cur = self
        for sub in path:
            # search
            obj = cur.get_child(sub)
            if obj is None and create:
                # create new node if need
                obj = cur.add_child(sub)
            # check if search done
            if obj is None:
                break
            cur = obj
        return obj

    def items(self):
        return self.child.items()

    def dump(self, indent=0):
        """dump tree to string"""
        tab = '    '*(indent-1) + ' |- ' if indent > 0 else ''
        print(tab+str(self.name))
        for name, obj in self.items():
            obj.dump(indent+1)

    def revise(self,name,new_name):
        if name in self.child:
            del self.child[name]
            self.add_child(new_name)

    def path_revise(self,a=None):
        '''path'''
        if self.parent!=None:
            self.parent.name=a
            return(self.parent.path_revise(a))
        else:
            return None
    
    def dump_file(self,A=None,indent=0):
        tab = '    '*(indent-1) + ' |- ' if indent > 0 else ''
        print(str(tab+str(self.name)), file = A)
        for name, obj in self.items():
            obj.dump_file(A,indent+1)