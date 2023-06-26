FROM ubuntu:22.04 as builder

RUN apt update \
    && apt upgrade -y \
    && apt install build-essential libssl-dev -y

WORKDIR /app

COPY sender.c receiver.c ./

RUN gcc -Wall -O0 -o sender sender.c
RUN gcc -Wall -O0 -o receiver receiver.c

FROM ubuntu:22.04

WORKDIR /app

COPY --from=builder /app/sender /app/receiver ./
