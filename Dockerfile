# Define la imagen base
FROM python:3.10

# Instala pip y Poetry


# Define el directorio de trabajo
WORKDIR /stardewApp

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.4.1

COPY poetry.lock pyproject.toml ./
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
RUN pip install --upgrade pip

RUN pip install "poetry==$POETRY_VERSION"

RUN poetry config virtualenvs.create false
RUN poetry install #--no-dev

# Copia los archivos de la aplicación
COPY . .


# Instala las dependencias de Python usando Poetry

# Define el comando para ejecutar la aplicación
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "createsuperuser2", "--username","root", "--password","root", "--noinput", "--email", "'root@root.com'"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

