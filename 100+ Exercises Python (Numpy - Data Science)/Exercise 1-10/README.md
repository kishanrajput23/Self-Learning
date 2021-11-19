# 📌 Exercise 1
## Check if all elements from the following arrays return the logical value True:

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])
 
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])
 
C = np.array([[True, False, False],
              [True, True, True]])
 
D = np.array([0.1, 0.3])

**Tip: Use the function np.all()**

### Expected result:

**A: True\
B: False\
C: False\
D: True**


# 📌 Exercise 2
## Check if all elements from the following arrays return the logical value True along the axis with index 1:



A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])
 
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])
 
C = np.array([[True, False, False],
              [True, True, True]])

**Tip: Use the function np.all() with the axis argument.**

### Expected result:

**A: [ True  True]\
B: [ True False]\
C: [False  True]**
