from typing import List


def foo(nums: List[int]) -> List[int]:
    result=1
    list=[]
    for i in nums:
        result*=i

    for i in nums:
        list.append(int(result/i))

    return list



