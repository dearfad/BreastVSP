from faker import Faker


class BreastVSP():

    def __init__(self):
        self.name = ''
        self.age = ''
        self.address = ''


def get_patient_info():
    faker = Faker(locale="zh_CN")
    breastvsp = BreastVSP()
    breastvsp.name = faker.name_female()
    breastvsp.address = faker.address()
    breastvsp.age = faker.pyint(15, 80)
    return breastvsp


if __name__ == "__main__":
    breastvsp = get_patient_info()
    print(breastvsp.name)
