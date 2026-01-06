# Gamzan E-Commerce

A modern e-commerce web application built with Django 6.0 and Python 3.13.

## Features

- **User Authentication** - Custom user model with registration, login, and logout
- **Product Catalog** - Browse products by category with detailed product pages
- **Product Images** - Multiple images per product with gallery view
- **Responsive Design** - Mobile-first CSS architecture
- **Admin Dashboard** - Full Django admin for managing products, categories, and users

## Tech Stack

- **Backend**: Django 6.0, Python 3.13
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3 (custom CSS with CSS variables)
- **Image Processing**: Pillow
- **Code Formatting**: Black
- **Environment Management**: python-decouple

## Installation

### Prerequisites

- Python 3.13+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sample_e_com
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file**

   Create a `.env` file in the project root:
   ```env
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   INTERNAL_IPS=127.0.0.1
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Project Structure

```
sample_e_com/
├── django_project/     # Main project configuration
│   ├── settings.py     # Django settings
│   ├── urls.py         # Root URL configuration
│   └── wsgi.py         # WSGI application
├── accounts/           # User authentication app
│   ├── models.py       # CustomUser model
│   ├── views.py        # Signup view
│   └── forms.py        # User registration form
├── home/               # Landing page app
│   └── views.py        # Homepage with featured products
├── products/           # Product catalog app
│   ├── models.py       # Category, Product, ProductImage
│   ├── views.py        # List and detail views
│   └── admin.py        # Admin configuration
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── home.html       # Homepage
│   ├── products/       # Product templates
│   └── registration/   # Auth templates
├── static/css/         # Stylesheets
│   ├── base.css        # CSS variables and reset
│   ├── navigation.css  # Header and nav styles
│   ├── products.css    # Product page styles
│   ├── forms.css       # Form styles
│   ├── home.css        # Homepage styles
│   └── utilities.css   # Helper classes
└── media/              # User-uploaded files
```

## Development Commands

```bash
# Run development server
python manage.py runserver

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test

# Format code
black .
```

## Data Models

### CustomUser
Extended Django user with additional fields:
- `age` - User's age
- `phone` - Phone number

### Category
Product categories with:
- `name` - Category name
- `slug` - URL-friendly identifier
- `is_active` - Visibility toggle

### Product
Products with:
- `name`, `slug`, `description`
- `price` - Price in UZS
- `stock_quantity` - Inventory count
- `category` - Foreign key to Category
- `is_available` - Availability toggle

### ProductImage
Multiple images per product:
- `image` - Image file
- `is_primary` - Primary image flag
- `order` - Display order

## License

This project is for educational purposes.
