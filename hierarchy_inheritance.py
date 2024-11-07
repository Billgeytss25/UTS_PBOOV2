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


# Kelas turunan dari User: Seller
class Seller(User):
    def addProduct(self, productName, description, price, stock):
        print(f"Menambahkan produk '{productName}' dengan deskripsi '{description}', harga {price}, stok {stock}")

    def processOrder(self, orderId, status):
        print(f"Memproses pesanan dengan ID {orderId}, status: {status}")


# Kelas turunan dari User: Admin
class Admin(User):
    def removeUser(self, userId):
        print(f"Menghapus pengguna dengan ID: {userId}")

    def generateReport(self, reportType, startDate, endDate):
        print(f"Menghasilkan laporan '{reportType}' dari {startDate} hingga {endDate}")


# Contoh penggunaan dari Hierarchy Inheritance
# Membuat objek Seller
seller = Seller("sellerPro", "seller@example.com", 202)
seller.login()                                 # User login
seller.addProduct("Kopi Arabika", "Kopi dengan aroma khas", 150000, 50)  # Menambahkan produk
seller.processOrder(3001, "Dalam pengiriman")  # Memproses pesanan
seller.logout()                                # User logout

# Membuat objek Admin
admin = Admin("adminMaster", "admin@example.com", 303)
admin.login()                                  # User login
admin.removeUser(202)                          # Menghapus pengguna
admin.generateReport("transaksi", "2024-01-01", "2024-12-31")  # Membuat laporan
admin.logout()                                 # User logout
