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
        "ສະຕີງ": {
            "ຕຸກ": {"ນ້ອຍ": 120000},
            "ປອ໋ງ": {"ນ້ອຍ": 135000},
            "ແກ້ວ": {"ນ້ອຍ": 110000},
        },
        "M150": {
            "ຕຸກ": {"ນ້ອຍ": 130000},
            "ປອ໋ງ": {"ນ້ອຍ": 145000},
            "ແກ້ວ": {"ນ້ອຍ": 120000},
        },
        "ກະທີງແດງ": {
            "ຕຸກ": {"ນ້ອຍ": 130000},
            "ປອ໋ງ": {"ນ້ອຍ": 145000},
            "ແກ້ວ": {"ນ້ອຍ": 120000},
        },
        "ສະປອນເຊີ": {
            "ຕຸກ": {"ນ້ອຍ": 125000},
            "ປອ໋ງ": {"ນ້ອຍ": 140000},
            "ແກ້ວ": {"ນ້ອຍ": 115000},
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


def choose_size_with_price(title, size_prices, unit_name):
    """ສະແດງຂະໜາດພ້ອມລາຄາຕໍ່ຫົວໜ່ວຍ ແລ້ວສົ່ງຂະໜາດທີ່ເລືອກກັບຄືນ."""
    sizes = list(size_prices.keys())

    while True:
        print(f"\n{title}")
        for i, size in enumerate(sizes, start=1):
            price = size_prices[size]
            print(f"{i}. {size} - {money(price)}/{unit_name}")

        choice = input("ເລືອກເລກ: ").strip()
        if not choice.isdigit():
            print("ກະລຸນາໃສ່ເປັນຕົວເລກ.")
            continue

        index = int(choice)
        if 1 <= index <= len(sizes):
            return sizes[index - 1]

        print(f"ກະລຸນາເລືອກ 1 ຫາ {len(sizes)}.")


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
        size = choose_size_with_price(
            "ຂັ້ນຕອນທີ 4: ເລືອກຂະໜາດນ້ຳດື່ມ",
            product_data[package_type],
            package_type,
        )
    else:
        # ເບຍ ແລະ ນ້ຳອັດລົມ ຕ້ອງເລືອກປະເພດພາຊະນະກ່ອນ.
        product_type = choose_from_list(
            "ຂັ້ນຕອນທີ 3: ເລືອກບັນຈຸພັນ",
            list(product_data.keys()),
        )

        # ກໍລະນີເບຍແກ້ວມີຂະໜາດດຽວ ຈຶ່ງຂ້າມການເລືອກຂະໜາດ.
        if category == "ເບຍ" and product_type == "ແກ້ວ":
            package_type = "ລາງ"
            size = "ມາດຕະຖານ"
            print(f"\nຂັ້ນຕອນທີ 4: ຂະໜາດ {size} - {money(product_data[product_type][size])}/{package_type}")
        else:
            if category == "ເບຍ" and product_type == "ປອ໋ງ":
                size_unit = "ແກັດ"
            else:
                size_unit = "ໜ່ວຍ"

            size = choose_size_with_price(
                "ຂັ້ນຕອນທີ 4: ເລືອກຂະໜາດຜະລິດຕະພັນ",
                product_data[product_type],
                size_unit,
            )

        # ກໍລະນີເບຍ: ກຳນົດປະເພດໄຊ້ໃຫ້ເລີຍຕາມເງື່ອນໄຂ.
        if category == "ເບຍ" and product_type == "ປອ໋ງ":
            package_type = "ແກັດ"
        elif category == "ເບຍ" and product_type == "ແກ້ວ":
            package_type = "ລາງ"
        else:
            # ນ້ຳອັດລົມໃຫ້ຜູ້ໃຊ້ເລືອກ ແພັກ/ແກັດ/ລາງ.
            package_type = choose_from_list(
                "ຂັ້ນຕອນທີ 5: ເລືອກປະເພດໄຊ້",
                PACKAGE_OPTIONS,
            )

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

    print("\n" + "=" * 70)
    print("ໃບບິນສູນສົ່ງນ້ຳທຸກປະເພດ")
    print("=" * 70)
    print(f"ຊື່ລູກຄ້າ: {first_name} {last_name}")
    print("-" * 70)
    print(f"{'ລຳດັບ':<6}{'ສິນຄ້າ':<18}{'ປະເພດ':<10}{'ຂະໜາດ':<12}{'ຈຳນວນ':<8}{'ລວມ':>14}")
    print("-" * 70)

    for i, item in enumerate(orders, start=1):
        product_detail = f"{item['product_type']}/{item['package_type']}"
        print(
            f"{i:<6}"
            f"{item['name']:<18}"
            f"{product_detail:<10}"
            f"{item['size']:<12}"
            f"{item['quantity_text']:<8}"
            f"{money(item['total']):>14}"
        )

    print("-" * 70)
    print(f"ລາຄາລວມກ່ອນຫຼຸດ: {money(subtotal)}")
    print(f"ສ່ວນຫຼຸດ: {int(rate * 100)}% = {money(discount)}")
    print(f"ລາຄາຕ້ອງຈ່າຍທັງໝົດ: {money(final_total)}")
    print("=" * 70)
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

    print_bill(first_name, last_name, orders)


# ຄຳສັ່ງນີ້ເຮັດໃຫ້ main() ຖືກລັນເມື່ອເປີດໄຟລ໌ນີ້ໂດຍກົງ.
if __name__ == "__main__":
    main()
