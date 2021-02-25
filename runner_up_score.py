scores = [6, 6, 6, 6, 6]
scores2 = [2, 3, 6, 6, 5]
scores3 = [-1, -2, -3, -4, -1]


def find_runner_up(scores):
    scores.sort(reverse=True)
    max_score = max(scores)
    scores.remove(max_score)
    for score in scores:
        if score == max_score:
            scores.remove(score)
    print(scores)
    print("The runner up score is:", max(scores))


find_runner_up(scores)
find_runner_up(scores2)
find_runner_up(scores3)
