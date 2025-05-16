# todoism

A minimal Flask-based “todo list” web application demonstrating basic routing, templating, and in-memory data storage.

## Features

- List existing todos  
- Add new todos via HTML form  
- Delete todos  

## Prerequisites

- Python 3.7 or newer  
- `pip` package manager  

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/todoapp.git
   cd todoapp
   ```

2. (Optional) Create and activate a virtual environment:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

No additional configuration is required. For production use, consider:

- Disabling debug mode  
- Using a persistent datastore (e.g. SQLite, PostgreSQL)  
- Serving static assets via a CDN or web server  

## Usage

1. Start the development server:  
   ```bash
   python app.py
   ```

2. Open your browser at `http://localhost:5000/`

## Project Structure

```
todoapp/
├── app.py                # Application entry point
├── requirements.txt      # Python dependencies
└── templates/
    └── index.html        # Jinja2 template for main page
```

## Extending

1. **Persistent storage**: Replace the in-memory list with a database model (e.g. Flask-SQLAlchemy).  
2. **User sessions**: Add user authentication to support multiple users.  
3. **API**: Expose REST endpoints for client-side frameworks or mobile apps.  
