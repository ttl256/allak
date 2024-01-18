import pytest

from allak.mac.mac import MAC


@pytest.mark.parametrize(
    "mac, want",
    [
        ("000000000000", "00:00:00:00:00:00"),
        ("00-00-00-00-00-00", "00:00:00:00:00:00"),
        ("00:00:00:00:00:00", "00:00:00:00:00:00"),
        ("0000.0000.0000", "00:00:00:00:00:00"),
        ("0.000.00-00.000:0", "00:00:00:00:00:00"),
        ("ab:ce:DE:f0:12:34", "ab:ce:de:f0:12:34"),
    ],
)
def test_normalize_valid(mac: str, want: str):
    got = MAC(mac)
    assert want == got


@pytest.mark.parametrize(
    "mac",
    [
        "bT:d0:74:44:5c:1d",
    ],
)
def test_normalize_invalid_char(mac: str):
    with pytest.raises(ValueError, match="Invalid character"):
        MAC(mac)


@pytest.mark.parametrize(
    "mac",
    [
        "bc:d0:74:44:5c:1d:1",
    ],
)
def test_normalize_invalid_long(mac: str):
    with pytest.raises(ValueError, match="More than 12 hex digits"):
        MAC(mac)


@pytest.mark.parametrize(
    "mac, want",
    [
        ("bc:d0:74:44:5c:1d", "bed0:74ff:fe44:5c1d"),
    ],
)
def test_eui64(mac: str, want: str):
    got = MAC(mac).eui64()
    assert want == got
