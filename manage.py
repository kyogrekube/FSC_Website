#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as runserver

runserver.default_port = "80"  # Running on port 80

def create_users():
    """Create admin and standard user if they don't exist."""
    import django
    django.setup()  # Initialize Django
    from django.contrib.auth.models import User

    # Create admin user
    if not User.objects.filter(username='fscAdminUser').exists():
        User.objects.create_superuser(
            username='fscAdminUser',
            email='fscaccountemail@gmail.com',
            password='RCOSfall2024'
        )
        print("Admin user created successfully.")
    else:
        print("Admin user already exists.")

    """# Create standard user (non-admin)
    if not User.objects.filter(username='phi_gamma_delta').exists():
        User.objects.create_user(
            username='phi_gamma_delta',
            email='phi_gamma_delta@example.com',
            password='phi_gamma_delta'
        )
        print("Standard user 'phi_gamma_delta' created successfully.")
    else:
        print("Standard user 'phi_gamma_delta' already exists.")"""

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Create users when running the server
    if sys.argv[1] == 'runserver':
        create_users()  # Create admin and standard user

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
