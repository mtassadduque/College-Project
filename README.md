# Government College of Technology, Samanabad, Faisalabad — Website

A responsive Django website with three pages: **Home**, **Contact**, and **Login / Sign up**.

## Features

- Fully responsive layout (desktop, tablet, mobile with a hamburger menu)
- **Home** page: hero, department listing, stats strip, about section
- **Contact** page: form that saves submissions to the database (visible in Django admin) and shows a success message
- **Login / Sign up**: Django's built-in authentication, with a custom sign-up form (username, name, email, password) and styled templates
- Django admin panel to view contact messages and manage users

## Project structure

```
gct_website/
├── manage.py
├── requirements.txt
├── college_site/        # project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── main/                 # the app
    ├── models.py         # ContactMessage model
    ├── forms.py          # ContactForm, SignUpForm
    ├── views.py           # home, contact, login, signup views
    ├── urls.py
    ├── admin.py
    ├── templates/main/    # base.html, home.html, contact.html, login.html, signup.html
    └── static/main/css/style.css
```

## Setup

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations** (creates the SQLite database and tables):
   ```bash
   python manage.py migrate
   ```

4. **Create an admin account** (optional, to view contact messages in `/admin/`):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. Visit **http://127.0.0.1:8000/** in your browser.

## Pages

| Page      | URL          | Notes                                             |
|-----------|--------------|----------------------------------------------------|
| Home      | `/`          | College overview, departments, stats               |
| Contact   | `/contact/`  | Contact form → saved to DB, viewable in `/admin/`   |
| Login     | `/login/`    | Existing users log in                               |
| Sign up   | `/signup/`   | New users register (auto logged in after signup)   |
| Logout    | `/logout/`   | POST-only, linked from the nav bar once logged in   |

## Before deploying to production

This project ships with development-friendly defaults. Before putting it online, you should:

- Set `DEBUG = False` in `college_site/settings.py`
- Replace `SECRET_KEY` with a new, secret value (and load it from an environment variable)
- Set `ALLOWED_HOSTS` to your real domain
- Switch the database from SQLite to Postgres/MySQL for production traffic
- Run `python manage.py collectstatic` and serve static files via your web server / a CDN
- Serve the app over HTTPS

## Customizing

- **College details** (departments, stats, address, phone): edit `main/views.py` (the `DEPARTMENTS` and `STATS` lists) and `main/templates/main/contact.html` (the info card).
- **Colors / fonts**: all design tokens are CSS variables at the top of `main/static/main/css/style.css`.
- **Logo**: the `.brand-mark` in `base.html` is currently a text badge ("GCT"); swap in an `<img>` tag if you have an official crest.
