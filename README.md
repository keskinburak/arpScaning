# arpScaning

# Gerekli Kütüphaneler

Uygulamanın çalışması için `scapy` ve `configparser` kütüphanelerini yüklemeniz gerekmektedir.

```
sudo pip install scapy
```

```
sudo pip install configparser
```

# Uygulamayı Çalıştırmak

Uygulamayı çalıştırmadan önce hangi IP aralığında tarama yapılacağını belirtmek için kodun 6. satırında bulunan `ARP(pdst="192.168.2.0/24")`bölümündeki aralığı istediğiniz şekilde değiştirerek ayarlayınız.
Çalıştırmak için root kullanıcı olmak gerekli olduğu için aşağıdaki şekilde çalıştırınız.

```
sudo python arpScaning.py
```
İlk çalıştırdığınızda ağda bulunan cihazları MAC ve IP adresleriyle `onlineDevices.txt` dosyasına ekler .
Daha sonra ki çalıştırmalarımızda ağda bulunan yeni cihazları yada IP'si değişmiş olan cihazları tespit ederek kullanıcıya bu değişiklikleri kaydetmeyi isteyip istemediğini sorar.
