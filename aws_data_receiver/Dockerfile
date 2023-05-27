# Etap 1: Budowanie aplikacji
FROM python:3.9-slim AS build-stage

WORKDIR /app

# Skopiuj pliki requirements.txt
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj pozostałe pliki źródłowe
COPY . .

# Etap 2: Uruchamianie aplikacji
FROM python:3.9-slim AS production-stage

WORKDIR /app

RUN pip install uvicorn fastapi

# Skopiuj zbudowane pliki z etapu 1
COPY --from=build-stage /app /app

# Otwórz port 80
EXPOSE 8000

# Uruchom aplikację FastAPI
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
