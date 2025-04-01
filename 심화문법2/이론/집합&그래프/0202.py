import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from elice_utils import EliceUtils
elice_utils = EliceUtils()

dates = ["1월 {}일".format(day) for day in range(1, 32)]
temperatures = list(range(1, 32))

pos = range(len(dates))

font = fm.FontProperties(fname='./NanumBarunGothic.ttf')

plt.bar(pos, temperatures, align='center')

plt.xticks(pos, dates, rotation='vertical', fontproperties=font)

plt.title('1월 중 기온 변화', fontproperties=font)

plt.ylabel('온도', fontproperties=font)

plt.tight_layout()

plt.savefig('graph.png')
elice_utils.send_image('graph.png')