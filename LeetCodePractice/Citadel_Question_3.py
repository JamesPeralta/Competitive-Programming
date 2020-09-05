from collections import deque


def dropped_requests(request_times):
    per_sec_queue = deque()
    per_ten_sec_queue = deque()
    per_sixty_sec_queue = deque()

    dropped = 0
    time = 1
    for req in request_times:
        # Clear queues as time progresses
        if req > time:
            # clear per_sec_queue
            for _ in range(len(per_sec_queue)):
                per_sec_queue.popleft()

            # clear per_ten_sec queue of anything older than i - 9
            while len(per_ten_sec_queue) > 0:
                if per_ten_sec_queue[0] < req - 9:
                    per_ten_sec_queue.popleft()
                else:
                    break

            # clear per_ten_sec queue of anything older than i - 9
            while len(per_sixty_sec_queue) > 0:
                if per_sixty_sec_queue[0] < req - 59:
                    per_sixty_sec_queue.popleft()
                else:
                    break
            time = req

        # Append requests to queue
        per_sec_queue.append(req)
        per_ten_sec_queue.append(req)
        per_sixty_sec_queue.append(req)

        # If any queues are overfilling drop the request
        if len(per_sec_queue) > 3 or len(per_ten_sec_queue) > 20 or len(per_sixty_sec_queue) > 60:
            dropped += 1

    return dropped


# requests = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
requests = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
ans = dropped_requests(requests)

print(ans)
