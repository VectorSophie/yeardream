from elice_utils import EliceUtils
elice_utils = EliceUtils()
import pandas as pd

a = pd.Series([20, 15, 30, 25, 35], name='age')
b = pd.Series([68.5, 60.3, 53.4, 74.1, 80.7], name='weight')
c = pd.Series([180, 165, 155, 178, 185], name ='height')

human = pd.DataFrame([a,b,c])
print(human,'\n')

def main():
    
    print(human.loc['age'],'\n')
    print(human.iloc[0],'\n')
 
    print(human.loc['weight':'height'],'\n')
    print(human.iloc[1:3],'\n')
     
    sex = ['F','M','F','M','F']

    human.loc['sex'] = sex
    print(human,'\n')

    tmp = human.drop(['height'])
    print(tmp,'\n')

if __name__ == "__main__":
    main()
