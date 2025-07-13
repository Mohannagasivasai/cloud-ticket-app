# 🎫 Cloud Ticket Booking App

A simple **Flask web application** for booking movie tickets — built and run using **Docker**.

## ✅ Features

- Movie booking form (name, email, movie, showtime)
- Seat selection page
- Booking confirmation
- Clean HTML templates
- Dockerized for easy deployment

## 📂 Project Structure

- `app.py` - Flask application logic
- `templates/` - HTML pages (`index.html`, `select_seats.html`, `book.html`, `confirmation.html`)
- `Dockerfile` - Instructions to build Docker image
- `docker-compose.yml` - (Optional) for future expansion
- `requirements.txt` - Python dependencies

## 🚀 How to Run Locally

### Prerequisites:
- Docker installed on your system

### Run with Docker:

```bash
git clone https://github.com/Mohannagasivasai/cloud-ticket-app.git
cd cloud-ticket-app
docker build -t cloud-ticket-app .
docker run -d -p 5000:5000 --name cloud-ticket-app cloud-ticket-app
Then go to your browser:
http://localhost:5000
