def find_duplicate(nums):
    if len(nums) < 2:
        return False

    MIN_V = 1
    MAX_V = len(nums) - 1

    n = sorted(nums)

    for i in range(len(n) - 1):
        if not isinstance(n[i], int) or n[i] < MIN_V or n[i] > MAX_V:
            return False
        if n[i] == n[i+1]:
            return n[i]

    return False
