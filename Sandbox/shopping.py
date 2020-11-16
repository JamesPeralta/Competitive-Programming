from collections import defaultdict


def getMinScore(products_nodes, products_edges, products_from, products_to):
    adjacency_list = defaultdict(set)
    for node_one, node_two in zip(products_from, products_to):
        adjacency_list[node_one].add(node_two)
        adjacency_list[node_two].add(node_one)

    all_trios = set()
    for node in range(1, product_nodes + 1):
        find_trio(adjacency_list, node, set(), all_trios)

    all_trios = list(all_trios)
    minimium = float("inf")
    for trio in all_trios:
        total_sum = 0
        for node in trio:
            total_sum += len(adjacency_list[node] - set(trio))

        minimium = min(minimium, total_sum)

    print(all_trios)
    if minimium == float("inf"):
        return -1
    else:
        return minimium


def find_trio(adjacency_list, node, path, all_trios):
    if len(path) == 3:
        if valid_trio(adjacency_list, path):
            sorted_path = sorted(list(path))
            path_arr = tuple(sorted_path)
            if path_arr not in all_trios:
                all_trios.add(path_arr)
        return

    for neighb in adjacency_list[node]:
        if neighb in path:
            continue

        path.add(neighb)
        find_trio(adjacency_list, neighb, path, all_trios)
        path.remove(neighb)


def valid_trio(adjacency_list, trio):
    for node_one in trio:
        for node_two in trio:
            if node_one == node_two:
                continue

            if node_two not in adjacency_list[node_one]:
                return False

    return True


# product_nodes = 6
# product_edges = 6
# products_from = [1, 2, 2, 3, 4, 5]
# products_to = [2, 4, 5, 5, 5, 6]
# product_nodes = 5
# product_edges = 6
# products_from = [1, 1, 2, 2, 3, 4]
# products_to = [2, 3, 3, 4, 4, 5]
# product_nodes = 5
# product_edges = 6
# products_from = [1, 1, 2, 2, 3, 4]
# products_to = [2, 3, 3, 4, 4, 5]
product_nodes = 5
product_edges = 6
products_from = [2, 2, 3, 3, 3, 4, 4, 5, 6, 6]
products_to = [1, 3, 1, 4, 6, 1, 5, 6, 1, 2]
print(getMinScore(product_nodes, product_edges, products_from, products_to))