# COL-BI: Collaborate & Build Ideas

COL-BI is a web-based platform that connects students and professionals by helping them find teammates for their projects. Whether you’re working on academic assignments, hackathons, or personal projects, COL-BI makes collaboration easier by matching people based on skills, fields, and project requirements.

---

## 🚀 Features
- User registration and login system  
- Post project ideas and requirements  
- Search for teammates based on skills and interests  
- View and connect with potential collaborators  
- Responsive design using **HTML, CSS**  
- Backend powered by **Flask (Python)**  
- Data persistence using **MySQL**  

---

## 📂 Project Structure
Col-BI/
│── static/
│ ├── images/ # Images used in the UI
│ ├── style.css # Main stylesheet
│ └── style2.css # Additional styles
│
│── templates/
│ ├── about.html # About page
│ ├── find.html # Page to find teammates
│ ├── form.html # Input form for teammate requirements
│ ├── index.html # Homepage
│ ├── login.html # User login page
│ ├── register.html # User registration page
│ ├── search.html # Search functionality page
│ └── teammates.html # Display potential teammates
│
│── app.py # Flask backend
│── schema.sql # Database schema
│── README.md # Project documentation



---

## 🗄️ Database Schema
The database is defined in **schema.sql**. It contains two main tables:

- **users** → Stores registered users  
- **find_teammate** → Stores project requirements and teammate posts  

```sql
CREATE DATABASE IF NOT EXISTS colbi;
USE colbi;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS find_teammate (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    field VARCHAR(100) NOT NULL,
    current_proj VARCHAR(200) NOT NULL,
    teammate_specs TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
⚙️ Installation & Setup
Clone the repository


git clone https://github.com/your-username/Col-BI.git
cd Col-BI
Create and activate a virtual environment


python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install dependencies


pip install -r requirements.txt
Import the database


mysql -u root -p < schema.sql
Run the Flask app


python app.py
Open in browser


http://127.0.0.1:5000/
🛠️ Tech Stack
Frontend: HTML, CSS

Backend: Python Flask

Database: MySQL

Server: Localhost (Flask development server)

📌 Future Improvements
Add messaging/chat feature for teammates

Implement project categories and filtering

Add email verification and stronger authentication

Deploy on a cloud platform (Heroku, Render, etc.)

📸 Screenshots
(Add your project screenshots here for better visualization)

📜 License
This project is licensed under the MIT License.


---

✅ This is now **one single markdown block from top to bottom**.  
Do you want me to also create a **requirements.txt** for you so your repo is complete?