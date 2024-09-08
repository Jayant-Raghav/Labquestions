'''Define functions for as many cases as possible for each program. AT LEAST one function for each program is a must. For each program, you must define a function, _test(), with assert statements that check the correctness of each function. TAs will evaluate if you have used any test function with assert or not, and accordingly assign a score. It will be counted towards final evaluation.

(Note: Use of list / dictionary / sorting not allowed. )

This is the sequence generator question with some set of rules to be followed . Take any 4 digit number which has atleast 2 different digits as input . Follow , the following steps :

First arrange the digits in ascending order creating a number x(adding leading zeros if necessary) and then arrange the digits in descending order creating a number y .
Subtract the smaller number from the bigger number . Let that number be z = (y - x) . Print the number z . Go back to step 1 and repeat . (This process stops after a few steps, that is step 3 produces the same number.)
Do this with paper and pen to understand the same. An example for the same is as follows : Start with 1945

9541–1459=8082
8820–0288=8532
8532–2358=6174
7641–1467=6174

Given a suitable starting number, generate the sequence. It should not repeat; that is, it should stop before the repetition.

Example:

kaprekar_seq(1945) -->
8082
8532
6174
kaprekar_seq(5778) -->
2997
7173
6354
3087
8352
6174

Input Format

First line of the input contains an integer n .

Constraints

1000 <= n <= 9999 (Atleast 2 digits of n are different) .

Output Format

Ouput the sequence(1 number in 1 line) till the same number does not repeat as shown in the examples , see sample test for more clarity .'''

def asc(a,b,c,d):
    s=0
    if a<=b and a<=c and a<=d:
        s=s*10+a
        if b<=c and b<=d:
            s=s*10+b
            if c<=d:
                s=s*10+c
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+c
        elif c<=b and c<=d:
            s=s*10+c
            if b<=d:
                s=s*10+b
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+b
        else:
            s=s*10+d
            if b<=c:
                s=s*10+b
                s=s*10+c
            else:
                s=s*10+c
                s=s*10+b
            
    elif b<=a and b<=c and b<=d:
        
        s=s*10+b
        if a<=c and a<=d:
            s=s*10+a
            if c<=d:
                s=s*10+c
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+c
        elif c<=a and c<=d:
            s=s*10+c
            if a<=d:
                s=s*10+a
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+a
        else:
            s=s*10+d
            if a<=c:
                s=s*10+a
                s=s*10+c
            else:
                s=s*10+c
                s=s*10+a
    
    elif c<=a and c<=b and c<=d:
        
        s=s*10+c
        if a<=b and a<=d:
            s=s*10+a
            if b<=d:
                s=s*10+b
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+b
        elif b<=a and b<=d:
            s=s*10+b
            if a<=d:
                s=s*10+a
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+a
        else:
            s=s*10+d
            if a<=b:
                s=s*10+a
                s=s*10+b
            else:
                s=s*10+b
                s=s*10+a
    
    else:
        s=s*10+d
        if a<=b and a<=c:
            s=s*10+a
            if b<=c:
                s=s*10+b
                s=s*10+c
            else:
                s=s*10+c
                s=s*10+b
        elif b<=a and b<=c:
            s=s*10+b
            if a<=c:
                s=s*10+a
                s=s*10+c
            else:
                s=s*10+c
                s=s*10+a
        else:
            s=s*10+c
            if a<=b:
                s=s*10+a
                s=s*10+b
            else:
                s=s*10+b
                s=s*10+a
    return s
    
def dsc(a,b,c,d):
    s=0
    if a>=b and a>=c and a>=d:
        s=s*10+a
        if b>=c and b>=d:
            s=s*10+b
            if c>=d:
                s=s*10+c
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+c
        elif c>=b and c>=d:
            s=s*10+c
            if b>=d:
                s=s*10+b
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+b
        else:
            s=s*10+d
            if b>=c:
                s=s*10+b
                s=s*10+c
            else:
                s=s*10+c
                s=s*10+b
            
    elif b>=a and b>=c and b>=d:
        
        s=s*10+b
        if a>=c and a>=d:
            s=s*10+a
            if c>=d:
                s=s*10+c
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+c
        elif c>=a and c>=d:
            s=s*10+c
            if a>=d:
                s=s*10+a
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+a
        else:
            s=s*10+d
            if a>=c:
                s=s*10+a
                s=s*10+c
            else:
                s=s*10+c
                s=s*10+a
    
    elif c>=a and c>=b and c>=d:
        
        s=s*10+c
        if a>=b and a>=d:
            s=s*10+a
            if b>=d:
                s=s*10+b
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+b
        elif b>=a and b>=d:
            s=s*10+b
            if a>=d:
                s=s*10+a
                s=s*10+d
            else:
                s=s*10+d
                s=s*10+a
        else:
            s=s*10+d
            if a>=b:
                s=s*10+a
                s=s*10+b
            else:
                s=s*10+b
                s=s*10+a
    
    else:
        s=s*10+d
        if a>=b and a>=c:
            s=s*10+a
            if b>=c:
                s=s*10+b
                s=s*10+c
            else:
                s=s*10+c
                s=s*10+b
        elif b>=a and b>=c:
            s=s*10+b
            if a>=c:
                s=s*10+a
                s=s*10+c
            else:
                s=s*10+c
                s=s*10+a
        else:
            s=s*10+c
            if a>=b:
                s=s*10+a
                s=s*10+b
            else:
                s=s*10+b
                s=s*10+a
    return s                
    
def diff(n):    
    a=n%10
    n=n//10
    b=n%10
    n=n//10
    c=n%10
    d=n//10 
    diff1=dsc(a,b,c,d)-asc(a,b,c,d)
    return diff1
                
n=(int)(input())


p=0
q=diff(n)
while p!=q:
    print(q)
    p=q
    q=diff(p)

