class TreeNode:
    
    def __init__(self, data):   # Correct constructor
        self.data = data 
        self.children = []
        
    def add_child(self, child_node):
        self.children.append(child_node)
        
    def __repr__(self, level=0):   # Correct repr method
        ret = " " * (level * 2) + repr(self.data) + "\n"
        print(ret)
        
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret
    
# # Create nodes
# root = TreeNode("Electronics")
# laptop = TreeNode("Laptop")
# tv = TreeNode("Television")
# phone = TreeNode("Smartphone")

# # Add children to root
# root.add_child(laptop)
# root.add_child(tv)
# root.add_child(phone)

# print(root)
