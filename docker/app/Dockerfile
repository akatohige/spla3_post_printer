FROM ubuntu:latest

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    git \
    gcc-avr \
    avr-libc \
    make \
    python3 \
    python3-pip \
    dfu-programmer \
 && apt-get autoremove -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip \
 && pip install --no-cache-dir \
    pillow

# Clone LUFA & Switch-Fightstick repository
RUN git clone https://github.com/abcminiuser/lufa.git
RUN git clone https://github.com/Loloweb/Switch-Fightstick.git

# Fightstick
WORKDIR Switch-Fightstick
RUN rm ./makefile \
 && rm ./image.c

COPY ./Makefile .
COPY ./convert.py .
COPY ./entrypoint.sh .

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]