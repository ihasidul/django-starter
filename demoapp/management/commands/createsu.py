"""
Extend createsuperuser command to allow non-interactive creation of a
superuser with a password.

Instructions:

  mkdir -p path-to-your-app/management/commands/
  touch path-to-your-app/management/__init__.py
  touch path-to-your-app/management/commands/__init__.py

and place this file under path-to-your-app/management/commands/

Example usage:

  manage.py createsu \
          --username foo     \
          --password foo     \
          --email foo@foo.foo
"""
from xml.dom import UserDataHandler

from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = "Create a superuser with a password and email."

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--password",
            dest="password",
            default=None,
            help="Specifies the password for the superuser.",
        )
        parser.add_argument(
            "--email",
            dest="email",
            default=None,
            help="Specifies the email for the superuser.",
        )
        # parser.add_argument(
        #     '--username', dest='username', default=None,
        #     help='Specifies the username for the superuser.',
        # )

    def handle(self, *args, **options):
        options.setdefault("interactive", False)
        database = options.get("database")
        password = options.get("password")
        username = options.get("username")
        email = options.get("email")

        if not password or not username or not email:
            raise CommandError("--email --username and --password are required options")

        user_data = {
            "username": username,
            "password": password,
            "email": email,
        }
        print(user_data.get("username"))

        self.UserModel._default_manager.db_manager(database).create_superuser(
            username=user_data.get("username"),
            password=user_data.get("password"),
            email=user_data.get("email"),
        )
        # self.UserModel._default_manager.db_manager(
        #         database).create_superuser(**user_data)

        if options.get("verbosity", 0) >= 1:
            self.stdout.write("Superuser created successfully.")
