"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my honor, Daniela Gutierrez, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: adg4258
"""



def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if group_sum(start + 1, nums, target - nums[start]):
        return True
    return group_sum(start + 1, nums, target)


def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - nums[start])
    if group_sum_6(start + 1, nums, target - nums[start]):
        return True
    return group_sum_6(start + 1, nums, target)


def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if group_no_adj(start + 2, nums, target - nums[start]):
        return True
    return group_no_adj(start + 1, nums, target)


def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if nums[start] % 5 == 0:
        if start + 1 < len(nums) and nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target - nums[start])
        return group_sum_5(start + 1, nums, target - nums[start])
    if group_sum_5(start + 1, nums, target - nums[start]):
        return True
    return group_sum_5(start + 1, nums, target)

def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    i = start
    while i < len(nums) and nums[i] == nums[start]:
        i += 1
    clump_size = i - start
    if group_sum_clump(i, nums, target - nums[start] * clump_size):
        return True
    return group_sum_clump(i, nums, target)


def split_array_helper(start, nums, group1, group2):
    if start >= len(nums):
        return group1 == group2
    if split_array_helper(start + 1, nums, group1 + nums[start], group2):
        return True
    return split_array_helper(start + 1, nums, group1, group2 + nums[start])

def split_array(nums):  
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    return split_array_helper(0, nums, 0, 0)


def split_odd_10_helper(start, nums, group1, group2):
    if start >= len(nums):
        return group1 % 10 == 0 and group2 % 2 == 1
    if split_odd_10_helper(start + 1, nums, group1 + nums[start], group2):
        return True
    return split_odd_10_helper(start + 1, nums, group1, group2 + nums[start])

def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    return split_odd_10_helper(0, nums, 0, 0)


def split_53_helper(start, nums, group1, group2):
    # Base case: if we have processed all numbers, check if groups are equal
    if start >= len(nums):
        return group1 == group2
    # If the current number is divisible by 5, it must go into group1
    if nums[start] % 5 == 0:
        return split_53_helper(start + 1, nums, group1 + nums[start], group2) 
    # If the current number is divisible by 3 (but not 5), it must go into group2
    elif nums[start] % 3 == 0:
        return split_53_helper(start + 1, nums, group1, group2 + nums[start]) 
    # Otherwise, try putting the number in either group
    if split_53_helper(start + 1, nums, group1 + nums[start], group2):
        return True
    return split_53_helper(start + 1, nums, group1, group2 + nums[start])



def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    if not nums:
        return False
    return split_53_helper(0, nums, 0, 0)