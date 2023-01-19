from kinneyotp import Key

def test_key_with_defaults_and_seed_set():
    k = Key(seed=10)
    assert k.generated == "SBNPSAGOPIUZFBQPKCHX"
    assert len(k.generated) == 20


def test_key_with_defaults_and_seed_set_override_length():
    k = Key(seed=10, length=10)
    assert k.generated == "SBNPSAGOPI"
    assert len(k.generated) == 10
