FROM ubuntu:20.04
#RUN echo this is a very fake change!!!
RUN apt update && apt -y upgrade
RUN apt update && apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa 
RUN apt update && apt -y install python3.10 && apt -y install python3-pip && apt -y install --reinstall python3.10-distutils  
RUN apt update &&  update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
RUN apt update &&  update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
RUN apt update && apt -y install git && apt install nano
RUN apt update && apt install -y curl && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
RUN apt update && apt install -y build-essential libssl-dev ca-certificates libasound2 wget
RUN apt update && apt install -y alsa-base alsa-utils
RUN apt update && apt install -y openssh-client
RUN apt update && apt install -y dos2unix
ENV APIAUTH=62HM2HwibYLMSBArcTs6HGiwrjNuXsH-w9uN9svlX!GoZRW5z!4854GtrWm5D5itdowvmiM70KL4PLQp/vv?I1OVXWML4p76fRFqVe6EXlTPgTgidX0QH3yKZjEeEBrR70FH=muShmG5T7S3R7fi2clQX=zRDvpASs3?KVcxndSzD4MMv!0yY7PvTtv?rcHd8sQEs0tT4h67s/fLOKsPD2ID=wqBb/R-YnLtXW/pvE8xxSdDJjWQDva-n/7BROlM
WORKDIR /home 
RUN mkdir robocon
WORKDIR /robocon
RUN echo force rebuild from heree
RUN echo forceeeee
RUN echo yay fixed
RUN echo eee
#RUN apt update && echo force rerun! > /dev/null && git clone --single-branch --branch onRosie https://github.com/kev1n3151/RoboCon2024Sem2.git
RUN echo test10 && git clone --single-branch --branch onRosie https://github.com/kev1n3151/RoboCon2024Sem2.git
COPY rosiekey.pem /root/.ssh/rosiekey.pem
COPY rosiekeyhost /root/.ssh/rosiekeyhost
RUN chmod 600 /root/.ssh/rosiekey.pem
#ADD start.py /rosiecon/RosieCon2023Sem2/
RUN chmod +x /robocon/RoboCon2024Sem2/start.py
#RUN echo 'python3 /rosiecon/RosieCon2023Sem2/start.py' >> ~/.bashrc
#RUN echo 'ssh -t -i /root/.ssh/rosiekey.pem -o UserKnownHostsFile=/root/.ssh/rosiekeyhost ubuntu@ec2-52-62-118-55.ap-southeast-2.compute.amazonaws.com -N &' >> ~/.bashrc
#RUN sleep 20
#CMD ssh -i /root/.ssh/rosiecon.pem -o UserKnownHostsFile=/root/.ssh/rosieconhost ubuntu@ec2-52-62-118-55.ap-southeast-2.compute.amazonaws.com -N &
WORKDIR /robocon/RoboCon2024Sem2/FrontEnd
RUN pip3 install -r requirements.txt 
ENV SPEECH_KEY=1860aa98934148fd8fb7df6b7919f5ab
ENV SPEECH_REGION=australiaeast
RUN sed -i 's/^defaults.pcm.surround/#&/' /usr/share/alsa/alsa.conf
RUN chmod +x /robocon/RoboCon2024Sem2/stop.py
RUN echo "trap 'echo Stopping Server...; python3 /robocon/RoboCon2024Sem2/stop.py' EXIT" >> ~/.bashrc
#CMD ["/bin/bash", "-c", "\ echo Rosie started; \ while :; do sleep 1; done"]
RUN chmod +x /robocon/RoboCon2024Sem2/startcon.sh
#RUN apt update && apt install -y iputils-ping
# Added action monitor scripts
COPY actionmonitor.sh /robocon/RoboCon2024Sem2
RUN chmod +x /robocon/RoboCon2024Sem2/actionmonitor.sh
#Copy tuck & untuck
COPY tuck /robocon/RoboCon2024Sem2/tuck
COPY untuck /robocon/RoboCon2024Sem2/untuck
#RUN chmod +x /robocon/RoboCon2024Sem2/tuck/run-tuck-docker
#RUN chmod +x /robocon/RoboCon2024Sem2/tuck/build-docker
#RUN chmod +x /robocon/RoboCon2024Sem2/untuck/run-untuck-docker
#RUN chmod +x /robocon/RoboCon2024Sem2/untuck/build-docker
CMD ["/bin/bash", "-c", "\ echo Rosie started; \ while :; do sleep 1; done"]
