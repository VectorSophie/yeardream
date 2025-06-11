import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils 
elice_utils = EliceUtils()
# 주량 데이터
drink_cup = pd.DataFrame({
    "cup": [22, 7, 19, 3, 10, 8, 19, 7, 15, 9, 35, 5], 
    "who": ["A", "E", "D", "B", "C", "A", "A", "A", "D", "B", "C", "B"],
    "stems": [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0]
})
print(drink_cup)

fig, ax = plt.subplots()

# 줄기-잎 그림을 그리는 코드를 작성해 주세요
plt.stem(drink_cup["stems"], drink_cup["cup"])

# 그래프를 그리는 코드입니다. 수정하지 마세요.
plt.show()
fig.savefig("stem_plot.png")
elice_utils.send_image("stem_plot.png")