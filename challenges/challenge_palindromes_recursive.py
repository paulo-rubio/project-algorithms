def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    elif low_index > high_index:
        return True

    else:
        return word[low_index] == word[high_index] and is_palindrome_recursive(word, low_index + 1, high_index - 1)
