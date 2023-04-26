def is_palindrome_iterative(word):
    """Faça o código aqui."""
    reversed_word = str()
    for index in range(len(word) - 1, -1, -1):
        reversed_word += word[index]

    return (reversed_word == word) and not word == ""
