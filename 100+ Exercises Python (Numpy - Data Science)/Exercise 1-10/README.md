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


# 📌 Exercise 3
## Check if any element of the following arrays returns the logical value True:

A = np.array([[0, 0, 0],
              [0, 0, 0]])
 
B = np.array([[0, 0, 0],
              [0, 1, 0]])
 
C = np.array([[False, False, False],
              [True, False, False]])
 
D = np.array([[0.1, 0.0]])

**Tip: Use the np.any() function.**

### Expected result:

**A: False\
B: True\
C: True\
D: True**


# 📌 Exercise 4
## Check if any element of the following arrays returns the logical value True along the axis with index 0:

A = np.array([[0, 0, 0],
              [0, 0, 0]])
 
B = np.array([[0, 0, 0],
              [0, 1, 0]])
 
C = np.array([[False, False, False],
              [True, False, False]])
 
D = np.array([[0.1, 0.0]])

**Tip: Use the np.any() function with the axis argument.**

### Expected result:

**A: [False False False]\
B: [False  True False]\
C: [ True False False]\
D: [ True False]**


# 📌 Exercise 5
## Check if the following array has missing data (np.nan):

A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

**Tip: Use the np.isnan() function.**

### Expected result:

**[[False False False  True]\
 [False  True False False]]**
