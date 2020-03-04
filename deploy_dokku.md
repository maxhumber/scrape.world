

![dokku](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.rodSWxgGl1-tlKWYKucBEQAAAA%26pid%3DApi&f=1)

#### Deploy: Dokku

Inspired by: [link](https://www.linode.com/docs/applications/containers/deploy-a-flask-application-with-dokku/)



**On Laptop**

0. Build the damn flask app... the bottom of it should look like:

```
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

1. Setup a damn environment (if you don't have one already):

```
python -m venv .venv
```

2. Activate it:

```
source .venv/bin/activate
```

12. Install and freeze what you need:

```
pip install gunicorn flask flask_simplelogin pandas
pip freeze > requirements.txt
```

13. Make sure it works locally:

```
python app.py
```

Specify a python `runtime.txt`:

```
python --version
echo "python-3.7.4" >> runtime.txt
```

16. Create a `Procfile`:

```
echo "web: gunicorn app:app --workers=4" >> Procfile
```

17. Push everything up to GitHub:

```
git add .
git commit -m '🚀'
git push
```













**Server**

1. Spin up a $5 server ([DigitalOcean](https://m.do.co/c/2909cd1f3f10) works)...
2. ssh into it:

```
ssh root@142.93.XXX.104
```

3. (Optional) Update everything:

```
sudo apt update
sudo apt -y upgrade
```

4. (Optional) Get "new" monitoring:

```
curl -sSL https://repos.insights.digitalocean.com/install.sh | sudo bash # skip
```

5. Configure firewall:

````
ufw app list
ufw allow OpenSSH
ufw enable
````

5. Add and tweak more firewall garbage [source](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04):

```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 22
sudo ufw allow http 
sudo ufw allow https
```

6. Poke another hole in 5000 (`sudo ufw allow PORT`):   

```
sudo ufw allow 5000
```

7. Install dokku:

```
wget https://raw.githubusercontent.com/dokku/dokku/v0.19.13/bootstrap.sh
sudo DOKKU_TAG=v0.19.13 bash bootstrap.sh
```

8. Navigate to the machine IP address in a browser and add your ssh key

```
# to copy and paste:
cat .ssh/id_rsa.pub
```

9. Add server IPv4 address to the hostname for now:

> 138.197.XXX.220



**On the Sever**

18. ssh back into the server (if you closed it):

```
ssh root@142.93.XXX.104
```

19. Create a dokku app:

```
dokku apps:create scrapeworld
```

20. Enable VHOST:

```
dokku domains:enable scrapeworld
```



**On local machine**

21. Go back to the app and add dokku as a remote:

```
git remote add dokku dokku@<SERVER IPv4 ADDRESS>:scrapeworld
```

22. Verify the remote is added:

```
git remote -v
```

23. Push it up:

```
git add .
git commit -m '🤞'
git push dokku master
```

24. Visit the server address to make sure it works!

25. Add a custom domain:
26. 

