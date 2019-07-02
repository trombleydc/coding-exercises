class Node:
    def __init__(self, name, length, is_file, depth):
        self.name = name;
        self.length = length;
        self.is_file = is_file;
        self.depth = depth;
        self.children = [];

def build_node():
    global line
    global idx
   
    depth = 0
    
    if line[idx] == '\n':
        idx += 1
    while line[idx] == '\t':
        depth += 1
        idx += 1

    name = ""
    is_file = False
    
    while idx < len(line) and line[idx] != '\n':
        if line[idx] == '.':
            is_file = True
        name += line[idx]
        idx += 1
    print(name, len(name), idx, depth, is_file)
    return Node(name, len(name), is_file, depth)

line = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.txt"
idx = 0   
root_list = []

def build_tree(past_depth):
    if idx < len(line): 
        if past_depth == -1: 
            node = build_node()
            root_list.append(node)
            node.children.append(build_tree(node.depth))
        
        if node.depth > past_depth
            node = build_node()
            node.children.append(build_tree(node.depth))
            return node
        
        if node.depth < past_depth
            

def build_tree(past_depth):
    if idx < len(line):
        node = build_node()

    if node.depth == past_depth + 1:
        return node
    else 
        build_tree()



#node_list = []
#
#while idx < len(line):
#    node_list.append(build_node())
#
#root_arr = []
#i = 0
#while i < len(node_list):
#    if depth == 0:
#        continue
#
