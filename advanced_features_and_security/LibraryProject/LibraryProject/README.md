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
