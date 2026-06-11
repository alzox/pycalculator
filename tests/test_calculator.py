import random
from ..parser import apply, calculate, scanner

def test_add():
    assert apply("+", 1, 1) == 2

def test_subtract():
    assert apply("-", 1, 1) == 0

def test_multiply():
    assert apply("*", 1, 1) == 1

def test_divide():
    assert apply("/", 1, 1) == 1

def test_add_fuzz():
    for _ in range(100):
        lval = random.randint(0,100)
        rval = random.randint(0,100)
        assert apply("+", lval, rval) == lval + rval

def test_substract_fuzz():
    for _ in range(100):
        lval = random.randint(0,100)
        rval = random.randint(0,100)
        assert apply("-", lval, rval) == lval - rval

def test_multiply_fuzz():
    for _ in range(100):
        lval = random.randint(0,100)
        rval = random.randint(0,100)
        assert apply("*", lval, rval) == lval * rval

def test_divide_fuzz():
    for _ in range(100):
        lval = random.randint(1,100)
        rval = random.randint(1,100)
        assert apply("/", lval, rval) == lval // rval

def test_calculate_add_fuzz():
    for _ in range(100):
        lval = str(random.randint(0,100))
        rval = str(random.randint(0,100))
        assert apply("+", lval, rval) == lval + rval
        results, remainder = scanner.scan("1+1")
        assert calculate(results) == 2


