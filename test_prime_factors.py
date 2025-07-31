from prime_factors import PrimeFactor

def test_prime_factor_of_1():
    prime_factors = PrimeFactor()
    assert 1 == 1


def test_prime_factor_of_1():
    prime_factors = PrimeFactor()
    assert prime_factors.of(1) == []

def test_prime_factor_of_2():
    prime_factors = PrimeFactor()
    assert prime_factors.of(2) == [2]

def test_prime_factor_of_3():
    prime_factors = PrimeFactor()
    assert prime_factors.of(3) == [3]

def test_prime_factor_of_4():
    prime_factors = PrimeFactor()
    assert prime_factors.of(4) == [2,2]

def test_prime_factor_of_6():
    prime_factors = PrimeFactor()
    assert prime_factors.of(6) == [2,3]