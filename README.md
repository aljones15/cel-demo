
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
For the postgress database a docker image maybe used:
```sh
docker pull postgres
# note it is not recommended to run postgres w/o auth but this is a demo
sudo docker container run --env POSTGRES_HOST_AUTH_METHOD=trust postgres
```

A `settings.yml` file maybe used:
```sh
server:
  - port: 4346
  - domain: "localhost"
  - routes:
    - schedule: "/schedules"
database:
  -name: "cel"
  -user: "postgres"
  -password: ~
  -host: ~
  -port: ~
```

To get started, run the following:

```
$ nix develop
$ poetry run python -m sample_package
Hello, world!
```