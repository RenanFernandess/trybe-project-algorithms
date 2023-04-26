def is_palindrome_recursive(word, low_index=0, high_index=1):
    """Faça o código aqui."""
    if word == "":
        return False
    p = word[-1]
    if len(word) > 1:
        p += is_palindrome_recursive(word[:-1], low_index=(low_index + 1))
    if low_index == 0:
        return word == p
    return p
