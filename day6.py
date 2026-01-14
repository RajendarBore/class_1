1. How many types of operators in python.
2. What is the difference between logical and 'and' bitwise and.
3. What is the difference between logical or and bitwise or.
4. What are identity Operators.
    is, in not.
5. Output of print(9//2)
        4
6. What is the type a when a = 1,00,000
7. What is the type of 'inf'?
a) Boolean
b) Integer
c) Float
d) Complex
8. What does ~~~~~~5 evaluate to?
a)+5
b) -11
c) +11
d) -5
9. What is the purpose of not in operator.

    The not in operator is used to check if a value
    
10. What is the purpose pass statement in python.
11. Which function overloads the >> operator.
12. Output of "format(10/3)" and what is the return type.

    3.333
    
13. Output of "Sathya" > "sathya".

False

14. Output of 10 and 10.
15. Output of 10 and 0.
16. Output of 0 and 10.
17. Output of 0 and 0.
18. Output of 0 or 10.
19. Which is the correct operator for power(xy)?

b) X**y

d) None of the mentioned
20. Which one of these is floor division?

b) //

d) None of the mentioned
21. What is the order of precedence in python?
i) Parentheses ii) Exponential iii) Multiplication iv) Division
v) Addition vi) Subtraction
a) i,ii,iii,iv,v,vi

22. Mathematical operations can be performed on a string.
State whether true or false.
b) False
23. Operators with the same precedence are evaluated in
which manner?
a) Left to Right

24. What is the output of this expression, 3*1**3?

c) 3

25. The expression Int(x) implies that the variable x is
converted to integer. State whether true or false.
a) True

26. Which one of the following have the highest precedence
in the expression?
 d) Parentheses
27. Which of the following is invalid?

d) none of the mentioned
28. Which of the following is an invalid variable?

b) 1st_string

29. Which of the following is not a keyword?
a) eval

30. Which of the following is an invalid statement?

b) a b c = 1000 2000 3000

31. Which of the following cannot be a variable?
a) __init__
b) in
c) it
d) on


1. 2+3-5*6+7-9*3/2
    5 * 6 = 30
9 * 3 = 27 → 27 / 2 = 13.5
2 + 3 = 5
5 - 30 = -25
-25 + 7 = -18
-18 - 13.5 = -31.5
-31.5


2. 3*4-5/6+7-8*9+2-3*7

3 * 4 = 12
5 / 6 ≈ 0.8333
8 * 9 = 72
3 * 7 = 21
12 - 0.8333 ≈ 11.1667
11.1667 + 7 = 18.1667
18.1667 - 72 = -53.8333
-53.8333 + 2 = -51.8333
-51.8333 - 21 = -72.8333


3. 6-7*8+9/5-8%3-7/2-3

7 * 8 = 56
9 / 5 = 1.8
8 % 3 = 2 (remainder of 8 ÷ 3)
7 / 2 = 3.5
6 - 56 = -50
-50 + 1.8 = -48.2
-48.2 - 2 = -50.2
-50.2 - 3.5 = -53.7
-53.7 - 3 = -56.7


4. 3*5-7+7*7-7/7+7%7

3 * 5 = 15
7 * 7 = 49
7 / 7 = 1.0
7 % 7 = 0
15 - 7 = 8
8 + 49 = 57
57 - 1.0 = 56.0
56.0 + 0 = 56.0


5. 3>=5-6+7-8

3 >= 5 - 6 + 7 - 8
5 - 6 = -1
-1 + 7 = 6
6 - 8 = -2
3 >= -2
True

6. 2>=4 and3==4
7. 2>=4 or 3==4
8. What is the output?
i=5; j=6; i=i+j; j=j-i;
print(i);
print(j);


9. What is the output?
i=2*3+5*6//7-3//2+7*6//3
j=i-3*4-5*6+7-3*4+7
i=i+j; j=j-i*3/2; i=i*7/-2+5;
j=j-3*4%7;
print(i); print(j);


10. What is the output of below
code snippet?
i = 3 * 4 - 6 + 7 // 2 + 4;
j = 3 * 5 - 6 // 7 + 8 % 9 - 3 * 5 + 7;
i = i + j; j = j - i; print(i); print(j);

3 * 4 = 12
7 // 2 = 3
i = 12 - 6 + 3 + 4
= 6 + 3 + 4
= 13
i = 13

3 * 5 = 15
6 // 7 = 0
8 % 9 = 8
3 * 5 = 15
j = 15 - 0 + 8 - 15 + 7
= 15 + 8 - 15 + 7
= 15 - 15 + 15
= 15
j=15

i = i + j → i = 13 + 15 = 28
j = j - i → j = 15 - 28 = -13
=28=i
=-13=j




11. What is the output?
a = "sathya"
b = "Tech"
c = a + b
print(c)
"sathyaTech"


12. What is the output?
s = "output is" + 2 + 3
print(s)


13. What is the output?
s =2 +3+5*6+7-3*5//6
print(s)


14. What is the output?
b = 5+2-3*5+7/2-3/4>6-
5+4*3/9+9-2/3

5 + 2 - (3*5) + (7/2) - (3/4)
= 5 + 2 - 15 + 3.5 - 0.75
= 7 - 15 + 3.5 - 0.75
= -8 + 3.5 - 0.75
= -5.25
6 - 5 + (4*3/9) + 9 - (2/3)
= 6 - 5 + (12/9) + 9 - 0.6667
= 1 + 1.3333 + 9 - 0.6667
= 10.6666
-5.25 > 10.6666
False

print(b)
15. What is the output?
i = 7
j=3
b=i>=j
print(b)

is True

fales
16. What is the output?

print(2+3-5*6+7-8)

2 + 3 = 5
5 - 30 = -25
-25 + 7 = -18
-18 - 8 = -26
-26


print(5**6)

5 * 5 = 25
25 * 5 = 125
125 * 5 = 625
625 * 5 = 3125
3125 * 5 = 15625
15625

print(5*6)

30


print(2+4)

6


print(2+3.5)

5.5

print((2>3))

fales

print(12//5+12%5)

12//5=2
12%5=2
2+2=4
4

17. 3>4 and 3<5

False

18. 5+3*7-9>4+5*6 and 4<5

5 + 3*7 - 9
= 5 + 21 - 9
= 26 - 9
= 17
4 + 5*6
= 4 + 30
= 34
17 > 34  → False
4 < 5  → True
fales and true is False


19. 4**4

256


20. 6*2-3/4+4-3//2

6 * 2 = 12
3 / 4 = 0.75
3 // 2 = 1
12 - 0.75 = 11.25
11.25 + 4 = 15.25
15.25 - 1 = 14.25

