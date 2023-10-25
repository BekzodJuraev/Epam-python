from typing import Union

NumType = Union[int, float]


def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
    result = (12 * a + 25 * b) / (1 + a ** (2 ** b))

    # add your code here
    return round(result,2)



print(some_expression_with_rounding(1.4,2.55))

