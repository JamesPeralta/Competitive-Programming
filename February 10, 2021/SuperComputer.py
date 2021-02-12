"""
N-bit memory

Flip the kth bit of memory
Count how many bits between l ar 3 are set to 1

k is the number of bits in memory

All bits are set to 0


"""
first_line = input()
bits, queries = first_line.split(" ")

bits = int(bits)
queries = int(queries)


set_bits = set()
for query in range(queries):
    line = input()
    command = line.split(" ")
    if command[0] == "F":
        to_set = int(command[1])
        if to_set in set_bits:
            set_bits.remove(to_set)
        else:
            set_bits.add(to_set)
    else:
        start = int(command[1])
        end = int(command[2])
        count = 0
        for key in set_bits:
            if start <= key <= end:
                count += 1
        print(count)
