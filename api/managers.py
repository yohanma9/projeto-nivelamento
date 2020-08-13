from django.contrib.auth.models import UserManager
from safedelete.managers import SafeDeleteManager


class ClienteManager(SafeDeleteManager, UserManager):
    pass
