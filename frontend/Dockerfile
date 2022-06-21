FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*
RUN npm install -g yarn

RUN mkdir -p /srv/app/
WORKDIR /srv/app
COPY ./package*.json ./
RUN yarn global add @vue/cli
RUN yarn install

# Bundle app source
COPY . .

EXPOSE 8080

CMD [ "yarn", "serve"]
