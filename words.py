def print_upper_words(words):
    """Print each word on separate line, uppercased.
        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """
    for word in words:
        print(word.upper())
def print_upper_words2(words):
    """Print each word on sep line, uppercased, if starts with E or e.
        >>> print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())
def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given
        >>> print_upper_words3(["abc","Ed","Al","xyz"],must_start_with=["A", "E"])
        ED
        AL
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
