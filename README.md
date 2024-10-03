# AI Powered Learning Hub

AI Powered Learning Hub is a web-based platform that aims to revolutionize learning experiences using artificial intelligence. The project is built on **Django** for the backend and utilizes **HTML**, **CSS**, **JavaScript**, and **Bootstrap** for the frontend. It offers personalized learning content, interactive quizzes, and user-friendly dashboards to improve engagement and progress tracking.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Deployment](#deployment)
- [License](#license)

## Features

- **User Authentication**: Register, login, and logout capabilities.
- **AI-Powered Personalization**: AI-driven recommendations for learning materials.
- **Interactive Quizzes**: Test your knowledge with dynamic quizzes and get immediate feedback.
- **Responsive Design**: Built using Bootstrap, the platform works seamlessly on all device sizes.
- **Learning Progress Dashboard**: Users can track their learning progress with detailed stats and metrics.
- **Content Management**: Admins can easily manage learning materials and user interactions.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6), Bootstrap 5.x
- **Database**: SQLite (default) or PostgreSQL/MySQL (optional)
- **AI Integration**: Third-party AI services or custom algorithms
- **Deployment**: (Optional) Heroku, AWS, or any Django-supported hosting platform

## Prerequisites

Before you start, ensure you have the following installed:

- **Python 3.x**
- **Django 4.x** or higher
- **Virtualenv** (optional but recommended)
- **Bootstrap 5.x**
- Basic knowledge of HTML, CSS, and JavaScript

## Installation

Step 1: Clone the Repository
git clone https://github.com/your-username/ai-powered-learning-hub.git
cd ai-powered-learning-hub

Step 2: Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Apply Migrations
python manage.py migrate

Step 5: Run the Development Server
python manage.py runserver

Step 6: Access the Web Application
Open your browser and go to http://127.0.0.1:8000/ to start using the application.

## Docker Setup

If you'd prefer to run the project using Docker, follow these steps:

### Step 1: Build the Docker Image
Ensure you have Docker and Docker Compose installed on your machine.

Create a Dockerfile in the root directory with the following content:
Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim
Step 2: Set the working directory in the container
WORKDIR /app
Step 3: Copy the current directory contents into the container at /app
COPY . /app/
Step 4: Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
Step 5: Make port 8000 available to the world outside this container
EXPOSE 8000
Step 6: Define environment variable
ENV DJANGO_SETTINGS_MODULE=ai_hub.settings
Step 7: Run the command to start Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

### Step 2: Create a docker-compose.yml File

Create a docker-compose.yml file in the root directory:
version: '3'
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DEBUG=1
    depends_on:
      - db
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: ai_hub
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
      
### Step 3: Build and Run the Containers
Now you can build and run your Django app and PostgreSQL database using Docker Compose.

docker-compose up --build
This will spin up the Django app and a PostgreSQL database in a container.

### Step 4: Access the Application
Open your browser and navigate to http://127.0.0.1:8000/ to view your app.

### Step 5: Stopping the Containers
To stop the Docker containers, run:

docker-compose down

## Usage

After running the development server, here’s how you can use the platform:

Register/Login: Sign up or log in to access the dashboard.
Explore Learning Modules: Browse through available learning modules and materials.
Take Quizzes: Attempt interactive quizzes to test your knowledge.
AI-Powered Recommendations: Receive personalized learning suggestions based on quiz performance and learning history.
Track Progress: Use your dashboard to view progress and learning stats.

## Admin Panel

For managing users and content, Django’s admin panel can be accessed at http://127.0.0.1:8000/admin/.

## Deployment

To deploy the project to a production environment:

Set up environment variables for the Django settings (DEBUG=False, ALLOWED_HOSTS, etc.).
Install a production-ready web server like Gunicorn.
Configure your database (PostgreSQL, MySQL, etc.).
Use a hosting platform such as Heroku, AWS, or DigitalOcean.

## License

The Laravel framework is open-sourced software licensed under the MIT license.

Thank you for using AI Powered Learning Hub! We hope you have a great experience.
