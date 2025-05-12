from elice_utils import EliceUtils
import matplotlib.pyplot as plt
elice_utils = EliceUtils()
# 술자리 참석 상대도수 데이터 
labels = ["A", "B", "C", "D", "E"]
ratio = [33,25,17,17,8]
    
# 원형 그래프 
fig, ax = plt.subplots()

# Q1. 원형 그래프를 만드는 코드를 작성해 주세요
plt.pie(ratio,labels = labels)
plt.axis("equal")

# 그래프를 그리는 코드입니다. 수정하지 마세요.
plt.show()
fig.savefig("pie_plot.png")
elice_utils.send_image("pie_plot.png")