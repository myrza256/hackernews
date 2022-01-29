# Python test assessment by DevelopsToday


## Product Features
- Listing of all the links (no login required)
- Link Creation
- User Creation
- JWT Based authentication
- Vote registration and unregistration by logged in Users

## Python env
- The project uses Python 3.8. Use [PyEnv](https://github.com/pyenv/pyenv) to install the required version
- Python environment in managed through [Poetry](https://python-poetry.org/)
- Install Poetry using instructions present [here]()
- Install the project virtual env and packages using the command. **Make sure you have set the `local` Python version to 3.7**
```sh
poetry install
```
- Start the project virtual env using the command
```
poetry shell
```
- To check out more details about your virtualenv please run the command
```sh
poetry env info
```
- In case of questions, please checkout the guide to maintaining virtual envs and python versions with over [here](https://python-poetry.org/docs/managing-environments/)

## Application Details
- Python 3.7
- Django 2.2
- Django Filters
- [Graphene Django](https://github.com/graphql-python/graphene-django)
- [Django GraphQL JWT](https://github.com/flavors/django-graphql-jwt)
- The Insomnia API collection can be used to interact with the application locally is present over [here](https://github.com/darth-dodo/reimagined-broccoli/blob/master/Insomnia_2020-04-19.json)

## API interaction
- The GraphQL interface can be accessed using the inbuilt Graphene UI present at `localhost:8000/grapqhl` but it does not support JWT Auth
- To use GraphQL with JWT Auth checkout **[Insomnia](https://insomnia.rest/)** or **[Postman](https://www.postman.com/)**


# Precommit hooks
- isort
- flake8
- black
- in built precommit checks

## Seed data
- From the root of the repo, run the following management command to generate the seed data
```sh
python manage.py seed_data
```
