"""
Module: main
Description: main py file, kicks off the program by reading in the given text file
argument.
Informed agent gets all the time it wants to solve the puzzle, provided it does
not cause a Recursion error. Uninformed agent gets two minutes. If the informed
agent deems the puzzle unsolve-able the app cuts short and returns. Stats in the
form of time and actions taken & the completed board are displaye for the user.
"""
import sys
from board import Board
from utils.timer import Timer
from informed_agent import InformedAgent
from uninformed_agent import UninformedAgent

sys.setrecursionlimit(100000)

if len(sys.argv) < 2:
    print("Please provide a Sudoku puzzle file as an argument.")
    sys.exit(1)

PUZZLE_FILE = sys.argv[1]

try:
    with open(PUZZLE_FILE, "r", encoding="utf-8") as file:
        un_agent_board = Board(PUZZLE_FILE)
        agent_board = Board(PUZZLE_FILE)

    try:
        # Provide set and initial board for user
        print("\n==__== ... Agents attempt to solve ... ==__==\n")
        print("Initial Board: \n")
        un_agent_board.display()
        print("\nSet: \n")
        print(sorted(list(un_agent_board.get_variable_set())))
        print("\nBoth agents attempting to solve the board ... \n")

        # Instantiate our agents, start a timer
        un_agent = UninformedAgent(un_agent_board)
        un_timer = Timer()
        un_timer.start()
        agent = InformedAgent(agent_board)
        agent_timer = Timer()
        agent_timer.start()

        if agent.solve():
            agent_timer.stop()
            if un_agent.solve():
                un_timer.stop()
                un_agent_board.display()
                print("\nSolved by both agents!\n")
                print("Stats: \n")
                print("Uninformed Agent:")
                print(f"Elapsed time: {un_timer.get_elapsed_time():.2f} seconds")
                print(f"Action count: {un_agent.action_count}")
                print("---------")
                print("Informed Agent:")
                print(f"Elapsed time: {agent_timer.get_elapsed_time():.2f} seconds")
                print(f"Action count: {agent.action_count}")
            else:
                if un_timer.get_elapsed_time() > 120:
                    agent_board.display()
                    print("Uninformed agent unable to solve in less than 2 minutes\n")
                    print("Solved by informed agent!\n")
                    print("Stats: \n")
                    print(f"Elapsed time: {agent_timer.get_elapsed_time():.2f} seconds")
                    print(f"Action count: {agent.action_count}")
                else:
                    print("Unsolvable")
                    print("Current state of the board:\n")
                    un_agent_board.display()
        else:
            print("Unsolvable")
            print("Current state of the board:\n")
            un_agent_board.display()

    except RecursionError:
        sys.stdout.write("\r            \n")
        print("One or both agents unable to solve without Recursion Error")
        print("Current state of the board:\n")
        agent.display()


except FileNotFoundError:
    print("File not found:", PUZZLE_FILE)
    sys.exit(1)
