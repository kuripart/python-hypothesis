import hypothesis.strategies as s
from hypothesis import given, settings
import mpu.string  # Martins Python Utilities
from main import factorize

# property-testing framework tries to find a simple example which makes the test fail. This process is called shrinking.
@given(s.integers(min_value=1, max_value=6))
def test_factorize_multiplication_property(n):
    """The product of the integers returned by factorize(n) needs to be n."""
    factors = factorize(n)
    product = 1
    for factor in factors:
        product *= factor
    assert product == n, f"factorize({n}) returned {factors}"


@given(s.emails())
@settings(max_examples=5)
def test_is_email(email):
    print (email)
    assert mpu.string.is_email(email), f"is_email({email}) returned False"


@given(s.ip_addresses(v=4))
@settings(max_examples=5)
def test_is_ipv4(ip):
    print(ip)
    assert mpu.string.is_ipv4(str(ip)), f"is_ipv4({ip}) returned False"