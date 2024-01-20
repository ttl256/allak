# allak
A CLI tool to produce an IPv6 address with the host portion being a modified EUI-64.

## Installation

Python version: >=3.11

### Using pip

Inside a virtual environment

```
pip install allak
allak-cli --help
```

Without a virtual environment

```
pip install --user allak
allak-cli --help
```

## Usage
Package functionality is provided by an entrypoint `allak-cli`.

```
allak-cli [OPTIONS] PREFIX MAC

  Given IPv6 PREFIX of prefix-length 64 and MAC address returns IPv6 host
  address with interface identifier as modified EUI-64.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.
```

## Meta

Allak is a mountain in Sweden, a village in Altai, a train station in Korea.