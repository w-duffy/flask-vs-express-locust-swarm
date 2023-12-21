FROM node:14-slim

WORKDIR /usr/src/app

# Just testing express
RUN npm install express

COPY . .

EXPOSE 3000

CMD ["node", "app.js"]
