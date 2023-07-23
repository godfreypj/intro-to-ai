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
            # Instantiate an agent with our rack list, start timer
            rack_list = list(line.strip())
            agent = Agent(rack_list)
            agent_timer = Timer()
            agent_timer.start()

            # Solve the rack, report the stats
            print("\n\nBeep Boop ... solving ...   ***************************\n")
            print(f"Score: {agent.solve()}")
            agent_timer.stop()
            agent.display()

            # Display stats to the user
            print(f"\nTIME: {agent_timer.get_elapsed_time():.2f}")
            print("\nBeep boop ... solved! :) ... **************************\n")


except FileNotFoundError:
    print("File not found:", RACK_FILE)
    sys.exit(1)
