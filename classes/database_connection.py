import mysql.connector
from tkinter import messagebox

class DBConnection():
    """Connection to the database"""
    def __init__(self) -> None:
        try:
            self.db = mysql.connector.connect(
                host="127.0.0.1", 
                port=3308,
                user="root", 
                passwd="My@Root_2000",
                database="harmony_hues_db"
            )

            # self.db = mysql.connector.connect(
            #     host="localhost", 
            #     user="root", 
            #     passwd="My@Root_2000",
            #     database="harmony_hues_db"
            # )
            self.my_cursor = self.db.cursor()
            
        except:
            messagebox.showerror(title="Database Error", message="Fail to establish a connection to database")
            exit()
