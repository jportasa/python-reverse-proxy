# Typeform exercice

## How to run the environment?

git clone https://github.com/jportasa/python_web_mirror.git

from inside the repo path do:

docker-compose up -d

and test with curl http://server:80/test

note that there are 2 docker containers, one for thebaackend and another for reverse proxy
reverse proxy sends packets to backend to port 3000
