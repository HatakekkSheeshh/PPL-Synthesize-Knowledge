"""
    Let lst be a list of integer and n be any value, use high-order function approach to write 
    function dist(lst,n) that returns the list of pairs of an element of lst and n.
"""

def dist(lst, n):
    def pair(x) -> tuple :
        return (x,n)
    return list(map(pair, lst))


print(dist([1,2,3], 4))