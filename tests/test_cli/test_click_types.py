from ipaddress import IPv6Network

import click
import pytest

from allak.cli import click_types
from allak.mac.mac import MAC as MAC_


@pytest.mark.parametrize(
    "prefix, want",
    [
        ("2001:db8:b081:b401::/64", IPv6Network("2001:db8:b081:b401::/64")),
    ],
)
def test_ipv6_network_valid(prefix: str, want: IPv6Network) -> None:
    got = click_types.IPv6Network_().convert(prefix, param=None, ctx=None)
    assert want == got


@pytest.mark.parametrize(
    "prefix",
    [
        "garbage",
    ],
)
def test_ipv6_network_invalid(prefix: str) -> None:
    with pytest.raises(
        click.exceptions.BadParameter, match="Expected IPv6 prefix, got"
    ):
        click_types.IPv6Network_().convert(prefix, param=None, ctx=None)


@pytest.mark.parametrize(
    "prefix",
    [
        "2001:db8:b081:b401::/65",
        "2001:db8::/48",
    ],
)
def test_ipv6_network_prefixlen(prefix: str) -> None:
    with pytest.raises(
        click.exceptions.BadParameter, match="Expected prefix-length to be 64"
    ):
        click_types.IPv6Network_().convert(prefix, param=None, ctx=None)


@pytest.mark.parametrize(
    "mac, want",
    [
        ("ab:cd:EF:01:23:45", MAC_("ab:cd:ef:01:23:45")),
    ],
)
def test_mac_valid(mac: str, want: MAC_) -> None:
    got = click_types.MAC().convert(mac, param=None, ctx=None)
    assert want == got


@pytest.mark.parametrize(
    "mac",
    [
        "ab:cd:ef:01:23:45:1",
        "ab:cd:ef:ff:00:0",
        "bT:d0:74:44:5c:1d",
    ],
)
def test_mac_invalid(mac: str) -> None:
    with pytest.raises(click.exceptions.BadParameter):
        click_types.MAC().convert(mac, param=None, ctx=None)
