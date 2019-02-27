import time
from itertools import islice
from functools import reduce
"""
Generator of infinite fibbonaci sequence numbers
"""
def inifinteFibbo():
    first = 0; second = 1 
    while(True):
        yield first
        addition = first + second
        first = second
        second = addition

"""
Use the islice function to generate fibbonaci elements (that will not be taken into account) until lower, 
and start iterating from there until higher (this elements will be taken into account) so, if lower is 2 
so at the end, generate fibbonaci elements in range [lower, higher) taking into account that the first position will be 0
"""
def fibboInRange(lower, higher):
    return islice(inifinteFibbo(), lower, higher)
