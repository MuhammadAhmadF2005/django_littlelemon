
````markdown
# 🍋 Little Lemon — Django Web App

Capstone-style Django web application for a restaurant, featuring menu listings, detailed item pages, and admin management.

---

## 📌 Project Overview

- **Menu Browsing:** View all menu items on a listing page.
- **Detail View:** Click on a menu item to see full details.
- **Admin Interface:** Manage menu items using Django’s built-in admin.
- **Built With:**  
  - Django 5.x  
  - SQLite (default) or MySQL (optional)  
  - HTML, CSS, Django templates

---

## 🚀 Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/MuhammadAhmadF2005/django_littlelemon.git
   cd django_littlelemon
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install django
   ```

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

   Visit the app at [http://127.0.0.1:8000/menu/](http://127.0.0.1:8000/menu/)
   Admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧩 App Structure

* `restaurant/models.py` – Defines the `MenuItem` model.
* `restaurant/views.py` –

  * `menu` view — lists items
  * `display_menu_item` view — shows item details
* `restaurant/urls.py` – URL routing for both views.
* `restaurant/admin.py` – Registers `MenuItem` for admin.
* `templates/` –

  * `menu.html` – listing page
  * `menu_item.html` – detail page
  * `base.html` – common layout

---

## ✅ Usage

* Use the Admin panel to add or edit menu items.
* Visit `/menu/` to see a listing of all items.
* Visit `/menu_item/<id>/` to view detailed info.

---

## 🔧 Customization Options

* **Database:** Switch to MySQL by updating `DATABASES` in `settings.py` and installing `mysqlclient` or `pymysql`.
* **Design:** Update the CSS under `static/` to change frontend styles.
* **Functionality:**

  * Add fields like `description` or `image` to the model
  * Create a Reservation app to let users book a table

---

## 🧱 Similar Projects

Similar student projects built from the [Meta Django Course Capstone](https://github.com/karisalim/littlelemon-django) ([github.com][1], [github.com][2], [github.com][3], [github.com][4]) include menu lists, admin support, and full CRUD functionality.

---

## 👤 Author

**Muhammad Ahmad** — Django developer
View portfolio or contact via GitHub: `@MuhammadAhmadF2005`

---

## 📝 License

This project is open-source under MIT License. Copy, modify, or use it freely. ❤️

```

