import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

years = [2013, 2014, 2015, 2016, 2017]
temperatures = [5, 10, 15, 20, 17]

def draw_graph():
    pos = range(len(years))  # [0, 1, 2, 3, 4]
    
    plt.bar(pos, temperatures, align='center')

    plt.xticks(pos, years)

    plt.savefig('graph.png')
    elice_utils.send_image('graph.png')

print('막대 차트를 출력합니다.')
draw_graph()