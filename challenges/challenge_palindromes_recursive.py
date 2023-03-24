def is_palindrome_recursive(wd, li, hi):
    if len(wd) == 0:
        return False

    elif li > hi:
        return True

    else:
        return wd[li] == wd[hi] and is_palindrome_recursive(wd, li + 1, hi - 1)
