'''Define functions for as many cases as possible for each program. AT LEAST one function for each program is a must.
For each program, you must define a function, _test(), with assert statements that check the correctness of each function. TAs will evaluate if you have used any test function with assert or not, and accordingly assign a score. It will be counted towards final evaluation.
The following iterative sequence is defined for the set of positive integers:

n = n / 2 if n is even

and n = 3 * n + 1 if n is odd

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. Which starting number, <= N produces the longest chain? If many possible such numbers are there print the maximum one.

Use of lists and any other data structures is not allowed

Input Format

A single line integer n

Constraints

1 <= n <= 1000

Output Format

A single line integer representing the starting number which generates the longest sequence.

For example, when n = 10, we see that the collatz sequence for 9 is the longest sequence possible.

Collatz sequence for n = 9:

9 -> 28 -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

containing 19 steps. '''

def num(n):
    c=0
    while n>1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        c=c+1
    return c

n=(int)(input())
s=0
a=0
for i in range(1,n+1):
    if num(i)>=s:
        s=num(i)
        a=i
print(a)
    