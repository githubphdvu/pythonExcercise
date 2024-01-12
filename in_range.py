def in_range(nums, lowest, highest):
    """Print numbers inside range
    For example:
      in_range([1,2,3,4,5],2,4)
    should print:
      2 fits
      3 fits
      4 fits
    """
    for num in nums:
        if num >= lowest and num <= highest:
            print(f"{num} fits")
            
in_range([1,2,3,4,5],2,4)           
