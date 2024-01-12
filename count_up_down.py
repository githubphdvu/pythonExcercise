def count_up(start, stop):
    """Print all numbers from start to stop (inclusive)"""

    while start <= stop:
        print(start)
        start+= 1
count_up(1,5)        

def count_down(start,stop):
    for i in range(start,stop-1,-1):
        print(i)
count_down(5,1)