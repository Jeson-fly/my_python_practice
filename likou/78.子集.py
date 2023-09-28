from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        暴力方法
        """
        res = []
        for i in range(len(nums)):
            if not res:
                res.append([])
                res.append([nums[i]])
            else:
                tmp = []
                for cur in res:
                    tmp.append(cur + [nums[i]])
                res.extend(tmp)
        return res


if __name__ == '__main__':
    s = Solution()
    cases = [
        [1, 2, 3]
    ]
    # for case in cases:
    #     s.subsets(case)
    s = set()
    s.add(1)
    print(bool(s))
