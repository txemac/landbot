# pull official base image
FROM python:3.13.1-slim

# set work directory
WORKDIR /api

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi --without dev


# Copy project
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
