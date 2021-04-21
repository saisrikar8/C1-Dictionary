'''
03/08/2021

Review

List:
mutable, []

List functions

  LIST.insert(INDEX, ELEMENT)
  LIST.append(ELEMENT)
  LIST.remove(ELEMENT)
  LIST.pop(INDEX)

LIST[INDEX] = ELEMENT

Tuple
immutable, ()


___________________________________________________

Dictionary
Another type of list, stores data/values inside the curly brackets, {}.
Similar to a list, it is mutable, however the index is a key, which is liked to data/values.

Ex.
student = {}
student["name"] = "John"
student["age"] = 12
student["weight"] = "120lbs"
student["school"] = "Evergreen"
student["Python"] = True
print(student["age"])
print(student["weight"])
print(student["Python"])


Time
Handles time-related tasks

Formula

import time # Importing the time library

Useful Time functions
1. time.time()
  - returns floating-point numbers in seconds passed since epoch(Jan. 1st 1970, 00:00 UTC)
  - Use it for Date arthmetic (etc. duration)

  import time
  print (time.time())

2. time.sleep(NUMBER)
  - Suspends(delays) execution of the current thread for the given number of seconds
  import time
  for x in range(10):
    print(str(x) + " seconds has passed")
    time.sleep(60)

'''


# Exercise 1
'''
Expected output:
*
*  *
*  *  * 
*  *  *  *
*  *  *  *  *

'''
print("Exercise 1")
for x in range(5):
  print("*  " * (x + 1))

# Exercise 2
'''
Expected output:
*  *  *  *  *
*  *  *  *
*  *  * 
*  *
*
'''
print("\nExercise 2")
for i in range(5):
  print("*  " * (5 - i))

#Exercise 3
'''
            *
         *  *
      *  *  * 
   *  *  *  *
*  *  *  *  *

'''
print("\nExercise 3")
for y in range(5):
  print(" " * 3 * (4 - y) + "*  " * (y+1))

#Exercise 4
print("\nExercise 4")
'''
*  *  *  *  *
   *  *  *  *
      *  *  *
         *  *
            *

'''

for z in range(5):
  print(" " * 3 * z + "*  " * (5 - z))