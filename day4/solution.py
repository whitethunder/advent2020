import re

class Passport:
    REQUIRED_FIELDS = {'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}
    EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    def __init__(self, passport_data):
        self.passport_data = p.split()

    def valid(self) -> bool:
        fields_present = set()
        for datum in self.passport_data:
            key, value = datum.split(':')
            fields_present.add(key)

            if (key == 'byr' and not self.valid_birth_year(value) or
                key == 'iyr' and not self.valid_issue_year(value) or
                key == 'eyr' and not self.valid_expiration_year(value) or
                key == 'hgt' and not self.valid_height(value) or
                key == 'hcl' and not self.valid_hair_color(value) or
                key == 'ecl' and not self.valid_eye_color(value) or
                key == 'pid' and not self.valid_passport_id(value)):
                return False

        return self.REQUIRED_FIELDS.issubset(fields_present)


    def valid_birth_year(self, year) -> bool:
        return 1920 <= int(year) <= 2002

    def valid_issue_year(self, year) -> bool:
        return 2010 <= int(year) <= 2020

    def valid_expiration_year(self, year) -> bool:
        return 2020 <= int(year) <= 2030

    def valid_height(self, height) -> bool:
        result = re.match('(\d+)(\w*)', height)
        height = result.group(1)
        units = result.group(2)

        if units == 'cm':
            return 150 <= int(height) <= 193
        elif units == 'in':
            return 59 <= int(height) <= 76
        else:
            return False

    def valid_hair_color(self, color) -> bool:
        return bool(re.match('#[0-9a-f]{6}', color))

    def valid_eye_color(self, color) -> bool:
        return(color in self.EYE_COLORS)

    def valid_passport_id(self, id) -> bool:
        return bool(re.match(r'^\d{9}$', id))


file = open('input.txt')
passports = file.read().split("\n\n")
valid_count = 0

for p in passports:
    passport = Passport(p)
    if passport.valid():
        valid_count += 1

print(valid_count)
