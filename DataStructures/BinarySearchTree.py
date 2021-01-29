import random


class Node:
    def __init__(self, val=float("inf"), left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            prev, curr = None, self.root
            while curr:
                prev = curr
                if val <= curr.val:
                    curr = curr.left
                else:
                    curr = curr.right

            if val <= prev.val:
                prev.left = Node(val)
            else:
                prev.right = Node(val)

    def search(self, val):
        curr = self.root
        steps = 0
        while curr:
            if curr.val == val:
                print("FOUND", steps)
                return curr.val
            elif val <= curr.val:
                curr = curr.left
            else:
                curr = curr.right
            steps += 1

        print("NOT FOUND", steps)
        return float("inf")

    def delete(self, val):
        self.delete_node(self.root, val)

    def delete_node(self, node, val):
        if node is None:
            print("Node not found: ", val)
            return None
        elif node.val == val and node.left is None and node.right is None:
            print("Node deleted: ", val)
            return None

        if node.val == val:
            if node.right:
                succ = self.get_successor(node)
                node.val, succ.val = succ.val, node.val
                node.right = self.delete_node(node.right, val)
            else:
                pred = self.get_predecessor(node)
                node.val, pred.val = pred.val, node.val
                node.left = self.delete_node(node.left, val)
        elif val < node.val:
            node.left = self.delete_node(node.left, val)
        else:
            node.right = self.delete_node(node.right, val)

        return node

    def get_successor(self, node):
        succ = node.right
        while succ.left:
            succ = succ.left

        return succ

    def get_predecessor(self, node):
        pred = node.left
        while pred.right:
            pred = pred.right

        return pred

    def inorder(self):
        result = []
        self.inorder_recurse(self.root, result)
        return result

    def inorder_recurse(self, node, result):
        if node is None:
            return

        self.inorder_recurse(node.left, result)
        result.append(node.val)
        self.inorder_recurse(node.right, result)
        return

    def validate_bst(self):
        return self.validate_recurse(self.root, float("-inf"), float("inf"))

    def validate_recurse(self, node, low, high):
        if node is None:
            return True

        return low < node.val <= high and self.validate_recurse(node.left, low, node.val) and self.validate_recurse(node.right, node.val, high)


def __testbst__():
    bst = BST()

    populated = []
    for i in range(15):
        new_num = random.randint(-100, 100)
        bst.insert(new_num)
        populated.append(new_num)

    print(populated)
    print(bst.inorder(), bst.validate_bst())
    while True:
        val = input("Delete Mode: ")
        if val == "q":
            break

        print(bst.delete(int(val)))
        print(bst.inorder(), bst.validate_bst())


__testbst__()
