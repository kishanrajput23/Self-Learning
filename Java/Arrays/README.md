# Arrays Assignment Questions 

**📌1.** Write a program to initialize an integer array and print the sum and average of the array.

**📌2.** Write a program to initialize an integer array and find the maximum and minimum value of an array.

**📌3.** Write a program to initialize an integer array with values and check if a given number is present in the array or not. If the number is not found, it will print -1 else it will print the index value of the given  number in the array.
```
Ex1) Array elements are {1,4,34,56,7} and the search element is 90 then the O/P : -1

Ex2) Array elements are {1,4,34,56,7} and the search element is 56 then the O/P : 4 
```

**📌4.** Initialize an integer array with ascii values and print the corresponding character values in a single row.

**📌5.** Write a program to find the largest 2 numbers and the smallest 2 numbers in the given array.

**📌6.** Write a program to initialize an array and print them in a sorted order.

**📌7.** Write a program to remove the duplicate elements in an array and print new array.
```
Eg) Array Elements--> {12,34,12,45,67,89} 
O/P: 12,34,45,67,89
```

**📌8.** Write a program to print the sum of the elements of an array following the given below condition. If the array has 6 and 7 in succeeding orders, ignore the numbers between 6 and 7 and consider the other numbers for calculation of sum. 
```
Eg1) Array Elements - 10,3,6,1,2,7,9 
O/P: 22 [i.e 10+3+9] 

Eg2) Array Elements - 7,1,2,3,6 
O/P: 19 

Eg3) Array Elements - 1,6,4,7,9 
O/P: 10	
```

**📌9.** Print a version of the given array where all the 10's have been removed. The remaining elements should shift left towards the start of the array as needed, and the empty spaces at the end of the array should be 0. So {1, 10, 10, 2} yields {1, 2, 0, 0}. You may modify and display the given array or make a new array. 
```
withoutTen([1, 10, 10, 2]) --> [1, 2, 0, 0] 

withoutTen([10, 2, 10]) --> [2, 0, 0] 

withoutTen([1, 99, 10]) --> [1, 99, 0]
```

**📌10.** Print an array that contains the exact same numbers as the given array, but rearranged so that all the even numbers come before all the odd numbers. Other than that, the numbers can be in any order. You may modify and return the given array, or make a new array.
```
evenOdd({1, 0, 1, 0, 0, 1, 1}) → {0, 0, 0, 1, 1, 1, 1}

evenOdd({3, 3, 2}) → {2, 3, 3}

evenOdd({2, 2, 2}) → {2, 2, 2}
```

**📌11.** Write a program for Given an array of type int, print true if every element is 1 or 4.
```
only14([1, 4, 1, 4]) true

only14([1, 4, 2, 4]) - false

only14(01. 11) - true
```

**📌12.** Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
```
middleWay({1, 2, 3}, {4, 5, 6}) → {2, 5}

middleWay({7, 7, 7}, {3, 8, 0}) → {7, 8}

middleWay({5, 2, 9}, {1, 4, 5}) → {2, 4}
```

**📌13.** Write a program to reverse the elements of a given 2x2 array. Four Four integer numbers needs to be passed as Command Line arguments 

```
Example1:
     C:\>java Sample 1 2 3
     O/P Expected : Please enter 4 integer numbers

Example2:
     C:\>java Sample 1 2 3 4
     O/P Expected : 
     
  The given array is :
  1 2 
  3 4 

  The reverse of the array is :
  4 3 
  2 1
```
	
**📌14.** Write a program to find greatest number in a 3x3 array. The program is supposed to receive 9 integer numbers as command line arguments.

```
Example1:
     C:\>java Sample 1 2 3
     O/P Expected : Please enter 9 integer numbers

Example2:
     C:\>java Sample 1 23 45 55 121 222 56 77 89
     O/P Expected : 

The given array is :
1 23 45 
55 121 222 
56 77 89 

The biggest number in the given array is 222
```
