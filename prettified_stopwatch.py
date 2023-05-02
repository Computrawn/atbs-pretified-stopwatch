#! python3
# prettified_stopwatch.py — An exercise in keeping time and scheduling.
# For more information, see project_details.txt.

import logging
import time


logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


print(
    """Press ENTER to begin. 
Afterward, press ENTER to "click" the stopwatch. 
Press Ctrl-C to quit."""
)
input()
print("Started.")
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_num_str = str(lap_num)
        lap_time = str(round(time.time() - last_time, 2))
        lap_parenthesis = f"({lap_time})"
        total_time = str(round(time.time() - start_time, 2))
        print(
            f"Lap # {lap_num_str.rjust(3)}: {total_time.rjust(10)} {lap_parenthesis.rjust(10)}",
            end="",
        )
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print("\nDone.")
