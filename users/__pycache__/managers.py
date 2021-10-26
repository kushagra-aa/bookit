from django.contrib.auth.base_user import BaseUserManager


class CustomAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser Must be Staff')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser Must be Superuser')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
