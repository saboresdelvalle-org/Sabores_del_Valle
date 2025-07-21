# Imagen base con Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos locales al contenedor
COPY . /app

# Comando para ejecutar un servidor web simple que sirva los archivos
CMD ["python", "-m", "http.server", "8000"]
