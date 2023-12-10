FROM tensorflow/tensorflow:latest-gpu

ARG DEBIAN_FRONTEND=noninteractive

# Install apt dependencies
RUN apt-get update && apt-get install -y \
    git \
    gpg-agent \
    protobuf-compiler \
    python3-cairocffi \
    python3-lxml \
    python3-tk \
    wget \
    libsm6 \
    libxext6 \
    libxrender-dev

# Add new user to avoid running as root
# RUN useradd -ms /bin/bash tensorflow
# USER tensorflow

RUN mkdir /app

COPY requirements.txt /app

WORKDIR /app

RUN python -m pip install -U pip
RUN python -m pip install -r requirements.txt

COPY . /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
