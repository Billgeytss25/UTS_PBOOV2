# Kelas dasar User
class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"{self.username} berhasil login dengan email {self.email}")

    def logout(self):
        print(f"{self.username} berhasil logout")


# Kelas turunan BasicUser dari User
class BasicUser(User):
    def viewProduct(self, productId):
        print(f"Menampilkan informasi produk dengan ID: {productId}")

    def addToCart(self, productId, quantity):
        print(f"Menambahkan produk dengan ID {productId} ke keranjang belanja sejumlah {quantity} item")


# Kelas turunan PremiumUser dari BasicUser
class PremiumUser(BasicUser):
    def applyVoucher(self, voucherCode, cartTotal):
        print(f"Menerapkan voucher '{voucherCode}' pada total belanja sebesar {cartTotal}")

    def requestPrioritySupport(self, issueDescription):
        print(f"Menghubungi dukungan prioritas untuk masalah: {issueDescription}")


# Kelas turunan Seller dari User
class Seller(User):
    def addProduct(self, productName, description, price, stock):
        print(f"Menambahkan produk '{productName}' dengan deskripsi '{description}', harga {price}, stok {stock}")

    def processOrder(self, orderId, status):
        print(f"Memproses pesanan dengan ID {orderId}, status: {status}")


# Pembuatan objek dan penggunaan metode
# Membuat objek PremiumUser
premium_user = PremiumUser("Buddy-Anduk", "buddy22@example.com", 101)
premium_user.login()
premium_user.viewProduct(1001)                          # Menampilkan informasi produk
premium_user.addToCart(1001, 3)                         # Menambahkan produk ke keranjang
premium_user.applyVoucher("DISKON50", 50000)           # Menerapkan voucher
premium_user.requestPrioritySupport("Produk rusak")    # Meminta dukungan prioritas
premium_user.logout()

print("\n")

# Membuat objek Seller
seller = Seller("sellerPro", "seller@example.com", 202)
seller.login()
seller.addProduct("Kopi Arabika", "Kopi dengan aroma khas", 150000, 50)  # Menambahkan produk baru
seller.processOrder(3001, "Dalam pengiriman")                           # Memproses pesanan
seller.logout()
