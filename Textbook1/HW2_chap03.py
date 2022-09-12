# HW2

import statistics as st # 계산 모듈
from matplotlib import pyplot as plt # 그래프 모듈
import sympy as sp # 미분적분 모듈
from sympy.abc import x, y

'''
3-3. The strength of a concrete specimen.
'''
# Continuous(연속형)

'''
3-4. The number of convenience options selected by an
automobile buyer.
'''
# Discrete(이산형)

'''
3-11. If P(XA)  0.4, and P(XB)  0.6 and the intersection
of sets A and B is empty,
(a) Are sets A and B mutually exclusive? (상호배타적)
# YES (A와 B의 교집합은 0)
(b) Find P(X  A'). = 1 - 0.4 = 0.6
(c) Find P(X  B). = 1 - 0.6 = 0.4
(d) Find P(X  A  B). = 0.6 + 0.4 = 1
'''

'''
3-13. Let P(X < 15) = 0.3, P(15 < X < 24) = 0.6, and
P(X > 20) = 0.5.
(a) Find P(X > 15).
(b) Find P(X < 24).
(c) Find P(15 < X < 20).
(d) If P(18 < X < 24) = 0.4, find P(X < 18).
''' 
# a)
1-0.3 # 0.7
# b)
0.3+0.6 # 0.9
# c)
0.3+0.6-0.5 # 0.4
# d)
0.3+0.6-0.4 # 0.5

'''
3-14. Suppose that an ink cartridge is classified as being
overfilled, medium filled, or underfilled with a probability of
0.40, 0.45, and 0.15, respectively.
(a) What is the probability that a cartridge is classified as not
underfilled?
(b) What is the probability that a cartridge is either overfilled
or underfilled?
'''
# a) not underfilled
1-0.15 # 0.85
# b) overfilled or underfilled
0.40+0.15 # 0.55

'''
3-15. Let X denote the life of a semiconductor laser (in
hours) with the following probabilities:
P(X < 5000) = 0.05 and P(X > 7000) = 0.45.
(a) What is the probability that the life is less than or equal to
7000 hours?
(b) What is the probability that the life is greater than 5000
hours?
(c) What is P(5000 < X < 7000)?
'''
# a) P(X<7000)
1-0.45 # 0.55
# b) P(X>5000)
1-0.05 # 0.95
# c)
0.45-0.05 # 0.40

'''
3-16. Let E1 denote the event that a structural component
fails during a test and E2 denote the event that the component
shows some strain but does not fail. Given P(E1) = 0.15 and
P(E2) = 0.30,
(a) What is the probability that a structural component does
not fail during a test?
(b) What is the probability that a component either fails or
shows strain during a test?
(c) What is the probability that a component neither fails nor
shows strain during a test?
'''
# a) structial component does not fail
1-0.15 # 0.85
# b) component fails or shows
0.15+0.30 # 0.45
# c) component not fails or not shows
1-0.45 # 0.55

'''
3-18. Let X denote the number of patients who suffer an infection
within a floor of a hospital per month with the following
probabilities:
x 0 1 2 3
P(X = x) 0.7 0.15 0.1 0.05
Determine the following probabilities:
(a) Less than one infection
(b) More than three infections
(c) At least one infection
(d) No infections
'''
# a) P(X<1)
0.7
# b) P(X>3)
1-0.7-0.15-0.1-0.05 # 0
# c) P(X>=1)
1-0.7 # 0.3
# d) P(X=0)
0.7

'''
3-23. Suppose that f (x) = e^(-(x-6)) for 6 > x and f (x) = 0 for
x <= 6. Determine the following probabilities.
(a) P(X > 6) (b) P(6 < X < 8)
(c) P(X < 8) (d) P(X > 8)
(e) Determine x such that P(X<x)=0.95.
'''
fx = sp.E**(-(x-6))
Fx = sp.integrate(fx) # 적분
fx_1 = sp.diff(fx) # 미분
# a) 6~Inf 적분
(-Fx.subs(x,6)).evalf() # 1
# b) 6~8 적분
(Fx.subs(x,8)-Fx.subs(x,6)).evalf() # 0.86
# c) -Inf~8 적분: -Inf~6까지 0이기 때문에 b)와 계산 방식이 같음
(Fx.subs(x,8)-Fx.subs(x,6)).evalf() # 0.86
# d) 8~Inf 적분
1-(Fx.subs(x,8)-Fx.subs(x,6)).evalf() # 0.14
# e) 6~n 적분값이 0.95인 n값을 구하여라.
n = 6-sp.ln(0.05)
n # 8.99573227355399 = 9

'''
3-25. The pdf of the time to failure of an electronic component
in a copier (in hours) is f(x) = [exp(-x/3000)]/3000
for x>0 and f(x) = 0 for x<=0. Determine the probability that
(a) A component lasts more than 1000 hours before failure.
(b) A component fails in the interval from 1000 to 2000 hours.
(c) A component fails before 3000 hours.
(d) Determine the number of hours at which 10% of all components
have failed.
(e) Determine the mean.
'''
fx = (sp.E**(-x/3000))/3000
Fx = sp.integrate(fx) # 적분
# a) P(X>1000)
1-(Fx.subs(x,1000)-Fx.subs(x,0)).evalf() # 0.72
# b) P(1000<X<2000)
(Fx.subs(x,2000)-Fx.subs(x,1000)).evalf() # 0.20
# c) P(X<3000)
(Fx.subs(x,3000)-Fx.subs(x,0)).evalf() # 0.63
# d) P(0<X<n)=0.1인 경우 n값을 구하여라.
# (Fx.subs(x,n)-Fx.subs(x,0)).evalf() = 0.1 일 때, n값
# Fx(n)-Fx(0) = 0.1
# Fx(n) = -0.9
# -sp.E(-n/3000) = -0.9
n = -sp.ln(0.9)*3000
n # 316.08
# e) Determine the mean.
mean_fx = x*(sp.E**(-x/3000))/3000
mean_Fx = sp.integrate(mean_fx)
(-mean_Fx.subs(x,0)).evalf() # 3000

'''
3-31. Suppose the cumulative distribution function of the
length (in millimeters) of computer cables is
F(x) =
- 0 (x<=1200)
- 0.1x-120 (1200<x<=1210)
- 1 (x>1210)
(a) Determine P(x<1208).
(b) If the length specifications are 1195<x<1205 millimeters,
what is the probability that a randomly selected computer
cable will meet the specification requirement?
'''
Fx = 0.1*x-120
# a) P(X<1208)
(Fx.subs(x,1208)).evalf() # 0.80
# b) P(1195<X<1205): 1200 이하는 0이기 때문에 제외
(Fx.subs(x,1205)-Fx.subs(x,1200)).evalf() # 0.50

'''
3-32. The thickness of a conductive coating in micrometers
has a density function of 600x^-2 for 100um<x<120um
and zero for x elsewhere.
(a) Determine the mean and variance of the coating thickness.
(b) If the coating costs $0.50 per micrometer of thickness on
each part, what is the average cost of the coating per part?
'''
# a) mean and variance
# 평균: 적분(x*fx)
mean_fx = x*(600*x**(-2))
mean_Fx = sp.integrate(mean_fx) # 적분
(mean_Fx.subs(x,120)-mean_Fx.subs(x,100)).evalf() # 109.40
# 표준편차: 적분(x^2*fx)-미분**2
var_fx = 600
var_Fx = 600*x
(var_Fx.subs(x,120)-var_Fx.subs(x,100)).evalf() - 109.40**2 # 31.64
# b) Average Cost = Coating Cost X Mean of the Coating Thickness
0.50*109.39 # $54.70

'''
3-33. A medical linear accelerator is used to accelerate electrons
to create high-energy beams that can destroy tumors
with minimal impact on surrounding healthy tissue. The beam
energy fluctuates between 200 and 210 MeV (million electron
volts). The cumulative distribution function is
F(X)=
- 0 (x<200)
- 0.1*x-20 (200<x<210)
- 1 (x>210)
Determine the following.
(a) P(X<209) (b) P(200<X<208) (c) P(X>209)
(d) What is the probability density function?
(e) Graph the probability density function and the cumulative
distribution function.
(f) Determine the mean and variance of the beam energy.
'''
Fx1 = 0.1*x-20
Fx2 = 1
# a) P(X<209)
(Fx1.subs(x,209)).evalf() # 0.9
# b) P(200<X<208)
(Fx1.subs(x,208)-Fx1.subs(x,200)).evalf() # 0.8
# c) P(X>209)
1-(Fx1.subs(x,209)).evalf() # 0.1
# d) 확률밀도함수란?
# 특정 사건이 발생할 확률을 나타낸 것으로,
# 모든 확률 값은 0 이상이어야 하고 전체 확률 값의 합은 1이어야 한다.
# e) 그래프 그리기
# 확률밀도함수: f(x)
fx = [0.1]*11
x_ = [i for i in range(200,211)]
plt.plot(x_,fx)
plt.xlabel('BeamEnergyFluctuates(MeV)')
plt.ylabel('f(x)')
plt.show()
# 누적분포함수: F(x)
sp.plot(Fx1,(x,200,210))
sp.show()
# f) mean and variance
# 평균
fx = sp.diff(Fx1)
mean_fx = x*fx
mean_Fx = sp.integrate(mean_fx)
(mean_Fx.subs(x,210)-mean_Fx.subs(x,200)).evalf() # 205
# 표준편차
var_fx = fx*(x**2)
var_Fx = sp.integrate(var_fx)
(var_Fx.subs(x,210)-var_Fx.subs(x,200)).evalf()-(205)**2 # 8.33

'''
3-36. Given the cdf F(x)=0 for for x<0,
F(x)=1-exp(-x/2) for x>0 determine the following:
(a) P(X<1)
(b) P(X>2)
(c) P(1<X<2)
(d) x such that P(X<x)=0.95
(e) pdf
'''
Fx = 1-sp.E**(-x/2)
# a) P(X>1)
(Fx.subs(x,1)-Fx.subs(x,0)).evalf() # 0.39
# b) P(X>2)
1-(Fx.subs(x,2)-Fx.subs(x,0)).evalf() # 0.37
# c) P(1<X<2)
(Fx.subs(x,2)-Fx.subs(x,1)).evalf() # 0.24
# d) P(0<X<n)=0.95
# 1-sp.E**(-n/2) = 0.95
# 0.05 = sp.E**(-n/2)
# sp.ln(0.05) = -n/2
n = -sp.ln(0.05)*2
n # 6
# e) f(x)
fx = sp.diff(Fx)
fx # exp(-x/2)/2

import scipy as sp
'''
3-41. Assume that X is normally distributed with a mean of
20 and a standard deviation of 2. Determine the following.
(a) P(X<24) (b) P(X<18)
(c) P(18<X<22) (d) P(14<X<26)
(e) P(16<X<20) (f) P(20<X<26)
'''
# mean=20, sd=2
sp.stats.norm(20,2) # 확률 밀도 함수(PDF): 분위수, 누적 분포 함수(CDF): x축
# a) P(X>24)
1-sp.stats.norm(20,2).cdf(24) # 0.023
# b) P(X<18)
sp.stats.norm(20,2).cdf(18) # 0.159
# c) P(18<X<22)
sp.stats.norm(20,2).cdf(22)-sp.stats.norm(20,2).cdf(18) # 0.683
# d) P(14<X<26)
sp.stats.norm(20,2).cdf(26)-sp.stats.norm(20,2).cdf(14) # 0.997
# e) P(16<X<20)
sp.stats.norm(20,2).cdf(20)-sp.stats.norm(20,2).cdf(16) # 0.477
# f) P(20<X<26)
sp.stats.norm(20,2).cdf(26)-sp.stats.norm(20,2).cdf(20) # 0.499

'''
3-48. The fill volume of an automated filling machine used
for filling cans of carbonated beverage is normally distributed
with a mean of 12.4 fluid ounces and a standard deviation of
0.1 fluid ounce.
(a) What is the probability that a fill volume is less than 12
fluid ounces?
(b) If all cans less than 12.1 or greater than 12.6 ounces are
scrapped, what proportion of cans is scrapped?
(c) Determine specifications that are symmetric about the
mean that include 99% of all cans.
'''
# a) P(X<12)
sp.stats.norm(12.4,0.1).cdf(12) # 3.167e-05 = 0
# b) P(X<12.1) or P(X>12.6)
sp.stats.norm(12.4,0.1).cdf(12.1)+1-sp.stats.norm(12.4,0.1).cdf(12.6) # 0.024
# c) P(a<X<b) = 0.99
sp.stats.t.interval(.95,12.4,0.1)
# (-2.07, 2.27)
