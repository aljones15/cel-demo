
### Setup

This project was built using [nix's default flake](https://wiki.nixos.org/wiki/Flakes) for python around the package manager [poetry](https://python-poetry.org/). It is recommened to just treat it as a poetry project. Additionally, this project requires a postgres server.

Poetry setup
```sh
poetry install
```

Here are the commands:
```sh
poetry run serve
poetry run poll
```

To get started, run the following:

```
$ nix develop
$ poetry run python -m sample_package
Hello, world!
```