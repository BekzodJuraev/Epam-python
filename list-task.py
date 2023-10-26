from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    # TODO: Add your code here
    array=[]
    for i in str_list:
        if i not in array:
            array.append(i)
    array.sort()
    return array



