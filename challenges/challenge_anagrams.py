def merge(left: str, right: str, length: int):
    left_index, right_index = 0, 0
    word = ""

    for _ in range(length):
        if left_index >= len(left):
            word += right[right_index]
            right_index += 1
        elif right_index >= len(right):
            word += left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            word += left[left_index]
            left_index += 1
        else:
            word += right[right_index]
            right_index += 1

    return word


def sort_word(word):
    mid = len(word) // 2
    if mid > 0:
        left = sort_word(word[:mid])
        right = sort_word(word[mid:])
        word = merge(left, right, length=len(word))
    return word


def is_anagram(first_string: str, second_string: str):
    """Faça o código aqui."""
    if first_string:
        first_string = sort_word(first_string.lower())
    if second_string:
        second_string = sort_word(second_string.lower())

    result = (
        False
        if not (first_string and second_string)
        else first_string == second_string
    )

    return (first_string, second_string, result)
