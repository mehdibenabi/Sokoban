class SokobanPuzzle :

    def __init__(self,grid,player_pos,boxes,targets):

        self.grid=grid
        self.player_pos=player_pos
        self.boxes=boxes
        self.targets=targets

    def isGoal(self):
        return all(box in self.targets for box in self.boxes)

    def successor_function(self):
        successors = []
        directions = { "UP": (-1, 0), "DOWN":(1, 0),"LEFT" : (0, -1),"RIGHT":(0, 1) } 

        for direction in directions:
            new_player_pos = (self.player_pos[0] + direction[0], self.player_pos[1] + direction[1])

           
            if self.grid[new_player_pos[0]][new_player_pos[1]] != 'O':
                if new_player_pos in self.boxes: 
                    new_box_pos = (new_player_pos[0] + direction[0], new_player_pos[1] + direction[1])
                    
                    
                    if self.grid[new_box_pos[0]][new_box_pos[1]] != 'O' and new_box_pos not in self.boxes:
                       
                        new_boxes = list(self.boxes)
                        new_boxes.remove(new_player_pos)
                        new_boxes.append(new_box_pos)
                       
                        successors.append((direction, SokobanPuzzle(self.grid, new_player_pos, new_boxes, self.targets)))
                        
                else:
                    
                    successors.append((direction, SokobanPuzzle(self.grid, new_player_pos, self.boxes, self.targets)))
                    

        return successors



class Node:
    def __init__(self, state, parent=None, action=None, g=0):
        self.state = state  
        self.parent = parent
        self.action = action
        self.g = g 
        self.f = 0

    def get_path(self):
    
        node= self
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]  

    def get_solution(self):
        return [node.action for node in self.get_path()[1:]]
    
    def set_f(self, heuristic):
        self.f = self.g + heuristic(self.state)
