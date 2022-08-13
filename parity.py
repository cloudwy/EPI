"""
1. Bruto-Force
"""
def parity_brutoforce(x:int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


"""
2. Improvement1:erases the lowest set bit in a word in a single operation
"""
def parity_eraselsb(x:int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


"""
Test Case
1. 44 = 00101100
2. 46 = 00101110
"""
def test_parity_brutoforce_odd():
    assert parity_brutoforce(44) == 1


def test_parity_brutoforce_even():
    assert parity_brutoforce(46) == 0


def test_parity_eraselsb_odd():
    assert parity_eraselsb(44) == 1


def test_parity_eraselsb_even():
    assert parity_eraselsb(46) == 0


if __name__ == "__main__":
    test_parity_brutoforce_odd()
    test_parity_brutoforce_even()
    test_parity_eraselsb_odd()
    test_parity_eraselsb_even()
    print("Everything passed")
