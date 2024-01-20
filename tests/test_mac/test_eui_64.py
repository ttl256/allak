from ipaddress import IPv6Network

import pytest

from allak.mac.eui_64 import eui_64
from allak.mac.mac import MAC


@pytest.mark.parametrize(
    "prefix, mac, want",
    [
        (
            IPv6Network("2001:db8:b081:b401::/64"),
            MAC("00-00-00-00-00-00"),
            "2001:db8:b081:b401:200:ff:fe00:0",
        ),
        (
            IPv6Network("2001:db8::/64"),
            MAC("FC:99:47:75:CE:E0"),
            "2001:db8::fe99:47ff:fe75:cee0",
        ),
    ],
)
def test_eui64(prefix: IPv6Network, mac: MAC, want: str) -> None:
    got = eui_64(prefix, mac)
    assert want == got


@pytest.mark.parametrize(
    "prefix, mac",
    [
        (
            IPv6Network("2001:db8:b081:b401::/65"),
            MAC("00-00-00-00-00-00"),
        ),
        (
            IPv6Network("2001:db8::/48"),
            MAC("FC:99:47:75:CE:E0"),
        ),
    ],
)
def test_eui64_len(prefix: IPv6Network, mac: MAC) -> None:
    with pytest.raises(ValueError, match="Expected prefix-length to be 64"):
        eui_64(prefix, mac)
