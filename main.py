def has_subsequence_summing_to_target(nums, target):
    """
    Returns True if there's a subsequence of consecutive numbers in nums
    that sums up to target, otherwise False.
    """
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == target:
                return True
            if current_sum > target:
                break
    return False

# Test
nums = [1, 2, 3, 4, 5]
target = 9
print(has_subsequence_summing_to_target(nums, target))  # True, because 2 + 3 + 4 = 9
nums = [1, 4, 3, 5]
target = 9
print(has_subsequence_summing_to_target(nums, target))  # False