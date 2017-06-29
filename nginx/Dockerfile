FROM ubuntu:latest

MAINTAINER BüşraYenidoğan <yenidoganbusra@gmail.com>


#Paket listelerini download et
RUN apt-get update

#Nginx paketini yükle
RUN apt-get install -y nginx

#Bir sonraki adım Web sitemizin içeriğini /var/www/html e taşımak.Bu işlemi 
#gerçekleştirmek için ADD instructionunu kullanıcazç

ADD [ "./index.html","/var/www/html" ]

#Nginxi dinlediği HTTP(80) numaralı portun Docker networking modülü üzerinden 
#erişilmek üzere EXPOSE edilmesidir.
EXPOSE 80

#Containeri başlatırken bu komutu çalıştırmak için 
ENTRYPOINT nginx -g 'daemon off;'
