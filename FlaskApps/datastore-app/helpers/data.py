from google.cloud import datastore
from flask_bcrypt import Bcrypt
client = datastore.Client()
bcrypt = Bcrypt()


class Loginbase:
    def __init__(self, email):
        self.email = email

    def logininfo(self):
        key = client.key("AUTH", self.email)
        entity = client.get(key)
        return entity

    def deleteacc(self):
        key = client.key("AUTH", self.email)
        client.delete(key)
        return None


class Signupbase:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def signupinfo(self):
        with client.transaction():
            key = client.key("AUTH", self.email)
            task = datastore.Entity(key=key)
            task.update(
                {
                    "name": self.name,
                    "email": self.email,
                    "password": bcrypt.generate_password_hash(self.password).decode('utf-8')
                }
            )
            client.put(task)
            return task


class ForgotPassword:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def forgotpassword(self):
        with client.transaction():
            key = client.key("AUTH", self.email)
            entity = client.get(key)
            if not entity.get("email") == self.email and self.password:
                return "Wrong Email or enter new password again"
            entity["password"] = bcrypt.generate_password_hash(self.password).decode('utf-8')
            client.put(entity)
            return entity
