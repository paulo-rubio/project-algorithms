def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    firstI = 0
    lastI = len(word)-1
    while firstI < lastI:
        if word[firstI] != word[lastI]:
            return False
        firstI += 1
        lastI -= 1
    return True
