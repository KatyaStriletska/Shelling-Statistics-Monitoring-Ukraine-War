# Stage 1: Build React app
FROM node:18 AS frontend-build

WORKDIR /app/client
COPY client/package*.json ./
RUN npm install
COPY client/ .
RUN npm run build

# Stage 2: Set up Flask backend with React build
FROM python:3.10
WORKDIR /app

# Copy backend files
COPY analysis-data-backend/ .
RUN pip install -r requirements.txt

# Copy React build files directly into the specified static folder
COPY --from=frontend-build /app/client/build /app/client/build

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"

