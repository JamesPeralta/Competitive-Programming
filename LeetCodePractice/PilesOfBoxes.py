def piles_of_boxes(boxes):
    boxes = sorted(boxes, reverse=True)

    index = 0
    same_level = 1
    maximum = boxes[0]
    steps = 0
    while index + 1 < len(boxes):
        if boxes[index + 1] == maximum:
            same_level += 1
        else:
            steps += same_level
            maximum = boxes[index + 1]
            same_level += 1

        index += 1

    return steps


# arr = [1, 3, 5]
# arr = [2]
arr = [2, 3, 3]
print(piles_of_boxes(arr))
