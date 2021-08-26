# Seismic Tracker

## Set up

### 1.- Install Docker

If Docker is not already installed lets proceed to install it, by either using the [official documentation](https://docs.docker.com/engine/install/), or the script from [GetDocker](https://get.docker.com/). Furthermore, we will install Docker Compose for development, and/or building the container images; Docker compose installation guide can be found [here](https://docs.docker.com/compose/install/).

### 2.1.- Initialize a Docker Swarm (Production only)

Set up the manager node.

```sh
sudo docker swarm init --advertise-addr $(hostname -i)
```

Save the stack file (docker-compose.yml) into the machine and create a new stack.

```sh
sudo docker stack deploy --compose-file docker-compose.yml earthquakes
```

### 2.2.- Start using Docker Compose (Development only)

To initialize the application using Docker Compose, we can simple go to the project's folder and run the following command.

```sh
sudo docker-compose up
```

However, as the database is going to be missing at this point, we need to complete the below steps, and might need to restart the application afterwards, as the api service would have failed, and might not recover on its own.


### 3.- Create database

Go to the [Adminer UI](http://localhost:8080) (Current user is _root_, and password can be found on the docker-compose file, under `MYSQL_ROOT_PASSWORD`). Once logged in, click on `Create Database` and create one called `locations`.
### 4.- Add starting locations to the database

Locations can be added either directly by API calls, or by using [Adminer](http://localhost:8080).

Some example API calls are set below for convenience.

```sh
curl --location --request POST 'http://127.0.0.1:80/locations/add' \
    --form 'identifier="tokyo_japon"' \
    --form 'name="Tokyo, Japon"' \
    --form 'latitude="35.6895"' \
    --form 'longitude="139.69171"'
```

```sh
curl --location --request POST 'http://127.0.0.1:80/locations/add' \
    --form 'identifier="los_angeles_ca"' \
    --form 'name="Los Angeles, CA"' \
    --form 'latitude="34.052235"' \
    --form 'longitude="-118.243683"'
```

```sh
curl --location --request POST 'http://127.0.0.1:80/locations/add' \
    --form 'identifier="san_francisco_ca"' \
    --form 'name="San Francisco, CA"' \
    --form 'latitude="37.733795"' \
    --form 'longitude="-122.446747"'
```

### 5.- Verify that the application is running as expected

Now that everything is set up, go to the application, which in a local machine will be at the standard [localhost](http://127.0.0.1:80), and 3 locations should be visible.

