
# Imagen base ligera
FROM python:3.11-alpine

# Establece directorio de trabajo
WORKDIR /app

# Copia archivos al contenedor
COPY requirements.txt .
COPY app.py .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8080

# Comando por defecto
CMD ["python", "app.py"]

