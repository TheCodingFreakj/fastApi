#Stage 1
FROM node:17-alpine as builder
WORKDIR /app
COPY wip_ui/wip_ui_app/package*.json .
RUN npm install
COPY wip_ui/wip_ui_app/ .
RUN npm run build

#Stage 2
FROM python:3.12.2-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder . /app/build
COPY coresetup /app/coresetup
COPY shopify_app /app/shopify_app
COPY wip_ui /app/wip_ui
COPY shopify_app /app/shopify_app
COPY shopify_auth /app/shopify_auth
COPY manage.py /app/manage.py
COPY requirements.txt /app/requirements.txt
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["/app/docker-entrypoint.sh"]