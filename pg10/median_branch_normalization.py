def normalize(batch):
    from statistics import median
    round(median(batch), 1)
    median = round(median(batch), 1)
    return list(map(lambda x : x - median, batch))

def batch_norm(alist, batch_size):
    for low in range(0, len(alist), batch_size):
        up = low + batch_size
        yield normalize(alist[low : up])

print(list(batch_norm([1, 2, 3], 2)))