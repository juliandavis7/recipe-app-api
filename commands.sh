# run app
docker-compose up

# run tests
docker-compose run --rm app sh -c "python manage.py test"