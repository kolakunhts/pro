from itertools import product
# ສວ່ນທີ1: ກຳນົດຂໍ້ມູນສີນຄ້າແລະລາຄາ
PRODUCTS = {
     "ເບຍ": {
        "ເບຍລາວ": {
            "ປອ໋ງ": {"ນ້ອຍ": 290000, "ກາງ": 330000},
            "ແກ້ວ": {"ມາດຕະຖານ": 210000},
        },
        "ເບຍນ້ຳຂອງ": {
            "ປອ໋ງ": {"ນ້ອຍ": 270000, "ກາງ": 310000},
            "ແກ້ວ": {"ມາດຕະຖານ": 200000},
        },
        "ເບຍລ້ານຊ້າງ": {
            "ປອ໋ງ": {"ນ້ອຍ": 300000, "ກາງ": 340000},
            "ແກ້ວ": {"ມາດຕະຖານ": 220000},
        },
        "ເບຍໂຄ້ດເບີກ": {
            "ປອ໋ງ": {"ນ້ອຍ": 360000, "ກາງ": 410000},
            "ແກ້ວ": {"ມາດຕະຖານ": 260000},
        },
        "ເບຍ1664ແບນ": {
            "ປອ໋ງ": {"ນ້ອຍ": 420000, "ກາງ": 480000},
            "ແກ້ວ": {"ມາດຕະຖານ": 300000},
        },
        "ເບຍໄຫເນີເກັນ": {
            "ປອ໋ງ": {"ນ້ອຍ": 390000, "ກາງ": 450000},
            "ແກ້ວ": {"ມາດຕະຖານ": 290000},
        },
        "ເບຍຫຼວງພະບາງ": {
            "ປອ໋ງ": {"ນ້ອຍ": 310000, "ກາງ": 350000},
            "ແກ້ວ": {"ມາດຕະຖານ": 230000},
        },
    },
    "ນ້ຳອັດລົມ": {
        "ແປບຊີ": {
            "ຕຸກ": {"ນ້ອຍ": 85000, "ກາງ": 115000, "ໃຫຍ່": 145000},
            "ປອ໋ງ": {"ນ້ອຍ": 120000, "ກາງ": 160000},
            "ແກ້ວ": {"ມາດຕະຖານ": 120000},
        },
        "ໂຄຄາໂຄລາ": {
            "ຕຸກ": {"ນ້ອຍ": 90000, "ກາງ": 120000, "ໃຫຍ່": 150000},
            "ປອ໋ງ": {"ນ້ອຍ": 125000, "ກາງ": 165000},
            "ແກ້ວ": {"ມາດຕະຖານ": 125000},
        },
        "ເຊເວັນອັບ": {
            "ຕຸກ": {"ນ້ອຍ": 85000, "ກາງ": 110000, "ໃຫຍ່": 140000},
            "ປອ໋ງ": {"ນ້ອຍ": 115000, "ກາງ": 150000},
            "ແກ້ວ": {"ມາດຕະຖານ": 115000},
        },
        "ແຟນຕ້າ": {
            "ຕຸກ": {"ນ້ອຍ": 85000, "ກາງ": 110000, "ໃຫຍ່": 140000},
            "ປອ໋ງ": {"ນ້ອຍ": 115000, "ກາງ": 150000},
            "ແກ້ວ": {"ມາດຕະຖານ": 115000},
        },
        "ສະໄປ໋": {
            "ຕຸກ": {"ນ້ອຍ": 85000, "ກາງ": 110000, "ໃຫຍ່": 140000},
            "ປອ໋ງ": {"ນ້ອຍ": 115000, "ກາງ": 150000},
            "ແກ້ວ": {"ມາດຕະຖານ": 115000},
        },
        "ສະຕີງ(ແດງ)": {
            "ຕຸກ": {"ມາດຕະຖານ": 120000},
            "ປອ໋ງ": {"ມາດຕະຖານ": 135000},
        },
        "M150": {
            "ຂວດ": {"ມາດຕະຖານ": 145000},
        },
        "ສະເວັບ": {
            "ປອ໋ງ": {"ມາດຕະຖານ": 145000},
        },
        "ສະປອນເຊີ": {
            "ປອ໋ງ": {"ມາດຕະຖານ": 140000},
        },
    },
    "ນ້ຳດື່ມ": {
        "ນ້ຳດື່ມຫົວເສືອ": {"ແພັກ": {"ນ້ອຍ": 35000, "ກາງ": 45000, "ໃຫຍ່": 55000}},
        "ນ້ຳດື່ມດາວ": {"ແພັກ": {"ນ້ອຍ": 32000, "ກາງ": 42000, "ໃຫຍ່": 52000}},
        "ນ້ຳທີບ": {"ແພັກ": {"ນ້ອຍ": 33000, "ກາງ": 43000, "ໃຫຍ່": 53000}},
        "ນ້ຳດື່ມມີເນໂລ": {"ແພັກ": {"ນ້ອຍ": 36000, "ກາງ": 46000, "ໃຫຍ່": 56000}},
        "ນ້ຳດື່ມໂຊກທະວີ": {"ແພັກ": {"ນ້ອຍ": 30000, "ກາງ": 40000, "ໃຫຍ່": 50000}},
        "ນ້فظືມມີລາ": {"ແພັກ": {"ນ້ອຍ": 34000, "ກາງ": 44000, "ໃຫຍ່": 54000}},
    },
}

# ສວ່ນທີ2: ກຳນົດເມນູແລະຕົວເລືອກ
MODES = ["ສະເເດງສີນຄ້າທັງໝົດ", "ສະເເດງໝວດສິນຄ້າ"]  
OPTIONS = ["ເເພັກ", "ເເກັດ", "ລາງ"]
OPTIONS2 = ["ແກັດ", "ແພັກ"]
ONSIZE = "ບໍ່ມີຂະໜາດ"
AOTOCRATE = ["ສະຕີງ(ແດງ)", "M150", "ສະເວັບ", "ສະປອນເຊີ"]
GLASS = ["ແປບຊີ", "ໂຄຄາໂຄລາ", "ເຊເວັນອັບ", "ແຟນຕ້າ", "ສະໄປ໋"]

# ສວ່ນທີ3: ກຳນົດຟັງຊັ້ນສ່ວນຊ່ວຍເຫຼືອ      
def money(amount):
    return f"{amount:,} ກີບ"

def inputnotempty(message):
    while True:
        value = input(message)
        if value.strip() != "":
            return value
        print("ກະລຸນາໃສ່ຂໍ້ມູນ")

def choose_from_list(title, options):
    while True:
        print(f"\n{title}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        choice = input("ກະລຸນາເລືອກເລກສີນຄ້າທີທ່ານຕອ້ງການສະເເດງ: ").strip()
        if not choice.isdigit():
            print("ກະລຸນາໃສ່ເປັນຕົວເລກ.")
            continue
        index = int(choice)
        if 1 <= index <= len(options):
            return options[index - 1]
        print(f"ກະລຸນາເລືອກ 1 ຫາ {len(options)}.")

def choose_size(title, size_prices):
    sizes = list(size_prices.keys())
    while True:
        print(f"\n{title}")
        for i, size in enumerate(sizes, start=1):
            print(f"{i}. {size}")
        choice = input("ກະລຸນາເລືອກເລກຂະໜາດທີທ່ານຕອ້ງການ: ").strip()
        if not choice.isdigit():
            print("ກະລຸນາໃສ່ເປັນຕົວເລກ.")
            continue
        index = int(choice)
        if 1 <= index <= len(sizes):
            return sizes[index - 1]
        print(f"ກະລຸນາເລືອກ 1 ຫາ {len(sizes)}.")

# ແກ້ໄຂ Indentation (ການຍົກຍ້າຍຍໍ້ໜ້າ) ໃຫ້ຖືກຕ້ອງອອກມາຢູ່ນອກຟັງຊັນ choose_size
def show_step5_price(unit_price, package_type):
    print(f"ລາຄາ: {money(unit_price)}/{package_type}")

def input_quantity(unit_name):
    while True:
        value = input(f"ປ້ອນຈຳນວນ{unit_name}: ").strip()
        if not value.isdigit():
            print("ຈຳນວນຕ້ອງເປັນຕົວເລກ.")
            continue
        quantity = int(value)
        if quantity > 0:
            return quantity
        print("ຈຳນວນຕ້ອງຫຼາຍກວ່າ 0.")

def ask_yes_no(message):
    while True:
        answer = input(message).strip().lower()
        if answer in ("y", "n"):
            return answer
        print("ກະລຸນາກົດ y ຫຼື n ເທົ່ານັ້ນ.")

# ສ່ວນທີ 4: ຟັງຊັນສຳລັບສະແດງ ແລະ ເລືອກສິນຄ້າ
def show_all_products():
    all_products = []
    print("\nລາຍການສິນຄ້າທັງໝົດໃນສາງ")

    for category, products in PRODUCTS.items():
        print(f"\n{category}")
        for name in products.keys():
            all_products.append({"category": category, "name": name})
            print(f"{len(all_products)}. {name}")

    return all_products

def choose_from_all_products():
    all_products = show_all_products()

    while True:
        choice = input("\nກະລຸນາເລືອກເລກສິນຄ້າ: ").strip()
        if not choice.isdigit():
            print("ກະລຸນາໃສ່ເປັນຕົວເລກ.")
            continue

        index = int(choice)
        if 1 <= index <= len(all_products):
            selected = all_products[index - 1]
            return selected["category"], selected["name"]

        print(f"ກະລຸນາເລືອກ 1 ຫາ {len(all_products)}.")

def choose_product():
    view_mode = choose_from_list(
        "ຂັ້ນຕອນທີ 2: ເລືອກວິທີສະແດງສິນຄ້າ",
        MODES,
    )

    # ແກ້ໄຂເງື່ອນໄຂໃຫ້ກົງກັບຕົວປ່ຽນ MODES ທີ່ຜູ້ໃຊ້ກົດເລືອກ
    if view_mode == "ສະເເດງສີນຄ້າທັງໝົດ":
        category, product_name = choose_from_all_products()
    else:
        category = choose_from_list(
            "ເລືອກໝວດໝູ່ສິນຄ້າ",
            list(PRODUCTS.keys()),
        )
        product_name = choose_from_list(
            f"ເລືອກສິນຄ້າໃນໝວດ {category}",
            list(PRODUCTS[category].keys()),
        )

    product_data = PRODUCTS[category][product_name]

    if category == "ນ້ຳດື່ມ":
        package_type = "ແພັກ"
        size = choose_size(
            "ຂັ້ນຕອນທີ 4: ເລືອກຂະໜາດນ້ຳດື່ມ",
            product_data[package_type],
        )
        print(f"\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ {package_type}")
        show_step5_price(product_data[package_type][size], package_type)
    else:
        if len(product_data) == 1:
            product_type = list(product_data.keys())[0]
            print(f"\nຂັ້ນຕອນທີ 3: ບັນຈຸພັນ {product_type}")
        else:
            product_type = choose_from_list(
                "ຂັ້ນຕອນທີ 3: ເລືອກບັນຈຸພັນ",
                list(product_data.keys()),
            )

        if category == "ເບຍ" and product_type == "ແກ້ວ":
            package_type = "ລາງ"
            size = "ມາດຕະຖານ"
            print(f"\nຂັ້ນຕອນທີ 4: ຂະໜາດ {size}")
        elif ONSIZE in product_data[product_type]:
            package_type = "ແກັດ"
            size = ONSIZE
            print(f"\nຂັ້ນຕອນທີ 4: {size}")
        else:
            size = choose_size(
                "ຂັ້ນຕອນທີ 4: ເລືອກຂະໜາດຜະລິດຕະພັນ",
                product_data[product_type],
            )

        if category == "ເບຍ" and product_type == "ປອ໋ງ":
            package_type = "ແກັດ"
            print(f"\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ {package_type}")
            show_step5_price(product_data[product_type][size], package_type)
        elif category == "ເບຍ" and product_type == "ແກ້ວ":
            package_type = "ລາງ"
            print(f"\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ {package_type}")
            show_step5_price(product_data[product_type][size], package_type)
        elif product_name in AOTOCRATE:
            package_type = "ແກັດ"
            print(f"\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ {package_type}")
            show_step5_price(product_data[product_type][size], package_type)
        elif product_name in GLASS and product_type == "ແກ້ວ":
            package_type = "ລາງ"
            print("\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ ລາງ")
            show_step5_price(product_data[product_type][size], package_type)
        elif product_name in GLASS and product_type in ("ຕຸກ", "ປອ໋ງ"):
            package_type = choose_from_list(
                "ຂັ້ນຕອນທີ 5: ເລືອກປະເພດໄຊ້",
                OPTIONS2,
            )
            show_step5_price(product_data[product_type][size], package_type)
        else:
            package_type = choose_from_list(
                "ຂັ້ນຕອນທີ 5: ເລືອກປະເພດໄຊ້",
                OPTIONS,
            )
            show_step5_price(product_data[product_type][size], package_type)

    if category == "ນ້ຳດື່ມ":
        product_type = "ຕຸກ"
        unit_price = product_data[package_type][size]
    else:
        unit_price = product_data[product_type][size]

    quantity = input_quantity(package_type)
    total = unit_price * quantity

    return {
        "category": category,
        "name": product_name,
        "product_type": product_type,
        "size": size,
        "package_type": package_type,
        "unit_price": unit_price,
        "quantity": quantity,
        "quantity_text": f"{quantity} {package_type}",
        "total": total,
    }

def discount_rate(total):
    if total > 20000000:
        return 0.10
    if total >= 10000000:
        return 0.07
    if total >= 1000000:
        return 0.05
    return 0

def print_bill(first_name, last_name, orders):
    subtotal = sum(item["total"] for item in orders)
    rate = discount_rate(subtotal)
    discount = subtotal * rate
    final_total = subtotal - discount
    line_width = 86

    print("\n" + "=" * line_width)
    print("ໃບບິນສູນສົ່ງນ້ຳທຸກປະເພດ")
    print("=" * line_width)
    print(f"ຊື່ລູກຄ້າ: {first_name} {last_name}")
    print("-" * line_width)
    print(
        f"{'ລຳດັບ':<6}"
        f"{'ສິນຄ້າ':<18}"
        f"{'ບັນຈຸພັນ':<10}"
        f"{'ປະເພດໄຊ້':<12}"
        f"{'ຂະໜາດ':<12}"
        f"{'ຈຳນວນ':<10}"
        f"{'ລວມ':>14}"
    )
    print("-" * line_width)

    for i, item in enumerate(orders, start=1):
        print(
            f"{i:<6}"
            f"{item['name']:<18}"
            f"{item['product_type']:<10}"
            f"{item['package_type']:<12}"
            f"{item['size']:<12}"
            f"{item['quantity_text']:<10}"
            f"{money(item['total']):>14}"
        )

    print("-" * line_width)
    print(f"ລາຄາລວມກ່ອນຫຼຸດ: {money(subtotal)}")
    print(f"ສ່ວນຫຼຸດ: {int(rate * 100)}% = {money(discount)}")
    print(f"ລາຄາຕ້ອງຈ່າຍທັງໝົດ: {money(final_total)}")
    print("=" * line_width)
    print("ຂອບໃຈທີ່ໃຊ້ບໍລິການ")

# ສ່ວນທີ 6: ຟັງຊັນຫຼັກຂອງໂປຣແກຣມ
def main():
    print("===================WELCOME=====================")
    print("\nຂັ້ນຕອນທີ 1: ລັອກອິນຂໍ້ມູນລູກຄ້າ")
    first_name = inputnotempty("ປ້ອນຊື່: ")
    last_name = inputnotempty("ປ້ອນນາມສະກຸນ: ")
    orders = []
    while True:
        order = choose_product()
        orders.append(order)

        more = ask_yes_no("\nຂັ້ນຕອນທີ 7: ຢາກຊື້ເພີ່ມອີກບໍ່? (y/n): ")
        if more == "n":
            break

    print_bill(first_name, last_name, orders)
if __name__ == "__main__":
    main()