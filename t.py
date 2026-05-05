import datetime

# --- ຟັງຊັນກວດສອບຂໍ້ມູນທົ່ວໄປ ---
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
        print("⚠️ ແຈ້ງເຕືອນ: ເບີໂທຕ້ອງເປັນ 'ໂຕເລກ' ແລະ ມີ 7 ໂຕຂຶ້ນໄປ!")

def get_integer_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0: return val
            print("⚠️ ແຈ້ງເຕືອນ: ຈຳນວນຕ້ອງຫຼາຍກວ່າ 0!")
        except ValueError:
            print("⚠️ ແຈ້ງເຕືອນ: ກະລຸນາປ້ອນເປັນ 'ໂຕເລກ' ເທົ່ານັ້ນ!")

# --- ຖານຂໍ້ມູນ ---
brands = {"1": "ຫົວເສືອ", "2": "ນ້ຳທີບ", "3": "ທິວາລີ", "4": "Purra", "5": "ນ້ຳສີງ", "6": "ໂຊກທະວີ"}
types = {"1": "ຕຸກ", "2": "ແພັກ"}
sizes = {
    "1": {"name": "ໃຫຍ່", "price": 10},
    "2": {"name": "ກາງ", "price": 7},
    "3": {"name": "ນ້ອຍ", "price": 5}
}
sales_history = []

def water_delivery_system():
    while True:
        print("\n" + "=".center(45, "="))
        print("   🌟 ລະບົບສົ່ງນ້ຳດື່ມ (ປ້ອງກັນການເລືອກຜິດ) 🌟")
        print("=".center(45, "="))
        print("1. [ສັ່ງນ້ຳ] | 2. [ຖານຂໍ້ມູນ] | 3. [ອອກ]")
        
        main_choice = input("\nເລືອກເມນູ (1-3): ")

        if main_choice == "1":
            fname = get_alpha_input("ຊື່: ")
            lname = get_alpha_input("ນາມສະກຸນ: ")
            phone = get_phone_input("ເບີໂທ: ")
            address = input("ສະຖານທີ່ສົ່ງ: ")

            cart = [] 
            while True:
                # 1. ບັງຄັບເລືອກແບຣນ
                while True:
                    print("\n--- 📦 ເລືອກແບຣນ ---")
                    for k, v in brands.items(): print(f"{k}. {v}")
                    b_choice = input("ເລືອກໝາຍເລກ (1-6): ")
                    if b_choice in brands: break
                    print(f"❌ ບໍ່ມີໝາຍເລກ {b_choice}! ກະລຸນາເລືອກ 1 ຫາ 6 ເທົ່ານັ້ນ.")

                # 2. ບັງຄັບເລືອກປະເພດ
                while True:
                    print("\n--- 💧 ເລືອກປະເພດ ---")
                    for k, v in types.items(): print(f"{k}. {v}")
                    t_choice = input("ເລືອກໝາຍເລກ (1-2): ")
                    if t_choice in types: break
                    print(f"❌ ບໍ່ມີໝາຍເລກ {t_choice}! ກະລຸນາເລືອກ 1 ຫຼື 2 ເທົ່ານັ້ນ.")

                # 3. ບັງຄັບເລືອກຂະໜາດ
                while True:
                    print("\n--- 📏 ເລືອກຂະໜາດ ---")
                    for k, v in sizes.items(): print(f"{k}. {v['name']} ({v['price']} ກີບ)")
                    s_choice = input("ເລືອກໝາຍເລກ (1-3): ")
                    if s_choice in sizes: break
                    print(f"❌ ບໍ່ມີໝາຍເລກ {s_choice}! ກະລຸນາເລືອກ 1 ຫາ 3 ເທົ່ານັ້ນ.")

                qty = get_integer_input(f"ຕ້ອງການຈຳນວນຈັກ {types[t_choice]}?: ")
                
                cart.append({
                    "brand": brands[b_choice], "type": types[t_choice],
                    "size": sizes[s_choice]['name'], "price": sizes[s_choice]['price'],
                    "qty": qty, "total": sizes[s_choice]['price'] * qty
                })

                if input("\nຕ້ອງການເພີ່ມລາຍການອື່ນອີກບໍ່? (y/n): ").lower() != 'y': break

            # ອອກບິນ
            if cart:
                order_id = len(sales_history) + 1
                total = sum(i['total'] for i in cart)
                print("\n" + "🧾 " + "—"*35)
                print(f" ID: {order_id:04d} | ລູກຄ້າ: {fname}")
                for i in cart:
                    print(f" • {i['brand']} {i['type']}{i['size']} x {i['qty']} = {i['total']} ກີບ")
                print(f" ລວມສຸດທິ: {total} ກີບ")
                sales_history.append({"id": order_id, "name": f"{fname} {lname}", "total": total})
            
            input("\nກົດ Enter ເພື່ອກັບຄືນ...")

        elif main_choice == "2":
            print("\n📊 ຖານຂໍ້ມູນການຂາຍ:")
            for s in sales_history: print(f"ID: {s['id']:04d} | {s['name']} | {s['total']} ກີບ")
            if not sales_history: print("ຍັງບໍ່ມີຂໍ້ມູນ.")
            input("\nກົດ Enter...")

        elif main_choice == "3": break

if __name__ == "__main__":
    water_delivery_system()