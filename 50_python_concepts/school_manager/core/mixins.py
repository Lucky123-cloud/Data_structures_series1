from django.utils import timezone


class TimestampMixin:
    def log_action(self, action):
        print(f"{timezone.now()}: {action}")