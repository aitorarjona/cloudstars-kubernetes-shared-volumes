FROM ubuntu:22.04 as builder

RUN apt update \
    && apt upgrade -y \
    && apt install build-essential libssl-dev -y

WORKDIR /app

COPY procA.cpp procB.cpp ./

RUN g++ -Wall -O0 -o proc proc.cpp -lcrypto

FROM ubuntu:22.04

WORKDIR /app

COPY --from=builder /app/proc ./
