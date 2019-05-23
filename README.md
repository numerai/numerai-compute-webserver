# numerai-compute-webserver

## Setup

Setup a virtualenv
```
virtualenv venv
```

Whenever working on this project, active that virtualenv:
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

### Heroku

```
heroku login
heroku create numerai-compute-node-$YOURNAME
git push heroku master
```

### DigitalOcean

A full featured (but very complicated) example of setting up a flask webserver in DigitialOcean is available at https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
