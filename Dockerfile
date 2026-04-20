FROM python:3.10

WORKDIR /app

COPY . .

CMD ["sh", "-c", "python main.py && tail -f /dev/null"]