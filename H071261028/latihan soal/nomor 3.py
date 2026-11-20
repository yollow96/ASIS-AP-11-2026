class AkunBank:
    def __init__(self, pemilik, saldo, pin):
        self.__pemilik = pemilik
        self.__saldo = saldo
        self.__pin = pin
        self.__salah_pin = 0
        self.__terblokir = False

    @property
    def saldo(self):
        return self.__saldo

    def cek_pin(self, pin):
        if self.__terblokir:
            print("Akun terblokir!")
            return False

        if pin != self.__pin:
            self.__salah_pin += 1
            print("PIN salah!")

            if self.__salah_pin >= 3:
                self.__terblokir = True
                print("Akun terblokir karena 3 kali salah PIN!")

            return False

        self.__salah_pin = 0
        return True

    def ganti_pin(self, pin_lama, pin_baru):
        if not self.cek_pin(pin_lama):
            return False

        if not isinstance(pin_baru, str) or len(pin_baru) != 6 or not pin_baru.isdigit():
            print("PIN baru harus 6 digit angka!")
            return False

        self.__pin = pin_baru
        print("PIN berhasil diubah!")
        return True

    def tarik(self, jumlah, pin):
        if not self.cek_pin(pin):
            return False

        if jumlah <= 0 or jumlah > self.__saldo:
            print("Saldo tidak mencukupi atau jumlah tidak valid!")
            return False

        self.__saldo -= jumlah
        print(f"Penarikan Rp {jumlah:,.0f} berhasil!")
        return True

    def transfer(self, tujuan, jumlah, pin):
        if not self.cek_pin(pin):
            return False

        if jumlah <= 0 or jumlah > self.__saldo:
            print("Saldo tidak mencukupi atau jumlah tidak valid!")
            return False

        if tujuan is self:
            print("Tidak bisa transfer ke rekening sendiri!")
            return False

        self.__saldo -= jumlah
        tujuan.__saldo += jumlah

        print(f"Transfer Rp {jumlah:,.0f} berhasil!")
        return True

akun1 = AkunBank("Budi", 1000000, "123456")
akun2 = AkunBank("Andi", 500000, "654321")

print("=== DATA REKENING AWAL ===")
print(f"Saldo Budi : Rp {akun1.saldo:,.0f}")
print(f"Saldo Andi : Rp {akun2.saldo:,.0f}")

print("\n=== PENARIKAN ===")
akun1.tarik(200000, "123456")

print("\n=== TRANSFER ===")
akun1.transfer(akun2, 300000, "123456")

print("\n=== GANTI PIN ===")
akun1.ganti_pin("123456", "111222")

print("\n=== SALDO AKHIR ===")
print(f"Saldo Budi : Rp {akun1.saldo:,.0f}")
print(f"Saldo Andi : Rp {akun2.saldo:,.0f}")

print("\n=== UJI BLOKIR AKUN ===")
akun1.tarik(100000, "000000")
akun1.tarik(100000, "000000")
akun1.tarik(100000, "000000")
