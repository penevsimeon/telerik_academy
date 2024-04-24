def count_occurrences(words: list) -> dict:
    occurrences = {}

    for word in words:

        if word in occurrences:
            occurrences[word] += 1

        else:
            occurrences[word] = 1

    return occurrences


def two_sum(numbers: list, target_sum: int) -> tuple:
    d = {}
    for i in range(len(numbers)):
        current_number = numbers[i]
        complement = target_sum - current_number
        if complement in d:
            return (d[complement], i)
        d[current_number] = i
    return (-1, -1)


def special_coins(coins: str, catalogue: str) -> int:
    catalogue_set = set(catalogue)
    count = 0

    for coin in coins:

        if coin in catalogue_set:
            count += 1

    return count


def are_isomorphic(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    d1 = {}
    d2 = {}

    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]

        if char1 in d1 and d1[char1] != char2:
            return False
        elif char2 in d2 and d2[char2] != char1:
            return False

        d1[char1] = char2
        d2[char2] = char1

    return True

# egg
# add
