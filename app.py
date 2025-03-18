# Ana uygulama dosyası - MVC sistemini çalıştırır.

from controllers.controller import MainController

def main():
    controller = MainController()
    
    while True:
        print("
1- Veri Ekle")
        print("2- Verileri Göster")
        print("3- Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            item = input("Eklemek istediğiniz veriyi girin: ")
            controller.add_item(item)
            print(f"✅ {item} başarıyla eklendi!")
        elif choice == "2":
            controller.show_items()
        elif choice == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("⚠️ Geçersiz giriş, tekrar deneyin.")

if __name__ == "__main__":
    main()
