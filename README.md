# Task Manager App

## Overview
This is a simple full-stack Task Manager application built using Flask (backend) and React (frontend). It allows users to create, update, and delete tasks.

---

## Tech Stack
- Backend: Python (Flask)
- Frontend: React
- Database: SQLite

---

## Features
- Add new task
- Mark task as done
- Delete task

---

## Architecture
The application follows a client-server architecture:
- React frontend sends HTTP requests to Flask APIs
- Flask processes requests and interacts with the SQLite database
- Data is returned as JSON and rendered in the UI

---

## Project Structure
- backend: Contains Flask API and database logic
- frontend: Contains React UI components

---

## Technical Decisions
- Flask was chosen for its simplicity and lightweight API development
- React was used for building a dynamic and responsive UI
- SQLite was used for easy setup and local storage

---

## Validation & Correctness
- Input validation ensures empty tasks cannot be added
- API routes handle errors such as missing or invalid data

---

## AI Usage
AI tools were used for:
- Generating boilerplate code
- Debugging errors
- Structuring the project

All generated code was manually reviewed and tested.

---

## Risks / Limitations
- No authentication system
- No data persistence across environments
- Basic UI with limited styling

---

## Future Improvements
- Add user authentication (login/signup)
- Add task priority and due dates
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
