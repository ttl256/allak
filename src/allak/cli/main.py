from ipaddress import IPv6Network

import click

from allak.cli.click_types import IPV6NETWORK, MACADDR
from allak.mac.eui_64 import eui_64
from allak.mac.mac import MAC


@click.command()
@click.argument("prefix", type=IPV6NETWORK)
@click.argument("mac", type=MACADDR)
@click.version_option()
def main(prefix: IPv6Network, mac: MAC) -> None:
    """
    Given IPv6 PREFIX of prefix-length 64 and MAC address returns
    IPv6 host address with interface identifier as modified EUI-64.
    """
    print(eui_64(prefix, mac))
