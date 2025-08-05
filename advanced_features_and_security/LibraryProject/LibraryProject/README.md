# LibraryProject - Permissions & Groups Management

This project demonstrates managing user **permissions and groups** in a Django application to control access to specific features based on roles.

## 📁 App: `bookshelf`

### 🔐 Custom Permissions

The `Book` model in `bookshelf/models.py` includes the following custom permissions:

- `can_view`: Can view book entries
- `can_create`: Can add new books
- `can_edit`: Can modify existing books
- `can_delete`: Can remove books

Permissions are declared in the `Meta` class of the `Book` model.

### 👥 User Groups and Assigned Permissions

| Group    | Permissions                        |
|----------|------------------------------------|
| Viewers  | `can_view`                         |
| Editors  | `can_view`, `can_create`, `can_edit` |
| Admins   | All permissions (`can_*`)          |

Groups are created and configured via the Django Admin Panel.



