class MaxHeap:
    def __init__(self):
        self.arr = []

    def __str__(self):
        return str(self.arr)

    def __len__(self):
        return len(self.arr)

    def peek(self):
        return self.arr[0]

    def push(self, num):
        self.arr.append(num)
        curr_index = len(self.arr)
        parent = self.get_parent(curr_index)
        while parent - 1 >= 0 and num > self.arr[parent - 1]:
            self.arr[parent - 1], self.arr[curr_index - 1] = self.arr[curr_index - 1], self.arr[parent - 1]
            curr_index = parent
            parent = self.get_parent(curr_index)

    def pop(self):
        if len(self.arr) == 0:
            return -1

        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[0]
        res = self.arr.pop()

        if len(self.arr) == 0:
            return res

        curr_index = 1
        max_child, is_left = self.get_children(curr_index)
        while self.arr[curr_index - 1] < max_child:
            if is_left:
                left = curr_index * 2
                self.arr[left - 1], self.arr[curr_index - 1] = self.arr[curr_index - 1], self.arr[left - 1]
                curr_index = left
            else:
                right = curr_index * 2 + 1
                self.arr[right - 1], self.arr[curr_index - 1] = self.arr[curr_index - 1], self.arr[right - 1]
                curr_index = right

            max_child, is_left = self.get_children(curr_index)

        return res

    def get_children(self, index):
        left = self.arr[index * 2 - 1] if index * 2 <= len(self.arr) else float("-inf")
        right = self.arr[index * 2 + 1 - 1] if index * 2 + 1 <= len(self.arr) else float("-inf")

        if left > right:
            return left, True
        else:
            return right, False

    def get_parent(self, index):
        return index // 2
