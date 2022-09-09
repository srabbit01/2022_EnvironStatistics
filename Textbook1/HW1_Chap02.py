# HW1

import statistics as st # 계산 모듈
from matplotlib import pyplot as plt # 그래프 모듈

'''
2-2. In Applied Life Data Analysis (Wiley, 1982), Wayne
Nelson presents the breakdown time of an insulating fluid
between electrodes at 34 kV. The times, in minutes, are as follows:
0.19, 0.78, 0.96, 1.31, 2.78, 3.16, 4.15, 4.67, 4.85, 6.50,
7.35, 8.01, 8.27, 12.06, 31.75, 32.52, 33.91, 36.71, and 72.89.
Calculate the sample average and sample standard deviation.
Construct a dot diagram of the data.
'''
time = [0.19, 0.78, 0.96, 1.31, 2.78, 3.16, 4.15, 4.67, 4.85, 6.50,
        7.35, 8.01, 8.27, 12.06, 31.75, 32.52, 33.91, 36.71, 72.89]
electrode = [34] * len(time)
st.mean(time) # 14.358947368421052
st.stdev(time) # 18.880454883508158
plt.scatter(x=time,y=electrode) # dot diagram
plt.xlabel('Times')
plt.ylabel('Electrodes(kV)')
plt.show()

'''
2-3. Seven oxide thickness measurements of wafers are
studied to assess quality in a semiconductor manufacturing
process. The data (in angstroms) are 1264, 1280, 1301, 1300,
1292, 1307, and 1275. Calculate the sample average and sample
standard deviation. Construct a dot diagram of the data.
'''
tickness = [1264, 1280, 1301, 1300, 1292, 1307, 1275]
zero = [0] * len(tickness)
st.mean(tickness) # 1288.4285714285713
st.stdev(tickness) # 15.799336936056767
plt.scatter(tickness, y=zero)
ax = plt.gca() # y축 눈금 없애기
ax.axes.yaxis.set_visible(False)
plt.xlabel('Tickness')
plt.show()

'''
2-4. An article in the Journal of Structural Engineering
(Vol. 115, 1989) describes an experiment to test the yield
strength of circular tubes with caps welded to the ends. The
first yields (in kN) are 96, 96, 102, 102, 102, 104, 104, 108,
126, 126, 128, 128, 140, 156, 160, 160, 164, and 170.
Calculate the sample average and sample standard deviation.
Construct a dot diagram of the data.
'''
fy = [96, 96, 102, 102, 102, 104, 104, 108,
      126, 126, 128, 128, 140, 156, 160, 160, 164, 170]
zero = [0] * len(fy)
st.mean(fy) # 126.22222222222223
st.stdev(fy) # 26.138894966416608
plt.scatter(fy, y=zero)
ax = plt.gca()
ax.axes.yaxis.set_visible(False)
plt.xlabel('FirstYields(kN)')
plt.show()

'''
2-6. Preventing fatigue crack propagation in aircraft structures
is an important element of aircraft safety. An engineering
study to investigate fatigue crack in n  9 cyclically loaded
wing boxes reported the following crack lengths (in mm):
2.13, 2.96, 3.02, 1.82, 1.15, 1.37, 2.04, 2.47, and 2.60.
Calculate the sample average and sample standard deviation.
Construct a dot diagram of the data.
'''
cl = [2.13, 2.96, 3.02, 1.82, 1.15, 1.37, 2.04, 2.47, 2.60]
zero = [0] * len(cl)
st.mean(cl) # 2.1733333333333333
st.stdev(cl) # 0.6560106706449218
plt.scatter(cl, y=zero)
ax = plt.gca()
ax.axes.yaxis.set_visible(False)
plt.xlabel('CrackLengths(mm)')
plt.show()

'''
2-9. For each of Exercises 2-1 through 2-8, discuss whether the
data result from an observational study or a designed experiment.
- Observational Study: 2-1, 2-2, 2-3, 2-5, 2-6, 2-7
- Designed Experiment: 2-4, 2-8
'''

