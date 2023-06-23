class VacuumAgent:
    def __init__(self):
        self.actions = ["Suck", "Move North", "Move East", "Move South", "Move West"]

    def search(self, state):
        return self.dfs(state, 0, [])

    def dfs(self, state, depth, path):
        if depth == 10:
            return None

        if self.goal_test(state):
            return path

        for action in self.actions:
            new_state = self.apply_action(state, action)
            new_path = path + [action]

            result = self.dfs(new_state, depth + 1, new_path)
            if result is not None:
                return result

            # Backtrack by undoing the action
            new_state = self.undo_action(state, action)
            if new_state is not None:
                return new_state

        return None  # Return None if goal state is not found within depth limit

    def goal_test(self, state):
        return state == [[False, False], [False, False]]

    def apply_action(self, state, action):
        new_state = [row[:] for row in state]  # create a deep copy of the state
        agent_pos = self.find_agent_position(new_state)

        if action == "Suck":
            if new_state[agent_pos[0]][agent_pos[1]]:
                new_state[agent_pos[0]][agent_pos[1]] = False
        elif action == "Move North":
            new_agent_pos = (agent_pos[0] - 1, agent_pos[1])
            if self.is_valid_position(new_agent_pos):
                new_state[agent_pos[0]][agent_pos[1]] = False
                new_state[new_agent_pos[0]][new_agent_pos[1]] = True
        elif action == "Move East":
            new_agent_pos = (agent_pos[0], agent_pos[1] + 1)
            if self.is_valid_position(new_agent_pos):
                new_state[agent_pos[0]][agent_pos[1]] = False
                new_state[new_agent_pos[0]][new_agent_pos[1]] = True
        elif action == "Move South":
            new_agent_pos = (agent_pos[0] + 1, agent_pos[1])
            if self.is_valid_position(new_agent_pos):
                new_state[agent_pos[0]][agent_pos[1]] = False
                new_state[new_agent_pos[0]][new_agent_pos[1]] = True
        elif action == "Move West":
            new_agent_pos = (agent_pos[0], agent_pos[1] - 1)
            if self.is_valid_position(new_agent_pos):
                new_state[agent_pos[0]][agent_pos[1]] = False
                new_state[new_agent_pos[0]][new_agent_pos[1]] = True

        printer.print_state(new_state)
        printer.print_depth_limit()
        return new_state

    def find_agent_position(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j]:
                    return (i, j)
        return None

    def is_valid_position(self, pos):
        return 0 <= pos[0] < 2 and 0 <= pos[1] < 2

    def undo_action(self, state, action):
        # Undo the action by reverting the state to the previous state
        new_state = [row[:] for row in state]  # create a deep copy of the state

        if action == "Suck":
            new_state[0][0] = True
        elif action == "Move North":
            new_state[0][0] = False
            new_state[0][1] = False
        elif action == "Move East":
            new_state[0][0] = False
            new_state[1][0] = False
        elif action == "Move South":
            new_state[0][0] = False
            new_state[0][1] = False
        elif action == "Move West":
            new_state[0][0] = False
            new_state[1][0] = False

        return new_state


class VacuumWorldPrinter:
    def __init__(self):
        self.depth_limit = 0

    def print_state(self, state):
        print("Current state:")
        for row in state:
            print(row)
        print()

    def print_depth_limit(self):
        print("Depth limit:", self.depth_limit)
        print("------------------------------------")

    def increase_depth_limit(self):
        self.depth_limit += 1


# Example usage
agent = VacuumAgent()
initial_state = [[True, True], [True, False]]
printer = VacuumWorldPrinter()

printer.print_state(initial_state)
printer.print_depth_limit()

result = agent.search(initial_state)

if result is None:
    print("Goal state not found within depth limit.")
else:
    print("Actions to reach the goal state:")
    for action in result:
        new_state = agent.apply_action(initial_state, action)

        printer.print_state(new_state)
        printer.print_depth_limit()

        initial_state = new_state
        printer.increase_depth_limit()
