import seaborn as sns 
import matplotlib.pyplot as plt 

from elice_utils import EliceUtils
elice_utils = EliceUtils()

df = sns.load_dataset('tips') 

x_data = df['total_bill']
 
y_data = df['tip']

sns_plot = sns.regplot(x_data,y_data,color='red')

fig = sns_plot.get_figure()
fig.savefig("plot.png")
elice_utils.send_image("plot.png")