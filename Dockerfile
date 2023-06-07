FROM ubuntu:latest
LABEL authors="Mohammad"

ENTRYPOINT ["top", "-b"]
# Install python
RUN apt-install python3.9-minimal libpython3.9-stdlib python3.9-distutils