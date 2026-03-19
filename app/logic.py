# main logic for dfs 
# import 
from typing import List, Dict
#list -- input edges 
# dict -- graph structure 
#function to take edges each edge u depends on v 
def resolve_dependencies_logic(edges: List[List[str]]):
    #graph and node structure 
    graph: Dict[str, List[str]] = {} # adjancy list
    nodes = set() #all unique nodes 
    for u, v in edges:
        if v not in graph:
            graph[v] = [] #ensure it exists 
            graph[v].append(u) # edge direction v-> u do v first then u
            nodes.add(u)
            nodes.add(v) # store all nodes 
            # add missing nodes as they may not have outgoing edges 
    for node in nodes:
        if node not in graph:
            graph[node] = []

    # state tracking 0 - unvisited, 1 - visiting in path 2 - visited done 
    state = {node: 0 for node in nodes}
    result = []
    path = []
    cycle_path = []

    def dfs(node):
        nonlocal cycle_path #modify outer variable # dont create new variable use from above.
        if state[node] == 1: # node in path - cycle found 
            idx = path.index(node) #find source
            cycle_path = path[idx:] + [node] # extract path
            return True # stop dfs 
        if state[node] == 2: # already processed - no revisit return false
           return False
        
        state[node] = 1 # mark visiting start explore
        path.append(node) # add to path

        for neighbour in graph[node]: # traverse dependencies
           if dfs(neighbour): # if cycle  found stop everything
              return True
    
        path.pop()  #remove node
        state[node] = 2  #mark done 
        result.append(node) #add to result
        return False  # no cycle 
    
    for node in nodes: # run dfs on all nodes 
        if state[node] == 0: # only for unvisited ones 
            if dfs(node):  # if found return 
                return {"cycle": cycle_path}
    
    result.reverse() # return in topological order
    return{"order": result}

        