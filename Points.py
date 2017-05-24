class Points:
    k = 0
    a = []

    def __init__(self, k):
        self.k = k

    def add(self, *coords):
        self.a.append(coords)

    def remove(self, *coords):
        for kort in self.a:
            if kort == coords:
                self.a.remove(kort)
                break

    def range_query(self, *coord_ranges):
        result = []
        for kort in self.a:
            ok = True
            for i in range(self.k):
                if kort[i] < coord_ranges[i][0] or kort[i] > coord_ranges[i][1]:
                    ok = False
                    break
            if ok:
                result.append(kort)
        return [c for c in self.a if coord_ranges[0] <= c <= coord_ranges[1]]


ps = Points(2)
ps.add(1, 1)
ps.add(3, 1)
print(list(ps.range_query((1, 3), (1, 1)))) # [(1, 1), (3, 1)]
ps.add(3, 1)
print(list(ps.range_query((2, 3), (1, 1)))) # [(3, 1), (3, 1)]
ps.remove(2, 1)
ps.remove(3, 1)
print(list(ps.range_query((1, 3), (1, 1)))) # [(1, 1), (3, 1)]
