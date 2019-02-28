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
  a = []
  for i in list_of_values:
    if(i[0]=='line_item'):
      

      
    else:
      a.append(i)

    # for j in i:
    # mr.emit(a) 

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
