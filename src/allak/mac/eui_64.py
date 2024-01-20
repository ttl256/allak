from ipaddress import IPv6Address, IPv6Network

from allak.mac.mac import MAC


def eui_64(prefix: IPv6Network, mac: MAC) -> str:
    if prefix.prefixlen != 64:
        raise ValueError(f"Expected prefix-length to be 64, got {prefix.prefixlen}")
    hi = IPv6Address(str(prefix.network_address))
    lo = int(mac.eui64().replace(":", ""), 16)
    return str(IPv6Address(int(hi) + lo).compressed)
