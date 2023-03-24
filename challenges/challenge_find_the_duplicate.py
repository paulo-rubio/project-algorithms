def find_duplicate(nums):
    if len(nums) < 2:
        return False

    MIN_VALUE = 1
    MAX_VALUE = len(nums) - 1

    nums_sorted = sorted(nums)

    for i in range(len(nums_sorted) - 1):
        if not isinstance(nums_sorted[i], int) or nums_sorted[i] < MIN_VALUE or nums_sorted[i] > MAX_VALUE:
            return False
        if nums_sorted[i] == nums_sorted[i+1]:
            return nums_sorted[i]

    return False
