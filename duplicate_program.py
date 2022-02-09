# Write a code that prints out the first occurrence of a duplicate in a given array of integers
# Sample Input: [1,2,3,2,1]
# Output: 2


def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate


print(find_first_duplicate( [1,2,3,2,1]))