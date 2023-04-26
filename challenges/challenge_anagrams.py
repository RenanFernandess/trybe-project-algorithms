def merge(word, start, mid, end):
    first_half = word[start:mid]
    second_half = word[mid:end]
    first_index, second_index = 0, 0

    for index in range(start, end):
        if first_index >= len(first_half):
            word[index] = second_half[second_index]
            second_index += 1
        elif second_index >= len(second_half):
            word[index] = first_half[first_index]
            first_index += 1
        elif first_half[first_index] < second_half[second_index]:
            word[index] = first_half[first_index]
            first_index += 1
        else:
            word[index] = second_half[second_index]
            second_index += 1


def sort_word(word, start=0, end=None):
    if type(word) == str:
        word = [*word]
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (start + end) // 2
        sort_word(word, start, end=mid)
        sort_word(word, start=mid, end=end)
        merge(word=word, start=start, mid=mid, end=end)
    return "".join(word)


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
