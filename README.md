### ✅ **PART 1: BACKEND (Django + DRF)**

---

#### 📁 Step 1: Setup Django Project

```bash
mkdir asset-access-control
cd asset-access-control
python -m venv venv
pip install virtualenv
venv\Scripts\activate.bat  ( for windows activate your env for project  )
pip install django djangorestframework
django-admin startproject backend
cd backend
django-admin startapp core
```

Update `backend/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'core',
]

AUTH_USER_MODEL = 'core.User'
```

#### 🛠️ Step 2: Define Models (`core/models.py`)

#### 🧱 Step 3: Create & Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 🔐 Step 4: Create Custom Permissions (`core/permissions.py`)

```python
from rest_framework import permissions

class IsOrgMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
```

#### 📦 Step 5: Create Serializers (`core/serializers.py`)

#### 🌐 Step 6: Create Asset View (`core/views.py`)

#### 🔁 Step 7: Add URL Routing (`core/urls.py`)

#### 🧪 Step 8: Create Superuser & Dummy Users

Then go to the admin panel and:

- Add `Organization`
- Add 2 users:
  - **admin / admin** with role `ADMIN`
  - **member / member** with role `MEMBER`
- Add some `Asset`s for the same organization

#### 🔒 Step 9: Enable Authentication (SimpleSessionAuth)

Add to `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```


while need to register model in admin :


To register all models (`Organization`, `Asset`, and your custom `User`) in the Django admin so you can easily manage and perform CRUD operations via the admin interface, you need to:

1. **Create a custom admin for each model.**
2. **Ensure your custom user model is correctly hooked into Django admin.**

Below is the code you can add in your `backend/core/admin.py` file:

## ✅ Step-by-Step Fix: Enable CORS in Django

You're getting this error because **Django is blocking cross-origin requests** by default. React (running on `localhost:3000`) is trying to fetch from Django (`127.0.0.1:8000`), which is **cross-origin**, and **CORS (Cross-Origin Resource Sharing)** needs to be explicitly enabled.

---

## ✅ Step-by-Step Fix: Enable CORS in Django

---

### ✅ 1. Install `django-cors-headers`

In your Django backend environment:

```bash
pip install django-cors-headers
```

---

### ✅ 2. Add to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
```

---

### ✅ 3. Add Middleware in `settings.py` **at the top**

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # <-- add this at the very top
    'django.middleware.common.CommonMiddleware',
    ...
]
```

---

### ✅ 4. Allow the React frontend to access the API

Add this to your `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

> 🔁 If you're using `127.0.0.1:3000` instead of `localhost`, add that too:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

---

### ✅ 5. Restart Django Server

After saving your changes, run:

```bash
python manage.py runserver
```

---

### 🔃 Now try again

Your frontend should now be able to successfully call:

```bash
http://127.0.0.1:8000/api/assets/
```

---

### ✅ Optional: Allow All Origins (only for development)

If you're still getting errors and just want to quickly test during development, add this instead:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

> ⚠️ **Do not use this in production**. Use `CORS_ALLOWED_ORIGINS` instead.

---

Let me know if you want me to help you configure this with your current Django settings file.

### ✅ Final Steps:

1. Create a superuser to access the admin:
   ```bash
   python manage.py createsuperuser
   ```

2. create a middleware & register on setting.py file like this:

    ```
    MIDDLEWARE = [
        'backend.middleware.mock_auth.MockAuthenticationMiddleware',  # <-- add here middleware -->
    ]
    ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Visit: `http://127.0.0.1:8000/admin/`


add custom data in after login admin panel ..


Now backend is ready!

If you want to  test these apis then follow page like :  check-test.txt  file step by step


####  Frontend Setup 

bash

```
npx create-react-app frontend 
cd frontend
npm run start
```

## Visit react url :  http://localhost:3000/