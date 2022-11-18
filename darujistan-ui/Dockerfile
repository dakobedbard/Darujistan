FROM node:14-slim

RUN mkdir /bardui
WORKDIR /bardui
RUN apt-get -qq -y update \
    && apt-get install -qq -y  curl jq
COPY .npmrc /bardui/.npmrc
COPY tsconfig.json /bardui/tsconfig.json
COPY package.json /bardui

RUN npm install


COPY public /bardui/public
COPY src /bardui/src

ENV REACT_APP_API_ENDPOINT /api/2/
# RUN npm run build