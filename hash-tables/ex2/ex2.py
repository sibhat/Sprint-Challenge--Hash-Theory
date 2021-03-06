def hashing(string, size):
    # ans = 1
    if string:
        # for x in string:
        #     ans += ord(x) * 24
        return hash(string) % size
    return None


def reconstruct_trip(tickets):
    storage = {}
    ans = []
    for ticket in tickets:
        storage[ticket[0]] = ticket[1]

    starting_city = storage[None]
    ans.append(starting_city)
    try:
        destination_city = storage[starting_city]
    except KeyError:
        print("error")
        return []

    while(destination_city):
        ans.append(destination_city)
        destination_city = storage[destination_city]
    return ans


def reconstruct_trip_Hashed(tickets):
    hashed_storage = {}
    ans = []
    for ticket in tickets:
        key = hashing(ticket[0], len(tickets) * 5)
        if key in hashed_storage:
            print("handle this situtaiton")
        else:
            hashed_storage[key] = ticket[1]

    starting_city = hashed_storage[None]
    ans.append(starting_city)

    starting_city_code = hashing(starting_city, len(tickets) * 5)
    try:
        destination_city = hashed_storage[starting_city_code]
    except KeyError:
        print("error")
        return []

    while(destination_city):
        ans.append(destination_city)
        starting_city_code = hashing(destination_city, len(tickets) * 5)

        destination_city = hashed_storage[destination_city]
    return ans


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    long_set = [
      ('PIT', 'ORD'),
      ('XNA', 'CID'),
      ('SFO', 'BHM'),
      ('FLG', 'XNA'),
      (None, 'LAX'),
      ('LAX', 'SFO'),
      ('CID', 'SLC'),
      ('ORD', None),
      ('SLC', 'PIT'),
      ('BHM', 'FLG'),
    ]
    ans = reconstruct_trip(long_set)
    print("ans is ", ans)
