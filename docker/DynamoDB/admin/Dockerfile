FROM ubuntu:18.04

RUN apt update
RUN apt install -y apt nodejs npm vim net-tools
RUN npm install dynamodb-admin -g
RUN echo "export DYNAMO_ENDPOINT=http://10.0.0.3:8000" >> ~/.bashrc

CMD dynamodb-admin
