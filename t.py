data_list = []      # ເກັບລາຍຊື່ທຸກຄົນ
total_revenue = 0   # ເກັບຍອດເງິນລວມທັງໝົດ
print("=== ລະບົບລົງທະບຽນເຂົ້າຊົມສວນສັດ ===")
print("(ພິມ 'exit' ບ່ອນຊື່ ເພື່ອປິດໂປຣແກຣມ ແລະ ເບິ່ງສະຫຼຸບ)")
# 3. ຕົວໂປຣແກຣມຫຼັກ (Main Loop)
while True:
    print("-" * 30)
    name = input("ປ້ອນຊື່ຜູ້ເຂົ້າຊົມ: ").strip()
    # ກວດສອບວ່າຢາກອອກຈາກໂປຣແກຣມບໍ່
    if name.lower() == "exit":
        break 
    try:
        # ຮັບຄ່າອາຍຸ ແລະ ປ່ຽນເປັນຕົວເລກ
        age_input = int(input(f"ປ້ອນອາຍຸຂອງ {name}: "))
        
        # ເອີ້ນໃຊ້ Function ເພື່ອຫາ ກຸ່ມ ແລະ ລາຄາ
        group, price = check_entry_fee(age_input) 
        # ບວກລາຍໄດ້ເຂົ້າໃນຍອດລວມ
        total_revenue += price
        # ສະແດງຜົນການລົງທະບຽນທັນທີ
        print(f"✅ ລົງທະບຽນສຳເລັດ!")
        print(f"   👉 ກຸ່ມ: {group} | ຄ່າເຂົ້າ: {price:,} ກີບ")
        # ເກັບຂໍ້ມູນລົງໃນ List ເພື່ອສະຫຼຸບຕອນຈົບ
        data_list.append(f"ຊື່: {name:10} | ກຸ່ມ: {group:8} | ລາຄາ: {price:6,} ກີບ")
    except ValueError:
        print("❌ ຂໍ້ຜິດພາດ: ກະລຸນາປ້ອນອາຍຸເປັນ 'ຕົວເລກ' ເທົ່ານັ້ນ!")
        continue
# 4. ສະແດງຜົນສະຫຼຸບລວມ (Final Summary)
print("\n" + "="*45)
print("📜 ສະຫຼຸບລາຍງານການເຂົ້າຊົມທັງໝົດ")
print("="*45)
if not data_list:
    print("ບໍ່ມີຂໍ້ມູນຜູ້ເຂົ້າຊົມໃນມື້ນີ້.")
else:
    for record in data_list:
        print(record)
    print("-" * 45)
    print(f"💰 ລາຍຮັບທັງໝົດໃນມື້ນີ້: {total_revenue:,} ກີບ")
    print(f"👥 ຈຳນວນຜູ້ເຂົ້າຊົມທັງໝົດ: {len(data_list)} ຄົນ")
print("="*45)
print("ຂອບໃຈທີ່ໃຊ້ບໍລິການ")