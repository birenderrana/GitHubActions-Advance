FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 80

CMD ["gunicorn","--bind", "0.0.0.0:80", "app:app"]