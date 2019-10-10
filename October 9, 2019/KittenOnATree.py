kitten_location = input()

branch_id = 0
branches_dict = {}
root = 10000
while branch_id >= 0:
    branch = input()
    if branch == "-1":
        break
    else:
        branches_array = branch.split(" ")
        if root == 10000:
            root = branches_array[0]
        for index, leaf in enumerate(branches_array):
            if index == 0:
                continue
            else:
                branches_dict[leaf] = branches_array[0]
        continue


path = kitten_location
last_branch = kitten_location
while not last_branch == root:
    last_branch = branches_dict[last_branch]
    path = path + " " + last_branch

print(path)