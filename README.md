# Seismic Tracker

## Set up

### Create database
### Add locations to the database

The initial locations can be added either directly by API calls, or by using [Adminer](http://localhost:8080) (Current user is _root_, and password can be found on docker-compose file).

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
