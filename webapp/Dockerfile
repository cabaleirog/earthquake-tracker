# Docker Container using Multi-Stage builds.

# Stage 1: Build the application.
FROM node:16.7-alpine3.14 as node
WORKDIR /code
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Move the application into Nginx.
FROM nginx:1.19-alpine
COPY --from=node /code/dist/webapp /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
