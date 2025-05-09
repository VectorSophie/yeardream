from matplotlib.figure import Figure
import json
from contextlib import suppress


def submit(ax1, ax2):
    submit_list = []

    value = None
    with suppress(Exception):
        axl1 = ax1.lines[0]
        value = axl1.get_xydata().tolist()
    submit_list.append(value)

    value = None
    with suppress(Exception):
        axl2 = ax2.lines[0]
        value = axl2.get_xydata().tolist()
    submit_list.append(value)

    sub_dict = {"todo": submit_list}
    with open("todo.json", "w") as f:
        json.dump(sub_dict, f, ensure_ascii=False)
