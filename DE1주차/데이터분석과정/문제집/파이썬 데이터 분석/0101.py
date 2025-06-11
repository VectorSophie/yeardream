def scores_to_dict(scores):
    
    data = {}

    for i in scores:
        i = int(i)
        if i not in data.keys():
            data[i] = 1
        else:
            data[i] += 1

    return data

def get_min_max(data):

    min_value = min(data.keys())
    max_value = max(data.keys())

    return min_value, max_value


def get_max_count_value(data):

    max_count = max(data.values())

    max_count_num = 1

    for k in sorted(data.keys()):
	    if data[k] == max_count:
		    max_count_num = k

    return max_count_num


def main():

    N = int(input())

    scores = input().split(" ")

    data = scores_to_dict(scores)

    min_value, max_value = get_min_max(data)

    max_count_num = get_max_count_value(data)

    print(max_value, min_value, max_count_num)

if __name__ == "__main__":
    main()
