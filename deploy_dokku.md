

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

3. Install and freeze what you need:

```
pip install gunicorn flask flask_simplelogin pandas
pip freeze > requirements.txt
```

4. Make sure it still works locally:

```
python app.py
```

5. Specify a python `runtime.txt`:

```
python --version
echo "python-3.7.9" >> runtime.txt
```

6. (Optional) Deactivate your venv:

```
deactivate
```

7. Create a `Procfile`:

```
echo "web: gunicorn app:app --workers=4" >> Procfile
```

8. Push everything up to GitHub:

```
git add .
git commit -m '🚀'
git push
```



**On Server**

9. Spin up a $5 Ubuntu 18.04 server ([DigitalOcean](https://m.do.co/c/2909cd1f3f10) works)...

10. ssh into it:

```
ssh root@165.XXX.43.118
```

11. Update everything:

```
sudo apt update
sudo apt -y upgrade
```

12. Get "new" monitoring (DigitalOcean only):

```
curl -sSL https://repos.insights.digitalocean.com/install.sh | sudo bash
```

13. Setup firewall:

````
ufw app list
ufw allow OpenSSH
ufw enable
````

14. Add some rules ([source](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04)):

```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 22
sudo ufw allow http
sudo ufw allow https
```

15. Poke another hole in 5000 (`sudo ufw allow PORT`):   

```
sudo ufw allow 5000
```

16. Install dokku:

```
wget https://raw.githubusercontent.com/dokku/dokku/v0.19.13/bootstrap.sh
sudo DOKKU_TAG=v0.19.13 bash bootstrap.sh
```

17. Navigate to the machine IP address in a browser and add your ssh key

```
# to copy and paste:
cat .ssh/id_rsa.pub
```

18. Add server IPv4 address to the hostname for now:

> 165.XXX.43.118

19. Create a dokku app:

```
dokku apps:create scrapeworld
```

20. Enable VHOST:

```
dokku domains:enable scrapeworld
```



**On Laptop**

21. Add dokku as a remote:

```
git remote add dokku dokku@165.XXX.43.118:scrapeworld
```

22. Verify that the remote got added:

```
git remote -v
```

23. Push it up (for every new change just run these commands):

```
git add .
git commit -m '🤞'
git push dokku master
```

24. Hit the server address (`165.XXX.43.118`) to make sure it works!



#### Bonus: Custom Domain Instructions



**On Namecheap**

1. Add the following DNS records:

| Type                | Host | Value                               | TTL       |
| ------------------- | ---- | ----------------------------------- | --------- |
| A Record            | @    | 165.XXX.43.118                      | Automatic |
| URL Redirect Record | www  | http://scrape.world (Permanent 301) |           |
| A Record            | *    | 165.XXX.43.118                      | Automatic |

**On Server**

2. ssh into `root@165.XXX.43.118`

3. Install the Let’s Encrypt plugin for Dokku:

```
sudo dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git
```

4. Set the `DOKKU_LETSENCRYPT_EMAIL` environment variable to the email for Let’s Encrypt:

```
dokku config:set scrapeworld DOKKU_LETSENCRYPT_EMAIL=first.last@email.com
```

5. Add the application and domain (http://`scrape.world` is the actual domain!):

```
dokku domains:add scrapeworld scrape.world
```

6. Create the SSL certificate. NGINX will automatically start serving the application over HTTPS on port 443:

```
dokku letsencrypt scrapeworld
```

7. Run this as a cron job so the certificate will renew automatically:.

```
dokku letsencrypt:cron-job --add
```
