class User:
    def __init__(self, _user_id, name, __access_user):
        self._user_id = _user_id
        self.name = name
        self.access = __access_user
        self.names = []

    def get_user_id(self):
        print(self._user_id)
        return self._user_id

    def get__access_user(self):
        __access_user="доступ разрешен"
        print(self.access)
        return self.access


class Admin(User):
    def __init__(self, _user_id, name, access_user, access_admin):
        super().__init__(_user_id, name, access_user)
        self.__access_admin = access_admin  # Оставляем одно подчеркивание для защиты

    def add_user(self):
        # Количество имен, которые вы хотите ввести.
        num_of_names = int(input("Enter the number of names you want to input: "))

        # Используем цикл for для ввода имен
        for i in range(num_of_names):
            name = input(f"Enter name {i + 1}: ")
            self.names.append(name)

        print("The list of names you entered is:", self.names)

    def remove_user(self):
        del_name = input("Enter the name you want to remove: ")
        if del_name in self.names:
            self.names.remove(del_name)
            print(f"{del_name} has been removed from the list.")
        else:
            print(f"{del_name} is not in the list.")

    def set_private(self, access_status):
        self.__access_admin = access_status
        return access_status

    def get_status(self):
        print(self.__access_admin)
        return self.__access_admin


# Пример использования
admin_status = Admin(_user_id=1, name="AdminName", access_user="full", access_admin="full")
au = User(_user_id=2, name="g", _User__access_user=None)

# Получение информации о пользователе
print(admin_status.get_user_id())
print(admin_status.name)
print(admin_status.access)
print(admin_status.set_private("private_access"))
print(au.get__access_user)

# Добавление пользователей
admin_status.add_user()

# Удаление пользователя
admin_status.remove_user()

au.get__access_user()
