from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    array=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            array.append("FizzBuzz")
        elif i%3==0:
            array.append("Fizz")
        elif i%5==0:
            array.append("Buzz")

        else:
            array.append(i)


    return array








