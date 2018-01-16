FROM httpd:alpine

RUN apk add --update nodejs nodejs-npm
RUN npm install

RUN npm run build
COPY ./dist/ /usr/local/apache2/htdocs
