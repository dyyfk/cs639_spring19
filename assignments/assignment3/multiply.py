import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function


def mapper(rec):
    if rec[0] == 'a':
        i = rec[1]
        val = rec[3]
        for j in range(5):
            mr.emit_intermediate((i, j), val)
    else:
        j = rec[2]
        val = rec[3]
        for i in range(5):
            mr.emit_intermediate((i, j), val)

        # Implement the REDUCE function


def reducer(key, list_of_values):
    sum = 0
    for i in range(5):
        j = i + 5
        sum += list_of_values[i] * list_of_values[j]
    mr.emit([key[0], key[1], sum])

    # Do not modify below this line
    # =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
