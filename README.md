# 📜 QuillFlow 🖋️

A clean and modern blogging platform built with **Flask**, styled using **custom CSS with a gradient-glassmorphism theme**, and secured with **Flask-Talisman** for HTTP security headers. Users can **create, view, edit, and delete blog posts** through a simple UI and manage them with a SQLite database.

---

## 🚀 Features

- 🖊️ Add, Edit, Delete blog posts
- 📚 View all posts on the homepage
- 🔒 Basic HTTP security with [Flask-Talisman](https://github.com/GoogleCloudPlatform/flask-talisman)
- 🧩 SQLite database integration via SQLAlchemy
- 🎨 Custom styled UI with gradient effects and responsive layout
- 🧪 RESTful API extension with optional `api.py` module

---

## 🛠️ Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Talisman
- **Database**: SQLite
- **Frontend**: HTML, CSS (custom gradient/glass effect)
- **API**: Flask blueprint (optional)
- **Templating**: Jinja2

---

## 🧰 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flask-blog.git
cd flask-blog
````
---
## 🧾 Folder Structure 
```bash
flask-blog/
│
├── app.py               # Main Flask app
├── models.py            # SQLAlchemy model for blog posts
├── api.py               # (Optional) API blueprint
├── static/
│   └── style.css        # Custom styles
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── add_post.html
│   ├── edit_post.html
│   └── delete_post.html
└── blog.db              # SQLite database

