from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker
from database_tables import User, db_class, Department, Enrolls
from terminal_input import input_red, print_red, input_green, print_green, enter_your_choice, input_validation,print_red_on_cyan


class Main:
    def __init__(self):
        # connection with database
        try:
            self.db_engine = create_engine(
                f"mysql+mysqlconnector://arun:{quote_plus('test')}@localhost:3306/test")
        except Exception as e:
            print(e)
        Session = sessionmaker()
        Session.configure(bind=self.db_engine)
        self.session = Session()

    def creation_struct_tables(self):
        try:
            db_class.metadata.create_all(self.db_engine)
        except Exception as e:
            print(e)

    def registration(self):
        try:
            print_red("Please enter your details for the creation of account")
            # print(User.__table__.columns.keys())
            _temp = {}
            a = True
            for i in User.__table__.columns.keys()[1:]:
                while a:
                    var = input_validation[i](input_red(f"Enter {i}"))
                    if var[0]:
                        break
                    else:
                        print(var[1])
                _temp[i] = var
            print(_temp)
            print(_temp.items())
            user_row = User(name=_temp['name'], email=_temp['email'], password=_temp['password'],
                            user_type=_temp['user_type'])
            self.session.add(user_row)
            self.session.commit()
            _temp = []
        except Exception as e:
            print(e)

    def main_menu(self):
        print_green("Welcome to ...")
        print_red("Please select your choice")
        print_green("1. Registration")
        print_green("2. Login")
        choice = enter_your_choice()
        if choice == 1:
            self.registration()
        else:
            self.login()

    def login(self):
        var = input_red("Enter your Email")
        password = input_red("Enter your password")
        data_password = self.session.query(User).filter_by(
            email=var).first().json
        if data_password['password'] == password:
            print_green("Password was correct")
            if data_password['user_type'] == 'student':
                self.student_menu(data_password['name'])
            elif data_password['user_type'] =='admin':
                self.admin_menu(data_password['name'])
        else:
            print_red("Please enter your correct password")
            self.main_menu()

    def admin_menu(self,name):
        print_red("admin menu")
        print_red("1. all students details")
        print_red("2. edit department details")
        print_red("3. edit student user details")
        print_red("4. see the enroll details")
        choice = enter_your_choice()
        if int(choice) ==1 :
            data = self.session.query(User).all()
            for row in data:
                print(row.json)
        elif int(choice) ==2:
            print_red_on_cyan("Have to implement")
        elif int(choice) ==3:
            self.edituser()
        elif int(choice) ==4:
            self.full_enroll_details()

    def full_enroll_details(self):
        data = self.session.query(Enrolls).all()
        for row in data:
            print(row.json)
        self.main_menu()

    def edituser(self):
        try:
            print_red("Change the User details Menu")
            which_user = input_red("Which user provide email id:")
            data = self.session.query(User).filter_by(email=which_user).one()
            if data:
                print_green("User details is ")
                json_data = data.json
                print(json_data)
                columns_list = data.__table__.columns.keys()[1:]
                for id, field in enumerate(columns_list):
                    print_red(f"{id}: {field}")
                val = enter_your_choice()
                value = input_red("Enter your value:")
                data = self.session.query(User).filter_by(name=json_data['name']).update(
                    {columns_list[int(val)]: value})
                print(data)
                self.session.commit()
            self.main_menu()
        except Exception as e:
            print(e)

    def student_menu(self, name):
        print_red("student menu")
        exist_or_not = self.session.query(Enrolls).filter_by(name=name).first()
        if exist_or_not:
            print_green("1. edit the details")
        else:
            print_green("0. Enroll")

        choice = enter_your_choice()
        if choice == 0:
            self.enrollment()
        elif choice == 1:
            self.edit_enrollment(exist_or_not)

    def enrollment(self):
        try:
            print_red("Please enter your details for the Enrollment")
            _temp = {}
            a = True
            for i in Enrolls.__table__.columns.keys()[1:]:
                while a:
                    var = input_validation[i](input_red(f"Enter {i}"))
                    if var[0]:
                        break
                    else:
                        print(var[1])
                _temp[i] = var
            print(_temp)
            print(_temp.items())
            dep_row = Enrolls(name=_temp['name'], Age=int(_temp['Age']), cofmarks=_temp['cofmarks'],
                              department=_temp['department'])
            self.session.add(dep_row)
            self.session.commit()
            _temp = []
            self.main_menu()
        except Exception as e:
            print(e)

    def edit_enrollment(self, data):
        print_red("Edit your enrollment form")
        print_green("Your enrollment details:-")
        json_data = data.json
        print(json_data)
        print_red("Which field you want to edit?")
        columns_list = data.__table__.columns.keys()[2:]
        for id, field in enumerate(columns_list):
            print_red(f"{id}: {field}")
        val = enter_your_choice()
        value = input_red("Enter your value:")
        data = self.session.query(Enrolls).filter_by(name=json_data['name']).update({columns_list[int(val)]:value})
        print(data)
        self.session.commit()
        self.main_menu()


# crush,partner,babe

if __name__ == '__main__':
    print_red_on_cyan("Details of database")
    print_red({'username':'arun',
               'password':'test',
               'port':3306,
               'database':'test'})
    run = Main()
    # creation of all the basic tables required for the Application.
    run.creation_struct_tables()
    run.main_menu()
