from faker import Faker


class BreastVSP():

    def __init__(self):
        self.name = ''
        self.age = ''
        self.address = ''
        self.intro = ''
        self.phone = ''


def get_patient_info():
    faker = Faker(locale="zh_CN")
    breastvsp = BreastVSP()
    breastvsp.name = faker.name_female()
    breastvsp.age = faker.pyint(15, 80)
    breastvsp.address = faker.address()
    breastvsp.phone = faker.phone_number()
    breastvsp.intro = faker.text()
    return breastvsp


if __name__ == "__main__":
    breastvsp = get_patient_info()
    print(breastvsp.name)
