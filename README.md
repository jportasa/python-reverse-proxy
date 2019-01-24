# Typeform exercice

## How to run the environment?

git clone https://github.com/jportasa/python_web_mirror.git

from inside the repo path do:

docker-compose up -d

and test with curl http://server:80/test

note that there are 2 docker containers, one for thebaackend and another for reverse proxy
reverse proxy sends packets to backend to port 3000

```root@ip-10-0-2-239:~/python-reverse-proxy# docker ps
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS                NAMES
126d8fbdc3ab        python-backend:latest   "python app/echo-ser…"   38 seconds ago      Up 37 seconds                            python-r                              everse-proxy_backend_1
646daccda12a        nginx-proxy:latest      "nginx -g 'daemon of…"   38 seconds ago      Up 37 seconds       0.0.0.0:80->80/tcp   python-r                              everse-proxy_nginx-proxy_1
```