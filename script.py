import sys

# List containing values
my_list = [1, 'b', 'a', 1, 'a', 'd', 1, 'a', 'f', 'a']

# Loop through the list
for i in my_list:
    if i == 'a':
        print("Approval needed for 'a' in Jenkins.")
        sys.exit(100)  
    else:
        print("'a' not found, found:", i)

print("Python script completed.")
