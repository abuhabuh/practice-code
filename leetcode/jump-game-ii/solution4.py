"""
Approach:
    Assume 1 hop and look for route
    Assume 2 hops and look for route
    Assume 3 hops and look for route
    ...

Optimized approach, but still not fast enough for an even bigger data set.
Fucking leetcode...
"""
import pdb
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0

        # don't look back further than the biggest number
        # TODO: this was a cheap hack and falls apart when numbers are large
        max_lookback = max(nums)

        # paths through master list composed of indexes
        paths: List[List] = [[len(nums)-1]]

        while True:

            new_paths = {}
            while paths:
                """
                For each path, take the lowest indexed "stop" on the path and
                create a new path for any lower indexed "stops" that can reach
                it
                """
                path = paths.pop()
                target_idx = path[-1]
                # iterate through all ower "stops"
                i = max(0, target_idx - max_lookback)
                while i < target_idx:
                    if i + nums[i] >= target_idx:
                        if i == 0:
                            return len(path)

                        # This "stop" can reach the target in 1 step so append
                        # a new path
                        if i not in new_paths:
                            new_paths[i] = path + [i]
                        else:
                            if len(path) + 1 < len(new_paths[i]):
                                new_paths[i] = path + [i]

                    i += 1
            for _, path in new_paths.items():
                paths.append(path)



print(f'******** RUNNING TESTS')

s = Solution()

input_list = [2,3,1,1,4]
expected = 2
res = s.jump(input_list)
assert res == expected, f'{res} is not min number of jumps'
input_list = [1,2]
expected = 1
res = s.jump(input_list)
assert res == expected, f'{res} is not min number of jumps'
input_list = [3,2,1]
expected = 1
res = s.jump(input_list)
assert res == expected, f'{res} is not min number of jumps'
input_list = [1]
expected = 0
res = s.jump(input_list)
assert res == expected, f'{res} is not min number of jumps'
input_list = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
expected = 13
res = s.jump(input_list)
assert res == expected, f'{res} is not min number of jumps'
input_list = [8,4,8,2,5,6,5,3,5,3,3,1,6,5,8,7,4,6,8,2,3,1,2,7,5,1,2,1,8,1,3,3,7,8,8,4,2,6,5,1,7,5,6,8,2,7,5,6,7,2,2,5,7,4,4,6,8,7,2,4,8,5,2,3,6,3,5,1,6,8,3,1,7,7,1,8,2,3,5,8,6,5,3,4,1,8,7,3,7,2,1,1,2,8,5,1,8,3,5,5,3,3,8,8,1,6,1,8,5,1,1,6,6,1,8,4,2,3,4,6,4,8,6,7,8,6,2,3,2,6,7,1,3,4,1,5,5,3,6,5,1,5,5,1,1,1,4,2,5,2,6,1,5,3,5,3,7,6,7,7,1,1,6,3,5,2,6,7,5,8,2,1,2,1,4,7,3,6,7,2,7,1,6,4,4,6,6,6,6,3,4,5,5,1,5,3,5,7,3,4,5,3,1,3,7,6,2,2,5,7,7,6,3,4,2,5,4,1,3,3,6,2,1,1,3,5,7,4,5,4,8,4,5,7,6,7,5,5,5,4,1,6,1,6,6,3,1,8,6,3,8,5,8,7,6,8,4,5,1,5,7,7,1,3,5,5,4,1,4,8,2,5,5,6,3,4,8,1,5,4,1,8,2,6,5,4,8,8,5,7,1,8,4,1,5,5,7,1,6,5,8,4,3,3,8,7,1,4,3,1,4,5,2,7,8,3,4,4,6,7,7,5,4,3,2,4,2,5,2,6,8,8,2,7,8,2,6,8,5,6,3,3,4,2,3,1,4,1,8,8,2,5,2,1,5,8,2,8,2,4,6,8,6,6,6,5,6,8,5,7,2,1,5,2,8,8,7,1,1,5,2,5,6,6,3,8,3,5,6,4,5,7,8,2,6,7,4,5,7,3,8,2,4,5,1,8,7,5,2,8,1,7,1,3,1,1,4,4,1,1,3,3,3,8,1,8,4,5,4,7,1,1,2,6,7,5,8,8,1,3,8,2,7,4,8,8,1,2,5,5,5,7,4,2,2,4,6,7,6,4,3,5,8,1,7,6,6,2,1,6,2,5,2,8,3,3,5,7,2,1,8,5,5,6,8,8,8,8,1,3,5,2,1,6,3,8,4,7,8,2,8,4,2,4,8,4,2,4,6,3,7,2,1,3,5,2,5,4,7,8,7,6,3,3,7,6,2,4,6,7,8,6,6,4,2,8,7,5,5,8,8,8,1,2,6,1,8,1,1,4,2,7,8,5,6,4,7,3,7,3,2,6,5,7,8,5,1,3,3,3,6,8,7,3,3,4,7,5,8,2,4,7,8,1,6,8,7,5,4,2,3,3,8,8,6,3,8,2,8,6,2,2,5,8,3,7,5,8,5,7,2,7,1,7,2,3,1,1,8,2,4,8,8,1,2,1,2,2,8,6,6,5,1,1,1,5,1,8,5,6,1,4,4,8,5,8,3,3,3,5,2,5,3,7,3,5,4,3,2,4,8,7,6,4,4,4,3,8,7,8,2,4,6,5,6,3,4,5,3,2,6,6,7,2,5,1,5,6,2,3,4,3,3,3,3,2,4,3,7,1,3,5,3,2,5,5,7,6,1,2,3,2,3,8,3,6,7,4,3,8,3,7,2,7,5,2,6,8,2,5,1,2,8,7,8,3,1,1,7,3,6,5,7,2,8,3,3,7,2,3,7,6,1,8,4,5,3,3,8,5,1,1,7,3,6,1,7,6,2,2,6,1,6,8,1,7,4,1,3,4,6,6,4,4,3,4,4,7,5,2,2,8,7,6,5,4,3,2,8,8,2,1,3,5,7,5,2,4,7,2,2,8,3,8,7,4,8,5,3,3,5,5,2,1,7,6,7,1,3,3,2,2,8,8,6,2,8,3,2,3,8,6,4,7,7,8,2,3,6,4,8,3,3,2,1,7,6,3,8,4,8,3,1,6,3,1,2,8,8,2,2,7,2,5,7,3,5,8,8,3,8,6,6,2,6,6,4,7,6,1,7,8,6,8,1,2,3,3,6,2,7,1,2,1,1,6,8,6,6,1,2,6,8,2,4,7,1,1,3,3,7,4,8,3,4,6,3,6,1,6,4,3,6,7,4,8,5,7,2,3,1,5,3,5,3,3,3,6,8,6,6,8,3,8,3,6,2,6,4,1,6,8,1,1,6,6,6,3,6,4,7,1,1,4,2,5,5,8,2,6,8,1,7,5,4,7,4,7,3,1,5,7,1,5,1,1,8,2,2,3,3,4,3,7,6,1,7,2,8,5,6,5,4,8,2,4,3,1,2,7,3,3,3,3,4,6,2,1,4,8,1,4,3,2,7,6,8,8,7,2,3,1,4,1,3,3,8,8,6,2,3,3,7,3,1,5,5,2,8,8,3,7,7,7,7,3,7,3,7,4,5,5,8,4,8,1,4,3,7,8,5,7,1,6,2,4,3,6,5,7,2,7,5,1,1,6,3,3,7,7,7,4,6,7,2,3,2,8,5,7,8,7,2,7,7,8,7,3,4,4,5,3,6,2,2,1,4,8,5,1,2,8,4,7,8,2,1,4,4,6,5,6,2,2,6,3,1,8,1,3,3,3,8,1,3,7,7,5,8,3,7,3,8,3,7,8,2,1,4,4,2,7,3,8,1,8,4,8,8,6,6,8,5,2,6,2,3,6,1,5,2,4,6,5,6,8,3,8,2,1,8,6,8,3,2,4,3,4,7,5,6,6,6,4,8,1,5,6,1,1,2,6,4,3,2,1,2,4,1,4,4,8,2,8,8,2,1,2,4,4,5,1,5,5,6,2,4,8,4,7,3,4,2,5,7,7,3,5,5,8,5,7,5,4,4,6,5,6,5,2,5,7,4,3,5,8,3,7,3,7,3,7,5,8,4,3,3,4,6,1,3,3,6,2,4,5,4,4,8,4,6,5,1,1,2,4,7,3,8,8,1,2,3,6,7,7,4,5,3,5,7,3,4,8,8,6,6,2,3,3,8,3,1,3,3,2,8,3,5,7,2,6,2,7,3,3,3,7,5,1,2,7,8,4,7,1,4,6,5,1,2,6,3,7,7,5,4,8,7,1,1,7,2,4,7,8,5,2,6,6,5,4,8,6,1,4,5,5,3,7,4,4,2,3,6,8,6,8,4,1,8,2,3,8,3,1,6,2,8,6,1,4,3,4,8,6,6,5,8,7,4,2,1,3,7,6,7,1,3,2,2,8,1,5,2,6,7,8,2,8,5,2,3,7,7,6,8,3,4,6,8,2,8,7,1,4,1,3,6,1,8,2,8,6,8,7,1,2,5,6,5,3,4,7,5,3,4,8,4,8,3,2,7,7,6,2,4,8,1,1,2,8,6,6,2,2,4,3,8,6,7,7,1,8,7,2,2,3,2,4,1,2,6,3,6,8,5,1,6,4,7,4,2,4,5,6,8,3,7,1,5,2,8,1,2,6,3,5,4,3,3,8,2,7,1,2,1,1,8,7,6,3,8,2,8,4,2,1,1,2,3,8,8,6,5,4,1,5,5,7,8,2,8,6,6,3,7,1,5,2,2,5,2,6,5,7,3,2,8,7,8,3,7,6,5,6,7,3,4,1,3,2,3,6,4,6,1,1,8,3,2,2,1,1,4,3,4,6,6,2,8,1,6,6,1,1,6,8,8,6,4,8,3,4,5,5,5,8,8,5,8,2,1,4,6,6,7,3,6,8,4,3,4,6,3,7,8,6,1,7,1,5,1,1,6,3,3,3,7,4,1,3,1,5,1,5,4,3,4,4,6,2,3,8,0,0,0,0,0,0,0]
expected = 284
res = s.jump(input_list)
assert res == expected, f'{res} is not min number of jumps'
