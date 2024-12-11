**App Code Structure**

flask_app/
├── app/
│   ├── __init__.py                # Create and register the Flask app
│   ├── main/
│   │   ├── __init__.py            # Main blueprint initialization
│   │   ├── routes.py              # Main routes and logic
│   │   └── templates/             # Templates for the 'main' blueprint
│   │       ├── home.html          # Home page template
│   │       └── about.html         # About page template
│   ├── auth/
│   │   ├── __init__.py            # Auth blueprint initialization
│   │   ├── routes.py              # Auth routes and logic
│   │   └── templates/             # Templates for the 'auth' blueprint
│   │       ├── login.html         # Login page template
│   │       └── signup.html        # Signup page template
│   └── templates/                 # Global templates (e.g., base.html)
│       └── base.html              # Base layout template
├── run.py                         # Main entry point to run the app
└── requirements.txt               # Project dependencies

