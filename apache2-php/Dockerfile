FROM ereborlugimli/myapache2

MAINTAINER Büşra Yenidoğan Versiyon: 0.1

RUN apt-get update && apt-get install -y php7.0 php7.0-mysql libapache2-mod-php7.0 curl lynx-cur && apt-get clean && rm -rf /var/lib/apt/lists/*

#Enable apache mods.

RUN a2enmod php7.0
RUN a2enmod rewrite

#Updare the PHP .ini file, enable <? ?> tags and quieten logging.

RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.0/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.0/apache2/php.ini

#Copy this repo into place.
ADD www /var/www/site

