FROM node:22.6.0

WORKDIR /frontend

COPY . .

RUN npm install -g yarn && yarn

EXPOSE 3000

CMD ["yarn", "start"]