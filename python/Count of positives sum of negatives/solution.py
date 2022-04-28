def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    count = 0
    sum = 0
    for number in arr:
        if number > 0:
            count += 1
        elif number < 0:
            sum += number
            
    return [count,sum]
