# tkinter modülünü içe aktar
import tkinter as tk
from tkinter import filedialog
# hashlib modülünü içe aktar
import hashlib

# uygulama penceresini oluştur
window = tk.Tk()
window.title("Hash Doğrulama Uygulaması")
window.geometry("600x400")

# gökkuşağı renkleri listesi
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# renk değiştirme fonksiyonu
def change_color():
    # global değişkenleri kullan
    global colors, index
    # pencerenin arka plan rengini değiştir
    window.config(bg=colors[index])
    # renk listesinin sonuna gelince başa dön
    index = (index + 1) % len(colors)
    # 1 saniye sonra fonksiyonu tekrar çağır
    window.after(1000, change_color)

# dosya seçme fonksiyonu
def select_file():
    # global değişkenleri kullan
    global file_path, file_label
    # dosya seçme penceresini aç
    file_path = filedialog.askopenfilename()
    # seçilen dosyanın adını etikete yaz
    file_label.config(text=file_path)
    # hash hesaplama fonksiyonunu çağır
    calculate_hash()

# hash hesaplama fonksiyonu
def calculate_hash():
    # global değişkenleri kullan
    global file_path, md5_label, sha1_label, sha256_label, sha512_label, ripemd_label
    # seçilen dosyayı okumak için aç
    with open(file_path, "rb") as f:
        # dosyanın içeriğini oku
        data = f.read()
        # md5 hash değerini hesapla ve etikete yaz
        md5 = hashlib.md5(data).hexdigest()
        md5_label.config(text=md5)
        # sha1 hash değerini hesapla ve etikete yaz
        sha1 = hashlib.sha1(data).hexdigest()
        sha1_label.config(text=sha1)
        # sha256 hash değerini hesapla ve etikete yaz
        sha256 = hashlib.sha256(data).hexdigest()
        sha256_label.config(text=sha256)
        # sha512 hash değerini hesapla ve etikete yaz
        sha512 = hashlib.sha512(data).hexdigest()
        sha512_label.config(text=sha512)
        # ripemd hash değerini hesapla ve etikete yaz
        ripemd = hashlib.new("ripemd160", data).hexdigest()
        ripemd_label.config(text=ripemd)

# hash doğrulama fonksiyonu
def verify_hash():
    # global değişkenleri kullan
    global verify_entry, result_label, md5_label, sha1_label, sha256_label, sha512_label, ripemd_label
    # hash doğrulama fonksiyonu
def verify_hash():
    # global değişkenleri kullan
    global verify_entry, result_label, md5_label, sha1_label, sha256_label, sha512_label, ripemd_label
    # giriş kutusundan hash değerini al
    hash_value = verify_entry.get()
    # hash değeri boşsa uyarı ver
    if not hash_value:
        result_label.config(text="Lütfen bir hash değeri girin.")
        return
    # hash değeri seçilen dosyanın hash değerlerinden biriyle eşleşiyorsa doğrulama başarılı mesajı ver
    if hash_value == md5_label.cget("text") or \
       hash_value == sha1_label.cget("text") or \
       hash_value == sha256_label.cget("text") or \
       hash_value == sha512_label.cget("text") or \
       hash_value == ripemd_label.cget("text"):
        result_label.config(text="Doğrulama başarılı. Dosya bütünlüğü korunmuş.")
    # eşleşmiyorsa doğrulama başarısız mesajı ver
    else:
        result_label.config(text="Doğrulama başarısız. Dosya bütünlüğü bozulmuş.")

# renk değiştirme fonksiyonunu çağır
index = 0 # renk listesinin başlangıç indeksi
change_color()

# dosya seçme butonunu oluştur
select_button = tk.Button(window, text="Dosya Seç", command=select_file)
select_button.place(x=50, y=50)

# seçilen dosyanın adını gösteren etiketi oluştur
file_label = tk.Label(window, text="Seçilen dosya yok")
file_label.place(x=150, y=50)

# md5 etiketini oluştur
md5_text = tk.Label(window, text="MD5:")
md5_text.place(x=50, y=100)
md5_label = tk.Label(window, text="")
md5_label.place(x=100, y=100)

# sha1 etiketini oluştur
sha1_text = tk.Label(window, text="SHA1:")
sha1_text.place(x=50, y=150)
sha1_label = tk.Label(window, text="")
sha1_label.place(x=100, y=150)

# sha256 etiketini oluştur
sha256_text = tk.Label(window, text="SHA256:")
sha256_text.place(x=50, y=200)
sha256_label = tk.Label(window, text="")
sha256_label.place(x=100, y=200)

# sha512 etiketini oluştur
sha512_text = tk.Label(window, text="SHA512:")
sha512_text.place(x=50, y=250)
sha512_label = tk.Label(window, text="")
sha512_label.place(x=100, y=250)

# ripemd etiketini oluştur
ripemd_text = tk.Label(window, text="RIPEMD:")
ripemd_text.place(x=50, y=300)
ripemd_label = tk.Label(window, text="")
ripemd_label.place(x=100, y=300)

# doğrulama giriş kutusunu oluştur
verify_entry = tk.Entry(window)
verify_entry.place(x=350, y=100)

# doğrulama butonunu oluştur
verify_button = tk.Button(window, text="Doğrula", command=verify_hash)
verify_button.place(x=350, y=150)

# doğrulama sonucunu gösteren etiketi oluştur
result_label = tk.Label(window, text="")
result_label.place(x=350, y=200)

# uygulama penceresinin ana döngüsünü başlat
window.mainloop()