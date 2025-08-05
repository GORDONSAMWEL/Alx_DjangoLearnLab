# LibraryProject - Advanced Features and Security

## Overview

This Django project demonstrates the implementation of:
- A custom user model with extended fields.
- Custom user manager.
- Admin interface integration for the custom user model.
- Role-based access control using permissions and groups.

---

## Custom User Model

Located in `bookshelf/models.py`, the `CustomUser` model extends `AbstractUser` and adds:
- `date_of_birth` (DateField)
- `profile_photo` (ImageField)

### Custom User Manager

Handles the creation of users and superusers while supporting the new fields.

---

## Custom Permissions

Defined on the `Book` model:

```python
class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]




# Security Configuration Overview

## HTTPS and Secure Redirects

To ensure secure web communication, the following settings were added to `settings.py`:

### 🔒 Enforced HTTPS
- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enables HSTS for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Covers all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Enables preload list submission.

### 🍪 Secure Cookies
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`

### 🛡️ Secure Headers
- `X_FRAME_OPTIONS = 'DENY'`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `SECURE_BROWSER_XSS_FILTER = True`

## Deployment Notes

Ensure your production environment supports HTTPS:
- Install SSL certificates (e.g., via Let’s Encrypt).
- Update web server config (e.g., Nginx):
  ```nginx
  server {
      listen 443 ssl;
      server_name yourdomain.com;

      ssl_certificate /etc/ssl/certs/your-cert.pem;
      ssl_certificate_key /etc/ssl/private/your-key.pem;

      location / {
          proxy_pass http://127.0.0.1:8000;
      }
  }
