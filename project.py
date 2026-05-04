import datetime

def get_alpha_input(prompt):
    while True:
        user=input(prompt).strip()
        if user.replace(" ","").isalpha() and user!="":
            return user
        print("⚠️  ກະລຸນາປອ້ນແຕ່ ໂຕໜັງສື ແລະ ຫ້າມປະຫວ່າງ!")
def get_phone_input(prompt):
    while True:
        user=input(prompt).strip()
        if user.isdigit() and len(user)>=7:
            return user
        print("⚠️  ກະລຸນາປອ້ນ ເບີໂທ ຂອງທ່ານໃຫ້ຖືກຕອ້ງ")
def get_integer_input(prompt):
    while True:
        try:
            val=int(input(prompt))
            if val>0: return val
            print("⚠️  ຈຳນວນຕ້ອງຫຼາຍກວ່າ 0!")
        except ValueError:
            print("⚠️  ກະລຸນາປອ້ນເປັນ ໂຕເລກ ເທົ່ານັ້ນ!")
brands={"1":"ຫົວເສືອ","2":"ນ້ຳທີບ","3":"ທິວາລີ","4":"Purra","5":"ນ້ຳສີງ","6":"ໂຊກທະວີ"}
