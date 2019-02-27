import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    title = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, title)



# Implement the REDUCE function
def reducer(key, list_of_values):
    a = []
    for v in set(list_of_values):
      a.append(v)
    mr.emit((key, a))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
