#### Deploy: Dokku

**On Digital Ocean**

[source](https://www.linode.com/docs/applications/containers/deploy-a-flask-application-with-dokku/)

1. Spin up a $5 sever...
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

9. Skip the Hostname for now... just put:

> localhost 



**On local machine**

10. Setup a damn environment:

```
python -m venv .venv
```

11. Activate it:

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

14. The bottom of your flask app should look like:

```
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

15. Specify a python `runtime.txt`:

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





#### Dokku Deploy



Go back to your app and try to add dokku as a remote:

```
git remote add dokku dokku@example.com:box
```





