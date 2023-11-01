from apps.auth_user.models import CustomUser


class UserService:

    def __init__(self):
        self.model = CustomUser

    def get_user_by_id(self, user_id):
        return self.model.objects.get(id=user_id)

    def get_by_username(self, username):
        return self.model.objects.filter(username=username).first()

    def create_user(self, username, email, password):
        user = self.model.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
