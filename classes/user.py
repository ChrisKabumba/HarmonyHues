from classes.database_connection import DBConnection
import smtplib
import random
from datetime import datetime

EMAIL = "christian.kabumba@strathmore.edu"
PSSWD = "qbif nqgf ryxh duay"

class RegisterUserData:
    """Data structure for holding the data necessary to register a user"""
    def __init__(self) -> None:
        self.first_name: str
        self.middle_name: str
        self.last_name: str
        self.email: str
        self.phone_number: str
        self.date_of_birth: None
        self.current_address: str
        self.password: str

class Content:
    """Data structure that holds a content to be stored to a database"""
    def __init__(self) -> None:
        self.poster_id: int
        self.time_posted: datetime
        self.post_type: str
        self.post: str

class User:
    def __init__(self) -> None:
        self.id: int
        self.first_name: str
        self.middle_name: str
        self.last_name: str
        self.email: str
        self.phone_number: str
        self.date_of_birth: None
        self.current_address: str
        self.db_connect = DBConnection()

    def sign_in(self, email:str, password:str) -> bool:
        """Return true if it successfully created an object with the user details. False otherwise"""

        #Query database here with username and fetch password
        user_data = None
        try:
            self.db_connect.my_cursor.execute(f"SELECT * FROM users WHERE email='{email}'")
            for row in self.db_connect.my_cursor:
                user_data = row
        except:
            return False

        #Check password against password from the database. If match, return True, or else, False
        if user_data != None:
            db_password = user_data[8]
            if db_password == password:
                self.id = user_data[0]
                self.first_name =  user_data[1]
                self.middle_name = user_data[2]
                self.last_name = user_data[3]
                self.email = user_data[5]
                self.phone_number = user_data[4]
                self.date_of_birth = user_data[7]
                self.current_address = user_data[6]
                return True
            else:
                return False

        else:
            return False
        
    def sign_up(self, registerUserData: RegisterUserData) -> bool:
        #Register a user with the appropriate data that is write the data to the database
        first_name = registerUserData.first_name
        middle_name = registerUserData.middle_name
        last_name = registerUserData.last_name
        email = registerUserData.email
        phone_number = registerUserData.phone_number
        date_of_birth = registerUserData.date_of_birth
        current_address = registerUserData.current_address
        password = registerUserData.password

        try:
            sql = "INSERT INTO users(first_name, middle_name, last_name, current_address, date_of_birth, _password, email, phone_number)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (first_name, middle_name, last_name, current_address, date_of_birth, password, email, phone_number)
            #If process succeed, return true, or else, return false
            self.db_connect.my_cursor.execute(sql, data)
            self.db_connect.db.commit()
            return True
        
        except:
            return False
        
    def send_otp(self, email:str) -> str:
        """Generate OTP code for signing up"""
        #this method is tied to the sign up method
        #generate OTP here     
        otp_code = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

        #send here
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PSSWD)
            mssg = f"Subject: HarmonyHues: OTP code for \n\nYour OTP code is: {otp_code}"
            connection.sendmail(from_addr=EMAIL, to_addrs=email, msg=mssg)

        #return the OTP string
        return otp_code

    def sign_out(self):
        """Sign a logged in user out"""
        #set class variables to 0 or empty strings
        self.id = 0
        self.first_name =  ""
        self.middle_name = ""
        self.last_name = ""
        self.email = ""
        self.phone_number = ""
        self.date_of_birth = ""
        self.current_address = ""

    def upload_content(self, content: Content) -> bool:
        """Upload content to the database. If succeed, it returns true, or else, false. The post_type can take these values:
        photo, video, text, or location"""
        #Write the content here
        poster_id = content.poster_id
        time_posted = content.time_posted
        post_type = content.post_type
        post = content.post

        sql = "INSERT INTO post_contents(poster_id, time_posted, post_type, post) VALUES(%s, %s, %s, %s)"
        data = (poster_id, time_posted, post_type, post)
        try:
            self.db_connect.my_cursor.execute(sql, data)
            self.db_connect.db.commit()
            return True
        except:
            return False

    def remove_content(self, poster_id: int, time_posted: datetime) -> bool:
        """Remove a posted content"""
        #Remove a posted content here. Need the primary key
        sql = "DELETE FROM post_contents WHERE poster_id=%s AND time_posted=%s"
        data = (poster_id, time_posted)
        try:
            self.db_connect.my_cursor.execute(sql, data)
            self.db_connect.db.commit()
            return True
        except:
            return False

    def get_content(self, poster_id: int) -> list:
        #This method returns the content posted by a poster from the database. It is tied to remove_content
        contents = []

        try:
            self.db_connect.my_cursor.execute(f"SELECT * FROM post_contents WHERE poster_id={poster_id}")
            for data in self.db_connect.my_cursor:
                contents.append(data)
            return contents
        except:
            return []

    def share_content(self) -> bool:
        pass
        #Share content of a user with another one

    def edit_profile(self) -> bool:
        """Edit the profile of a user"""

    def choose_interest(self) -> bool: 
        """Allow one to pick an interest"""

    def browse_content(self) -> bool:
        """Allow one to see a posted content"""

    def join_community(self) -> bool:
        """Allow one to join a community"""

    def plan_event(self) -> bool:
        """Allow one to plan an event that other members can attend"""
        

#Next task:html and css files. Include attributes in User and Admin classes