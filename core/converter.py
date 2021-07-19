from persiantools import characters, digits
from persiantools.jdatetime import JalaliDate

from core.exceptions import WrongDateFormat


class PersianPathConverter:
    regex = '[۰۱۲۳۴۵۶۷۸۹-]+'

    def to_python(self, value):
        try:
            persian_value = value.split('-')
            english_value = [int(digits.fa_to_en(x)) for x in persian_value]
            date = JalaliDate(english_value[0], english_value[1], english_value[2]).to_gregorian()
            # print(date)
            return date
        except (ValueError, IndexError):
            raise ValueError

    def to_url(self, value):
        return value

# if __name__ == '__main__':
#     date = ['۱۳۹۵', '۰۴', '۴۴']
#     english_value = [int(digits.fa_to_en(x)) for x in date]
#     try:
#         print(JalaliDate(int(english_value[0]), int(english_value[1]),
#                      int(english_value[2])).to_gregorian())
#     except ValueError:
#         print('value error')
