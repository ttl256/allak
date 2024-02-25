from typing import Self


class MAC(str):
    """
    Represents a MAC address (EUI-48).

    Allowed input is rather liberal: 12 hex digits separated by ':', '-', '.' in any
    combination.
    """

    def __new__(cls, mac: str) -> Self:
        return super().__new__(cls, MAC._normalize_mac(mac))

    def __init__(self, mac: str) -> None:
        self._mac = self.replace(":", "")

    @staticmethod
    def _normalize_mac(mac: str) -> str:
        """
        Returns MAC address in the form of xx:xx:xx:xx:xx:xx.
        """
        valid_chars = set("0123456789abcdef")
        acceptable_chars = valid_chars.union(set(":-."))
        xs: list[str] = []
        done: bool = False
        for idx, char in enumerate(mac):
            _char = char.lower()
            if _char not in acceptable_chars:
                raise ValueError(
                    f"Not a MAC address: {mac!r}. Invalid character: {char!r}, position"
                    f" {idx}"
                )
            if done is True:
                raise ValueError(f"Not a MAC address: {mac!r}. More than 12 hex digits")
            if _char in valid_chars:
                xs.append(_char)
            if len(xs) == 12:
                done = True
        if done is False:
            raise ValueError(f"Not a MAC address: {mac!r}. Less than 12 hex digits")
        return ":".join("".join(xs[i : i + 2]) for i in range(0, len(xs), 2))

    def eui64(self) -> str:
        """
        Convert MAC address (EUI-48) to interface ID based on modified EUI-64.
        """
        m = int(self._mac, 16)
        hi = (m >> 24) ^ 0x020000
        lo = m & 0xFFFFFF
        plain = format((hi << 40) + (0xFFFE << 24) + lo, "016x")
        return ":".join(plain[i : i + 4] for i in range(0, len(plain), 4))
