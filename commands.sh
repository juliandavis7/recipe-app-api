# build container
docker-compose build

# run app
docker-compose up

# terminate all running containers
docker-compose down

# run tests
docker-compose run --rm app sh -c "python manage.py test"