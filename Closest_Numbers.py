def closestNumbers(arr):
    new_arr = sorted(arr)
# karşılaştırma işlemleri için sınırsız bir üst değer olarak kullanılır.
    min_diff = float('inf')
    closest_pairs = []

    for i in range(len(new_arr) - 1):
        diff = new_arr[i + 1] - new_arr[i]
        if diff < min_diff:
            min_diff = diff
            closest_pairs = [new_arr[i], new_arr[i + 1]]
        elif diff == min_diff:
# extend() metodu, Python listelerinde kullanılan ve bir listenin sonuna başka bir listeyi eklemek için kullanılır.
            closest_pairs.extend([new_arr[i], new_arr[i + 1]])

    return closest_pairs