import collections as queue;

def BFS (s, successorsFn , isGoal):
    open=queue.Queue() 
    closed =[]

    init_node = Node(s, None , None)

    if(isGoal(init_node.state)):
        return init_node
    
    open.put(init_node)
    closed =[]

    while not open.empty():
        n = open.get()
        closed.append(n.state)
        for action, state in successorsFn(n.state):
            if state not in closed:
                if isGoal(state):
                    return Node(state, n, action)
                open.put(Node(state, n, action))