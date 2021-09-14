"""Assignment 1

Fill in the following function skeletons (deleting the 'raise NotImplementedError' lines as you go) - descriptions are provided in the PDF, and briefly in the docstring (the triple quote thing at the top of each function).

Some assert statements have been provided - write more of them to test your code!
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built
    in function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    if n > 0:
        return(n)
    if n < 0:
        n = n *-1
        return(n)
assert absolute(-1) == 1, "absolute of -1 failed"
assert absolute(-20000) == 20000, "absolute of -20000 failed"
assert absolute(-2) == 2, "absolute of -2 failed"


assert absolute(-1) == 1, "absolute of -1 failed"

def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed
    in number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
    if n < 2:
        return 1 
    else:
        factorial = 1
        #factorial is n times every number preceding it until it reaches one (ex. 5! = 5x4x3x2x1))
        while n > 1:
            factorial = n*factorial
            print (n, factorial)
            n = n-1
        print (n, factorial, "n is done running")
        return factorial
        
assert factorial(5) == 120, "factorial of 5 failed"
assert factorial(4) == 24, "factorial of 4 failed"
assert factorial(3) == 6, "factorial of 3 failed"




T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list,
    starting with the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the
            returned list)

    Returns:
        a list of every of other item in the original list starting with the first
    """


def every_other(lst:list)->list:
    return(lst[0::2])
assert every_other([1, 2, 3, 4, 5]) == [1,3,5], "every_other of [1,2,3,4,5] failed"
assert every_other([1, 2, 3, 4, 5, 6, 7]) == [1,3,5, 7], "every_other of [1,2,3,4,5,6,7] failed"

assert every_other([1, 2, 3, 4, 5]) == [1,3,5], "every_other of [1,2,3,4,5] failed"

def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list.
    Cannot use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    x = (len(lst) - 1)
    y = 0
    while x > -1:
        y = y + lst[x]
        x = x - 1
    print (x,y)
    return y
    
assert sum_list([1, 2]) == 3, "sum_list of [1,2] failed"
assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"    
assert sum_list([1, 2, 3, 4]) == 10, "sum_list of [1,2,3,4] failed"


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    return sum_list(lst)/len(lst)




assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
assert mean([1, 2, 3, 4, 5, 6, 7]) == 4, "mean of [1,2,3,4,5,6,7] failed"
assert mean([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5, "mean of [1,2,3,4,5,6,7,8,9] failed"

def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.
    If the list has an even number of values, it computes the mean of the two
    center values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    lengthList = len(lst)
    if (lengthList % 2 == 0):
        firstMiddle = lst[lengthList//2]
        secondMiddle = lst[(lengthList//2) - 1]
        median = (firstMiddle + secondMiddle) // 2
        return median
    else:
        return lst[lengthList//2]


assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"
assert median([1, 2, 3, 4, 5, 6, 7]) == 4, "median of [1,2,3,4,5, 6, 7] failed"
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5, "median of [1,2,3,4,5, 6, 7, 8, 9] failed"

def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it,
    knocking out every third name (wrapping around) until only two names are
    left. In other words, when you hit the end of the list, wrap around and keep
    counting from where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd
    first knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on
    Nathan and 'goose' on Sasha - knocking him out and leaving only Nathan and
    Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    i = 0
    current = ['duck1', 'duck2', 'goose']
    index = 0
    while len(lst) > 2:
        if  i > len(lst):
            i = i - len(lst)
        if current[index] == 'goose':
            lst.pop(i)
            if index >= 2:
                index = 0
            i = i + 1
            index = index + 1
            r
    return(lst)
    


names = ["sasha", "nathan", "jennie", "shane", "will", "sara"]
assert duck_duck_goose(names) == ["sasha", "will"]

nombres = ['sahana', 'maddy', 'charlie', 'hong']
assert duck_duck_goose(nombres) == ['sahana','hong']

theoffice = ['michael','dwight','jim','pam']
assert duck_duck_goose(theoffice) == ['michael','pam']
                                      

print("All tests passed!")
