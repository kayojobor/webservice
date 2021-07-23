
#### Requirements
- Docker 

## Installation

### Build Docker image
- This web service uses HTTP basic authentication. See the config file for username and password. This can be turn into dictionary

- To enable SSL, generate the certificate and private key into the key folders. This can be done with following command

Private keys
```
$ openssl genrsa -out privkey.pem 2048
```

Public Keys
```
$ openssl req -new -x509 -days 365 -key privkey.pem -out cert.pem
```

- Build the docker image using the following command:
```
docker-compose build
```

### Start web service
```
docker-compose up -d    # d in detach mode
```

### Inspecting running container

run command below to see all container
```
$ docker ps
```
Enter the app container name as specified in docker compos file

```
$ docker exec -it json-webservice  bash

```
### Note:

The port number, user credential, switching SSL or off  can be change from the config file
