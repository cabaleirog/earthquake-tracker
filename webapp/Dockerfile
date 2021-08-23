FROM node:16.7-alpine3.14

WORKDIR /code

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]
