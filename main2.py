import numpy as np

data=[("name","S15"),("class",int),("height",float)]
detail=[("James",5,48.5),("Sirius",6,53.4),("Peter",5,44.6),("Remus",5,56.4)]
students=np.array(detail,dtype=data)
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students,order="height"))