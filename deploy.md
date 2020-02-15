#### Digital Ocean

Get a digital ocean docker droplet

Get better monitoring

```
curl -sSL https://repos.insights.digitalocean.com/install.sh | sudo bash
```



#### Postgres Database

[Original Guide](https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198)

Configure a postgres database

```
docker pull postgres
```

Create a volume

```
mkdir -p $HOME/docker/volumes/postgres
```

Start the container

```
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=password -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
```

Login with

```
import psycopg2 # pip install psycopg2-binary

HOST = '138.XXX.145.169'
PORT = 5432
DB = 'postgres'
USER = 'postgres'
PASSWORD = 'password'

con = psycopg2.connect(
    database=DB,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)
```



### Docker traffic generating app

[Original Guide](https://runnable.com/docker/python/dockerize-your-python-application)







## Deploy: Docker + DigitalOcean



#### Docker Container Instructions

1. [uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker)

#### Initial Server Setup

2. Configure DigitalOcean Docker Image

3. ssh into the machine:

```
ssh root@142.93.XXX.104
```

4. Update everything:

```
sudo apt update # skip
sudo apt -y upgrade # skip
sudo apt install make
sudo apt install unzip
```

5. Get new monitoring:

```
curl -sSL https://repos.insights.digitalocean.com/install.sh | sudo bash # skip
```

6. Create a new user:

```
adduser mvml
```

> enter password

7. Adjust permissions:

```
usermod -aG sudo mvml
sudo usermod -aG docker mvml
rsync --archive --chown=mvml:mvml ~/.ssh /home/mvml
```

8. Sign in with the new user:

```
ssh mvml@142.93.XXX.104
```

#### Get the app on the machine

9. Run the following commands:

```
wget https://github.com/maxhumber/mvml/archive/master.zip
unzip master.zip
mv MVML-master repomatic
rm -f master.zip
```

#### Build and start Docker

10. Run the following:

```
cd repomatic
make build
make run
```

