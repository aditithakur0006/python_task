import os
import sys

my_list = [1, 'b', 'a', 1, 'a', 'd', 1, 'a', 'f', 'a']
progress_file = "progress.txt"

if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        last_index = int(f.read().strip())
else:
    last_index = 0  
for i in range(last_index, len(my_list)):
    if my_list[i] == 'a':
        print("Approval needed for 'a' in Jenkins.")
        
        with open(progress_file, "w") as f:
            f.write(str(i + 1))  
        sys.exit(100)  
    else:
        print(f"'a' not found, found: {my_list[i]}")  

if os.path.exists(progress_file):
    os.remove(progress_file)

print("Python script completed.")
