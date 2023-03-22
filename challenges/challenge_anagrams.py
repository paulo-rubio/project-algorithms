def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    freq1 = {}
    freq2 = {}
    for char in first_string:
        freq1[char] = freq1.get(char, 0) + 1
    for char in second_string:
        freq2[char] = freq2.get(char, 0) + 1
    
    # Compara as frequências
    for char in freq1:
        if char not in freq2 or freq1[char] != freq2[char]:
            return False
    
    return True