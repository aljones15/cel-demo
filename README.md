
### Setup

This project was built using [nix's default flake](https://wiki.nixos.org/wiki/Flakes) for python around the package manager [poetry](https://python-poetry.org/). It is recommened to just treat it as a poetry project. This project uses an in memory SQLite server so no need for a database.

Poetry setup
```sh
poetry install
```

Here are the commands:
```sh
poetry run serve
poetry run poll
```
While not required for a postgress database a docker image maybe used:
```sh
docker pull postgres
# note it is not recommended to run postgres w/o auth but this is a demo
docker run --name postgres-no-auth -e POSTGRES_HOST_AUTH_METHOD=trust -d postgres
```

A `settings.yml` file is used:
```sh
server:
  - port: 4346
  - domain: "localhost"
  - routes:
    - schedule: "/schedules"
database:
  -name: "cel"
  -user: ~
  -password: ~
  -host: ~
  -port: ~
```

### Development
To run the server
```sh
poetry run python -m cel_services.server
```

To run the scheduler

```sh
poetry run poll
```