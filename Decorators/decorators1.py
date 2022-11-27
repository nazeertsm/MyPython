##Decorators
def main_welcome(func):

    def sub_welcome_class():
        print("Welcome to Bookmyshow")
        func()
        print("please select the show date and time")
    return sub_welcome_class()

@main_welcome
def selectMovie():
    print("please select the Movie")

#main_welcome(selectMovie)


