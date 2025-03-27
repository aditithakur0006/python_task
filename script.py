my_list = [1, 'b', 'a', 1, 'a', 'd', 1, 'a', 'f', 'a']

# Run loop 10 times
for iteration in range(10):
    print(f"Iteration {iteration + 1}:")

    for i in my_list:
        if i == 'a':
            print("Approval needed for 'a' in Jenkins.")
            exit(100)  # Exit with status 100 for Jenkins to request approval
        else:
            print(f"'a' not found, found: {i}")

print("Python script completed after 10 iterations.")
