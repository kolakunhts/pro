# ============================================================
# ລະບົບສູນສົ່ງນ້ຳທຸກປະເພດ
# ໂປຣແກຣມນີ້ໃຊ້ສຳລັບ:
# 1. ຮັບຊື່ ແລະ ນາມສະກຸນລູກຄ້າ
# 2. ໃຫ້ລູກຄ້າເລືອກສິນຄ້າຕາມໝວດໝູ່
# 3. ຄິດໄລ່ລາຄາ, ສ່ວນຫຼຸດ, ແລະ ອອກໃບບິນ
# ============================================================


# ------------------------------------------------------------
# ສ່ວນທີ 1: ຂໍ້ມູນສິນຄ້າ
# PRODUCTS ເປັນ dictionary ໃຫຍ່ທີ່ເກັບ:
# - ໝວດໝູ່ສິນຄ້າ: ເບຍ, ນ້ຳອັດລົມ, ນ້ຳດື່ມ
# - ຊື່ສິນຄ້າໃນແຕ່ລະໝວດ
# - ປະເພດພາຊະນະ: ຕຸກ, ປອ໋ງ, ແກ້ວ, ແພັກ
# - ຂະໜາດ ແລະ ລາຄາ
# ------------------------------------------------------------
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
            "ແກ້ວ": {"ນ້ອຍ": 90000, "ກາງ": 120000},
        },
        "ໂຄຄາໂຄລາ": {
            "ຕຸກ": {"ນ້ອຍ": 90000, "ກາງ": 120000, "ໃຫຍ່": 150000},
            "ປອ໋ງ": {"ນ້ອຍ": 125000, "ກາງ": 165000},
            "ແກ້ວ": {"ນ້ອຍ": 95000, "ກາງ": 125000},
        },
        "ເຊເວັນອັບ": {
            "ຕຸກ": {"ນ້ອຍ": 85000, "ກາງ": 110000, "ໃຫຍ່": 140000},
            "ປອ໋ງ": {"ນ້ອຍ": 115000, "ກາງ": 150000},
            "ແກ້ວ": {"ນ້ອຍ": 90000, "ກາງ": 115000},
        },
        "ແຟນຕ້າ": {
            "ຕຸກ": {"ນ້ອຍ": 85000, "ກາງ": 110000, "ໃຫຍ່": 140000},
            "ປອ໋ງ": {"ນ້ອຍ": 115000, "ກາງ": 150000},
            "ແກ້ວ": {"ນ້ອຍ": 90000, "ກາງ": 115000},
        },
        "ສະໄປ໋": {
            "ຕຸກ": {"ນ້ອຍ": 85000, "ກາງ": 110000, "ໃຫຍ່": 140000},
            "ປອ໋ງ": {"ນ້ອຍ": 115000, "ກາງ": 150000},
            "ແກ້ວ": {"ນ້ອຍ": 90000, "ກາງ": 115000},
        },
        "ສະຕີງ(ແດງ)": {
            "ຕຸກ": {"ບໍ່ມີຂະໜາດ": 120000},
            "ປອ໋ງ": {"ບໍ່ມີຂະໜາດ": 135000},
        },
        "M150": {
            "ຂວດ": {"ບໍ່ມີຂະໜາດ": 145000},
        },
        "ສະເວັບ": {
            "ປອ໋ງ": {"ບໍ່ມີຂະໜາດ": 145000},
        },
        "ສະປອນເຊີ": {
            "ປອ໋ງ": {"ບໍ່ມີຂະໜາດ": 140000},
            
        },
    },
    "ນ້ຳດື່ມ": {
        "ນ້ຳດື່ມຫົວເສືອ": {"ແພັກ": {"ນ້ອຍ": 35000, "ກາງ": 45000, "ໃຫຍ່": 55000}},
        "ນ້ຳດື່ມດາວ": {"ແພັກ": {"ນ້ອຍ": 32000, "ກາງ": 42000, "ໃຫຍ່": 52000}},
        "ນ້ຳທີບ": {"ແພັກ": {"ນ້ອຍ": 33000, "ກາງ": 43000, "ໃຫຍ່": 53000}},
        "ນ້ຳດື່ມມີເນໂລ": {"ແພັກ": {"ນ້ອຍ": 36000, "ກາງ": 46000, "ໃຫຍ່": 56000}},
        "ນ້ຳດື່ມໂຊກທະວີ": {"ແພັກ": {"ນ້ອຍ": 30000, "ກາງ": 40000, "ໃຫຍ່": 50000}},
        "ນ້ຳດື່ມມີລາ": {"ແພັກ": {"ນ້ອຍ": 34000, "ກາງ": 44000, "ໃຫຍ່": 54000}},
    },
}


# ------------------------------------------------------------
# ສ່ວນທີ 2: ຄ່າເມນູທີ່ໃຊ້ຊ້ຳ
# ການແຍກອອກມາແບບນີ້ເຮັດໃຫ້ແກ້ຂໍ້ຄວາມເມນູໄດ້ງ່າຍ.
# ------------------------------------------------------------
VIEW_MODES = ["ແບນ/ສະແດງສິນຄ້າທັງໝົດ", "ໝວດໝູ່"]
PACKAGE_OPTIONS = ["ແພັກ", "ແກັດ", "ລາງ"]
PACKAGE_OPTIONS_WITHOUT_CRATE = ["ແພັກ", "ແກັດ"]
NO_SIZE = "ບໍ່ມີຂະໜາດ"
AUTO_CRATE_PRODUCTS = ["ສະຕີງ(ແດງ)", "M150", "ສະເວັບ", "ສະປອນເຊີ"]
GLASS_TRAY_PRODUCTS = ["ແປບຊີ", "ໂຄຄາໂຄລາ", "ເຊເວັນອັບ", "ແຟນຕ້າ", "ສະໄປ໋"]


# ------------------------------------------------------------
# ສ່ວນທີ 2.1: list ສຳລັບເກັບຂໍ້ມູນ
# CUSTOMERS ເກັບຂໍ້ມູນລູກຄ້າ.
# ORDER_HISTORY ເກັບປະຫວັດການສັ່ງຊື້ແຕ່ລະໃບບິນ.
# ຂໍ້ມູນນີ້ເກັບໃນ memory ຂະນະທີ່ໂປຣແກຣມກຳລັງແລ່ນ.
# ------------------------------------------------------------
CUSTOMERS = []
ORDER_HISTORY = []


# ------------------------------------------------------------
# ສ່ວນທີ 3: ຟັງຊັນຊ່ວຍທົ່ວໄປ
# ຟັງຊັນໃນສ່ວນນີ້ໃຊ້ຊ້ຳຫຼາຍຈຸດ ເພື່ອກັນ error.
# ------------------------------------------------------------
def money(amount):
    """ແປງຕົວເລກເງິນໃຫ້ມີ comma ແລະ ຕໍ່ທ້າຍດ້ວຍຄຳວ່າ ກີບ."""
    return f"{amount:,.0f} ກີບ"


def input_not_empty(message):
    """ຮັບຂໍ້ຄວາມຈາກຜູ້ໃຊ້ ແລະ ບໍ່ອະນຸຍາດໃຫ້ປ່ອຍວ່າງ."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("ກະລຸນາປ້ອນຂໍ້ມູນ ຫ້າມປ່ອຍວ່າງ.")


def choose_from_list(title, options):
    """ສະແດງເມນູຕາມ list ແລ້ວບັງຄັບໃຫ້ເລືອກເລກທີ່ຖືກຕ້ອງ."""
    while True:
        print(f"\n{title}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("ເລືອກເລກ: ").strip()
        if not choice.isdigit():
            print("ກະລຸນາໃສ່ເປັນຕົວເລກ.")
            continue

        index = int(choice)
        if 1 <= index <= len(options):
            return options[index - 1]

        print(f"ກະລຸນາເລືອກ 1 ຫາ {len(options)}.")


def choose_size(title, size_prices):
    """ສະແດງຂະໜາດໃຫ້ເລືອກ ແລ້ວສົ່ງຂະໜາດທີ່ເລືອກກັບຄືນ."""
    sizes = list(size_prices.keys())

    while True:
        print(f"\n{title}")
        for i, size in enumerate(sizes, start=1):
            print(f"{i}. {size}")

        choice = input("ເລືອກເລກ: ").strip()
        if not choice.isdigit():
            print("ກະລຸນາໃສ່ເປັນຕົວເລກ.")
            continue

        index = int(choice)
        if 1 <= index <= len(sizes):
            return sizes[index - 1]

        print(f"ກະລຸນາເລືອກ 1 ຫາ {len(sizes)}.")


def show_step5_price(unit_price, package_type):
    """ສະແດງລາຄາສິນຄ້າໃນຂັ້ນຕອນທີ 5 ຕາມປະເພດໄຊ້."""
    print(f"ລາຄາ: {money(unit_price)}/{package_type}")


def input_quantity(unit_name):
    """ຮັບຈຳນວນສິນຄ້າຕາມຫົວໜ່ວຍ ໂດຍຕ້ອງເປັນຕົວເລກ ແລະ ຫຼາຍກວ່າ 0."""
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
    """ຖາມຄຳຖາມທີ່ຕອບໄດ້ພຽງ y ຫຼື n ເທົ່ານັ້ນ."""
    while True:
        answer = input(message).strip().lower()
        if answer in ("y", "n"):
            return answer
        print("ກະລຸນາກົດ y ຫຼື n ເທົ່ານັ້ນ.")


def save_customer(first_name, last_name):
    """ສ້າງ dictionary ຂໍ້ມູນລູກຄ້າ ແລ້ວເກັບເຂົ້າ list CUSTOMERS."""
    customer = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": f"{first_name} {last_name}",
    }
    CUSTOMERS.append(customer)
    return customer


def save_order_history(customer, orders):
    """ເກັບຂໍ້ມູນໃບບິນ 1 ໃບເຂົ້າ list ORDER_HISTORY."""
    subtotal = sum(item["total"] for item in orders)
    rate = discount_rate(subtotal)
    discount = subtotal * rate
    final_total = subtotal - discount

    bill_data = {
        "customer": customer,
        "orders": orders,
        "subtotal": subtotal,
        "discount_rate": rate,
        "discount": discount,
        "final_total": final_total,
    }
    ORDER_HISTORY.append(bill_data)
    return bill_data


def show_saved_data_count():
    """ສະແດງຈຳນວນຂໍ້ມູນທີ່ເກັບໄວ້ໃນ list."""
    print("\nຂໍ້ມູນຖືກເກັບໃນ list ແລ້ວ")
    print(f"- CUSTOMERS: {len(CUSTOMERS)} ລູກຄ້າ")
    print(f"- ORDER_HISTORY: {len(ORDER_HISTORY)} ໃບບິນ")


# ------------------------------------------------------------
# ສ່ວນທີ 4: ຟັງຊັນສຳລັບສະແດງ ແລະ ເລືອກສິນຄ້າ
# ------------------------------------------------------------
def show_all_products():
    """ສະແດງລາຍຊື່ສິນຄ້າທັງໝົດໃນສາງ ໂດຍກຳນົດເລກໃຫ້ແຕ່ລະສິນຄ້າ."""
    all_products = []
    print("\nລາຍການສິນຄ້າທັງໝົດໃນສາງ")

    for category, products in PRODUCTS.items():
        print(f"\n{category}")
        for name in products.keys():
            all_products.append({"category": category, "name": name})
            print(f"{len(all_products)}. {name}")

    return all_products


def choose_from_all_products():
    """ໃຫ້ລູກຄ້າເລືອກສິນຄ້າຈາກລາຍການທັງໝົດດ້ວຍເລກລຳດັບ."""
    all_products = show_all_products()

    while True:
        choice = input("\nເລືອກເລກສິນຄ້າ: ").strip()
        if not choice.isdigit():
            print("ກະລຸນາໃສ່ເປັນຕົວເລກ.")
            continue

        index = int(choice)
        if 1 <= index <= len(all_products):
            selected = all_products[index - 1]
            return selected["category"], selected["name"]

        print(f"ກະລຸນາເລືອກ 1 ຫາ {len(all_products)}.")


def choose_product():
    """ໃຫ້ລູກຄ້າເລືອກສິນຄ້າ 1 ລາຍການ ແລ້ວສົ່ງຂໍ້ມູນ order ກັບຄືນ."""
    view_mode = choose_from_list(
        "ຂັ້ນຕອນທີ 2: ເລືອກວິທີສະແດງສິນຄ້າ",
        VIEW_MODES,
    )

    if view_mode == "ແບນ/ສະແດງສິນຄ້າທັງໝົດ":
        # ໂໝດນີ້ຈະສະແດງສິນຄ້າທຸກອັນພ້ອມເລກລຳດັບ
        # ແລະໃຫ້ເລືອກສິນຄ້າຈາກເລກນັ້ນໂດຍກົງ.
        category, product_name = choose_from_all_products()
    else:
        # ໂໝດນີ້ເລືອກຕາມໝວດໝູ່ກ່ອນ ແລ້ວຈຶ່ງເລືອກສິນຄ້າ.
        category = choose_from_list(
            "ເລືອກໝວດໝູ່ສິນຄ້າ",
            list(PRODUCTS.keys()),
        )
        product_name = choose_from_list(
            f"ເລືອກສິນຄ້າໃນໝວດ {category}",
            list(PRODUCTS[category].keys()),
        )

    product_data = PRODUCTS[category][product_name]

    # ຖ້າເປັນນ້ຳດື່ມ: ຂ້າມການເລືອກປະເພດຕຸກ/ປອ໋ງ/ແກ້ວ
    # ແລ້ວກຳນົດ package_type ເປັນ "ແພັກ" ອັດຕະໂນມັດ.
    if category == "ນ້ຳດື່ມ":
        package_type = "ແພັກ"
        size = choose_size(
            "ຂັ້ນຕອນທີ 4: ເລືອກຂະໜາດນ້ຳດື່ມ",
            product_data[package_type],
        )
        print(f"\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ {package_type}")
        show_step5_price(product_data[package_type][size], package_type)
    else:
        # ເບຍ ແລະ ນ້ຳອັດລົມ ຕ້ອງເລືອກປະເພດພາຊະນະກ່ອນ.
        if len(product_data) == 1:
            product_type = list(product_data.keys())[0]
            print(f"\nຂັ້ນຕອນທີ 3: ບັນຈຸພັນ {product_type}")
        else:
            product_type = choose_from_list(
                "ຂັ້ນຕອນທີ 3: ເລືອກບັນຈຸພັນ",
                list(product_data.keys()),
            )

        # ກໍລະນີເບຍແກ້ວມີຂະໜາດດຽວ ຈຶ່ງຂ້າມການເລືອກຂະໜາດ.
        if category == "ເບຍ" and product_type == "ແກ້ວ":
            package_type = "ລາງ"
            size = "ມາດຕະຖານ"
            print(f"\nຂັ້ນຕອນທີ 4: ຂະໜາດ {size}")
        elif NO_SIZE in product_data[product_type]:
            # ສິນຄ້າບາງຢ່າງເປັນແກັດ ແລະ ບໍ່ມີຂະໜາດໃຫ້ເລືອກ.
            package_type = "ແກັດ"
            size = NO_SIZE
            print(f"\nຂັ້ນຕອນທີ 4: {size}")
        else:
            size = choose_size(
                "ຂັ້ນຕອນທີ 4: ເລືອກຂະໜາດຜະລິດຕະພັນ",
                product_data[product_type],
            )

        # ກໍລະນີເບຍ: ກຳນົດປະເພດໄຊ້ໃຫ້ເລີຍຕາມເງື່ອນໄຂ.
        if category == "ເບຍ" and product_type == "ປອ໋ງ":
            package_type = "ແກັດ"
            print(f"\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ {package_type}")
            show_step5_price(product_data[product_type][size], package_type)
        elif category == "ເບຍ" and product_type == "ແກ້ວ":
            package_type = "ລາງ"
            print(f"\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ {package_type}")
            show_step5_price(product_data[product_type][size], package_type)
        elif product_name in AUTO_CRATE_PRODUCTS:
            package_type = "ແກັດ"
            print(f"\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ {package_type}")
            show_step5_price(product_data[product_type][size], package_type)
        elif product_name in GLASS_TRAY_PRODUCTS and product_type == "ແກ້ວ":
            package_type = "ລາງ"
            print("\nຂັ້ນຕອນທີ 5: ປະເພດໄຊ້ ລາງ")
            show_step5_price(product_data[product_type][size], package_type)
        elif product_name in GLASS_TRAY_PRODUCTS and product_type in ("ຕຸກ", "ປອ໋ງ"):
            package_type = choose_from_list(
                "ຂັ້ນຕອນທີ 5: ເລືອກປະເພດໄຊ້",
                PACKAGE_OPTIONS_WITHOUT_CRATE,
            )
            show_step5_price(product_data[product_type][size], package_type)
        else:
            # ນ້ຳອັດລົມໃຫ້ຜູ້ໃຊ້ເລືອກ ແພັກ/ແກັດ/ລາງ.
            package_type = choose_from_list(
                "ຂັ້ນຕອນທີ 5: ເລືອກປະເພດໄຊ້",
                PACKAGE_OPTIONS,
            )
            show_step5_price(product_data[product_type][size], package_type)

    # ຫາລາຄາຕໍ່ໜ່ວຍຈາກ PRODUCTS ຕາມສິນຄ້າທີ່ເລືອກ.
    if category == "ນ້ຳດື່ມ":
        product_type = "ຕຸກ"
        unit_price = product_data[package_type][size]
    else:
        unit_price = product_data[product_type][size]

    quantity = input_quantity(package_type)
    total = unit_price * quantity

    # ສົ່ງຂໍ້ມູນການສັ່ງຊື້ 1 ລາຍການກັບຄືນໄປເກັບໃນ orders.
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


# ------------------------------------------------------------
# ສ່ວນທີ 5: ຟັງຊັນຄິດໄລ່ລາຄາ ແລະ ພິມໃບບິນ
# ------------------------------------------------------------
def discount_rate(total):
    """ຄືນຄ່າອັດຕາສ່ວນຫຼຸດຕາມຍອດຊື້ລວມ."""
    if total > 20000000:
        return 0.10
    if total >= 10000000:
        return 0.07
    if total >= 1000000:
        return 0.05
    return 0


def print_bill(first_name, last_name, orders):
    """ສະຫຼຸບລາຍການສັ່ງຊື້, ຄິດສ່ວນຫຼຸດ, ແລະ ພິມໃບບິນ."""
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


# ------------------------------------------------------------
# ສ່ວນທີ 6: ຟັງຊັນຫຼັກຂອງໂປຣແກຣມ
# main() ເປັນຈຸດເລີ່ມຕົ້ນ:
# - ສະແດງຫົວໂປຣແກຣມ
# - ຮັບຂໍ້ມູນລູກຄ້າ
# - ວົນຊ້ຳໃຫ້ຊື້ຫຼາຍລາຍການໄດ້
# - ພິມໃບບິນເມື່ອລູກຄ້າບໍ່ຊື້ຕໍ່
# ------------------------------------------------------------
def main():
    print("=" * 70)
    print("ລະບົບສູນສົ່ງນ້ຳທຸກປະເພດ")
    print("=" * 70)

    print("\nຂັ້ນຕອນທີ 1: ລັອກອິນຂໍ້ມູນລູກຄ້າ")
    first_name = input_not_empty("ປ້ອນຊື່: ")
    last_name = input_not_empty("ປ້ອນນາມສະກຸນ: ")
    customer = save_customer(first_name, last_name)

    # orders ໃຊ້ເກັບລາຍການສິນຄ້າທີ່ລູກຄ້າເລືອກທັງໝົດ.
    orders = []
    while True:
        order = choose_product()
        orders.append(order)

        # ຖ້າຕອບ y ຈະກັບໄປເລືອກສິນຄ້າອີກ,
        # ຖ້າຕອບ n ຈະອອກຈາກ loop ແລ້ວພິມໃບບິນ.
        more = ask_yes_no("\nຂັ້ນຕອນທີ 7: ຢາກຊື້ເພີ່ມອີກບໍ່? (y/n): ")
        if more == "n":
            break

    save_order_history(customer, orders)
    print_bill(first_name, last_name, orders)
    show_saved_data_count()


# ຄຳສັ່ງນີ້ເຮັດໃຫ້ main() ຖືກລັນເມື່ອເປີດໄຟລ໌ນີ້ໂດຍກົງ.
if __name__ == "__main__":
    main()
