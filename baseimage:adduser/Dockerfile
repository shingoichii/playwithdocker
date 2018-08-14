FROM phusion/baseimage

#RUN addgroup admin
#RUN useradd -m --group admin -s /bin/bash ksuser
#RUN echo 'ksuser:screencast' | chpasswd

###CMD ["/sbin/my_init"]

RUN rm -f /etc/service/sshd/down

EXPOSE 22
RUN apt-get update
RUN apt-get -y install sudo make gcc
RUN apt-get clean

COPY newuser.sh /tmp/newuser.sh
ENTRYPOINT ["/tmp/newuser.sh"]
