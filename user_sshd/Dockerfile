#FROM ubuntu:18.04
FROM ubuntu:18.04full

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN addgroup admin
RUN useradd -m --group admin -s /bin/bash ksuser
RUN echo 'ksuser:screencast' | chpasswd
#RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
