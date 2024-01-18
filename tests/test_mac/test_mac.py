import pytest

from allak.mac.mac import MAC


@pytest.mark.parametrize(
    "mac, want",
    [
        ("abcdef012345", "ab:cd:ef:01:23:45"),
        ("ab-cd-ef-01-23-45", "ab:cd:ef:01:23:45"),
        ("ab:cd:ef:01:23:45", "ab:cd:ef:01:23:45"),
        ("abcd.ef01.2345", "ab:cd:ef:01:23:45"),
        ("a.bcd.ef-01.234:5", "ab:cd:ef:01:23:45"),
        ("ab:cd:EF:01:23:45", "ab:cd:ef:01:23:45"),
    ],
)
def test_normalize_valid(mac: str, want: str) -> None:
    got = MAC(mac)
    assert want == got


@pytest.mark.parametrize(
    "mac",
    [
        "bT:d0:74:44:5c:1d",
        "bc:d0:74:44:5c:1d\\",
        "bc:d0:74:44:5c:1dP",
        "1111R",
    ],
)
def test_normalize_invalid_char(mac: str) -> None:
    with pytest.raises(ValueError, match="Invalid character"):
        MAC(mac)


@pytest.mark.parametrize(
    "mac",
    [
        "ab:cd:ef:01:23:45:1",
        "aaaaaaaaaaaaB",
        "1.ab:cd:ef:01:23:45",
        "ab:cd:ef:fffe:01:23:45",
    ],
)
def test_normalize_invalid_long(mac: str) -> None:
    with pytest.raises(ValueError, match="More than 12 hex digits"):
        MAC(mac)


@pytest.mark.parametrize(
    "mac, want",
    [
        ("bc:d0:74:44:5c:1d", "bed0:74ff:fe44:5c1d"),
        ("39-A7-94-07-CB-D0", "3ba7:94ff:fe07:cbd0"),
        ("0015.2BE4.9B60", "0215:2bff:fee4:9b60"),
        ("FC:99:47:75:CE:E0", "fe99:47ff:fe75:cee0")
    ],
)
def test_eui64(mac: str, want: str) -> None:
    got = MAC(mac).eui64()
    assert want == got
