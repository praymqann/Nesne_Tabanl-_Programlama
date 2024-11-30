import random
import time

class Kumanda():
    def __init__(self, tv_durum ='Kapalı',tv_ses=0,kanal_listesi = ['Trt'],kanal ='trt'):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi =kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if (self.tv_durum == 'Açık'):
            print("Televizyon zaten acık")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum = 'Açık'
    
    def tv_kapat(self):
        if(self.tv_durum == 'Kapalı'):
            print("televizyon zaten kapalı")
        else
            print ("televizyon kapanıyor...")
            self.tv_durum = 'Kapalı'

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi Azalt: '<'/n Sesi Arttır:'>'\nÇıkışı:'çıkış'")
                if (cevap == '<'):
                    if(self.tv_ses != 0):
                        self.tv_ses -= 1

                        print(f"SES:{slef.tv_ses}")
                