print("======== Hello welcome =========")
import datetime

# --- ຖານຂໍ້ມູນສິນຄ້າ ---
brands = {"1": "ຫົວເສືອ", "2": "ນ້ຳທີບ", "3": "ທິວາລີ", "4": "Purra", "5": "ນ້ຳສີງ", "6": "ໂຊກທະວີ"}
types = {"1": "ຕຸກ", "2": "ແພັກ"}
sizes = {
    "1": {"name": "ໃຫຍ່", "price": 10},
    "2": {"name": "ກາງ", "price": 7},
    "3": {"name": "ນ້ອຍ", "price": 5}
}

sales_history = []

# --- ຟັງຊັນສຳລັບກວດສອບການປ້ອນໂຕເລກ (Error Handling) ---
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            # ພະຍາຍາມປ່ຽນຄ່າເປັນໂຕເລກຖ້ວນ
            return int(user_input)
        except ValueError:
            # ຖ້າປ່ຽນບໍ່ໄດ້ (ປ້ອນໂຕໜັງສື) ໃຫ້ສະແດງຂໍ້ຄວາມແຈ້ງເຕືອນ
            print("⚠️ ແຈ້ງເຕືອນ: ກະລຸນາປ້ອນເປັນ 'ໂຕເລກ' ເທົ່ານັ້ນ!")

def water_delivery_system():
    while True:
        print("\n" + "="*45)
        print("   🌟 ລະບົບຈັດການການສົ່ງນ້ຳດື່ມ (v1.1) 🌟")
        print("="*45)
        print("1. [ສັ່ງນ້ຳ] - ເພີ່ມລາຍການໃໝ່")
        print("2. [ຖານຂໍ້ມູນ] - ສະຫຼຸບການຂາຍທັງໝົດ")
        print("3. [ອອກ] - ອອກຈາກລະບົບ")
        print("-" * 45)
        
        main_choice = input("ກະລຸນາເລືອກເມນູ (1-3): ")

        if main_choice == "1":
            print("\n--- 📝 ປ້ອນຂໍ້ມູນລູກຄ້າ ---")
            fname = input("ຊື່: ")
            lname = input("ນາມສະກຸນ: ")
            phone = input("ເບີໂທ: ")
            address = input("ສະຖານທີ່ສົ່ງ: ")

            cart = [] 

            while True:
                print("\n--- 📦 ເລືອກແບຣນນ້ຳດື່ມ ---")
                for k, v in brands.items():
                    print(f"{k}. {v}")
                b_choice = input("ເລືອກໝາຍເລກແບຣນ: ")
                
                print("\n--- 💧 ເລືອກປະເພດ ---")
                for k, v in types.items():
                    print(f"{k}. {v}")
                t_choice = input("ເລືອກໝາຍເລກປະເພດ: ")

                print("\n--- 📏 ເລືອກຂະໜາດ ---")
                for k, v in sizes.items():
                    print(f"{k}. {v['name']} ({v['price']} ກີບ)")
                s_choice = input("ເລືອກໝາຍເລກຂະໜາດ: ")

                if b_choice in brands and t_choice in types and s_choice in sizes:
                    # ໃຊ້ຟັງຊັນ get_integer_input ເພື່ອກວດສອບຈຳນວນ
                    qty = get_integer_input(f"ຕ້ອງການຈຳນວນຈັກ {types[t_choice]}?: ")
                    
                    item_total = sizes[s_choice]['price'] * qty
                    cart.append({
                        "brand": brands[b_choice],
                        "type": types[t_choice],
                        "size": sizes[s_choice]['name'],
                        "unit_price": sizes[s_choice]['price'],
                        "qty": qty,
                        "total": item_total
                    })
                else:
                    print("❌ ໝາຍເລກທີ່ເຈົ້າເລືອກບໍ່ມີໃນລະບົບ, ກະລຸນາເລືອກໃໝ່!")

                cont = input("\nຕ້ອງການເພີ່ມລາຍການອື່ນອີກບໍ່? (y/n): ").lower()
                if cont != 'y':
                    break

            # --- ຄິດໄລ່ ແລະ ອອກບິນ ---
            if cart:
                order_id = len(sales_history) + 1
                now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                sub_total = sum(item['total'] for item in cart)
                grand_total = sub_total # ປັບແຕ່ງສ່ວນຫຼຸດເພີ່ມໄດ້ບ່ອນນີ້

                print("\n" + "🧾 " + "—"*35)
                print(f"       ບິນຮັບເງິນ ID: {order_id:04d}")
                print(f" ວັນທີ: {now}")
                print(f" ລູກຄ້າ: {fname} {lname}")
                print(" " + "-"*35)
                for i in cart:
                    print(f" • {i['brand']} ({i['type']}{i['size']})")
                    print(f"   {i['qty']} x {i['unit_price']} = {i['total']} ກີບ")
                print(" " + "-"*35)
                print(f" ລວມສຸດທິ:     {grand_total} ກີບ")
                print("—"*35)

                sales_history.append({
                    "order_id": order_id,
                    "customer": f"{fname} {lname}",
                    "total": grand_total
                })
            
            input("\nກົດ Enter ເພື່ອກັບຄືນເມນູຫຼັກ...")

        elif main_choice == "2":
            print("\n📊 ຖານຂໍ້ມູນການຂາຍຊົ່ວຄາວ:")
            if not sales_history:
                print("ຍັງບໍ່ມີຂໍ້ມູນ.")
            else:
                for s in sales_history:
                    print(f"ID: {s['order_id']:04d} | {s['customer']} | {s['total']} ກີບ")
            input("\nກົດ Enter ເພື່ອກັບຄືນ...")

        elif main_choice == "3":
            print("ປິດລະບົບ...")
            break

if __name__ == "__main__":
    water_delivery_system()