FROM ubuntu:latest
LABEL authors="jao"

ENTRYPOINT ["top", "-b"]