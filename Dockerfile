# Stage 1: Build React app
FROM node:18 AS frontend-build

# Set working directory in the frontend
WORKDIR /client

# Copy package.json and install dependencies
COPY client/package*.json ./
RUN npm install
RUN npm install plotly

# Copy the entire React app source code and build it
COPY client/ .
RUN npm run build

# Stage 2: Set up Flask backend with the React build
FROM python:3.10

# Set working directory in the backend
WORKDIR /

# Copy and install backend dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Flask app code into the container
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Set environment variables if needed
# ENV FLASK_ENV=production

# Start the Flask application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

