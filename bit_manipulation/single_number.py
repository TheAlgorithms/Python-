"""
    Given a non-empty array of integers nums, every element
    appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity
    and use only constant extra space.

    Reference: https://leetcode.com/problems/single-number/
"""


def single_number(nums: list) -> int:
    """
    :param nums: A non-empty array of any integers nums,
                 every element appears twice except for one.
    :return: element that appears only one time
    """
    result = 0

    for el in nums:
        result ^= el

    return result
