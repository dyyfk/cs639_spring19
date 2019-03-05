import MapReduce
import sys

"""
Assymetric Relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function


def mapper(rec):
    mr.emit_intermediate(rec[0], rec[1])
    mr.emit_intermediate(rec[1], (rec[1], rec[0]))
    # Implement the REDUCE function


def reducer(key, list_of_values):
    rels = []
    mentioned = []
    for i in list_of_values:
        if isinstance(i, tuple):
            rels.append(i[1])
        else:
            mentioned.append(i)
    for i in rels:
        if i not in mentioned:
            mr.emit([key, i])


    # Do not modify below this line
    # =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
