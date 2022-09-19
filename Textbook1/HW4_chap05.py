# HW4

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

'''
5-3. Two machines are used for filling plastic bottles with a
net volume of 16.0 ounces. The fill volume can be assumed
normal, with standard deviation 1  0.020 and 2  0.025
ounces. A member of the quality engineering staff suspects
that both machines fill to the same mean net volume, whether
or not this volume is 16.0 ounces. A random sample of 10 bottles
is taken from the output of each machine.
# 1) Machine1: 16.03, 16.01, 16.04, 15.96, 16.05, 15.98, 16.05, 16.02, 16.02, 15.99
# 2) Machine2: 16.02, 16.03, 15.97, 16.04, 15.96, 16.02, 16.01, 16.01, 15.99, 16.00
(a) Do you think the engineer is correct? Use the P-value
approach.
(b) If 알파=0.05, what is the power of the test in part (a) for a
true difference in means of 0.04?
(c) Find a 95% CI on the difference in means. Provide a practical
interpretation of this interval.
(d) Assuming equal sample sizes, what sample size should be
used to ensure that 베타=0.01 if the true difference in
means is 0.04? Assume that 알파=0.05.
'''

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

'''
5-9. Consider the situation described in Exercise 5-5. What
sample size would be required in each population if we wanted
the error in estimating the difference in mean burning rates to
be less than 4 cm/s with 99% confidence?
'''

'''
5-10. Consider the road octane test situation described in
Exercise 5-8. What sample size would be required in each
population if we wanted to be 95% confident that the error in
estimating the difference in mean road octane number is less
than 1?
'''

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

'''
5-14. For the laundry detergent problem in Exercise 5-12,
test the hypothesis that the mean active concentrations are the
same for both types of catalyst. What is the P-value for this
test? What are your conclusions? Compare your answer to that
found in part (b) of Exercise 5-12, and comment on why they
are the same or different.
'''

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