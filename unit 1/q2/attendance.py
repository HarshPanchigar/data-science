def calculate_percentage(attended, total):
    return (attended / total) * 100

def identify(attendance):
    res = []
    for i in attendance:
        if i < 75:
            res.append(i)
    return res


def average(attendance):
    return sum(attendance) / len(attendance)