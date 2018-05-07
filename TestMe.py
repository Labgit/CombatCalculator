import Dice as d

d = d.Dice()

d.add(4)
d.add(4)
d.add(4)
d.add(4)

for x in range(1000):
    d.roll()

print("Count: " + str(d.count()))
print("Mean: " + str(d.mean()))
print("Mode: " + str(d.mode()))
print("Counts Per Outcome: " + str(d.countPerOutcome()))

import pyodbc
