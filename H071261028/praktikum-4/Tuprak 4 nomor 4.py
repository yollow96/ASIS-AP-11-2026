# def suhu (nilai_suhu, skala_asal, skala_tujuan):
#     try: 
#         if skala_asal not in ("C", "F", "K"):
#            raise ZeroDivisionError ("Skala tidak dikenali")
#         if skala_tujuan not in ("C", "F", "K"):
#            raise ZeroDivisionError ("Skala tidak dikenali")
        
#         if skala_asal == "C":
#            celcius = nilai_suhu 
#         elif skala_asal == "F":
#            celcius = (nilai_suhu - 32) * 5/9
#         elif skala_asal == "K":
#            celcius = nilai_suhu - 273.15

#         if skala_tujuan == "C":
#             hasil = celcius 
#         elif skala_tujuan == "F":
#             hasil = (celcius * 9 / 5) + 32
#         elif skala_tujuan == "K":
#             hasil = celcius + 273.15

#         return hasil
#     except:
#         return "hasil konversi tidak valid"
# print("=== Konversi Suhu ===")
# while True:
#     nilai_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar):")
#     if nilai_suhu == "selesai":
#         break
#     try:
#         nilai_suhu = float(nilai_suhu)
#     except:
#         print("Suhu harus berupa angka")
#         continue
#     skala_asal = input("Skala asal (C/F/K):").upper()
#     skala_tujuan = input("Skala tujuan (C/F/K):").upper()

#     if skala_asal not in ["C", "F", "K"] or skala_tujuan not in ["C", "F", "K"]:
#         print("Skala tidak dikenali")
#         continue
       
#     hasil = suhu(nilai_suhu, skala_asal, skala_tujuan)
#     print("Hasil:", nilai_suhu, skala_asal, "=", hasil, skala_tujuan)
   

# def suhu(nilai_suhu,  skala_asal, skala_tujuan):
    
#     if skala_asal == "C":
#         celcius = nilai_suhu
#     elif skala_asal == "F":
#         celcius = (nilai_suhu - 32) * 5 / 9
#     elif skala_asal == "K":
#         celcius = nilai_suhu - 273.15

#     if skala_tujuan == "C":
#         hasil = celcius 
#     elif skala_tujuan == "F":
#         hasil = (celcius *9 / 5) + 32
#     elif skala_tujuan == "K":
#         hasil = celcius + 273.15

#     return hasil
    
# print("=== Konversi suhu ===")
# while True:
#     try:
#         nilai_suhu =(input("Masukkan suhu (atau 'selesai' untuk keluar):"))
#         if nilai_suhu == 'selesai':
#             break
    
#         nilai_suhu = (float(nilai_suhu))
    
#         skala_asal = (input("Skala asal :"))
#         skala_tujuan = (input("Skala tujuan :"))

#         if skala_asal not in ["C", "F", "K"] or skala_tujuan not in ["C", "F", "K"]:
#             raise ZeroDivisionError ("Error: Skala tidak dikenali")
       
#         hasil = suhu(nilai_suhu, skala_asal, skala_tujuan)
#         print("Hasil :", nilai_suhu, skala_asal, "=", hasil, skala_tujuan)
#     except ZeroDivisionError as e:
#         print(e)
#         continue

    


    # def suhu(nilai_suhu, skala_asal, skala_tujuan):
    #     try:
    #         if skala_asal not in ["C", "F", "K"]:
    #             raise ZeroDivisionError ("Skala tidak dikenali")
    #         if skala_tujuan not in ["C", "F", "K"]:
    #             raise ZeroDivisionError ("Skala tidak dikenali")

    #         if skala_asal == "C":
    #             celcius = nilai_suhu
    #         elif skala_asal == "F":
    #             celcius = (nilai_suhu - 32) * 5 / 9
    #         elif skala_asal == "K":
    #             celcius = nilai_suhu - 273.15

    #         if skala_tujuan == "C":
    #             hasil = celcius
    #         elif skala_tujuan == "F":
    #             hasil = (celcius * 9 / 5) + 32
    #         elif skala_tujuan == "K":
    #             hasil = celcius + 273.15
    #             return hasil
    #     except:
    #         return "Hasil konversi tidak valid"

def suhu(nilai_suhu, skala_asal, skala_tujuan):
    if skala_asal == "c":
        celcius = nilai_suhu
    elif skala_asal == "f":
        celcius = (nilai_suhu - 32) * 5 / 9
    elif skala_asal == "k":
        celcius = nilai_suhu - 273.15

    if skala_tujuan == "c":
        hasil = celcius
    elif skala_tujuan == "f":
        hasil = (celcius * 9 / 5) + 32
    elif skala_tujuan == "k":
        hasil = celcius + 273.15
    return hasil

while True:
    try:
        nilai_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar):")
        if nilai_suhu.lower() == 'selesai':
            break 
        nilai_suhu = float(nilai_suhu)

        skala_asal = input("Skala asal (C/F/K) :").lower()
        skala_tujuan = input("Skala tujuan (C/F/K) :").lower()

        if skala_asal not in ["c", "f", "k"] or skala_tujuan not in ["c", "f", "k"]:
            raise Exception ("Error : skala suhu tidak dikenali")
        hasil = suhu(nilai_suhu, skala_asal, skala_tujuan)
        print("Hasil :", nilai_suhu, skala_asal, "=", hasil, skala_tujuan)
    except Exception as e:
        print(e)
        continue



        