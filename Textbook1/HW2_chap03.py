# HW2

import statistics as st # 계산 모듈
from matplotlib import pyplot as plt # 그래프 모듈

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
3-23. Suppose that f (x) = e^(-(x-6)) for 6 < x and f (x) = 0 for
x <= 6. Determine the following probabilities.
(a) P(X > 6) (b) P(6 < X < 8)
(c) P(X < 8) (d) P(X > 8)
'''
def func1(x):
    y = exp(-(x-6))
    return y
def func2(x):
    y_1 = -(x-6)*exp(-(x-6))
    return y_1
# a)

# b)

# c)

# d)


'''
3-25. The pdf of the time to failure of an electronic component
in a copier (in hours) is f (x)  [exp (x3000)]3000
for x0 and f (x) 0 for x0. Determine the probability that
(a) A component lasts more than 1000 hours before failure.
(b) A component fails in the interval from 1000 to 2000
hours.
(c) A component fails before 3000 hours.
(d) Determine the number of hours at which 10% of all components
have failed.
(e) Determine the mean.
'''

'''
3-31. Suppose the cumulative distribution function of the
length (in millimeters) of computer cables is
(a) Determine P(x 
 1208).
(b) If the length specifications are 1195 
 x 
 1205 millimeters,
what is the probability that a randomly selected computer
cable will meet the specification requirement?
'''

'''
3-32. The thickness of a conductive coating in micrometers
has a density function of 600x2 for 100 m 
 x 
 120 m
and zero for x elsewhere.
(a) Determine the mean and variance of the coating thickness.
(b) If the coating costs $0.50 per micrometer of thickness on
each part, what is the average cost of the coating per part?
'''

'''
3-33. A medical linear accelerator is used to accelerate electrons
to create high-energy beams that can destroy tumors
with minimal impact on surrounding healthy tissue. The beam
energy fluctuates between 200 and 210 MeV (million electron
volts). The cumulative distribution function is
Determine the following.
(a) P(X 
 209) (b) P(200 
 X 
 208) (c) P(X  209)
(d) What is the probability density function?
(e) Graph the probability density function and the cumulative
distribution function.
(f ) Determine the mean and variance of the beam energy.
'''

'''
3-36. Given the cdf F(x)  0 for for
0 6 x, determine the following:
(a) P(X<1)
(b) P(X>2)
(c) P(1<X<2)
(d) x such that P(X<x)=0.95
(e) pdf
'''

'''
3-41. Assume that X is normally distributed with a mean of
20 and a standard deviation of 2. Determine the following.
(a) P(X  24) (b) P(X  18)
(c) P(18  X  22) (d) P(14  X  26)
(e) P(16  X  20) (f ) P(20  X  26)
'''

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
