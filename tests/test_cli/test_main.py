import pytest
from click.testing import CliRunner

from allak.cli.main import main


@pytest.mark.parametrize(
    "prefix, mac, want",
    [
        (
            "2001:db8:b081:b401::/64",
            "00-00-00-00-00-00",
            "2001:db8:b081:b401:200:ff:fe00:0\n",
        ),
        (
            "2001:db8::/64",
            "FC:99:47:75:CE:E0",
            "2001:db8::fe99:47ff:fe75:cee0\n",
        ),
    ],
)
def test_main(prefix: str, mac: str, want: str) -> None:
    runner = CliRunner()
    out = runner.invoke(main, [prefix, mac])
    got = out.output
    assert want == got
