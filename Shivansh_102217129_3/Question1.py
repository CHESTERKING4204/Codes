import copy
import time

class BlockPuzzleSolver:

    def __init__(self):
        pass

    def solve(self):
        start_time = time.time()

        class State:
            def __init__(self, current_state, goal_state, total_num, moves=None):
                if moves is None:
                    moves = []
                self.current_state = current_state
                self.goal_state = goal_state
                self.total_num = total_num
                self.moves = moves

            def __eq__(self, other):
                return (self.current_state == other.current_state and
                        self.goal_state == other.goal_state and
                        self.total_num == other.total_num and
                        self.moves == other.moves)

            def __hash__(self):
                return hash((tuple(map(tuple, self.current_state)),
                             tuple(map(tuple, self.goal_state)),
                             self.total_num,
                             tuple(self.moves)))

            def goal_state_move(self):
                visited_states = set()

                stack = [self]
                while stack:
                    current_state = stack.pop()
                    print("Current State:")
                    print(current_state.current_state)
                    if current_state.difference() == 0:
                        return current_state.moves, current_state.current_state

                    visited_states.add(current_state)

                    new_state = current_state.select_move()
                    if new_state is not None and new_state not in visited_states:
                        stack.append(new_state)

                print("No solution found.")
                return None, None

            def select_move(self):
                for index, stack in enumerate(self.current_state):
                    for index2, stack2 in enumerate(self.current_state):
                        if index != index2:
                            curr_table, move = self.valid_state_move(self.current_state, index, index2)
                            new_state = State(curr_table, self.goal_state, self.total_num, copy.copy(self.moves))
                            new_state.moves.append(move)
                            return new_state

                for index, stack in enumerate(self.current_state):
                    if len(stack) > 1:
                        curr_table, move = self.valid_state_move(self.current_state, index, -1)
                        new_state = State(curr_table, self.goal_state, self.total_num, copy.copy(self.moves))
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
                    move = (top_block, right[-1])
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
                diff = self.total_num - same_num
                return diff

       
        initial_arrangement = [["A"], ["C", "B"]]
        goal_arrangement = [[], ["C", "B", "A"]] 

        total_num = sum(len(ls) for ls in initial_arrangement)
        state = State(initial_arrangement, goal_arrangement, total_num)
        solution, final_state = state.goal_state_move()

        if solution is not None:
            print("Solution found:")
            print("Moves:", solution)
            print("Final State:")
            print(final_state)

        end_time = time.time()
        run_time = str((end_time - start_time) * 1000)
        print("Running time:" + run_time + "ms")
        return solution, final_state


agent = BlockPuzzleSolver()
result = agent.solve()
print(result)
