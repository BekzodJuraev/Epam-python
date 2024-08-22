def generate_squares(x):
    square=1
    dic={}
    for item in range(1,x+1):
        square=item*item
        dic[item]=square

    return dic



print(generate_squares(5))