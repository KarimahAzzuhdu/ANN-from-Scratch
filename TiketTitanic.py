#Program Prediksi Survival Titanic Disaster
#Input sebuah list dan Output biner 1/0 berarti Survive/Death

import os

print("=====Beli Ticket=====")
kelas = int(input("Kelas Sosial-Ekonomi (Up=1,Mid=2,Low=3) : "))
jk = int(input("Jenis Kelamin (pria=0, wanita=1): "))
uk_rom = int(input("Jumlah Rombongan Keberangkatan : "))
usia = int(input("Usia : "))
tarif = int(input("Jumlah Uang yang bersedia dikeluarkan (USD): "))
print("====Terima Kasih!====")

#Kel_Usia
if usia<=20 :
    kel_usia = 0
elif usia<=26 :
    kel_usia = 1
elif usia<=30 :
    kel_usia = 2
elif usia<=38 :
    kel_usia = 3
else :
    kel_usia = 4

#Kel_tf
if tarif<8 :
    kel_tf = 0
elif tarif<11 :
    kel_tf = 1
elif tarif<22 :
    kel_tf = 2
elif tarif<40 :
    kel_tf = 3
else :
    kel_tf = 4

#Nilai Bobot dan Bias
model_weight = [-1.4228266960592637,
                4.57717330394075,
                0.1771733039407572,
                -0.6228266960592408,
                -0.6228266960592513]
model_bias = 2.5999999999999996

#fungsi single_predict
def single_predict_titanic(list_val, weight, bias):
    #mengalikan input value feature dengan bobot
    multiply = 0
    for i in range(0,len(list_val)) :
        multiply += weight[i] * list_val[i]

    #menjumlahkan seluruh hasil perkalian dengan bias
    Y_in = bias + multiply

    #fungsi aktivasi binary step/hardlimit
    if (Y_in >= 0):
        y_predict = 1
    else:
        y_predict = 0

    return y_predict

#Prediksi
print(" ")
print("=====Titanic Disaster Prediction====")
print("Prediksi nasibmu :")

pred_list = [kelas,jk,uk_rom,kel_usia,kel_tf]
targetku = single_predict_titanic(pred_list, model_weight, model_bias)
if targetku==1 :
    print('Selamat, kemungkinan besar kamu bisa Survive!')
else :
    print('Hati-hati, kemungkinan besar kamu Tidak bisa Survive!')
    print('Lebih baik jual kembali tiketmu!')

print("")
os.system('pause')