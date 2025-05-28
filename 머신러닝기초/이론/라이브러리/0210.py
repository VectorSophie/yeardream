import seaborn as sns 
import matplotlib.pyplot as plt 

from elice_utils import EliceUtils
elice_utils = EliceUtils()

df = sns.load_dataset('tips') 

sns_plot_size = sns.countplot(x='size', data=df)

g = sns.jointplot(x="total_bill",y="tip",data=df, kind="resid")

fig = sns_plot_size.get_figure()
fig.savefig("plot_siz.png")
elice_utils.send_image("plot_siz.png")

g.savefig("plot.png")
elice_utils.send_image("plot.png")