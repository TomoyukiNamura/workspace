FROM python:3.6

WORKDIR /app

# apt
RUN apt-get update && apt-get install -y git tar zip

# glue
RUN git clone -b glue-1.0 https://github.com/awslabs/aws-glue-libs.git

# java-maven
RUN curl -sL https://github.com/shyiko/jabba/raw/master/install.sh | bash && . ~/.jabba/jabba.sh
RUN /root/.jabba/bin/jabba install amazon-corretto@1.8.232-09.1
RUN wget https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz
RUN tar -zxvf apache-maven-3.6.0-bin.tar.gz
RUN echo "export JAVA_HOME=/root/.jabba/jdk/amazon-corretto@1.8.232-09.1" >> ~/.bashrc
RUN echo "export PATH=/root/.jabba/jdk/amazon-corretto@1.8.232-09.1/bin:/app/apache-maven-3.6.0/bin:$PATH" >> ~/.bashrc
RUN rm apache-maven-3.6.0-bin.tar.gz

# spark
RUN wget https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-1.0/spark-2.4.3-bin-hadoop2.8.tgz
RUN tar -zxvf spark-2.4.3-bin-hadoop2.8.tgz
RUN echo "export SPARK_HOME=/app/spark-2.4.3-bin-spark-2.4.3-bin-hadoop2.8" >> ~/.bashrc
RUN rm spark-2.4.3-bin-hadoop2.8.tgz