# Task Manager App

## Overview
This is a simple full-stack Task Manager application built using Flask (backend) and React (frontend). It allows users to create, update, and delete tasks.

---

## Architecture
The application follows a client-server architecture:
- React frontend sends HTTP requests to Flask APIs
- Flask backend processes requests and interacts with the database
- SQLite database stores task data

---

## Project Structure
- backend: Flask API and database logic
- frontend: React UI components

---

## Technical Decisions
- Flask was chosen for its simplicity and ease of building REST APIs
- React was used for creating a dynamic and interactive user interface
- SQLite was selected as a lightweight database for quick setup
- Axios was used for API communication between frontend and backend

---

## Validation & Correctness
- Input validation ensures that empty tasks cannot be added
- Backend handles invalid requests with proper error responses

---

## AI Usage
AI tools were used for:
- Generating boilerplate code
- Debugging errors
- Structuring the project

All generated code was reviewed and tested manually.

---

## Risks / Limitations
- No authentication system (anyone can access the app)
- Limited UI design (basic interface)
- No deployment (runs locally only)

---

## Extension Approach (Future Improvements)
- Add user authentication (login/signup)
- Add task priority and due dates
- Improve UI design
- Deploy application to cloud

---

## How to Run

### Backend
cd backend  
venv\Scripts\activate  
python app.py  

### Frontend
cd frontend  
npm install  
npm start  

---

I focused on building a clean and understandable solution as a beginner while ensuring correct functionality.
