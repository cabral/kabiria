
#### With help from: https://github.com/marcgibbons/django-selenium-docker

# Example: Django Selenium Tests with Docker


## Requirements
- Docker
- Docker-compose
- VNC Viewer (optional for debugging)

## Installation
`$ docker-compose build`

## Environment settings
`$ cp .env-example .env`

## Running the tests
1. Start the selenium container:

   `$ docker-compose start selenium`

2. Open VNC Viewer and connect to `localhost:5900`. Password is `secret`

3. Run the tests

    `$ docker-compose run django`

4. No on you can integrations tests with:

    `$ python manage.py test --exclude-tag=selenium`
