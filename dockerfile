# Imagen base de Python
FROM python:3.11-slim
# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copiar el código
COPY . /app/