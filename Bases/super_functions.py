#Takes a function and call  
def superFunction(function):
   print(function()) 

def sum():
   return 3+3

superFunction(sum)

#Lambdas
tuples = (1,2,3,4,5,2)
filteredTuple = tuple(sorted(lambda x: x == 2, tuples))

print(filteredTuple)

