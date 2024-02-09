class Point:
    def __init__(self):
        self.res = []

    def get_res(self, *date):
        self.res.append(date)


obj = Point()
obj.get_res(1, 2, 3)
print(obj.get_res())
