def high_bp(reading):
    return max(reading)

def low_bp(reading):
    return min(reading)

def average(reading):
    return sum(reading) / len(reading)

def count(reading):
    count = 0
    for i in reading:
        if i >= 140:
            count += 1
    return count