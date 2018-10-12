def get_indices_of_item_weights(weights, limit):
    hash_indeces = {}
    for (index, value) in enumerate(weights):
        check = limit - value
        if check in hash_indeces:
            return (index, hash_indeces[check])
        hash_indeces[value] = index
    return ()


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    arr = [4, 6, 10, 15, 16]
    limit = 21
    x = get_indices_of_item_weights([4, 4], 8)
    print(x)
