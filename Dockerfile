# Define la imagen base
FROM python:3.10

# Instala pip y Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
RUN pip install --upgrade pip

# Define el directorio de trabajo
WORKDIR /stardewApp

# Copia los archivos de la aplicación
COPY . .

# Instala las dependencias de Python usando Poetry
RUN poetry install

# Define el comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

