# Lesson 3.2

def user_info(**kwargs):
    return kwargs


name = input('Enter the name: ')
surname = input('Enter the surname: ')
birth_year = input('Enter the birth year: ')
city = input('Enter the city: ')
email = input('Enter the email address: ')
phone = input('Enter the phone number: ')

print(user_info(name=name, surname=surname, birth_year=birth_year, city=city, email=email, phone=phone))
