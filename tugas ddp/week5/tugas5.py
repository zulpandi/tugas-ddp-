kendaraan=["Pajero sport","mobil sport","Mitsubishi","2244cc"]

kendaraan.append("hitam")
kendaraan.append("768_juta")

kendaraan.insert(2,"roda empat")
kendaraan.remove("mobil sport")

print(kendaraan)

pilihan = (input("""Silahkan pilih nomor dibawah ini
untuk menggunakan alat dibawah
1. Persegi
2. Lingkaran
3. Segitiga
Pilihanmu? """))

match pilihan:

  case "1":
    s=int(input("masukkan sisi:"))
    jumlah=s*s
    print('luaspersegi',jumlah)
    
  case "2":
    r=int(input("memasukkan jari:"))
    luas=3.14*r*r
    print('luas lingkaran',luas)
    
  case "3":
    aku=1/2
    a=int(input("masukkan alas:"))
    t=int(input("masukkan tinggi:"))
    segitiga=0.5*a*t
    print('luas segitiga',segitiga)