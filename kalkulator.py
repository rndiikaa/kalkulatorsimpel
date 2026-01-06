while True:
    print("===== MENU KALKULATOR =====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("Terima kasih, program selesai.")
        break

    if pilihan in ["1", "2", "3", "4"]:
        n = int(input("Berapa banyak bilangan? "))
        angka = []

        for i in range(n):
            angka.append(float(input(f"Bilangan ke-{i+1}: ")))

        if pilihan == "1":
            hasil = sum(angka)

        elif pilihan == "2":
            hasil = angka[0]
            for x in angka[1:]:
                hasil -= x

        elif pilihan == "3":
            hasil = 1
            for x in angka:
                hasil *= x

        elif pilihan == "4":
            hasil = angka[0]
            for x in angka[1:]:
                if x == 0:
                    print("Error: Tidak bisa dibagi nol")
                    break
                hasil /= x

        print("Hasil:", hasil)

    else:
        print("Menu tidak valid")
