FROM python:3.11-slim AS base

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

FROM nginx:alpine
COPY nginx/fastapi.conf /etc/nginx/conf.d/default.conf
COPY --from=base /app /app

EXPOSE 8080
CMD ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8080 & nginx -g 'daemon off;'"]
