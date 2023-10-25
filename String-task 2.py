def get_longest_word( s: str) -> str:
    string=s.rsplit(" ")
    x=""

    for i in string:
        if len(i)>len(x):
            x=i
    return x





