# syntax=docker/dockerfile:1

# ---- Stage 1: build the static site (node for Tailwind + python for SSG) ----
FROM node:20-alpine AS builder
WORKDIR /app

# Python + Jinja2 for the generator
RUN apk add --no-cache python3 \
 && python3 -m venv /opt/venv \
 && /opt/venv/bin/pip install --no-cache-dir jinja2
ENV PATH="/opt/venv/bin:$PATH"

# Node deps (Tailwind CLI + plugins) — cached unless package files change
COPY package.json package-lock.json* ./
RUN npm ci || npm install

# Source + data
COPY tailwind.config.js ./
COPY src ./src
COPY data ./data

# Canonical/sitemap base URL (overridable via compose build arg)
ARG NUTRIBUCKS_SITE_URL=https://nutribucks.shop
ENV NUTRIBUCKS_SITE_URL=${NUTRIBUCKS_SITE_URL}

# 1) render HTML into dist/  2) compile Tailwind against the rendered output
RUN python3 src/build.py \
 && ./node_modules/.bin/tailwindcss -i ./src/assets/app.css -o ./dist/assets/app.css --minify

# ---- Stage 2: serve the static output with nginx ----
FROM nginx:1.27-alpine AS runtime
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD wget -qO- http://127.0.0.1/ >/dev/null 2>&1 || exit 1
CMD ["nginx", "-g", "daemon off;"]
