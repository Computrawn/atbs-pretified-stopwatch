#! python3
# prettified_stopwatch.py — An exercise in keeping time and scheduling.
# For more information, see project_details.txt.

import logging
import time
import pyperclip


logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


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
output_file = []

try:
    while True:
        input()
        lap_num_str = f"{str(lap_num)}:"
        lap_time = str(round(time.time() - last_time, 2))
        lap_parenthesis = f"({lap_time})"
        total_time = str(round(time.time() - start_time, 2))
        output_string = f"Lap #{lap_num_str.ljust(4)}{total_time.rjust(12)}{lap_parenthesis.rjust(15)}"
        print(output_string, end="")
        output_file.append(output_string)
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print("\nDone.")


with open("time_log.txt", "w", encoding="utf-8") as wf:
    for item in output_file:
        wf.write(item + "\n")

with open("time_log.txt", "r", encoding="utf-8") as rf:
    compiled_output = rf.read()
    pyperclip.copy(compiled_output)
