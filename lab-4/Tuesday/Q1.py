'''You are given a number. Convert the number to its binary representation and return the number.

Process

Divide the number by 2 and preserve the remainder and the quotient. The remainder becomes the first (ones) digit of the binary representation.
Repeatedly divide the quotient by 2 until it becomes 0, add the remainder as the next digits (tens, hundreds, thousand, …).
Report the binary representation constructed using remainders.
Refer to the sample test cases for detailed working of the test case.

Use of string and any other data structure is not allowed.

Use of any inbuilt library is not allowed.

Input Format

A single line integer input n

Constraints

0 <= n <= 1012

Output Format

Binary representation of the number

Sample Input 0

13
Sample Output 0

1101'''

def binnum(n):
    s=1
    while n!=0:
        r=n%2
        if r==0:
            s=s*10
        else:
            s=s*10+r
        n=n//2
        
    s1=0
    while s!=0:
        a=s%10
        s1=s1*10+a
        s=s//10
    return (s1//10)

def _test():
    assert binnum(25)==10001
    assert binnum(100)==1000100

n=int(input())
print(binnum(n))