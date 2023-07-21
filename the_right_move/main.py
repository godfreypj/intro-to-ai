"""
Module: main
Description: kicks off the agent by reading in the given rack from the argument.
Agent will report results before moving on to the next rack.
"""
import sys
from agent import Agent
from utils.timer import Timer

if len(sys.argv) < 2:
    print("Please provide a Rack list file as an argument.")
    sys.exit(1)

RACK_FILE = sys.argv[1]

try:
    # Iterate over our given file, each line is a rack
    with open(RACK_FILE, "r", encoding="utf-8") as file:
        for line in file:
            rack_list = list(line.strip())
            # Instantiate an agent with our rack list, start timer
            agent = Agent(rack_list)
            agent_timer = Timer()
            agent_timer.start()
            # Display the current state of the board and the rack, stop time
            print("Beep Boop ... solving ...   *************************\n")
            print(agent.solve())
            agent.display()
            agent_timer.stop()
            # Display stats to the user
            print(f"\nTIME: {agent_timer.get_elapsed_time():.2f}")
            print("\nBeep boop ... solved! :)\n")


except FileNotFoundError:
    print("File not found:", RACK_FILE)
    sys.exit(1)
