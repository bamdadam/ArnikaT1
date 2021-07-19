from persiantools import characters, digits
from persiantools.jdatetime import JalaliDate


class PersianPathConverter:
    regex = '[۰۱۲۳۴۵۶۷۸۹-]+'

    def to_python(self, value):
        try:
            persian_value = value.split('-')
            english_value = [int(digits.fa_to_en(x)) for x in persian_value]
            date = JalaliDate(english_value[0], english_value[1], english_value[2]).to_gregorian()
            print(date)
            return date
        except:
            raise ValueError

    def to_url(self, value):
        return value


# if __name__ == '__main__':
#     date = ['1399', '04', '27']
#     print(JalaliDate(int(date[0]), int(date[1]), int(date[2])).to_gregorian())
