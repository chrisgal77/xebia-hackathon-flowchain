# Wybierz obraz bazowy
FROM ubuntu:latest

# Aktualizuj system i zainstaluj wymagane narzędzia
RUN apt-get update \
    && apt-get install -y curl \
                          gnupg

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get clean

# Instaluj Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs

# Skonfiguruj środowisko pracy
WORKDIR /app

# Skopiuj pliki aplikacji do obrazu
COPY /webapp/. .

# Zainstaluj zależności
RUN npm install

RUN npm install hls.js

# Zbuduj aplikację
RUN npm run build

# Skonfiguruj serwer HTTP dla aplikacji
EXPOSE 8080

# Uruchom serwer HTTP po uruchomieniu kontenera
CMD ["npm", "run", "serve"]
