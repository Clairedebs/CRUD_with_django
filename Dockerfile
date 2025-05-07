# Utiliser l'image Python Alpine comme base
FROM python:alpine

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apk update && add --no-cache \
    postgresql-libs \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    libffi-dev\
    build base

# Copier les fichiers de requirements
COPY constraints.txt .

# Installer les dépendances Python
RUN pip install -r constraints.txt

# Copier le reste du projet
COPY . .

# Exposer le port
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]