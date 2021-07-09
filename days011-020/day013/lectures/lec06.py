# Use a Debugger
# The append is only executed once since is outside the for loop.
# Add a breakpoint on line 7, then run the debugger.
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# Fixing it...
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
