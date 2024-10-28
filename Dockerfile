# Stage 1: Build React app
FROM node:18 AS frontend-build

# Set working directory in the frontend
WORKDIR /client
# Copy package.json and install dependencies
COPY client/package*.json ./
RUN npm install
COPY client/ .
RUN npm run build

# Stage 2: Set up Flask backend with React build
FROM python:3.10

# Set working directory in the backend
WORKDIR /
# Copy and install backend dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose the port Flask will run on=
EXPOSE 5000

CMD ["python", "analysis-data-backend/app.py"]

