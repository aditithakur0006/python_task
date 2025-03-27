my_list = [1, 'b', 'a', 1, 'a', 'd', 1, 'a', 'f', 'a']

for i in my_list:
    if i == 'a':
        print("Approval needed for 'a' in Jenkins.")
        exit(100)  # Exit with status 100 each time 'a' is found
    else:
        print(f"'a' not found, found: {i}")

print("Python script completed.")
