import copy

class TowerOfBlocksSolver:

    def __init__(self):
        pass

    def solve(self):
        class BlockState:
            def __init__(self, current_state, goal_state, total_blocks, moves=None):
                if moves is None:
                    moves = []
                self.current_state = current_state
                self.goal_state = goal_state
                self.total_blocks = total_blocks
                self.moves = moves

            def __eq__(self, other):
                return (self.current_state == other.current_state and
                        self.goal_state == other.goal_state and
                        self.total_blocks == other.total_blocks and
                        self.moves == other.moves)

            def __hash__(self):
                return hash((tuple(map(tuple, self.current_state)),
                             tuple(map(tuple, self.goal_state)),
                             self.total_blocks,
                             tuple(self.moves)))

            def solve_with_depth_limit(self, depth_limit):
                return self.depth_limited_search(depth_limit)

            def depth_limited_search(self, depth_limit):
                return self.recursive_dls(self, depth_limit)

            def recursive_dls(self, node, depth):
                if node.difference() == 0:
                    return node.moves, node.current_state
                elif depth == 0:
                    return None, None

                for index, stack in enumerate(node.current_state):
                    for index2, stack2 in enumerate(node.current_state):
                        if index != index2:
                            curr_table, move = self.valid_state_move(node.current_state, index, index2)
                            new_state = BlockState(curr_table, node.goal_state, node.total_blocks, copy.copy(node.moves))
                            new_state.moves.append(move)

                            result, final_state = self.recursive_dls(new_state, depth - 1)
                            if result is not None:
                                return result, final_state

                for index, stack in enumerate(node.current_state):
                    if len(stack) > 1:
                        curr_table, move = self.valid_state_move(node.current_state, index, -1)
                        new_state = BlockState(curr_table, node.goal_state, node.total_blocks, copy.copy(node.moves))
                        new_state.moves.append(move)

                        result, final_state = self.recursive_dls(new_state, depth - 1)
                        if result is not None:
                            return result, final_state

                return None, None

            def select_move(self):
                for index, stack in enumerate(self.current_state):
                    for index2, stack2 in enumerate(self.current_state):
                        if index != index2:
                            curr_table, move = self.valid_state_move(self.current_state, index, index2)
                            new_state = BlockState(curr_table, self.goal_state, self.total_blocks, copy.copy(self.moves))
                            new_state.moves.append(move)
                            return new_state

                for index, stack in enumerate(self.current_state):
                    if len(stack) > 1:
                        curr_table, move = self.valid_state_move(self.current_state, index, -1)
                        new_state = BlockState(curr_table, self.goal_state, self.total_blocks, copy.copy(self.moves))
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

                diff = self.total_blocks - same_num
                return diff

       
        initial_arrangement = [["A"], ["C", "B"]]
        goal_arrangement = [[], ["C", "B", "A"]]

        total_blocks = sum(len(ls) for ls in initial_arrangement)
        state = BlockState(initial_arrangement, goal_arrangement, total_blocks)
        depth_limit = 1
        solution, final_state = state.solve_with_depth_limit(depth_limit)

        if solution is not None:
            print("Solution found:")
            print("Moves:", solution)
            print("Final State:")
            print(final_state)
        else:
            print("No solution found within the depth limit.")

        return solution, final_state


tower_solver = TowerOfBlocksSolver()
result = tower_solver.solve()
print(result)
