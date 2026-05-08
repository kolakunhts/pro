import datetime

# =========================
# FUNCTION INPUT
# =========================

def get_alpha_input(prompt):
    while True:
        user = input(prompt).strip()

        if user.isalpha() and user != "":
            return user

        print("⚠️  ກະລຸນາປ້ອນແຕ່ໂຕໜັງສືເທົ່ານັ້ນ!")


def get_phone_input(prompt):
    while True:
        user = input(prompt).strip()

        if user.isdigit() and len(user) >= 7:
            return user

        print("⚠️  ກະລຸນາປ້ອນເບີໂທໃຫ້ຖືກຕ້ອງ!")


def get_integer_input(prompt):
    while True:
        try:
            val = int(input(prompt))

            if val > 0:
                return val

            print("⚠️  ຈຳນວນຕ້ອງຫຼາຍກວ່າ 0!")

        except ValueError:
            print("⚠️  ກະລຸນາປ້ອນເປັນໂຕເລກເທົ່ານັ້ນ!")


# =========================
# DATABASE
# =========================

water_data = {
    "1": {
        "name": "ຫົວເສືອ",
        "ຕຸກ": {"1": 4000, "2": 7000, "3": 10000},
        "ແພັກ": {"1": 50000, "2": 45000, "3": 45000}
    },

    "2": {
        "name": "ນ້ຳທີບ",
        "ຕຸກ": {"1": 4000, "2": 6000, "3": 9000},
        "ແພັກ": {"1": 40000, "2": 45000, "3": 45000}
    },

    "3": {
        "name": "ທິວາລີ",
        "ຕຸກ": {"1": 3000, "2": 5000, "3": 8000},
        "ແພັກ": {"1": 40000, "2": 45000, "3": 45000}
    },

    "4": {
        "name": "Purra",
        "ຕຸກ": {"1": 6000, "2": 12000, "3": 20000},
        "ແພັກ": {"1": 60000, "2": 55000, "3": 60000}
    },

    "5": {
        "name": "ນ້ຳສີງ",
        "ຕຸກ": {"1": 5000, "2": 10000, "3": 15000},
        "ແພັກ": {"1": 60000, "2": 65000, "3": 65000}
    },

    "6": {
        "name": "ໂຊກທະວີ",
        "ຕຸກ": {"1": 3000, "2": 5000, "3": 8000},
        "ແພັກ": {"1": 42000, "2": 40000, "3": 40000}
    }
}

size_mapping = {
    "1": "ນ້ອຍ",
    "2": "ກາງ",
    "3": "ໃຫຍ່"
}

sales_history = []


# =========================
# MAIN SYSTEM
# =========================

def water_delivery():

    while True:

        print("\n" + "=" * 55)
        print("        💧 WELCOME TO WATER SYSTEM 💧")
        print("=" * 55)

        print("1. ສັ່ງນ້ຳ")
        print("2. ປະຫວັດການຂາຍ")
        print("3. ອອກຈາກລະບົບ")

        main_choice = input("\nເລືອກເມນູ (1-3): ")

        # =========================
        # ORDER
        # =========================

        if main_choice == "1":

            print("\n===== ຂໍ້ມູນລູກຄ້າ =====")

            customer_name = get_alpha_input("ຊື່: ")
            customer_lname = get_alpha_input("ນາມສະກຸນ: ")
            phone = get_phone_input("ເບີໂທ: ")
            address = input("ທີ່ຢູ່: ")

            cart = []

            while True:

                # =========================
                # BRAND
                # =========================

                while True:

                    print("\n===== ເລືອກແບຣນນ້ຳ =====")

                    for k, v in water_data.items():
                        print(f"{k}. {v['name']}")

                    brand_choice = input("ເລືອກແບຣນ (1-6): ")

                    if brand_choice in water_data:
                        break

                    print("⚠️  ກະລຸນາເລືອກໃຫ້ຖືກຕ້ອງ!")

                selected_brand = water_data[brand_choice]

                # =========================
                # TYPE
                # =========================

                while True:

                    print(f"\n===== {selected_brand['name']} =====")
                    print("1. ຕຸກ")
                    print("2. ແພັກ")

                    t_choice = input("ເລືອກ (1-2): ")

                    if t_choice == "1":
                        type_key = "ຕຸກ"
                        break

                    elif t_choice == "2":
                        type_key = "ແພັກ"
                        break

                    print("⚠️  ກະລຸນາເລືອກ 1 ຫຼື 2!")

                # =========================
                # SIZE
                # =========================

                while True:

                    print(f"\n===== ເລືອກຂະໜາດ ({type_key}) =====")

                    for k, size_name in size_mapping.items():

                        price = selected_brand[type_key][k]

                        print(f"{k}. {size_name} - {price:,} ກີບ")

                    s_choice = input("ເລືອກຂະໜາດ (1-3): ")

                    if s_choice in size_mapping:
                        break

                    print("⚠️  ກະລຸນາເລືອກ 1-3!")

                # =========================
                # QTY
                # =========================

                qty = get_integer_input(
                    f"ຈຳນວນ {size_mapping[s_choice]} {type_key}: "
                )

                unit_price = selected_brand[type_key][s_choice]

                total_price = unit_price * qty

                cart.append({
                    "brand": selected_brand["name"],
                    "type": type_key,
                    "size": size_mapping[s_choice],
                    "qty": qty,
                    "unit_price": unit_price,
                    "total": total_price
                })

                more = input(
                    "\nຕ້ອງການເພີ່ມສິນຄ້າອີກບໍ່? (y/n): "
                ).lower()

                if more != "y":
                    break

            # =========================
            # BILL
            # =========================

            if cart:

                order_id = len(sales_history) + 1

                total_all = sum(item["total"] for item in cart)

                now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

                print("\n" + "=" * 55)
                print("                 🧾 ໃບບິນ")
                print("=" * 55)

                print(f"ID: {order_id:04d}")
                print(f"ວັນທີ: {now}")

                print(
                    f"ລູກຄ້າ: {customer_name} {customer_lname}"
                )

                print(f"ເບີໂທ: {phone}")
                print(f"ທີ່ຢູ່: {address}")

                print("-" * 55)

                for item in cart:

                    print(
                        f"{item['brand']} "
                        f"[{item['type']} - {item['size']}]"
                    )

                    print(
                        f"{item['qty']} x "
                        f"{item['unit_price']:,} "
                        f"= {item['total']:,} ກີບ"
                    )

                    print("-" * 55)

                print(f"💰 ລວມທັງໝົດ: {total_all:,} ກີບ")

                print("=" * 55)

                sales_history.append({
                    "id": order_id,
                    "name": f"{customer_name} {customer_lname}",
                    "phone": phone,
                    "total": total_all
                })

            input("\nກົດ Enter ເພື່ອກັບເມນູ...")

        # =========================
        # SALES HISTORY
        # =========================

        elif main_choice == "2":

            if not sales_history:

                print("\n⚠️  ຍັງບໍ່ມີຂໍ້ມູນການຂາຍ!")

            else:

                print("\n" + "=" * 60)
                print("              📊 ປະຫວັດການຂາຍ")
                print("=" * 60)

                grand_total = 0

                for sale in sales_history:

                    print(
                        f"ID: {sale['id']:04d} | "
                        f"{sale['name']} | "
                        f"{sale['phone']} | "
                        f"{sale['total']:,} ກີບ"
                    )

                    grand_total += sale['total']

                print("=" * 60)

                print(
                    f"💰 ມູນຄ່າຂາຍລວມທັງໝົດ: "
                    f"{grand_total:,} ກີບ"
                )

                print("=" * 60)

            input("\nກົດ Enter ເພື່ອກັບເມນູ...")

        # =========================
        # EXIT
        # =========================

        elif main_choice == "3":

            print("\nກຳລັງປິດລະບົບ...")
            print("ຂອບໃຈທີ່ໃຊ້ງານ 💧")

            break

        else:
            print("⚠️  ກະລຸນາເລືອກ 1-3!")


# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":
    water_delivery()