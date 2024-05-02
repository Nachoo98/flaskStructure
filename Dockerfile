FROM python:3.12

WORKDIR /src

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

