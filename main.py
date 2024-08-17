
class User():
    def __int__(self, user_id, name, access_user):
        self.user_id = user_id
        self.name = name
        self.access = access_user
        names = []


class Admin(User):
    def __int__(self, access_admin):
        self.access_admin = access_admin

    def add_user(self, names):

            # Define the number of names you want to input
        num_of_names = int(input("Enter the number of names you want to input: "))

            # Use a for loop to take input for each name
        for i in range(num_of_names):
            name = input(f"Enter name {i + 1}: ")
            names.append(name)

            # Print the list of names
        print("The list of names you entered is:", names)
        return names

        # print(user_list)

    def remove_user(self, names):
       # del_name = input("Enter the name you want to remove: ")
        #names.remove(del_name)
       del_name = input("Enter the name you want to remove: ")
       if del_name in names:
           names.remove(del_name)
           print(f"{del_name} has been removed from the list.")
       else:
           print(f"{del_name} is not in the list.")

Admin.add_user()

Admin.remove_user()
