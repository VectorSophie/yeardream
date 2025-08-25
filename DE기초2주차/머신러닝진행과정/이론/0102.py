import pandas as pd
import numpy as np

DATA_PATH = './data/taxi_fare_data.csv'

def load_csv(path):

    data_frame = pd.read_csv(DATA_PATH)
    
    return data_frame

def statistical_features(data):
    
    _min = np.min(data)
    _max = np.max(data)
    _mean = np.mean(data)
    _median = np.median(data)
    _var = np.var(data)
    _std = np.std(data)
    
    return _min, _max, _mean, _median, _var, _std

df = load_csv(DATA_PATH)

df.info()

f_min, f_max, f_mean, f_median, f_var, f_std = statistical_features(df['fare_amount'])
print('\nfare_amount의', '최솟값:', f_min ,'최댓값:', f_max ,'평균값:', f_mean ,'중앙값:', f_median ,'분산값:', f_var ,'표준편차값:', f_std)

p_min, p_max, p_mean, p_median, p_var, p_std = statistical_features(df['passenger_count'])
print('passenger_count의', '최솟값:', p_min ,'최댓값:', p_max ,'평균값:', p_mean ,'중앙값:', p_median ,'분산값:', p_var ,'표준편차값:', p_std)