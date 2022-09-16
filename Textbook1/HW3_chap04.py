# HW3

import math as mt

'''
4-2. The Minitab output for a random sample of data is
shown below. Some of the quantities are missing. Compute the
values of the missing quantities.
- Var: X
- N: 16
- Mean: ?
- SE Mean:0.159 (평균 표준오차)
- StDev: ?
- Sum: 399.851
'''
# Mean(평균)
# = 합 / 표본수
399.851/16 # 25
# StDeV :
# 평균의 오차 * square(표본수)
0.159 * mt.sqrt(16) # 0.636

'''
4-5. Suppose we have a random sample of size 2n from a
population denoted by X, and E(X)=u and V(X)=(시그마)^2.
X1bar = 1/2n씨그마(2n/i=1)Xi and X2bar = 1/n씨그마(n/i=1)Xi 
be two estimators of u. Which is the better estimator of u?
Explain your choice.
'''
# X1bar = (X1+X2+...+Xn+...+X2n)/2n
# X2bar = (X1+X2+...+Xn)/n
# Solution
'''
평균에 대해
- X1bar 평균 = E(1/2n씨그마(2n/i=1)Xi) = E(씨그마(2n/i=1)Xi)/2n = (2nu)/2n = u
- X2bar 평균 = E(1/n씨그마(n/i=1)Xi) = E(씨그마(n/i=1))/n = (nu)/n = u
둘 다 u로 동일하다.
표준편차에 대해
- X1bar 표준편차 = V(X1bar) = 씨그마^2/2n
- X2bar 표준편차 = V(X2bar) = 씨그마^2/n
이다.
상대적 효율설 공식에 따라
V(X1bar)/V(X2bar) = (씨그마^2/2n)/(씨그마^2/n) = 1/2로 
분산이 더 작기 때문에 X1bar이 더 효율적임을 알 수 있다.
'''

'''
4-7. Suppose that 세타1 and 세타2 are unbiased estimators of the
parameter 세타. We know that V(세타1^)=2 and V(세타2^)=4 Which
estimator is better, and in what sense is it better?
'''
# Solution
'''
상대적 효율성 공식에 따라
V(세타1^)/V(세타2^) = 2/4 = 1/2로 
분산이 더 작기 때문에 세타1가 더 효율적임을 알 수 있다.
'''

'''
4-9. Calculate the relative efficiency of the two estimators in
Exercise 4-7.
'''
# V(세타1^)/V(세타2^) = 2/4 = 1/2

'''
4-10. Suppose that 세타1^ and 세타2^ are estimators of the parameter
세타. We know that E(세타1^)=세타, E(세타2^)=세타/2, V(세타1^)=10,
V(세타2^)=4. Which estimator is “better”? In what sense is it
better?
'''
# Solution
'''
세타^1 편향 = 0
세타^2 편향 = E(세타2^)-E(세타1^) = 세타/2-세타 = -세타/2
상대적 효율적 공식에 따라
(V(세타1^)+세타^1편향)/(V(세타2^)+세타^2편향) = (10+0^2)/(4+(-세타/2)^2)
세타1^가 효율적이기 위해 1보다 작아야 하기 때문에
(10+0^2)/(4+(-세타/2)^2)<=1
10/(4+세타^2/4)<=1
10<=(4+세타^2/4)
24<=세타^2
'''
# 따라서, 세타1^이 효율적이기 위해 세타<=-4.9 혹은 세타>=4.9여야 한다.
# 반대로, 세타2^가 효율적이기 위해 -4.9<=세타<=4.9여야 한다.

'''
4-12. Let three random samples of sizes n1=20, n2=10,
and n3=8 be taken from a population with mean u and variance
세타^2. Let (S^2)1, (S^2)2, and (S^2)3 be the sample variances. Show that
S^2=(20*(S^2)1+10*(S^2)2+8*(S^2)3)/38 is an unbiased estimator of 세타^2.
'''
# E(S^2) = E((20*(S^2)1+10*(S^2)2+8*(S^2)3)/38)
# = (E(20*(S^2)1)+E(10*(S^2)2)+8*E((S^2)3))/38
# = (20*세타^2+10*세타^2+8*세타^2)/38
# = (38*세타^2)/38 = 세타^2
# 따라서, 세타^2이 편향되지 않은 지표이다.

'''
4-15. A textile fiber manufacturer is investigating a new
drapery yarn, which has a standard deviation of 0.3 kg. The
company wishes to test the hypothesis H0: u=14 against
H1: u<14, using a random sample of five specimens.
(a) What is the P-value if the sample average is Xbar=13.7kg?
(b) Find 베타 for the case where the true mean elongation force
is 13.5 kg and we assume that 알파=0.05.
(c) What is the power of the test from part (b)?
4-16. Repeat Exercise 4-15 using a sample size of n=16
and the same critical region.
'''
# sd = 0.3, H0의 u=14

# a) Xbar=13.7인 경우 p-value는 무엇인가?
# Z = (Xbar-u)/(세타/sqrt(n))이기 때문에,
Z = (13.7-14)/(0.3/mt.sqrt(16)) # -4.0
# P(Z<=-4.0) = 0

# b) true mean elongation force=13.5, 알파=0.05
14-1.645*(0.3/mt.sqrt(16)) # 13.876625
# 베타 = P(Xbar>=13.876625) = 1-P(Z<=(13.876625-14)/(0.3/mt.sqrt(16)))
(13.876625-13.5)/(0.3/mt.sqrt(16)) # 5.02
# 따라서, 1-P(Z<=5.02) = 1-1 = 0

# c) the power of the test
# 1-베타 = 1-0 = 1

'''
4-17. In Exercise 4-15 with n=5:
(a) Find the boundary of the critical region if the type I error
probability is specified to be 알파=0.01.
(b) Find 베타 for the case when the true mean elongation force is 13.5 kg.
(c) What is the power of the test?
'''
# sd = 0.3, H0의 u=14, n=5

# a) Xbar=13.7인 경우 p-value는 무엇인가?
# Z = (Xbar-u)/(세타/sqrt(n))이기 때문에,
(13.7-14)/(0.3/mt.sqrt(5)) # -2.236
# P(Z<=-2.236) = 0

# b) true mean elongation force=13.5, 알파=0.05
14-1.645*(0.3/mt.sqrt(5)) # 13.78
# 베타 = P(Xbar>=13.78) = 1-P(Z<=(13.78-14)/(0.3/mt.sqrt(5)))
(13.78-13.5)/(0.3/mt.sqrt(5)) # 2.087
# 따라서, 1-P(Z<=2.087) = 1-0.9816
1-0.9816 # 0.0184

# c) the power of the test
# 1-베타 = 1-0.0184
1-0.0184 # 0.9816

'''
4-19. The heat evolved in calories per gram of a cement
mixture is approximately normally distributed. The mean is
thought to be 100 and the standard deviation is 2. We wish to
test H0: u=100 versus H1: u not= 100 with a sample of n=9 specimens.
(a) If the rejection region is defined as Xbar<98.5 or Xbar>101.5,
find the type I error probability 알파.
(b) Find 베타 for the case where the true mean heat evolved is 103.
(c) Find 베타  for the case where the true mean heat evolved is
105. This value of 베타 is smaller than the one found in part (b). Why?
'''
# mean=100, sd=2
# H0의 u=100, n=9

# a) Xbar<98.5 or Xbar>101.5
(98.5-100)/(2/mt.sqrt(9)) # P(Z<-2.25)
(101.5-100)/(2/mt.sqrt(9)) # P(Z>2.25)
# P(Z<-2.25)+P(Z>2.25)
0.01222+0.01222 # 0.02444

# b) if mean heat = 103
(98.5-103)/(2/mt.sqrt(9)) # P(Z<-6.75)
(101.5-103)/(2/mt.sqrt(9)) # P(Z>-2.25)
# P(Z>-2.25)-P(Z<-6.75)
0.01222-0 # 0.0122

# c) if mean heat = 105
(98.5-105)/(2/mt.sqrt(9)) # P(Z<-9.75)
(101.5-105)/(2/mt.sqrt(9)) # P(Z>-5.25)
# P(Z>-5.25)-P(Z<-9.75)
0-0 # 0
# b)보다 c)가 더 작은 이유?
# 채택역에서 103보다 105가 더 멀리 위치하기 때문이다.