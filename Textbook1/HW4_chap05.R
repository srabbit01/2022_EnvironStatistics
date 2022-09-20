# HW4

install.packages("BSDA")
library(BSDA)

'''
5-1. A computer program has produced the following output
for a hypothesis testing problem:
- Difference in sample means: 2.35
- Standard error of the difference in sample means: ?
- Test statistic: z0=2.01
- P-value: 0.0222
(a) What is the missing value for the standard error?
(b) Is this a two-sided or a one-sided test?
(c) If 알파=0.05, what are your conclusions?
(d) Find a 90% two-sided CI on the difference in means.
'''
# a) standard error?
# Z = (Xbar1-Xbar2)-(mu1-mu2)/sqrt(세타1^2/n1+세타2^2/n2)
# 따라서, 2.01 = (2.35)/SE
2.35/2.01 # 1.169154

# b)
# Z0=2.01일 때, P-value가 0.0222이기 때문에 One-sided test이다.

# c) If alpha=0.05?
# P-value가 0.0222기 때문에 < 0.05(알파)로 귀무가설은 기각된다.

# d) 90% Two-sided CI : 90% 신뢰구간 Z값 = +-1.64
2.35-1.64*1.17 # 최소 : 0.4312
2.35+1.64*1.17 # 최대 : 4.2688
# 0.4312 <= mu1-mu2 <= 4.2688

'''
5-2. A computer program has produced the following output
for a hypothesis testing problem:
Difference in sample means: 11.5
Standard error of the difference in sample means: ?
Test statistic: z0=-1.88
P-value: 0.0601
(a) What is the missing value for the standard error?
(b) Is this a two-sided or a one-sided test?
(c) If 알파=0.05, what are your conclusions?
(d) Find a 95% two-sided CI on the difference in means.
'''
# a) -1.88 = (11.5)/SE
11.5/(-1.88) # -6.117021

# b)
# Z0가 -1.88일 때, One-sided가 0.0301이기 때문에 Two-sided Test이다.

# c) If alpha=0.05?
# P-value가 0.0601기 때문에 < 0.05(알파)로 귀무가설은 기각된다.

# d) 95% Two-sided CI : 95% 신뢰구간 Z값 = +-1.96
11.5-1.96*(6.117021) # 최소 : -0.4893612
11.5+1.96*(6.117021) # 최대 : 23.48936
# -0.4893612 <= mu1-mu2 <= 23.48936

'''
5-3. Two machines are used for filling plastic bottles with a
net volume of 16.0 ounces. The fill volume can be assumed
normal, with standard deviation 세타1=0.020 and 세타2=0.025
ounces. A member of the quality engineering staff suspects
that both machines fill to the same mean net volume, whether
or not this volume is 16.0 ounces. A random sample of 10 bottles
is taken from the output of each machine.
# 1) Machine1: 16.03, 16.01, 16.04, 15.96, 16.05, 15.98, 16.05, 16.02, 16.02, 15.99
# 2) Machine2: 16.02, 16.03, 15.97, 16.04, 15.96, 16.02, 16.01, 16.01, 15.99, 16.00
(a) Do you think the engineer is correct? Use the P-value approach.
(b) If 알파=0.05, what is the power of the test in part (a) for a
true difference in means of 0.04?
(c) Find a 95% CI on the difference in means. Provide a practical
interpretation of this interval.
(d) Assuming equal sample sizes, what sample size should be
used to ensure that 베타=0.01 if the true difference in
means is 0.04? Assume that 알파=0.05.
'''
sd1 = 0.020
sd2 = 0.025
n = 10
m1 = c(16.03, 16.01, 16.04, 15.96, 16.05, 15.98, 16.05, 16.02, 16.02, 15.99)
m2 = c(16.02, 16.03, 15.97, 16.04, 15.96, 16.02, 16.01, 16.01, 15.99, 16.00)

# a)
Z = (mean(m1)-mean(m2))/sqrt(sd1**2/n+sd2**2/n) # 0.9877296
# Z=0.987의 표준정규분포 100% 확률을 찾으면 0.8365이다.
# 즉, P-value=1-2(1-0.8365)
1-2*(1-0.8365) # 0.673
# 결과적으로, 귀무가설이 채택됨을 알 수 있다.

# b) power = 1-베타
1.96-(0.04/sqrt(0.02**2/10+0.025**2/10)) # -1.990918
-1.96-(0.04/sqrt(0.02**2/10+0.025**2/10)) # -5.910918
# 베타 = Z정규분포(-1.99) - Z정규분포(-5.91)
#      = 0.0233 - 0 = 0.0233
# 따라서, Power = 1 - 0.0233 = 0.9767

# c) 95% Two-sided CI : 95% 신뢰구간 Z값 = +-1.96
(mean(m1)-mean(m2))-1.96*(sqrt(0.02**2/10+0.025**2/10)) # 최소 : -0.009843488
(mean(m1)-mean(m2))+1.96*(sqrt(0.02**2/10+0.025**2/10)) # 최대 : 0.02984349
# -0.009843488 <= mu1-mu2 <= 0.02984349

# d) 알파 = 0.05, 베타 = 0.02
n = ((1.96+2.05)**2)*(0.02**2+0.025**2)/(0.04**2)
n # 10

'''
5-4. Two types of plastic are suitable for use by an electronics
component manufacturer. The breaking strength of this
plastic is important. It is known that 세타1=세타2=1.0 psi. From a
random sample of size n1=10 and n2=12, we obtain
xbar1=162.7 and Xbar2=155.4. The company will not adopt plastic
1 unless its mean breaking strength exceeds that of plastic 2
by at least 10 psi. Based on the sample information, should it
use plastic 1? Use the P-value approach in reaching a decision.
'''
# true difference in means of 10
z0 = ((162.7-155.4)-10)/sqrt(1/10+1/12)
z0 # -6.305841
# P-value = 1-z정규분포(-6.30) = 1-0 = 1

'''
5-5. The burning rates of two different solid-fuel propellants
used in aircrew escape systems are being studied. It is
known that both propellants have approximately the same
standard deviation of burning rate; that is, 세타1=세타2=3cm/s.
Two random samples of n1=20 and n2=20 specimens are
tested; the sample mean burning rates are Xbar1=18.02cm/s
and Xbar2=24.37cm/s.
(a) Test the hypothesis that both propellants have the same
mean burning rate. Use a fixed-level test with 알파=0.05.
(b) What is the P-value of the test in part (a)?
(c) What is the 베타-error of the test in part (a) if the true difference
in mean burning rate is 2.5 cm/s?
(d) Construct a 95% CI on the difference in means u1-u2.
What is the practical meaning of this interval?
'''
# a)
z0 = (18.01-24.37)/sqrt(3**2/20+3**2/20)
z0 # -6.704029
# -6.70이 유의수준의 -1.96보다 작기 때문에 귀무가설이 기각된다.

# b) P-value = 2*(z정규분포(-6.70)) = 2*0 = 0

# c)
1.98-(2.5/sqrt(3**2/20+3**2/20)) # -0.6552314
1.98+(2.5/sqrt(3**2/20+3**2/20)) # 4.615231
# 베타 = z정규분포(-0.65) - z정규분포(4.61)
#      = 0.2678 - 0 = 0.2678

# d)
(18.01-24.37)-1.96*sqrt(3**2/20+3**2/20) # -8.219419
(18.01-24.37)+1.96*sqrt(3**2/20+3**2/20) # -4.500581
# 따라서, 95%에서의 u1-u2 범위는 -8.21 <= u1-u2 <= -4.50

'''
5-6. Two machines are used to fill plastic bottles with dishwashing
detergent. The standard deviations of fill volume are
known to be 세타1=0.10 and 세타2=0.15 fluid ounces for the two
machines, respectively. Two random samples of n1=12 bottles
from machine 1 and n2=10 bottles from machine 2 are
selected, and the sample mean fill volumes are Xbar1=30.61 and
Xbar2=30.34 fluid ounces. Assume normality.
(a) Construct a 90% two-sided CI on the mean difference in
fill volume. Interpret this interval.
(b) Construct a 95% two-sided CI on the mean difference in
fill volume. Compare and comment on the width of this
interval to the width of the interval in part (a).
(c) Construct a 95% upper-confidence bound on the mean
difference in fill volume. Interpret this interval.

5-7. Reconsider the situation described in Exercise 5-6.
(a) Test the hypothesis that both machines fill to the same
mean volume. Use the P-value approach.
(b) If 알파=0.05 and the 베타-error of the test when the true difference
in fill volume is 0.2 fluid ounces should not
exceed 0.1, what sample sizes must be used? Use 알파=0.05.
'''
# a)
z0 = (30.61-30.34)/sqrt(0.10**2/12+0.15**2/10)
z0 # 4.862432
# 따라서, P-value = 2(1-z정규분포(4.86)) = 2(1-1) = 0

# b) sample size : 알파=0.05, 베타=0.20
n = ((1.96+2.05)**2)*(0.10**2+0.15**2)/(0.1)**2
n # 52.26032
# 약 52개

'''
5-8. Two different formulations of an oxygenated motor
fuel are being tested to study their road octane numbers. The
variance of road octane number for formulation 세타1^2=1.5,
and for formulation 2 it is 세타2^2=1.2. Two random samples of
size n1=15 and n2=20 are tested, and the mean road octane
numbers observed are Xbar1=88.85 and Xbar2=92.54. Assume
normality.
(a) Construct a 95% two-sided CI on the difference in mean
road octane number.
(b) If formulation 2 produces a higher road octane number
than formulation 1, the manufacturer would like to detect
it. Formulate and test an appropriate hypothesis using the
P-value approach.
'''
# a)
(88.85-92.54)-1.96*sqrt(1.5/15+1.2/20) # -4.474
(88.85-92.54)+1.96*sqrt(1.5/15+1.2/20) # -2.906
# 따라서, -4.474 <= u1-u2 <= -2.906

# b)
z0 = (88.85-92.54)/sqrt(1.5/15+1.2/20)
z0 # -9.225
# 따라서, P-value = z정규분포(-9.225) = 0

'''
5-9. Consider the situation described in Exercise 5-5. What
sample size would be required in each population if we wanted
the error in estimating the difference in mean burning rates to
be less than 4 cm/s with 99% confidence?
'''
# 99% 신뢰구간에서 E=4이고, Z0.005=2.575이기 때문에
n = ((2.575/4)**2)*(3**2+3**2)
n # 7.459453
# n = 7개

'''
5-10. Consider the road octane test situation described in
Exercise 5-8. What sample size would be required in each
population if we wanted to be 95% confident that the error in
estimating the difference in mean road octane number is less
than 1?
'''
# 95% 신뢰구간에서 E=1이고, z0.025=1.96이기 때문에
n = ((1.96/1)**2)*(1.5+1.2)
n # 10.37232
# n = 10개

'''
5-11. A polymer is manufactured in a batch chemical
process. Viscosity measurements are normally made on each
batch, and long experience with the process has indicated that
the variability in the process is fairly stable with 세타=20.
Fifteen batch viscosity measurements are given as follows:
724, 718, 776, 760, 745, 759, 795, 756, 742, 740, 761, 749,
739, 747, 742. A process change is made that involves switching
the type of catalyst used in the process. Following the
process change, eight batch viscosity measurements are taken:
735, 775, 729, 755, 783, 760, 738, 780. Assume that process
variability is unaffected by the catalyst change. Find a 90% CI
on the difference in mean batch viscosity resulting from the
process change. What is the practical meaning of this interval?
'''
# B15 batch (stable with 세타=20)
B15 = c(724, 718, 776, 760, 745, 759, 795, 756, 742, 740, 761, 749,
        739, 747, 742)
mean(B15) # 750.2
sd(B15) # 19.12814
# n = 15
B8 = c(735, 775, 729, 755, 783, 760, 738, 780)
mean(B8) # 756.875
sd(B8) # 21.28338
# n = 8
# 90% 신뢰구간에서의 u1-u2
(750.2-756.87)-1.65*sqrt(19**2/15+21**2/8) # -21.3533
(750.2-756.87)+1.65*sqrt(19**2/15+21**2/8) #8.0133
# 따라서, -21.35 <= u1-u2 <= 8.01

'''
5-13. Consider the polymer batch viscosity data in
Exercise 5-11. If the difference in mean batch viscosity is 10
or less, the manufacturer would like to detect it with a high
probability.
(a) Formulate and test an appropriate hypothesis using the
P-value approach. What are your conclusions?
(b) Compare the results of part (a) to the 90% CI obtained in
Exercise 5-11 and discuss your findings.
'''
# 귀무가설 : u2-u1=10

# a)
z0 = ((756.87-750.2)-10)/sqrt(19**2/15+21**2/8)
z0 # -0.3742
# P(z<=-0.37) = 0.352
# 즉, 0.05 유의수준인 경우 귀무가설은 채택된다.

# b)
'''
위에 평균 점도가 10 이하임을 증명하지 못한다.
또한 신뢰구간이 양측이기 때문에 해당 검정과 일치하지 않는다.
그러나 신뢰구간 상한값은 21.485 이상임을 알 수 있다.
'''

'''
5-14. For the laundry detergent problem in Exercise 5-12,
test the hypothesis that the mean active concentrations are the
same for both types of catalyst. What is the P-value for this
test? What are your conclusions? Compare your answer to that
found in part (b) of Exercise 5-12, and comment on why they
are the same or different.
'''
# dataset
# catalyst1
c1 = c(66.1,64.0,64.4,60.0,65.3,66.9,61.5,63.5,61.6,62.3)
c2 = c(66.3,64.7,67.6,68.5,68.3,76.4,66.1,69.9,70.6,68.7)
z0 = (mean(c1)-mean(c2))/sqrt(sd(c1)**2/10+sd(c2)**2/10)
z0 # -4.156697
# P-value = 2(1-z표준정규표(-4.15)) = 2(1-1) = 0

'''
5-15. Consider the Minitab output shown below.
#
Two-Sample T-Test and CI: X1, X2
Two-sample T for X1 vs X2
N Mean StDev SE Mean
X1 20 50.19 1.71 0.38
X2 20 52.52 2.48 0.55
Difference = mu (X1) - mu (X2)
Estimate for difference: -2.33341
95% CI for difference: (-3.69547, -0.97135)
T-Test of difference = 0 (vs not=):
T-Value = -3.47, P-Value = 0.001, DF = 38
Both use Pooled StDev = 2.1277
#
(a) Can the null hypothesis be rejected at the 0.05 level? Why?
(b) Is this a one-sided or a two-sided test?
(c) If the hypotheses had been H0: mu1-mu2 = 2 versus H1: mu1-mu2 not= 2
would you reject the null hypothesis at the 0.05 level?
(d) If the hypotheses had been H0: mu1-mu2 = 2 versus H1: mu1-mu2 < 2
would you reject the null hypothesis at
the 0.05 level? Can you answer this question without
doing any additional calculations? Why?
(e) Use the output and the t table to find a 95% upper confidence
bound on the difference in means.
(f) What is the P-value if the alternative hypothesis is
H0: mu1-mu2 = 2 versus H1: mu1-mu2 not= 2?
'''
# a)
# P-value=0.001 < 유의수준 0.05 이하이이기 때문에 귀무가설은 기각된다.

# b)
# 양측검정

# c)
# '2'가 95% 신뢰구간 내에 들지 않기 때문에 귀무가설은 기각된다.

# d)
# u1-u2=2의 P-value는 더 작기 때문에 귀무가설은 기각된다.

# e)
# u1-u2+t0.5se = -2.33341+1.69*2.1277*sqrt(1/20+1/20)
-2.33341+1.69*2.1277*sqrt(1/20+1/20) # -1.196314

# f)
# T0 = (-2.3341-2)/(2.1277*sqrt(1/20+1/20))
(-2.3341-2)/(2.1277*sqrt(1/20+1/20)) # -6.441523