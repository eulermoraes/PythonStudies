from utils import database


USER_MENU = """ 
Enter:
- [1] Add new book
- [2] List books
- [3] Mark book as read
- [4] Delete book
- [q] Quit

What's your choice:
"""



def menu():
    user_input = ""
    while user_input != 'q':
        user_input = input(USER_MENU)
        if user_input == '1':
            add()
        elif user_input == '2':
            list()
        elif user_input == '3':
            is_read()
        elif user_input == '4':
            delete()
        else:
            print("Warning: Invalid option")



class book(self,name,author,read):
    def main(self,name,author,read):
        self.name = name
        self.author = author
        self.read = read

    def add():
        pass

    def list():
        pass

    def is_read():
        pass

    def delete():