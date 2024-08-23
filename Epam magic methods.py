class Counter:

    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        a = []
        for i in self.values:
            a.append(f'{i} {other}')
        return a

x = Counter([1,2,3])
print(x + "Mississippi")