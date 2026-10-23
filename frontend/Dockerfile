FROM node:24.20.0-slim AS build
WORKDIR /app
COPY package.json package-lock.json ./
COPY frontend/package.json frontend/package.json
COPY runner/package.json runner/package.json
RUN npm ci
COPY frontend ./frontend
RUN npm run build

FROM python:3.12-slim
WORKDIR /app
COPY --from=build /app/frontend/dist ./
USER 10001
CMD ["python", "-m", "http.server", "5173", "--bind", "0.0.0.0"]
