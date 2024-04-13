FROM python:3.12
ENV PYTHONUNBUFFERED 1
WORKDIR .
COPY requirements.txt /.
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN apt-get install imagemagick
RUN wget https://www.imagemagick.org/download/ImageMagick.tar.gz
RUN tar xf ImageMagick.tar.gz 
RUN cd ImageMagick-7* && ./configure && ./configure --with-modules && make && make -j 6 && make install
RUN ldconfig /usr/local/lib
ENV IMAGEMAGICK_BINARY=/usr/local/bin/magick
ADD . .
RUN chmod +777 /video /runtext /mysite /templates /marquee_effect manage.py db.sqlite3 

