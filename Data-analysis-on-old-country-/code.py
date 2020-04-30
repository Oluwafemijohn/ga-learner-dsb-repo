# --------------
#from io import StringIO
import numpy as np
new_record = [[50, 9, 4, 1, 0, 0, 40, 0]]
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
census = np.concatenate((data, np.asarray(new_record)))
print("\nCensus data: \n\n ", census)


# --------------
#Code starts here
age = census[:, 0]
print(age)
max_age = max(age)
min_age = min(age)
age_mean = np.mean(age)
print(age_mean)
#import statistics 
from statistics import stdev 
age_std = np.std(age)
print(age_std)




# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
minority_race = 3
print(minority_race)






























# race = census[:, 2]

#race = [0, 0, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
# print(race)
# race_0 = []
# race_1 = []
# race_2 = []
# race_3 = []
# race_4 = []
# for i in race:
#     if i == 0:
#         race_0.append(i)
#     elif (i ==1):
#         race_1.append(i)
#     elif (i ==2):
#         race_2.append(i)
#     elif (i ==3):
#         race_3.append(i)
#     elif (i ==4):
#         race_4.append(i)

# len_0 = len(race_0)
# len_1 = len(race_1)
# len_2 = len(race_2)
# len_3 = len(race_3)
# len_4 = len(race_4)
# race =["race_0", "race_1", "race_2", "race_3", "race_4"]
# minority_race = len(race_3)
# print(minority_race)





# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
# from statistics import mean
avg_pay_high = round(high[:,7].mean(), 2)
avg_pay_low = round(low[:,7].mean(), 2)
print(avg_pay_high)
print(avg_pay_low)


