FROM ghcr.io/snakepacker/python/base
LABEL authors="Mohammad"
# Install python
RUN apt-install python3.9-minimal libpython3.9-stdlib python3.9-distutils