# numerai-compute-webserver

## Setup

Setup a virtualenv
```
virtualenv venv
```

Whenever working on this project, activate that virtualenv:
```
source venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

Run the server
```
flask run
```

Test by going to the following url in your browser: http://localhost:5000/train or http://localhost:5000/submit


## Deploy

In order to use this webserver with Numer.ai compute, the server will have to be accessible from anywhere in the world.

That means you'll either have to:
1. Host on a publicly accessible cloud computer (ie. AWS, Google, Heroku, DigitalOcean)
2. Setup a local computer to be publicly accessible
    1. This includes forwarding ports
    2. Making sure your IP is static or setting up dynamic DNS
    3. Extra security concerns

While #2 is a good option if you're comfortable with setting up and running a webserver, we'll focus on #1, which is much easier for most users.

### DigitalOcean

Setup a digitalocean droplet: https://cloud.digitalocean.com/droplets/new?i=4bf4cd&size=s-4vcpu-8gb&region=sfo1

I recommend 8GB RAM to be safe, but you can go smaller if you know you don't need that much. Leave all the default choices, and scroll to the bottom and click `Create`.

You will be emailed the IP address and root password. Login with it like so:

```
ssh root@IP_FROM_EMAIL
```

Then execute the following:
```
apt update
apt install virtualenv

git clone https://github.com/numerai/numerai-compute-webserver.git
cd numerai-compute-webserver
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt

apt install supervisor
echo '[program:flask_project]
command = /root/numerai-compute-webserver/venv/bin/gunicorn app:app -b 0.0.0.0:80
directory = /root/numerai-compute-webserver
user = root' > /etc/supervisor/conf.d/flask_project.conf

supervisorctl reread
supervisorctl update
supervisorctl start flask_project
```

Your Numer.ai Compute webserver is now setup. You can test it by running `curl IP_FROM_EMAIL/train` or `curl IP_FROM_EMAIL/submit`
