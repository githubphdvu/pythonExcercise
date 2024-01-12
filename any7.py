def any7(A):
    """Are any of these numbers a 7? (True/False)"""
    for a in A:
        if a == 7: return True
    return False
print("should be true", any7([1,7]))
print("should be false", any7([1,2,]))

