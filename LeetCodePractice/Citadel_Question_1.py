import collections
"""
Bids have the form:
   [User_id, Num_of_shares, Bidding_price, Timestamp]
"""
bids = [[1, 5, 5, 0],
        [2, 7, 8, 1],
        [3, 7, 5, 1],
        [4, 10, 3, 3]]


# Return bidders who didn't receive shares in non-decreasing order
# Allocate the N shares to the bidders and return the losers
def get_losers(bidders, n):
    shares_left = n

    # The number of people who bid for a given price
    ties = collections.Counter([row[2] for row in bidders])

    bidders.sort(reverse=True, key=lambda x: x[2])

    index = 0
    winners = []
    losers = []
    while index < len(bidders):
        # Get the group of bidders that bid the same price if any
        start = index
        end = index + ties[bidders[index][2]]
        bid_group = bidders[start: end][:]

        bid_group.sort(key=lambda x: x[3])
        for bid in bid_group:
            # Add the rest of this group to the losers
            if shares_left <= 0:
                losers.append(bid[0])
            else:
                winners.append(bid[0])
                shares_left -= bid[1]

        # if somebody is a loser, the rest are losers too
        if len(losers) > 0:
            for bid in bidders[end:]:
                losers.append(bid[0])
            break

        index = end

    return sorted(losers)


print(get_losers(bids, 0))
