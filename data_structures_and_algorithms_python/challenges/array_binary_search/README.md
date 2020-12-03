# Binary Search

binary search is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array.


# Challenge

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.


# Approach & Efficiency

- first of all we have to find the array's length then get the **mid** by dividing it by 2
- we will use **while loop** in order to keep searching for the value
- if the value is bigger than the array's index it will return -1
- if rhe value is equal to **mid** then we will return it directly
- if rhe value is bigger thsn **mid** then we will decrease mid 
- if rhe value is less thsn **mid** then we will divide it by 2 

<img src= '/assets/binary_search2.jpg' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>



 
