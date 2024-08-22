from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    tuple_1=()
    while num > 1:
        x = num % 10
        num = num / 10
        tuple_1+=(int(x),)
    return tuple_1[::-1]


print(get_tuple(35015))




