# python_repo

partition.py determines whether the given list of integers can be divided into two lists whose sums are equal.

Time complexity here is O(n^2) as the loop runs n + (n-1) + (n-2) .... + (n-n) times

To reduce the execution time i've used nested loops instead of recursive function

Time complexity for the recursive function solution is O(2^n) and the execution time is considerably high.
