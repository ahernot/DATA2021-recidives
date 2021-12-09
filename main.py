import pandas as pd
import numpy as np
import datetime as dt

from functions import sigmoid, seuil
from preferences import *

path = 'src/data.csv'
df  = pd.read_csv(path, sep=';')


columns = df.columns

# regarder la distance entre score et récidive

# Drop is_recid == -1
df = df[df['is_recid'] != -1]
df.reset_index(inplace=True)

# Indices
indices_0 = df[df['is_recid'] == 0].index  # no recidive
indices_1 = df[df['is_recid'] == 1].index  # recidive



# CORRELATION
import seaborn as sn
import matplotlib.pyplot as plt


# Create sex_val
male_ids   = df[df['sex'] == 'Male'].index
female_ids = df[df['sex'] == 'Female'].index
sex_val = np.empty(df.shape[0])
sex_val[male_ids] = 1
sex_val[female_ids] = -1
df.insert(3, 'sex_val', sex_val)


# Calculate jail start & stop
jail_start = df['c_jail_in']
jail_start[pd.isna(jail_start)] = '1900-01-01 00:00:00'
jail_start_dt = np.array([dt.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S') for datetime_str in jail_start])

jail_stop = df['c_jail_out']
jail_stop[pd.isna(jail_stop)] = '1900-01-01 00:00:01'
jail_stop_dt = np.array([dt.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S') for datetime_str in jail_stop])

jail_duration = jail_stop_dt - jail_start_dt
jd_l = np.array([jd.days for jd in jail_duration])
jd_l[jd_l <= 0.] = 0.

df.insert(10, 'jail_start_dt', jail_start_dt)
df.insert(11, 'jail_stop_dt', jail_stop_dt)
df.insert(12, 'jail_duration', jd_l)



# CORRELATION MATRIX
corrMatrix = df[SELECTED_FEATURES].corr()
sn.heatmap(np.abs(corrMatrix), annot=True)
plt.show()











# Extract scores and recivide
scores = (df['decile_score'] / 10).to_numpy()
recid  = df['is_recid'].to_numpy()
#recid = sigmoid(recid)  # ponderate using sigmoid function (wrong given the percentages in each label)
recid = seuil(recid)


# Calculate distances
distances = np.abs(scores - recid)
# Pénalisation des faux négatifs: K * (1 - score) * récidive * nb_récidives
dist_mult = np.exp(1.1 * (1 - scores) * recid) # * nb_récidives  ## MULTIPLICATEUR TROP ABRUPT, CAR CAN BE =0 (if no récidive)
distances = np.multiply (distances, dist_mult)

score_mean_all = np.mean(distances)
score_mean_0 = np.mean(distances[indices_0])
score_mean_1 = np.mean(distances[indices_1])

print(f'\
mean(label==0):   {score_mean_0}\n\
mean(label==1):   {score_mean_1}\n\
mean(label==all): {score_mean_all}\
')

