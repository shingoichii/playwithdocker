FROM phusion/baseimage

RUN addgroup admin
#RUN useradd -m --group admin -s /bin/bash ksuser
#RUN echo 'ksuser:screencast' | chpasswd

RUN rm -f /etc/service/sshd/down

EXPOSE 22
CMD ["/sbin/my_init"]
RUN apt-get update
RUN apt-get -y install sudo make gcc

WORKDIR /Users/ichii/prj/playwithdocker
COPY newuser.sh /tmp/newuser.sh
ENTRYPOINT ["/tmp/newuser.sh"]
