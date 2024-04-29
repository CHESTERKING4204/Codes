import copy
from collections import deque

class BlockPuzzleSolver:

    def __init__(self):
        pass

    def find_solution(self):
        class State:
            def __init__(self, current_state, goal_state, total_num_blocks, moves=None):
                if moves is None:
                    moves = []
                self.current_state = current_state
                self.goal_state = goal_state
                self.total_num_blocks = total_num_blocks
                self.moves = moves

            def __eq__(self, other):
                return (self.current_state == other.current_state and
                        self.goal_state == other.goal_state and
                        self.total_num_blocks == other.total_num_blocks and
                        self.moves == other.moves)

            def __hash__(self):
                return hash((tuple(map(tuple, self.current_state)),
                             tuple(map(tuple, self.goal_state)),
                             self.total_num_blocks,
                             tuple(self.moves)))

            def bfs(self):
                visited_states = set()

                queue = deque([self])
                while queue:
                    current_state = queue.popleft()

                    if current_state.difference() == 0:
                        return current_state.moves, current_state.current_state

                    visited_states.add(current_state)

                    for index, stack in enumerate(current_state.current_state):
                        for index2, stack2 in enumerate(current_state.current_state):
                            if index != index2:
                                curr_table, move = self.valid_state_move(current_state.current_state, index, index2)
                                new_state = State(curr_table, current_state.goal_state, current_state.total_num_blocks,
                                                  copy.copy(current_state.moves))
                                new_state.moves.append(move)

                                if new_state not in visited_states:
                                    queue.append(new_state)
                                    visited_states.add(new_state)

                    for index, stack in enumerate(current_state.current_state):
                        if len(stack) > 1:
                            curr_table, move = self.valid_state_move(current_state.current_state, index, -1)
                            new_state = State(curr_table, current_state.goal_state, current_state.total_num_blocks,
                                              copy.copy(current_state.moves))
                            new_state.moves.append(move)

                            if new_state not in visited_states:
                                queue.append(new_state)
                                visited_states.add(new_state)

                return None, None  

            def select_move(self):
                for index, stack in enumerate(self.current_state):
                    for index2, stack2 in enumerate(self.current_state):
                        if index != index2:
                            curr_table, move = self.valid_state_move(self.current_state, index, index2)
                            new_state = State(curr_table, self.goal_state, self.total_num_blocks, copy.copy(self.moves))
                            new_state.moves.append(move)
                            return new_state

                for index, stack in enumerate(self.current_state):
                    if len(stack) > 1:
                        curr_table, move = self.valid_state_move(self.current_state, index, -1)
                        new_state = State(curr_table, self.goal_state, self.total_num_blocks, copy.copy(self.moves))
                        new_state.moves.append(move)
                        return new_state

                return None  
            
            def valid_state_move(self, table, start_index, end_index):
                temp_table = copy.deepcopy(table)
                left = temp_table[start_index]
                top_block = left.pop()
                right = []

                if end_index < 0:
                    temp_table.append(right)
                    move = (top_block, 'Table')
                else:
                    right = temp_table[end_index]
                    if right: 
                        move = (top_block, right[-1])
                    else:
                        move = (top_block, 'Table')
                right.append(top_block)

                if len(left) == 0:
                    temp_table.remove(left)
                return temp_table, move

            def difference(self):
                same_num = 0
     
                for left in self.current_state:
                    for right in self.goal_state:
                        index = 0
                        while index < len(left) and index < len(right):
                            if left[index] == right[index]:
                                same_num += 1
                                index += 1
                            else:
                                break
                        
                        if index < len(left) or index < len(right):
                            same_num -= min(len(left) - index, len(right) - index)

                diff = self.total_num_blocks - same_num
                return diff

       
        initial_arrangement = [["A"], ["C", "B"]]
        goal_arrangement = [[], ["C", "B", "A"]]

        total_num_blocks = sum(len(ls) for ls in initial_arrangement)
        state = State(initial_arrangement, goal_arrangement, total_num_blocks)
        solution, final_state = state.bfs()

        if solution is not None:
            print("Solution found:")
            print("Moves:", solution)
            print("Final State:")
            print(final_state)
        else:
            print("No solution found.")

        return


block_solver = BlockPuzzleSolver()
block_solver.find_solution()
