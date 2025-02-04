# Landbot Backend Challenge

## Description

The product department wants a system to be notified when a customer requests assistance from a bot. The bot will make an http call (like a webhook) with the following information:

- Topic: a string with values can be sales or pricing
- Description: a string with a description of the problem that needs assistance from.

You need to expose an API endpoint that will receive this call and depending on the selected topic will forward it to a different channel:

``` 
Topic    | Channel   
----------------------
Sales    | Slack
Pricing  | Email
```

## Notes:
- Slack and Email are suggestions. Select one channel that you like the most, the other can be a mock.
- There may be more topics and channels in the future.

## The solution should:
- Be written in your favorite language and with the tools with which you feel comfortable.
- Be coded as you do daily (libraries, style, testing...).
- Be easy to grow with new functionality.
- Be a dockerized app.


# Solution

## 1. Architecture: DDD? hexagonal? Clean Architecture?
After check the requirements, I think that the best architecture for this project is the Clean Architecture. This 
architecture is a good choice because it is easy to grow with new functionality and it is easy to test.
DDD or hexagonal are good choices too, but I think that Clean Architecture is the best choice for this project 
because it is a simple project, it don´t have a domain complex and in the future to add new topics and channels in the 
future is easy.

## 2. Libraries
- Python 3.13.1: the last version.
- Django and Django Rest Framework: Django is a high-level Python Web framework that encourages rapid development.
- No admin app: I don´t use the Django admin app because the requirements don´t need it.
- poetry: Poetry is a tool for dependency management and packaging in Python.
- flake8: Flake8 is a tool that checks for style guide violations in Python code.
- Black: Black is the uncompromising Python code formatter.
- pytest: The pytest framework makes it easy to write small tests, yet scales to support complex functional testing 
  for applications.
- Docker: Docker is a set of platform as a service products that use OS-level virtualization to deliver software in 
    packages.
- Docker-compose: Compose is a tool for defining and running multi-container Docker applications.
- No database: I don´t use a database because the requirements don´t need it. We can configure the funcionality with 
  a external file.
- CI: I use Github Actions to run the tests and the linters.
- Makefile: I use a Makefile to run the commands.
- Pydantic: Data validation and settings management using Python type hinting.

## 3. How to run the project
