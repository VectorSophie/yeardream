import pandas as pd

age = pd.Series([10,15,20,25,30], name= 'age')
print(age,'\n')

class_name = {'국어' : 90,'영어' : 70,'수학' : 100,'과학' : 80}
class_series = pd.Series(class_name)
print(class_series,'\n')

df = pd.DataFrame([[2,3],[3,4],[5,6]])
print(df,'\n')