import MapReduce
import sys

"""
JOIN in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function


def mapper(rec):
    mr.emit_intermediate(rec[1], rec)

# Implement the REDUCE function


def reducer(key, list_of_values):
    left = []
    right = []
    for v in list_of_values:
        if v[0] == 'order':
            left.append(v)
        if v[0] == 'line_item':
            right.append(v)
    for i in left:
        for j in right:
            res = []
            for k in i:
                res.append(k)
            for m in j:
                res.append(m)
            mr.emit(res)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
