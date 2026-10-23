# Local infrastructure

`docker-compose.yml` is the local foundation entry point. API and frontend use
the control network; the stateless demo uses a separate internal fixture network.
`docker compose --profile data up --build` additionally starts PostgreSQL and
Redis without publishing their ports. They are not yet connected to the API.

See `docs/ARCHITECTURE_DECISIONS.md` for the future isolated runner boundary and
public-target release gate. No hosted deployment or Docker daemon access from
application containers is configured.
