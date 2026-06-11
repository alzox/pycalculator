from math import remainder
from ..parser import scanner
import random
import string

def test_numbers_fuzz():
    for _ in range(100):
        num = str(random.randint(0,1000000000000000000))
        results, remainder = scanner.scan(num)
        assert len(results) == 1
        assert results[0][1] == num

def test_string_fuzz():
    for _ in range(100):
        characters = '()+*-/' + string.digits
        test_string = ''.join(random.choices(characters, k=5))
        results, remainder = scanner.scan(test_string)
        assert len(remainder) == 0  

def test_parenthesis():
    results, remainder = scanner.scan("(())")
    assert len(results) == 4
    assert results[0][1] == "("
    assert results[1][1] == "("
    assert results[2][1] == ")"
    assert results[3][1] == ")"

def test_operands():
    results, remainder = scanner.scan("*+-/")
    assert len(results) == 4
    assert results[0][1] == "*"
    assert results[1][1] == "+"
    assert results[2][1] == "-"
    assert results[3][1] == "/"

def test_whitespace():
    results, remainder = scanner.scan("4+ 3")
    assert len(results) == 3

def test_unrecognizable():
    results, remainder = scanner.scan("1+!3") # scanner does not continue if there is an error
    assert len(results) == 2
    assert len(remainder) == 2
