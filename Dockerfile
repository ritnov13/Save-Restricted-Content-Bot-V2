FROM python:3.10.4-slim-buster
# Add a new user "john" with user id 8877
RUN useradd -u 10001 john
# Change to non-root privilege
USER 10001
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN apt-get -y install git
RUN apt-get install -y wget python3-pip curl bash neofetch ffmpeg software-properties-common
COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
WORKDIR /app
COPY . .

CMD flask run -h 0.0.0.0 -p 8000 & python3 -m devgagan
# CMD gunicorn app:app & python3 -m devgagan
