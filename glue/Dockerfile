FROM python:3.6

WORKDIR /app

# linux command
RUN apt-get update && apt-get install -y git tar

# glue
RUN git clone https://github.com/awslabs/aws-glue-libs.git

# apache-maven
RUN wget https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz
RUN tar -zxvf apache-maven-3.6.0-bin.tar.gz
RUN echo "export PATH=/app/apache-maven-3.6.0/bin:$PATH" >> ~/.bashrc

# spark
RUN wget https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-1.0/spark-2.4.3-bin-hadoop2.8.tgz
RUN tar -zxvf spark-2.4.3-bin-hadoop2.8.tgz
RUN echo " export SPARK_HOME=/app/spark-2.4.3-bin-hadoop2.8" >> ~/.bashrc

# amazon-corretto
#RUN dpkg --install java-1.8.0-amazon-corretto-jdk_8.232.09-1_amd64.deb
RUN git clone https://github.com/shyiko/jabba.git
RUN curl -sL https://github.com/shyiko/jabba/raw/master/install.sh | bash
RUN bash ~/.jabba/jabba.sh
RUN echo " export JABBA_HOME=~/.jabba" >> ~/.bashrc
RUN sh ~/.bashrc
#RUN bash ~/.jabba/jabba.sh
#RUN jabba install amazon-corretto@1.8.232-09.2


