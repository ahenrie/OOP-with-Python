current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_int)

final_time_int = current_time_int + wait_time_int
print(final_time_int)

"""
Traceback (most recent call last):
  File "/home/codio/workspace/./code/know_errors.py", line 2, in <module>
    current_time = input("what is the current time (in hours)?")
EOFError: EOF when reading a line
what is the current time (in hours)?
"""
