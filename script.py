import os
import sys

# List to iterate
my_list = [1, 'b', 'a', 1, 'a', 'd', 1, 'a', 'f', 'a']
progress_file = "progress.txt"

# Read last processed index
if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        last_index = int(f.read().strip())
else:
    last_index = 0  # Start from beginning if no progress file

# Run the loop starting from last processed index
for i in range(last_index, len(my_list)):
    print(f"Processing element {i + 1}: {my_list[i]}")

    if my_list[i] == 'a':
        print("Approval needed for 'a' in Jenkins.")
        
        # Save progress before exiting
        with open(progress_file, "w") as f:
            f.write(str(i + 1))  # Save next index

        sys.exit(100)  # Exit with status 100 for approval

# If completed, remove progress file
if os.path.exists(progress_file):
    os.remove(progress_file)

print("Python script completed.")
