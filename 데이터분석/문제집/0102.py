import numpy as np

ANSWER = np.array([3, 1, 2, 2, 4, 4, 1, 3, 5, 5])

def grade_all(ar_students: np.ndarray) -> np.ndarray:
    scores = []

    for stud in ar_students:
        corr = stud == ANSWER
        score = corr.sum()
        scores.append(score)

    return np.array(scores)

def get_best_student(ar_scores: np.ndarray) -> int:
    best = ar_scores.argmax()
    return best


def stat_students(ar_scores: np.ndarray):
    mean = ar_scores.mean()
    std = ar_scores.std()
    return mean, std


def main():
    ar_stud = np.array(
        [
            [4, 4, 1, 3, 3, 3, 1, 3, 2, 4],
            [5, 5, 3, 2, 4, 2, 5, 2, 2, 4],
            [2, 4, 1, 5, 5, 5, 3, 3, 3, 5],
            [3, 5, 4, 3, 1, 3, 1, 1, 1, 4],
            [3, 2, 5, 1, 1, 4, 5, 3, 2, 3],
            [3, 2, 2, 4, 5, 2, 3, 2, 5, 5],
            [2, 4, 3, 2, 5, 2, 4, 4, 3, 4],
            [1, 3, 1, 3, 3, 5, 5, 3, 1, 5],
            [2, 5, 3, 2, 1, 5, 3, 5, 1, 2],
            [4, 2, 2, 1, 3, 5, 1, 5, 2, 1],
        ]
    )

    ar_scores = grade_all(ar_stud)
    print("모든 학생 점수:", ar_scores)

    best_student = get_best_student(ar_scores)
    print("1등 학생 번호:", best_student)

    mean, std = stat_students(ar_scores)
    print("평균:", mean)
    print("표준편차:", std)

if __name__ == "__main__":
    main()
