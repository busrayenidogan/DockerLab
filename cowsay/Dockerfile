FROM  ubuntu:latest

MAINTAINER Büşra Yenidoğan <yenidoganbusra@gmail.com>
RUN apt-get update && apt-get install -y cowsay fortune
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
