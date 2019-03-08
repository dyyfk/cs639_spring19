import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function


def mapper(rec):
    mr.emit_intermediate(rec[0], rec[1])


def reducer(key, list_of_values):
    mr.emit([key, len(list_of_values)])


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
