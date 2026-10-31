# 📝 Django Todo List Application

## 🎯 Project Purpose and Description
This project is a fully functional Task Management web application developed with Python and Django. 
The primary purpose of this application is to allow users to efficiently track their daily tasks, categorize them using custom tags, and manage their completion status in a user-friendly interface.

From a technical perspective, this project serves as a practical implementation of core Django concepts. It demonstrates proficiency in:
- Building robust MVT (Model-View-Template) architecture.
- Implementing relational database models (One-to-Many, Many-to-Many).
- Handling form validations and class-based generic views (CRUD operations).
- Optimizing database queries using `prefetch_related` to solve N+1 query problems.
- Managing sensitive data and configurations using environment variables (`.env`).
- Ensuring application reliability through automated unit testing.

## 🛠️ Technologies Used
- **Backend:** Python 3, Django 4.x
- **Database:** SQLite (default)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Environment Management:** `python-dotenv`

## 🚀 Setup Steps

Follow these exact instructions to configure and run the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/oleksijgrabovij/todo-list.git
   cd todo-list

2. **Create and activate a virtual environment:**
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On macOS/Linux: source venv/bin/activate

3. **Install required dependencies:**
   pip install -r requirements.txt

4. **Set up environment variables. Create a .env file and add:**
   SECRET_KEY=your_secret_key
   DEBUG=True

5. **Apply database migrations:**
   python manage.py migrate

6. **Run the development server:**
   python manage.py runserver

## Usage
Open http://127.0.0.1:8000/ in your browser. 
- Tasks: You can add, edit, delete, and toggle tasks (Complete/Undo).
- Tags: Manage tags and assign them to tasks for better organization.
- Pagination: Browse through your tasks and tags easily via the pagination controls at the bottom.