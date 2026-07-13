# 1. Usa una imagen base oficial de Python
FROM python:3.10-slim

# 2. Establece variables de entorno para evitar que Python escriba archivos .pyc y use buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Instala las dependencias del sistema necesarias (como los drivers de base de datos si usas SQL Server/Postgres)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia e instala los requerimientos de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia el resto del código del proyecto al contenedor
COPY . /app/

# 7. Expone el puerto en el que Django corre por defecto
EXPOSE 8000

# 8. Comando para arrancar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]