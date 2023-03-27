#### Description

Source code for easypolitics.app backend.

Read the case study here: https://uxfol.io/p/chrismehlhoff/0318d02a

#### Development

We use Docker containers for local development. To get started,

1. Ensure `docker` and `docker-compose` are installed on your local computer.
2. Rename `./.envs/.dev.example` to `./.envs/.dev` and edit values as necessary.
3. Run `docker compose -f dev.yml up -d` in root directory.
4. This command will build and launch two containers (i.e., Django and Postgres).
5. Furthermore, code is mounted via Docker volumes, which means changes on your local computer will sync up in Django
   container automatically.
6. Visit `127.0.0.1:8000` to view project.

Run the following commands to pull and insert bill information into Postgres:

1. Open terminal for `backend` Docker container.
2. Run `python manage.py collect` to collect bill information from propublica.org API.
3. Run `python manage.py insert` to insert bill information into Postgres.

#### Credits

- Product Designer - Chris Mehlhoff
- Lead Programmer - Steven Mehlhoff
