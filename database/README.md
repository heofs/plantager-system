## Running Postgres Docker

Build and run container

`docker build -t postgres . && docker run postgres`

Check container ip address

`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id`

Check connection

`psql -p 5432 -h 172.17.0.2 -U docker`

Build and run using docker-compose

`docker-compose up --build --renew-anon-volumes`
