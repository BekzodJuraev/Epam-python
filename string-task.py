def get_fractions(a_b: str, c_b: str) -> str:
    x=a_b.rsplit("/")
    y=c_b.rsplit("/")
    a=int(x[0])
    b=int(x[1])
    c=int(y[0])

    result=a+c

    return f"{a}/{b} + {c}/{b} = {result}/{b}"




