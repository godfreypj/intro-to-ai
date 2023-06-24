"""A module for simulating and solving the vacuum world problem.

This module provides classes for representing the vacuum world environment and
an agent that can search for a sequence of actions to clean the environment.
"""


class VacuumAgent:
    """An agent that searches for a sequence of actions to clean a 2x2 vacuum world."""

    def __init__(self):
        self.actions = ["Suck", "Move North", "Move East", "Move South", "Move West"]

    def search(self, state):
        "Calls depth-first-search"
        return self.dfs(state, 0, [])

    def dfs(self, state, depth, path):
        """Recursive method that uses depth-first-search until he goal state
        is found or the depth limit is reached"""
        if depth == 10:
            return None

        if self.goal_test(state):
            return path

        for current_action in self.actions:
            current_new_state = self.apply_action(state, current_action)
            new_path = path + [current_action]

            current_result = self.dfs(current_new_state, depth + 1, new_path)
            if current_result is not None:
                return current_result

            # Backtrack by undoing the action
            current_new_state = self.undo_action(state, current_action)
            if current_new_state is not None:
                return current_new_state

        return None  # Return None if goal state is not found within depth limit

    def goal_test(self, state):
        "Checks if we have reached the goal state (the board is clean)"
        return state == [[False, False], [False, False]]

    def apply_action(self, state, given_action):
        "Updates the states based on the given action. Uses a deep copy"
        updated_state = [row[:] for row in state]
        agent_pos = self.find_agent_position(updated_state)

        if given_action == "Suck":
            if updated_state[agent_pos[0]][agent_pos[1]]:
                updated_state[agent_pos[0]][agent_pos[1]] = False
        elif given_action == "Move North":
            new_agent_pos = (agent_pos[0] - 1, agent_pos[1])
            if self.is_valid_position(new_agent_pos):
                updated_state[agent_pos[0]][agent_pos[1]] = False
                updated_state[new_agent_pos[0]][new_agent_pos[1]] = True
        elif given_action == "Move East":
            new_agent_pos = (agent_pos[0], agent_pos[1] + 1)
            if self.is_valid_position(new_agent_pos):
                updated_state[agent_pos[0]][agent_pos[1]] = False
                updated_state[new_agent_pos[0]][new_agent_pos[1]] = True
        elif given_action == "Move South":
            new_agent_pos = (agent_pos[0] + 1, agent_pos[1])
            if self.is_valid_position(new_agent_pos):
                updated_state[agent_pos[0]][agent_pos[1]] = False
                updated_state[new_agent_pos[0]][new_agent_pos[1]] = True
        elif given_action == "Move West":
            new_agent_pos = (agent_pos[0], agent_pos[1] - 1)
            if self.is_valid_position(new_agent_pos):
                updated_state[agent_pos[0]][agent_pos[1]] = False
                updated_state[new_agent_pos[0]][new_agent_pos[1]] = True
        return updated_state

    def find_agent_position(self, state):
        "Returns the current position of the agent"
        for i, row in enumerate(state):
            for j, value in enumerate(row):
                if value:
                    return (i, j)
        return None

    def is_valid_position(self, pos):
        "Checks if position is beyond bounds of our world, to avoid overflow errors"
        return 0 <= pos[0] < 2 and 0 <= pos[1] < 2

    def undo_action(self, state, given_action):
        "Undo the given action by reverting the state to the previous state"
        updated_state = [row[:] for row in state]

        if given_action == "Suck":
            updated_state[0][0] = True
        elif given_action == "Move North":
            updated_state[0][0] = False
            updated_state[0][1] = False
        elif given_action == "Move East":
            updated_state[0][0] = False
            updated_state[1][0] = False
        elif given_action == "Move South":
            updated_state[0][0] = False
            updated_state[0][1] = False
        elif given_action == "Move West":
            updated_state[0][0] = False
            updated_state[1][0] = False

        return updated_state


class VacuumWorldPrinter:
    """A class to provide a visual representation of the vacuum world."""

    def __init__(self):
        self.depth_limit = 0

    def print_state(self, state, current_agent_position):
        """Prints the current state of the vacuum world with the agent's position."""
        print("Current state:")
        self._print_grid(state, current_agent_position)
        print()

    def _print_grid(self, state, current_agent_position):
        """Prints the grid representation of the vacuum world with the agent's position."""
        line = "+---+---+\n"
        for i, row in enumerate(state):
            print(line + "|", end="")
            for j, cell in enumerate(row):
                if (i, j) == current_agent_position:
                    print(" @ ", end="|")
                elif cell:
                    print(" * ", end="|")
                else:
                    print(" 0 ", end="|")
            print("\n", end="")
        print(line)

    def print_depth_limit(self):
        """Prints the current depth limit of the search."""
        print("Depth limit:", self.depth_limit)
        print("------------------------------------")

    def increase_depth_limit(self):
        """Increases the depth limit counter."""
        self.depth_limit += 1


# Using our vacuum class:
# Instantiate a new agent, Set an initial state, Instantiate a new printer
agent = VacuumAgent()
initial_state = [[True, True], [True, True]]
printer = VacuumWorldPrinter()

# Print initial state
agent_position = agent.find_agent_position(initial_state)
printer.print_state(initial_state, agent_position)
printer.print_depth_limit()

# Run the search
result = agent.search(initial_state)

if result is None:
    print("Goal state not found before depth limit of 10 reached.")
else:
    print("Actions to reach the goal state:")
    for action in result:
        new_state = agent.apply_action(initial_state, action)
        agent_position = agent.find_agent_position(new_state)

        printer.print_state(new_state, agent_position)
        printer.print_depth_limit()

        initial_state = new_state
        printer.increase_depth_limit()
