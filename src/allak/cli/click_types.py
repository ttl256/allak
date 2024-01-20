import ipaddress
from typing import Optional

import click

from allak.mac.mac import MAC as MAC_


class IPv6Network_(click.ParamType):
    def convert(
        self, value: str, param: Optional[click.Parameter], ctx: Optional[click.Context]
    ) -> ipaddress.IPv6Network:
        try:
            prefix = ipaddress.IPv6Network(value)
        except ValueError:
            self.fail(f"Expected IPv6 prefix, got {value!r}", param, ctx)
        else:
            if prefix.prefixlen != 64:
                self.fail(
                    f"Expected prefix-length to be 64, got {prefix.prefixlen}",
                    param,
                    ctx,
                )
            return prefix


class MAC(click.ParamType):
    def convert(
        self, value: str, param: Optional[click.Parameter], ctx: Optional[click.Context]
    ) -> MAC_:
        try:
            mac = MAC_(value)
        except ValueError as er:
            self.fail(str(er), param, ctx)
        else:
            return mac


IPV6NETWORK = IPv6Network_()
MACADDR = MAC()
