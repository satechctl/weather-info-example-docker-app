# Check weather for a given city

## Build docker image with "weather-info" application

    docker build -t weather-info .

## Run "weather-info" application in docker container

    docker run -ti -e OPENWEATHERMAP_API_KEY=<API-KEY> weather-info:latest <CITY-NAME>

    # example:
    docker run -ti -e OPENWEATHERMAP_API_KEY=f7s54s5b843m48gfde5s5s weather-info:latest Warsaw
