# Term Project
'''
About this file : cancer_patient_data.csv
This dataset contains information on patients with lung cancer, 
including their age, gender, air pollution exposure, alcohol use, dust allergy, 
occupational hazards, genetic risk, chronic lung disease, balanced diet, obesity, 
smoking status, passive smoker status, chest pain, coughing of blood, fatigue levels, 
weight loss, shortness of breath, wheezing, swallowing difficulty, clubbing of finger nails, 
frequent colds , dry coughs , and snoring. 
By analyzing this data we can gain insight into what causes lung cancer and how best to treat it.

- Age: The age of the patient. (Numeric)
- Gender: The gender of the patient. (Categorical)
- Air Pollution: The level of air pollution exposure of the patient. (Categorical)
- Alcohol use: The level of alcohol use of the patient. (Categorical)
- Dust Allergy: The level of dust allergy of the patient. (Categorical)
- OccuPational Hazards: The level of occupational hazards of the patient. (Categorical)
- Genetic Risk: The level of genetic risk of the patient. (Categorical)
- chronic Lung Disease: The level of chronic lung disease of the patient. (Categorical)
- Balanced Diet: The level of balanced diet of the patient. (Categorical)
- Obesity: The level of obesity of the patient. (Categorical)
- Smoking: The level of smoking of the patient. (Categorical)
- Passive Smoker: The level of passive smoker of the patient. (Categorical)
- Chest Pain: The level of chest pain of the patient. (Categorical)
- Coughing of Blood: The level of coughing of blood of the patient. (Categorical)
- Fatigue: The level of fatigue of the patient. (Categorical)
- Weight Loss: The level of weight loss of the patient. (Categorical)
- Shortness of Breath: The level of shortness of breath of the patient. (Categorical)
- Wheezing: The level of wheezing of the patient. (Categorical)
- Swallowing Difficulty: The level of swallowing difficulty of the patient. (Categorical)
- Clubbing of Finger Nails: The level of clubbing of finger nails of the patient. (Categorical)
'''

import pandas as pd
pd.set_option('display.max_columns',None)
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
import seaborn as sn
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import scipy as sp
from scipy import stats
from statsmodels.sandbox.stats.multicomp import MultiComparison
from statsmodels.stats.multicomp import pairwise_tukeyhsd

### 1. Data Loading
c_data = pd.read_csv('lung_cancer_data.csv')
c_data.info()
'''
RangeIndex: 1000 entries, 0 to 999
Data columns (total 26 columns):
 #   Column                    Non-Null Count  Dtype 
---  ------                    --------------  ----- 
 0   index                     1000 non-null   int64 
 1   Patient Id                1000 non-null   object
 2   Age                       1000 non-null   int64  > 나이(숫자형)
 3   Gender                    1000 non-null   int64  > 성별(범주형)
 4   Air Pollution             1000 non-null   int64  > 대기오염정도(1-8 범주형)
 5   Alcohol use               1000 non-null   int64  
 6   Dust Allergy              1000 non-null   int64 
 7   OccuPational Hazards      1000 non-null   int64  > 직업적 위험
 8   Genetic Risk              1000 non-null   int64  > 유전
 9   chronic Lung Disease      1000 non-null   int64  > 만성 폐질환
 10  Balanced Diet             1000 non-null   int64 
 11  Obesity                   1000 non-null   int64  > 비만
 12  Smoking                   1000 non-null   int64 
 13  Passive Smoker            1000 non-null   int64  > 수동 흡련자
 14  Chest Pain                1000 non-null   int64 
 15  Coughing of Blood         1000 non-null   int64 
 16  Fatigue                   1000 non-null   int64  > 피로
 17  Weight Loss               1000 non-null   int64  
 18  Shortness of Breath       1000 non-null   int64  > 숨가쁨
 19  Wheezing                  1000 non-null   int64  > 천명(음)
 20  Swallowing Difficulty     1000 non-null   int64  > 식이장애 : 삼키기 어려움
 21  Clubbing of Finger Nails  1000 non-null   int64  > 손톱 곤봉
 22  Frequent Cold             1000 non-null   int64  > 잦은 감기
 23  Dry Cough                 1000 non-null   int64  > 마른 기침
 24  Snoring                   1000 non-null   int64  > 코골이
 25  Level                     1000 non-null   object
dtypes: int64(24), object(2)
> 숫자형 데이터 Age(나이)를 제외하고는 전부 범주형 데이터
'''
c_data.head()
'''
  index Patient Id  Age  Gender  ...  Frequent Cold  Dry Cough  Snoring   Level
0      0         P1   33       1  ...              2          3        4     Low
1      1        P10   17       1  ...              1          7        2  Medium
2      2       P100   35       1  ...              6          7        2    High
3      3      P1000   37       1  ...              6          7        5    High
4      4       P101   46       1  ...              4          2        3    High
'''
## index와 Patient ID 변수 제거
cancer_data = c_data.iloc[:,2:]
## 독립변수(X)와 종속변수(y) 분리
X = cancer_data.iloc[:,:23] # 전부 숫자형 데이터
y = cancer_data.iloc[:,23] # 범주형 데이터
# 대기오염과 간암 발병 데이터 추출
cancer_poll = cancer_data.iloc[:,[2,23]]

### 2. EDA : 데이터 전처리
## 1) 결측치(NaN)
# 독립변수
X.isnull().any() # 결측치 없음
# 종속변수
y.isnull().any()
'''Level                       False'''
## 2) 이상치
# 독립변수
X.Age.describe() # 이상치 없음
'''
count    1000.000000
mean       37.174000
std        12.005493
min        14.000000
25%        27.750000
50%        36.000000
75%        45.000000
max        73.000000
Name: Age, dtype: float64
'''
# 종속변수
y.unique()
'''array(['Low', 'Medium', 'High'], dtype=object)'''
plt.pie(y.value_counts()) # 시각화
## 3) 데이터 인코딩
# 종속변수의 원-핫 인코딩
y_onehot = pd.get_dummies(data=y,columns=['Low', 'Medium', 'High'],drop_first=False)
y_onehot.head()
'''
   High  Low  Medium
0     0    1       0
1     0    0       1
2     1    0       0
3     1    0       0
4     1    0       0
'''
# 종속변수의 레이블 인코딩
encoder = LabelEncoder()
y_label = encoder.fit_transform(y)
cancer_data = cancer_data.iloc[:,:23]
cancer_data['Level']=y_label

### 3. 상관성 분석 및 주성분분석
## 1) 상관성 분석
# 독립변수 간 상관성 분석
X.corr()
cmap = sn.light_palette("darkgray",as_cmap=True)
sn.heatmap(X.corr(),annot=True,cmap=cmap) # 시각화
plt.show()
# 독립변수와 종속변수 상관성 분석
cancer_data.corr()['Level']
'''
Age                         0.042631
Gender                      0.086222
Air Pollution              -0.577269
Alcohol use                -0.434071
Dust Allergy               -0.264926
OccuPational Hazards       -0.363748
Genetic Risk               -0.423382
chronic Lung Disease       -0.432405
Balanced Diet              -0.618781
Obesity                    -0.561961
Smoking                    -0.611087
Passive Smoker             -0.638409
Chest Pain                 -0.494704
Coughing of Blood          -0.631118
Fatigue                    -0.403276
Weight Loss                -0.020537
Shortness of Breath        -0.140178
Wheezing                    0.167773
Swallowing Difficulty      -0.012880
Clubbing of Finger Nails    0.116746
Frequent Cold              -0.171678
Dry Cough                  -0.228720
Snoring                     0.014280
Level                       1.000000
'''
# 대기오염과 간암 발병율 상관성 분석
cancer_poll.corr() # -0.577269 = 상관성이 매우 낮음
## 2) 주성분 분석
# 차원축소
pca = PCA()
X_pca = pca.fit_transform(X)
# 주성분 분산비율 확인
var_ratio = pca.explained_variance_ratio_
'''
array([5.95422495e-01, 1.80039661e-01, 5.59291534e-02, 3.62639183e-02,
       2.82970894e-02, 2.13689474e-02, 1.18742208e-02, 1.11445233e-02,
       1.03793606e-02, 9.70021555e-03, 7.97569867e-03, 5.50767478e-03,
       5.21321024e-03, 4.52580787e-03, 4.16255753e-03, 3.04464536e-03,
       2.37625878e-03, 1.97278375e-03, 1.58181184e-03, 1.35868051e-03,
       7.66722709e-04, 6.22761545e-04, 4.71801856e-04])
> 10번째 주성분부터 누적 분산비율 0.95 이상
'''
plt.plot(var_ratio,color='r',linestyle='--',marker='o')
plt.show()
# 주성분 3개 추출
X_3pca = X_pca[:,:3]
X_3pca = pd.DataFrame(X_3pca)
X_3pca.corr()
cmap = sn.light_palette("darkgray",as_cmap=True)
sn.heatmap(X_3pca.corr(),annot=True,cmap=cmap) # 시각화
plt.show()
know_X3 = np.array(X_3pca)
# 주성분 10개 추출
X_10pca = X_pca[:,:10]
X_10pca = pd.DataFrame(X_10pca)
X_10pca.corr()
cmap = sn.light_palette("darkgray", as_cmap=True)
sn.heatmap(X_10pca.corr(), annot=True, cmap=cmap) # 시각화
plt.show()
know_X10 = np.array(X_10pca)

### 3. KNN 알고리즘
knn=KNeighborsClassifier(n_neighbors=3)
## 1) 주성분 3개
X_train3,X_test3,y_train3,y_test3 = train_test_split(know_X3,y_label,
                                                     test_size=0.2,
                                                     random_state=123)
model3=knn.fit(X=X_train3,y=y_train3)
y_pred3=model3.predict(X=X_test3)
# 모델 평가
confusion_matrix(y_test3,y_pred3)
'''
array([[78,  0,  0],
       [ 0, 67,  1],
       [ 0,  1, 53]], dtype=int64)
'''
accuracy_score(y_test3,y_pred3) # 0.99
classification_report(y_test3,y_pred3)
## 2) 주성분 10개
X_train10,X_test10,y_train10,y_test10 = train_test_split(know_X10,y_label,
                                                         test_size=0.2,
                                                         random_state=456)
model10=knn.fit(X=X_train10,y=y_train10)
y_pred10=model10.predict(X=X_test10)
# 모델 평가
confusion_matrix(y_test10,y_pred10)
'''
array([[69,  0,  0],
       [ 0, 65,  0],
       [ 0,  0, 66]], dtype=int64)
'''
accuracy_score(y_test10,y_pred10) # 1.0
classification_report(y_test10,y_pred10)

### 4. ANOVA
## 1) 범주(Level) 별 Air Pollution Level 분리
group1 = np.array(c_data[c_data.Level == 'Low']['Air Pollution'])
group2 = np.array(c_data[c_data.Level == 'Medium']['Air Pollution'])
group3 = np.array(c_data[c_data.Level == 'High']['Air Pollution'])
## 2) 시각화
# 박스플롯
plt.boxplot([group1,group1,group3],labels=['Low','Medium','High'],showmeans=True)
plt.show()
# 산점도
sn.scatterplot(x='Level',y='Air Pollution',data=cancer_data)
plt.show()
## 3) 정규성 검정
stats.shapiro(c_data['Air Pollution'][c_data.Level=='Low'])
# statistic=0.8597692847251892, pvalue=6.293161512941465e-16
stats.shapiro(c_data['Air Pollution'][c_data.Level=='Medium'])
# statistic=0.8224581480026245, pvalue=8.061549221528485e-19
stats.shapiro(c_data['Air Pollution'][c_data.Level=='High'])
# statistic=0.7332934737205505, pvalue=8.846435285859513e-24
# 4) 등분산성 검정
F_statistic, pVal = stats.f_oneway(group1, group2, group3)
F_statistic # 466.7855900468051
pVal # 8.613026974894385e-144
## 5) ANOVA 분석
F_statistic, pVal = stats.f_oneway(group1, group2, group3)
F_statistic # 466.7855900468051
pVal # 8.613026974894385e-144
# 모델 생성
df = pd.DataFrame(c_data,columns=['Air Pollution','Level'])   
df['AirPoll'] = df['Air Pollution'] 
model = ols('AirPoll ~ C(Level)', df).fit()
print(anova_lm(model))
'''
             df       sum_sq     mean_sq          F         PR(>F)
C(Level)    2.0  1991.545087  995.772543  466.78559  8.613027e-144
Residual  997.0  2126.854913    2.133255        NaN            NaN
'''
## 6) 사후분석
comp = MultiComparison(df['AirPoll'],df['Level'])
#  Bonferroni correction
result = comp.allpairtest(stats.ttest_ind,method='bonf')
result[0]
# Tuckey's HSD
hsd = pairwise_tukeyhsd(df['AirPoll'],df['Level'],alpha=0.05)
hsd.summary()
