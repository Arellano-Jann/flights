FROM node:21

RUN mkdir -p /app
WORKDIR /app

COPY ./static ./static

COPY package*.json ./

RUN npm install --force

# if volume mounted, no need to copy the universe
# COPY . .

ENV PORT=5173
EXPOSE 5173

# CMD ["make", "run"]