from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            date_obj = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date_obj)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone not found")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = Phone(new_phone).value
                return
        raise ValueError("Phone not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        bday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "—"
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {bday}"
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


class AddressBook(UserDict):

    def is_leap_year(self, year: int) -> bool:
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

    def adjust_for_leap_year(self, birthday: datetime.date, year: int) -> datetime.date:
        if birthday.month == 2 and birthday.day == 29:
            if not self.is_leap_year(year):
                return datetime(year, 2, 28).date()
        return birthday

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact not found")
        
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday = record.birthday.value
            try:
                birthday_this_year = birthday.replace(year=today.year)
            except ValueError:
                birthday_this_year = self.adjust_for_leap_year(birthday, today.year)

            if birthday_this_year < today:
                try:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                except ValueError:
                    birthday_this_year = self.adjust_for_leap_year(birthday, today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming