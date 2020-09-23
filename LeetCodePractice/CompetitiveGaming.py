def num_players(arr, k):
    ranks = [0 for i in range(0, 101)]

    # Bucket sort
    for score in arr:
        ranks[score] += 1

    cur_rank = 1
    best_players = 0
    for i in range(100, -1, -1):
        if ranks[i] > 0:
            # If it's rank is too high
            if cur_rank > k:
                break

            cur_rank += ranks[i]
            best_players += ranks[i]

    return best_players


scores = [100]
k = -1
print(num_players(scores, k))
