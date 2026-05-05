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
water_data= {
    "1":{
        "name":"ຫົວເສືອ",
        "ຕຸກ":{"1":4000,"2":7000,"3":10000},
        "ແພັກ":{"1":50000,"2":45000,"3":45000}
    },
    "2":{
        "name":"ນ້ຳທີບ",
        "ຕຸກ":{"1":4000,"2":6000,"3":9000},
        "ແພັກ":{"1":40000,"2":45000,"3":450000}
    },
    "3":{
        "name":"ທິວາລີ",
        "ຕຸກ":{"1":3000,"2":5000,"3":8000},
        "ແພັກ":{"1":40000,"2":45000,"3":45000}
    },
    "4":{
        "name":"Purra",
        "ຕຸກ":{"1":6000,"2":12000,"3":20000},
        "ແພັກ":{"1":60000,"2":55000,"3":60000}
    },
    "5":{
        "name":"ນ້ຳສີງ",
        "ຕຸກ":{"1":5000,"2":10000,"3":15000},
        "ແພັກ":{"1":60000,"2":65000,"3":650000}
    },
    "6":{
        "name":"ໂຊກທະວີ",
        "ຕຸກ":{"1":3000,"2":5000,"3":8000},
        "ແພັກ":{"1":42000,"2":40000,"3":40000}
    }
    
}
size_mapping={"1":"ນອ້ຍ","2":"ກາງ","3":"ໃຫຍ່"}
sales_history = []

def water_delivery():
    while True:
        print("wlecome to waterSystem")
        print("1. ສັ່ງນ້ຳ 2. ຖານຂໍ້ມູນການຂາຍ  3. ອອກ")
        main_choice=input("ເລືອກເມນູ (1-3): ")

        if main_choice=="1":
            name=get_alpha_input("ກະລຸນາປ້ອນຊື່ຂອງທ່ານ: ") 
            lname=get_alpha_input("ນາມສະກຸນ: ")  
            phone=get_phone_input("ເບີໂທ: ")
            address=input("ທີ່ຢູ່: ")
            cart=[]
            while True:
                while True: 
                    print("\nເລືອກແບຣນນ້ຳດື່ມ:")
                    for k, v in water_data.items():
                        print(f"{k}. {v['name']}")
                    brand_choice=input("ເລືອກແບຣນ (1-6): ")
                    if brand_choice in water_data:
                        break
                    print("⚠️  ກະລຸນາເລືອກແບຣນ ທີ່ ຖືກໃຫ້ຖືກຕອ້ງ!")

                selected_brand=water_data[brand_choice]
                while True:
                    print(f"\nກະລຸນາເລືອກປະເພດຂອງ '{selected_brand['name']} ")
                    print("1. ຕຸກ")
                    print("2. ແພັກ")
                    t_choice = input("ເລືອກໝາຍເລກ (1-2): ")
                    type_key = "ຕຸກ" if t_choice == "1" else "ແພັກ" if t_choice == "2" else None
                    if type_key: break
                    print("⚠️  ກະລຸນາເລືອກ 1 ຫຼື 2!")
                
                while True:
                    print(f"\nເລືອກຂະໜາດ ({type_key}):")
                    for k, name in size_mapping.items():
                        price = selected_brand[type_key][k]
                        print(f"{k}. {name} (ລາຄາ {price} ກີບ)")
                    s_choice = input("ເລືອກໝາຍເລກ (1-3): ")
                    if s_choice in size_mapping:
                        break
                    print("⚠️  ກະລຸນາເລືອກ 1-3!")
                qty = get_integer_input(f"ຕ້ອງການຈຳນວນ {size_mapping[s_choice]} {type_key} ກີບ?: ")
                unit_price = selected_brand[type_key][s_choice]
                item_total = unit_price * qty
                cart.append({
                    "brand": selected_brand['name'],
                    "type": type_key,
                    "size": size_mapping[s_choice],
                    "unit_price": unit_price,
                    "qty": qty,
                    "total": item_total
                })
                if input("\nຕ້ອງການເພີ່ມແບຣນອື່ນອີກບໍ່? (y/n): ").lower() != 'y':
                    break
            if cart:
                order_id = len(sales_history) + 1
                total_all = sum(i['total'] for i in cart)
                now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                print(f" ID: {order_id:04d} | ວັນທີ: {now}")
                print(f" ລູກຄ້າ: {name} {lname} ({phone})")
                print(f" ສົ່ງທີ່: {address}")
                for item in cart:
                   print(f" • {item['brand']} [{item['type']}{item['size']}]")
                   print(f"   {item['qty']} x {item['unit_price']} = {item['total']} ກີບ")
                print("-" * 47)
                print(f" ລວມສຸດທິ: {total_all:,} ກີບ")
                print("—"*45)
                sales_history.append({
                    "id": order_id, 
                    "name": f"{name} {lname}", 
                    "phone": phone, 
                    "total": total_all
                })
            input("\nກະລຸນາກົດ Enter ເພື່ອກັບໜ້າເລືອກ...")
        elif main_choice=="2":
            if not sales_history:
                print("\n   ຍັງບໍ່ມີຂໍ້ມູນການຂາຍ!")
            else:
                print("\n" + "📊 " + "—"*45)
                print(" ປະຫວັດການຂາຍ (Sales History) ")
                print("—"*45)
                for sale in sales_history:
                    print(f" ID: {sale['id']:04d} | ລູກຄ້າ: {sale['name']} | ເບີໂທ: {sale['phone']} | ຍອດລວມ: {sale['total']:,} ກີບ")
                print("—"*45)
            input("\n Enter ...")
        elif main_choice=="3":
              print("ກຳລັງປິດລະບົບ... ຂອບໃຈ!"); break
if __name__ == "__main__":
    water_delivery()