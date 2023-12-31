from django.conf import settings
from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                email = user[1]
                password = 'admin'
                print('Creating account for %s' % (email))
                admin = User.objects.create_superuser(
                    email=email, password=password)
                admin.is_active = True
                admin.is_team = True
                admin.save()
        else:
            print(
                'Admin accounts can only be initialized if no Accounts exist'
            )
