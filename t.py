import datetime

# --- ຟັງຊັນກວດສອບຂໍ້ມູນ (Error Handling) ---
def get_alpha_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.replace(" ", "").isalpha() and user_input != "":
            return user_input
        print("⚠️ ແຈ້ງເຕືອນ: ກະລຸນາປ້ອນແຕ່ 'ໂຕໜັງສື' ແລະ ຫ້າມປະຫວ່າງ!")

def get_phone_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit() and len(user_input) >= 7:
            return user_input
        print("⚠️ ແຈ້ງເຕືອນ: ເບີໂທຕ້ອງເປັນ 'ໂຕເລກ' 7 ຫຼັກຂຶ້ນໄປ!")

def get_integer_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0: return val
            print("⚠️ ແຈ້ງເຕືອນ: ຈຳນວນຕ້ອງຫຼາຍກວ່າ 0!")
        except ValueError:
            print("⚠️ ແຈ້ງເຕືອນ: ກະລຸນາປ້ອນເປັນ 'ໂຕເລກ' ເທົ່ານັ້ນ!")

# --- ຖານຂໍ້ມູນລາຄາແຍກຕາມແບຣນ (ສາມາດປັບແກ້ລາຄາໄດ້ຕາມໃຈ) ---
# ໂຄງສ້າງ: [ແບຣນ] -> [ປະເພດ] -> [ຂະໜາດ: 1-ໃຫຍ່, 2-ກາງ, 3-ນ້ອຍ]
water_data = {
    "1": {
        "name": "ຫົວເສືອ",
        "ຕຸກ": {"1": 10, "2": 7, "3": 5},
        "ແພັກ": {"1": 100, "2": 70, "3": 50}
    },
    "2": {
        "name": "ນ້ຳທີບ",
        "ຕຸກ": {"1": 9, "2": 6, "3": 4},
        "ແພັກ": {"1": 90, "2": 60, "3": 40}
    },
    "3": {
        "name": "ທິວາລີ",
        "ຕຸກ": {"1": 8, "2": 5, "3": 3},
        "ແພັກ": {"1": 80, "2": 50, "3": 30}
    },
    "4": {
        "name": "Purra",
        "ຕຸກ": {"1": 15, "2": 10, "3": 8},
        "ແພັກ": {"1": 150, "2": 100, "3": 80}
    },
    "5": {
        "name": "ນ້ຳສີງ",
        "ຕຸກ": {"1": 12, "2": 8, "3": 6},
        "ແພັກ": {"1": 120, "2": 80, "3": 60}
    },
    "6": {
        "name": "ໂຊກທະວີ",
        "ຕຸກ": {"1": 7, "2": 4, "3": 2},
        "ແພັກ": {"1": 70, "2": 40, "3": 20}
    }
}

size_names = {"1": "ໃຫຍ່", "2": "ກາງ", "3": "ນ້ອຍ"}
sales_history = []

def water_delivery_system():
    while True:
        print("\n" + "=".center(55, "="))
        print("   🌟 ລະບົບສົ່ງນ້ຳດື່ມ (Full Pricing System) 🌟")
        print("=".center(55, "="))
        print("\f","1. [ສັ່ງນ້ຳ] | 2. [ຖານຂໍ້ມູນການຂາຍ] | 3. [ອອກ]")
        
        main_choice = input("\nເລືອກເມນູ (1-3): ")

        if main_choice == "1":
            fname = get_alpha_input("ຊື່ລູກຄ້າ: ")
            lname = get_alpha_input("ນາມສະກຸນ: ")
            phone = get_phone_input("ເບີໂທ: ")
            address = input("ສະຖານທີ່ສົ່ງ: ")

            cart = []
            while True:
                # 1. ເລືອກແບຣນ
                while True:
                    print("\n--- 📦 ເລືອກແບຣນນ້ຳດື່ມ ---")
                    for k, v in water_data.items():
                        print(f"{k}. {v['name']}")
                    b_choice = input("ເລືອກໝາຍເລກ (1-6): ")
                    if b_choice in water_data: break
                    print("❌ ບໍ່ມີໃນລາຍການ, ກະລຸນາເລືອກ 1-6.")

                selected_brand = water_data[b_choice]

                # 2. ເລືອກປະເພດ
                while True:
                    print(f"\n--- 💧 ເລືອກປະເພດຂອງ '{selected_brand['name']}' ---")
                    print("1. ຕຸກ")
                    print("2. ແພັກ")
                    t_choice = input("ເລືອກໝາຍເລກ (1-2): ")
                    type_key = "ຕຸກ" if t_choice == "1" else "ແພັກ" if t_choice == "2" else None
                    if type_key: break
                    print("❌ ເລືອກບໍ່ຖືກ, ກະລຸນາເລືອກ 1 ຫຼື 2.")

                # 3. ເລືອກຂະໜາດ
                while True:
                    print(f"\n--- 📏 ເລືອກຂະໜາດ ({type_key}) ---")
                    for k, name in size_names.items():
                        price = selected_brand[type_key][k]
                        print(f"{k}. ຂະໜາດ{name} (ລາຄາ {price} ກີບ)")
                    s_choice = input("ເລືອກໝາຍເລກ (1-3): ")
                    if s_choice in size_names: break
                    print("❌ ເລືອກບໍ່ຖືກ, ກະລຸນາເລືອກ 1-3.")

                qty = get_integer_input(f"ຕ້ອງການຈຳນວນຈັກ {type_key}?: ")
                
                unit_price = selected_brand[type_key][s_choice]
                item_total = unit_price * qty
                
                cart.append({
                    "brand": selected_brand['name'],
                    "type": type_key,
                    "size": size_names[s_choice],
                    "unit_price": unit_price,
                    "qty": qty,
                    "total": item_total
                })

                if input("\nຕ້ອງການເພີ່ມແບຣນອື່ນອີກບໍ່? (y/n): ").lower() != 'y': break

            # --- ອອກບິນ (Receipt) ---
            if cart:
                order_id = len(sales_history) + 1
                total_all = sum(i['total'] for i in cart)
                now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                
                print("\n" + "🧾 " + "—"*45)
                print(f" ID: {order_id:04d} | ວັນທີ: {now}")
                print(f" ລູກຄ້າ: {fname} {lname} ({phone})")
                print(f" ສົ່ງທີ່: {address}")
                print("-" * 47)
                for i in cart:
                    print(f" • {i['brand']} [{i['type']}{i['size']}]")
                    print(f"   {i['qty']} x {i['unit_price']} = {i['total']} ກີບ")
                print("-" * 47)
                print(f" ລວມສຸດທິ: {total_all:,} ກີບ")
                print("—"*45)

                sales_history.append({
                    "id": order_id, 
                    "name": f"{fname} {lname}", 
                    "phone": phone, 
                    "total": total_all
                })
            input("\nກົດ Enter ເພື່ອກັບຄືນເມນູຫຼັກ...")

        elif main_choice == "2":
            print("\n📊 ສະຫຼຸບຖານຂໍ້ມູນການຂາຍຊົ່ວຄາວ:")
            if not sales_history:
                print("   [ ຍັງບໍ່ມີຂໍ້ມູນ ]")
            else:
                grand_revenue = 0
                for s in sales_history:
                    print(f"ID: {s['id']:04d} | {s['name']} ({s['phone']}) | ຍອດ: {s['total']:,} ກີບ")
                    grand_revenue += s['total']
                print("-" * 50)
                print(f"ລາຍໄດ້ລວມທັງໝົດ: {grand_revenue:,} ກີບ")
            input("\nກົດ Enter...")

        elif main_choice == "3":
            print("ກຳລັງປິດລະບົບ... ຂອບໃຈ!"); break

if __name__ == "__main__":
    water_delivery_system()