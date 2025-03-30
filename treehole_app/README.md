# Treehole App

## Overview
Treehole App is a simple Flask web application that allows users to register, log in, create posts, and comment on them. It utilizes SQLite for data storage and provides a straightforward interface for interaction.

## Features
- User registration and authentication
- Create, update, and delete posts
- Comment on posts
- View all posts and comments
- User favorites for posts

## Project Structure
```
treehole_app
├── src
│   ├── app.py                # Entry point of the Flask application
│   ├── database.py           # Database management and operations
│   ├── models.py             # Data models for User, Post, and Comment
│   ├── forms.py              # Form classes for user input
│   ├── routes.py             # URL routing and view functions
│   ├── templates             # HTML templates for rendering views
│   │   ├── base.html         # Base template for other pages
│   │   ├── index.html        # Main page displaying posts
│   │   ├── login.html        # Login form for users
│   │   └── register.html     # Registration form for new users
│   └── static                # Static files such as CSS
│       └── style.css         # Styles for the application
├── requirements.txt          # Project dependencies
└── README.md                 # Documentation for the project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd treehole_app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Ensure SQLite is installed and accessible.
   - Create the necessary tables in the SQLite database as defined in `database.py`.

## Usage
1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.