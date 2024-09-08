'''" Define functions for as many cases as possible for each program. AT LEAST one function for each program is a must. For each program, you must define a function, _test(), with assert statements that check the correctness of each function. TAs will evaluate if you have used any test function with assert or not, and accordingly assign a score. It will be counted towards final evaluation.

(Note: Use of list / dictionary / sorting not allowed. )

You are given F(1) = 1, F(2) = 1, F(3) = 2

For a given input n, generate F(n) such that

F(n) = F(n−1) + F(n−2) + F(n−3)

(Not allowed to use any data structure like list tuples) .
Output the value as the answer .

Input Format

First line contains a single integer n .

Constraints

1 <= n <= 10**6

Output Format

First line of the output contains a single integer x which is the value of F(n) '''



def num1(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n==3:
        return 2
    else:
        a,b,c=1,1,2
        s=c
        for i in range(4,n+1):
            s=s+a+b
            a=b
            b=c
            c=s
        return s
    
def _test():
    assert num1(7)==24
    assert num1(6)==13
    assert num1(10)==149
    
_test()    
n=(int)(input())
print(num1(n))
