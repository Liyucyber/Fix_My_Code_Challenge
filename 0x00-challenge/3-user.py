#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid
class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """
    __password = None
    def __init__(self):
        """
        Initialize a new user:
        - assigned an unique `id`
        """
        self.id = str(uuid.uuid4())
    @property
    def password(self):
        """
        Password getter
        """
        return self.__password
    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - `None` if `pwd` is `None`
        - `None` if `pwd` is not a string
        - Hash `pwd` in MD5 before assign to `__password`
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self._password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
	@@ -54,7 +54,7 @@ def is_valid_password(self, pwd):
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().upper() == self.__password


if __name__ == '__main__':
	@@ -84,7 +84,7 @@ def is_valid_password(self, pwd):
    if user_2.password is not None:
        print("User.password should be None if setter to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right \
password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right \
password")
    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")
    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")
    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set \
before")
