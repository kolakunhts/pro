print("=== Hello welcome ===")
import datetime

# --- ຖານຂໍ້ມູນສິນຄ້າ ---
brands = {
    "1": "ຫົວເສືອ", "2": "ນ້ຳທີບ", "3": "ທິວາລີ", 
    "4": "Purra", "5": "ນ້ຳສີງ", "6": "ໂຊກທະວີ"
}
types = {"1": "ຕຸກ", "2": "ແພັກ"}
sizes = {
    "1": {"name": "ໃຫຍ່", "price": 10},
    "2": {"name": "ກາງ", "price": 7},
    "3": {"name": "ນ້ອຍ", "price": 5}
}

# --- ຖານຂໍ້ມູນຊົ່ວຄາວ (ຈະຫາຍໄປເມື່ອປິດໂປຣແກຣມ) ---
sales_history = []

def water_delivery_system():
    while True:
        print("\n" + "="*45)
        print("    ລະບົບຈັດການການສົ່ງນ້ຳດື່ມ (v1.0) ")
        print("="*45)
        print("1. [ສັ່ງນ້ຳ] - ເພີ່ມລາຍການໃໝ່")
        print("2. [ຖານຂໍ້ມູນ] - ສະຫຼຸບການຂາຍທັງໝົດ")
        print("3. [ອອກ] - ອອກຈາກລະບົບ")
        print("-" * 45)
        
        main_choice = input("ກະລຸນາເລືອກເມນູ (1-3): ")

        if main_choice == "1":
            print("\n---  ປ້ອນຂໍ້ມູນລູກຄ້າ ---")
            fname = input("ຊື່: ")
            lname = input("ນາມສະກຸນ: ")
            phone = input("ເບີໂທ: ")
            address = input("ສະຖານທີ່ສົ່ງ: ")

            cart = [] 

            # Loop ການເລືອກສິນຄ້າ
            while True:
                print("\n---  ເລືອກແບຣນນ້ຳດື່ມ ---")
                for k, v in brands.items():
                    print(f"{k}. {v}")
                b_choice = input("ເລືອກແບຣນ (1-6): ")
                
                print("\n---  ເລືອກປະເພດ ---")
                for k, v in types.items():
                    print(f"{k}. {v}")
                t_choice = input("ເລືອກປະເພດ (1-2): ")

                print("\n---  ເລືອກຂະໜາດ ---")
                for k, v in sizes.items():
                    print(f"{k}. {v['name']} ({v['price']} ກີບ)")
                s_choice = input("ເລືອກຂະໜາດ (1-3): ")

                if b_choice in brands and t_choice in types and s_choice in sizes:
                    qty = int(input("ຈຳນວນທີ່ຕ້ອງການ: "))
                    
                    item_brand = brands[b_choice]
                    item_type = types[t_choice]
                    item_size = sizes[s_choice]
                    item_price = item_size['price']
                    total = item_price * qty

                    cart.append({
                        "brand": item_brand,
                        "type": item_type,
                        "size": item_size['name'],
                        "unit_price": item_price,
                        "qty": qty,
                        "total": total
                    })
                else:
                    print("❌ ຂໍ້ມູນບໍ່ຖືກຕ້ອງ, ກະລຸນາເລືອກໃໝ່!")

                cont = input("\nຕ້ອງການເພີ່ມລາຍການອື່ນອີກບໍ່? (y/n): ").lower()
                if cont != 'y':
                    break

            # --- ຄິດໄລ່ ແລະ ອອກບິນ ---
            order_id = len(sales_history) + 1
            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            sub_total = sum(item['total'] for item in cart)
            
            # (ຕົວຢ່າງ: ຖ້າຊື້ເກີນ 50 ກີບ ຫຼຸດໃຫ້ 2 ກີບ)
            discount = 2 if sub_total > 50 else 0
            grand_total = sub_total - discount

            print("\n" + " " + "—"*35)
            print(f"       ບິນຮັບເງິນ ID: {order_id:04d}")
            print(f" ວັນທີ: {now}")
            print(f" ລູກຄ້າ: {fname} {lname} ({phone})")
            print(f" ສົ່ງທີ່: {address}")
            print(" " + "-"*35)
            for i in cart:
                print(f" • {i['brand']} ({i['type']}{i['size']})")
                print(f"   {i['qty']} x {i['unit_price']} = {i['total']} ກີບ")
            print(" " + "-"*35)
            print(f" ລວມຍ່ອຍ:      {sub_total} ກີບ")
            print(f" ສ່ວນຫຼຸດ:      -{discount} ກີບ")
            print(f" ລວມສຸດທິ:     {grand_total} ກີບ")
            print("—"*35)

            # ບັນທຶກລົງຖານຂໍ້ມູນຊົ່ວຄາວ
            sales_history.append({
                "order_id": order_id,
                "customer": f"{fname} {lname}",
                "total": grand_total,
                "items_count": len(cart)
            })
            input("\nກົດ Enter ເພື່ອກັບຄືນເມນູຫຼັກ...")

        elif main_choice == "2":
            
            print("     ລາຍງານສະຫຼຸບຖານຂໍ້ມູນການຂາຍ")
            
            if not sales_history:
                print("   [ ຍັງບໍ່ມີຂໍ້ມູນການຂາຍໃນລະບົບ ]")
            else:
                total_all = 0
                for s in sales_history:
                    print(f"ID: {s['order_id']:04d} | {s['customer']} | {s['total']} ກີບ")
                    total_all += s['total']
                
                print(f"ຈຳນວນ Order ທັງໝົດ: {len(sales_history)} ລາຍການ")
                print(f"ລາຍໄດ້ລວມທັງໝົດ: {total_all} ກີບ")
            
            input("\nກົດ Enter ເພື່ອກັບຄືນເມນູຫຼັກ...")

        elif main_choice == "3":
            print("ກຳລັງປິດລະບົບ... ຂອບໃຈທີ່ໃຊ້ບໍລິການ!")
            break

# ເລີ່ມການເຮັດວຽກ
if __name__ == "__main__":
    water_delivery_system()


