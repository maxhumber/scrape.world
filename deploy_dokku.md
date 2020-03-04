#### Dokku

**Digital Ocean**

1. Spin up a $5 sever
2. 



#### App setup

Setup a blank repo (it's called box in this example):

```
git clone git@github.com:maxhumber/box.git
cd box
```

Setup a damn environment

```
python -m venv .venv
source .venv/bin/activate
pip install flask gunicorn
pip freeze > requirements.txt
echo ".venv" > .gitignore
```

Create a stupid flask app

```
touch hello.py
```

Fill it with:

```
import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

Create a Procfile

```
touch Profile
```

Fill it with 

```
web: gunicorn hello:app --workers=4
```

Push up to GitHub 



#### Dokku Deploy

[source](https://www.linode.com/docs/applications/containers/deploy-a-flask-application-with-dokku/)

1. Go get a server.

2. ssh into it:

   ```
   ssh root@138.197.133.51
   ```

3. Configure firewall:

   ````
   ufw app list
   ufw allow OpenSSH
   ufw enable
   ````

4. More firewall garbage [source](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04):

   ```
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   sudo ufw allow ssh
   sudo ufw allow 22
   sudo ufw allow http 
   sudo ufw allow https
   ```

5. If you need more ports: `sudo ufw allow PORT` for the port in question.   

   ```
   sudo ufw allow 5000
   ```

6. Install dokku:

   ```
   # for debian systems, installs dokku via apt-get
   wget https://raw.githubusercontent.com/dokku/dokku/v0.19.13/bootstrap.sh
   sudo DOKKU_TAG=v0.19.13 bash bootstrap.sh
   # go to your server's IP and follow the web installer 
   ```

7. Navigate to the machine IP address in a browser and add your ssh key

   ```
   cat .ssh/id_rsa.pub
   ```

8. Host name? Not sure: `ubuntu-s-1vcpu-1gb-tor1-01`



Go back to your app and try to add dokku as a remote:

```
git remote add dokku dokku@example.com:box
```





