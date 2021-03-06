def longest_increasing_subsequence(sequence):
    """
    Returns the length of the longest increasing non-contiguous sequence
    """
    length = len(sequence)
    counts = [1 for _ in range(length)]

    for i in range(1, length):
        for j in range(0, i):
            if sequence[j] < sequence[i]:
                counts[i] = max(counts[i], counts[j] + 1)
                print("counts[" + str(i) + "]:", counts[i])
            else:
                print("counts[" + str(i) + "]:", counts[i])

    return max(counts)


sequence = [1, 101, 10, 2, 3, 100, 4, 6, 2]
print("sequence:", sequence)

result = longest_increasing_subsequence(sequence)
print("result:", result)

sequence = [3, 10, 2, 1, 20]
print("sequence:", sequence)

result = longest_increasing_subsequence(sequence)
print("result:", result)

