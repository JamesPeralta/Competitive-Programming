def device_pairs(deviceCapacity, foregroundAppList, backgroundAppList):
    foregroundAppList = sorted(foregroundAppList, key=lambda x: x[1])
    backgroundAppList = sorted(backgroundAppList, key=lambda x: x[1])

    best_list = []
    optimal = float("-inf")
    for foreground_app in foregroundAppList:
        foreground_id = foreground_app[0]
        foreground_mem = foreground_app[1]

        index = len(backgroundAppList) - 1
        while index >= 0:
            background_id = backgroundAppList[index][0]
            background_mem = backgroundAppList[index][1]
            if background_mem + foreground_mem > deviceCapacity:
                index -= 1
            elif background_mem + foreground_mem > optimal:
                optimal = background_mem + foreground_mem
                best_list = [[foreground_id, background_id]]  # Clear best list
                index -= 1
            elif background_mem + foreground_mem == optimal:
                best_list.append([foreground_id, background_id])
                index -= 1
            else:
                break

    if optimal == float('-inf'):
        return [()]

    return best_list


# capac = 10
# foreground = [[4, 10], [1, 3], [2, 5], [3, 7]]
# background = [[4, 5], [1, 2], [2, 3], [3, 4]]
# capac = 7
# foreground = [[1, 2], [2, 4], [3, 6]]
# background = [[1, 2]]
# capac = 16
# foreground = [[2, 7], [3, 14]]
# background = [[2, 10], [3, 14]]
capac = 20
foreground = [[3, 14], [1, 8], [2, 7]]
background = [[1, 5], [2, 10], [3, 14]]
print(device_pairs(capac, foreground, background))