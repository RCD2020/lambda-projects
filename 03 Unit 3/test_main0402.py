import pytest
from main0402 import inc, Car

# python3 -m pytest test_main0402.py
# python3 -m pytest test_main0402.py --verbose

def test_inc_pn():
    assert inc(11) == 12
    assert inc(3) == 4
    
def test_inc_ze():
    assert inc(0) == 1

def test_inc_nn():
    assert inc(-1) == 0

def test_inc_fn():
    assert inc(1.5) == 2.5

# This will fail, as this function isn't intended to do that.
# def test_inc_lt():
#     assert inc('A') == 'B'

ford = Car('Ford', 'Focus', 2021)

def test_car_info():
    assert ford.make == "Ford"
    assert ford.mileage == 0