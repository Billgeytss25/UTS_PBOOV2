# Kelas dasar User
class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"{self.username} mantap coyy berhasil login dengan email {self.email}")

    def logout(self):
        print(f"{self.username} yoii berhasil logout")


# Kelas turunan pertama dari User: BasicUser
class BasicUser(User):
    def viewProduct(self, productId):
        print(f"Menampilkan informasi buat elu produk dengan ID: {productId}")

    def addToCart(self, productId, quantity):
        print(f"Menambahkan produk dengan ID {productId} ke keranjang belanja sebanyak {quantity} item")


# Kelas turunan kedua dari BasicUser: PremiumUser
class PremiumUser(BasicUser):
    def applyVoucher(self, voucherCode, cartTotal):
        print(f"Menerapkan voucher '{voucherCode}' pada total belanja sebesar {cartTotal}")

    def requestPrioritySupport(self, issueDescription):
        print(f"Menghubungi dukungan prioritas untuk masalah: {issueDescription}")


# Contoh penggunaan dari Multilevel Inheritance
# Membuat objek PremiumUser
premium_user = PremiumUser("bah Gojo", "gojosatoru22@gmail.com", 101)

# Memanggil metode yang tersedia
premium_user.login()                      # User login
premium_user.viewProduct(1001)            # Menampilkan produk
premium_user.addToCart(1001, 3)           # Menambahkan produk ke keranjang
premium_user.applyVoucher("DISKON50", 50000)  # Menerapkan voucher
premium_user.requestPrioritySupport("Produk tidak sesuai deskripsi")  # Meminta dukungan prioritas
premium_user.logout()                     # User logout

        
