import random

#Daftar ini memberikan gambaran tentang waktu acara.
Kalimat_starter = random.randint(1, 3)
if Kalimat_starter == 1 :
    kalimat_1 = ("Di malam yang sejuk,")
if Kalimat_starter == 2 :
    kalimat_1 = ("Di siang yang panas,")
if Kalimat_starter == 3 :
    kalimat_1 = ("Di pagi yang indah,")

#Daftar ini menceritakan tentang karakter utama dari cerita ini.
karakter = random.randint(1, 3)
if karakter == 1 :
    kalimat_2 = ("Leonardo sedang bermain Mobile Legend")
if karakter == 2 :
    kalimat_2 = ("Leonardo sedang duduk di teras")
if karakter == 3 :
    kalimat_2 = ("Leonardo sedang rebahan di kasur")

#Daftar ini menentukan hari yang tepat di mana beberapa insiden telah terjadi.
waktu = random.randint(1, 3)
if waktu == 1 :
    kalimat_3 = ("pada minggu itu.")
if waktu == 2 :
    kalimat_3 = ("pada senin itu.")
if waktu == 3 :
    kalimat_3 = ("pada sabtu itu.")

#Daftar ini mendefinisikan plot cerita.
story_plot = random.randint(1, 3)
if story_plot == 1 :
    kalimat_4 = ("Ia merasa bosan lalu pergi ke sebuah taman,")
if story_plot == 2 :
    kalimat_4 = ("Leo berencana untuk menonton film di biosko,")
if story_plot == 3 :
    kalimat_4 = ("Leonardo ingin pergi ke pantai,")

#Daftar ini mendefinisikan tempat di mana insiden itu terjadi.
tempat = random.randint(1, 3)
if tempat == 1 :
    kalimat_5 = ("di sana Leonardo bertemu dengan Margaret.")
if tempat == 2 :
    kalimat_5 = ("lalu ia melihat Margaret dari kejauhan.")
if tempat == 3 :
    kalimat_5 = ("saat sampai, Leo tak sengaja menemui Margaret.")

#Daftar ini mendefinisikan karakter kedua dari cerita.
second_character = random.randint(1, 3)
if second_character == 1 :
    kalimat_6 = ("Margaret yang sedang duduk sambil membaca buku menyapa Leo.")
if second_character == 2 :
    kalimat_6 = ("Margaret yang juga melihat Leonardo menyapanya.")
if second_character == 3 :
    kalimat_6 = ("Margaret menyapa Leo dengan lembut.")

#Daftar ini mendefinisikan usia karakter kedua.
usia = random.randint(1, 3)
if usia == 1 :
    kalimat_7 = ("Margaret masih berusia 19 tahun,")
if usia == 2 :
    kalimat_7 = ("Margaret berusia 20 tahun,")
if usia == 3 :
    kalimat_7 = ("Margaret berusia 21 tahun,")

#Daftar ini menceritakan tentang pekerjaan yang dilakukan karakter kedua.
pekerjaan = random.randint(1, 3)
if pekerjaan == 1 :
    kalimat_8 = ("Ia masih berkuliah di Universitas Tadikamesra.")
if pekerjaan == 2 :
    kalimat_8 = ("Ia bekerja sebagai babysitter.")
if pekerjaan == 3 :
    kalimat_8 = ("Saat ini ia bekerja sebagai pegawai negeri.")

print (kalimat_1, kalimat_2, kalimat_3, kalimat_4, kalimat_5, kalimat_6, kalimat_7, kalimat_8)