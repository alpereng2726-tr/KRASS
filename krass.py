import customtkinter as ctk
import sqlite3
import tkinter as tk
class KRASS:

    def __init__(self):
        self.soyagaci_frame = None
        self.pencere = ctk.CTk()
        self.pencere.title("KRASS")
        self.pencere.attributes("-fullscreen", True)
        sqlconn=sqlite3.connect("krass.db")
        self.cursor=sqlconn.cursor()
        self.sayfa1()

        self.pencere.mainloop()
    #SAYFA TASARIMLARI KISMI==========================================================================================0
    #SAYFA1
    def sayfa1(self):
        frame = ctk.CTkFrame(self.pencere,width=350,height=270)
        frame.pack(expand=True)
        frame.pack_propagate(False) #hocam bu fonksiyon framei widgetlara göre küçültmeyi engelliyomuş 

        self.kullaniciadı_label = ctk.CTkLabel(frame, text="Kullanıcı Adı")
        self.kullaniciadı_label.pack(pady=(0,5))

        self.kullaniciadı_entry = ctk.CTkEntry(frame, width=300, height=45)
        self.kullaniciadı_entry.pack(pady=(0,20))
        
        self.parola_label = ctk.CTkLabel(frame, text="Parola")
        self.parola_label.pack(pady=(0,5))

        self.parola_entry = ctk.CTkEntry(frame, width=300, height=45, show="*")
        self.parola_entry.pack(pady=(20))
        
        self.giris_button=ctk.CTkButton(frame,text="GİRİŞ YAP",fg_color="white",command=self.giris)
        self.giris_button.pack()

        #SAYFA2
    def sayfa2(self, username):
        self.sayfatemizle()

        frame = ctk.CTkFrame(self.pencere, height=50)
        frame.pack(fill="x", pady=10)

        welcomelabel = ctk.CTkLabel(frame, text=f"HOŞGELDİN {username}")
        welcomelabel.pack()

        frame2 = ctk.CTkFrame(self.pencere)
        frame2.pack(fill="both", expand=True, padx=10, pady=10)

        #=================== SOL PANEL ===================

        sol_panel = ctk.CTkFrame(frame2, width=300)
        sol_panel.pack(side="left", fill="y", padx=(0,10))
        sol_panel.pack_propagate(False)

        self.arama_entry = ctk.CTkEntry(
            sol_panel,
            placeholder_text="Hasta Ara..."
        )
        self.arama_entry.pack(fill="x", padx=10, pady=(10,5))

        self.arama_entry.bind(
            "<KeyRelease>",
            lambda event: self.hasta_listesini_olustur(self.arama_entry.get())
        )

        self.hasta_frame = ctk.CTkScrollableFrame(sol_panel)
        self.hasta_frame.pack(fill="both", expand=True, padx=10, pady=(0,10))

        #=================== SAĞ PANEL ===================

        self.sag_panel = ctk.CTkFrame(frame2)
        self.sag_panel.pack(side="left", fill="both", expand=True)

        # Hasta listesini ilk oluştur
        self.hasta_listesini_olustur()

    def kanserbutonlarıvesagpanel(self,isim,soyisim,yas):
        self.riskanaliz()

        for widget in self.sag_panel.winfo_children():
            widget.destroy()

        #================ ÜST KISIM ================

        ust_frame = ctk.CTkFrame(self.sag_panel)
        ust_frame.pack(fill="x", padx=20, pady=20)

        isim_label = ctk.CTkLabel(
            ust_frame,
            text=f"{isim} {soyisim}",
            font=("Arial", 24, "bold")
        )
        isim_label.pack(side="left")
        enabız_button=ctk.CTkButton(ust_frame,text="E NABIZ")
        enabız_button.pack(side="right",padx=10)
        yas_label = ctk.CTkLabel(
            ust_frame,
            text=f"Yaş : {yas}",
            font=("Arial", 20)
        )
        yas_label.pack(side="right")

        #================ KANSER BUTONLARI ================

        kanser_frame = ctk.CTkFrame(self.sag_panel)
        kanser_frame.pack(fill="x", padx=20, pady=20)

        akcıger_renk = self.kanser_riskleri["akciger"]
        ctk.CTkButton(
            kanser_frame,
            text="Akciğer Kanseri",
            width=140,
            height=60,
            fg_color=akcıger_renk,
            command=lambda: self.kanser_sec("akciger")
        ).grid(row=0, column=0, padx=10, pady=10)

        kolon_renk = self.kanser_riskleri["kolon"]
        ctk.CTkButton(
            kanser_frame,
            text="Kolon Kanseri",
            width=140,
            height=60,
            fg_color=kolon_renk,
            command=lambda: self.kanser_sec("kolon")
        ).grid(row=0, column=1, padx=10, pady=10)

        rahim_renk = self.kanser_riskleri["rahim"]
        ctk.CTkButton(
            kanser_frame,
            text="Rahim Kanseri",
            width=140,
            height=60,
            fg_color=rahim_renk,
            command=lambda: self.kanser_sec("rahim")
        ).grid(row=0, column=2, padx=10, pady=10)

        meme_renk = self.kanser_riskleri["meme"]
        ctk.CTkButton(
            kanser_frame,
            text="Meme Kanseri",
            width=140,
            height=60,
            fg_color=meme_renk,
            command=lambda: self.kanser_sec("meme")
        ).grid(row=0, column=3, padx=10, pady=10)
        
        prostat_renk = self.kanser_riskleri["prostat"]
        ctk.CTkButton(
            kanser_frame,
            text="Prostat Kanseri",
            width=140,
            height=60,
            fg_color=prostat_renk,
            command=lambda: self.kanser_sec("prostat")
        ).grid(row=0, column=4, padx=10, pady=10)

        farklı_renk = self.kanser_riskleri["farklı"]
        ctk.CTkButton(
            kanser_frame,
            text="farklı kanser türleri",
            width=140,
            height=60,
            fg_color=farklı_renk,
            command=lambda: self.kanser_sec("farklı")
        ).grid(row=1, column=0, padx=10, pady=10)

        ctk.CTkButton(
            kanser_frame,
            text="kalp krizi riski",
            width=140,
            height=60
        ).grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkButton(
            kanser_frame,
            text="Emboli riski",
            width=140,
            height=60
        ).grid(row=1, column=2, padx=10, pady=10)

        ctk.CTkButton(
            kanser_frame,
            text="Diyabet riski",
            width=140,
            height=60
        ).grid(row=1, column=3, padx=10, pady=10)


#SOYAĞACI KISMI (HOCAM ÇOK KARMAŞIK OLABİLDİĞİNCE DÜZGÜN YAZDIRIYOM )
    def soyagacı(self):

        if self.soyagaci_frame is not None:
            self.soyagaci_frame.destroy()

        self.soyagaci_frame = ctk.CTkFrame(self.sag_panel)
        self.soyagaci_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.canvas = tk.Canvas(
            self.soyagaci_frame,
            bg="white",
            highlightthickness=0
        )

        self.canvas.pack(fill="both", expand=True)

        self.canvas.after(50, self.soyagaci_ciz)




    def kisi_ciz(self,x,y,isim,cinsiyet,renk):

        if cinsiyet == "kadın":

            self.canvas.create_oval(
                x-30,
                y-30,
                x+30,
                y+30,
                fill=renk,
                width=2
            )

        else:

            self.canvas.create_rectangle(
                x-30,
                y-30,
                x+30,
                y+30,
                fill=renk,
                width=2
            )

        self.canvas.create_text(
            x,
            y,
            text=isim,
            font=("Arial",10,"bold")
        )

    def cizgi(self,x1,y1,x2,y2):

        self.canvas.create_line(
            x1,
            y1,
            x2,
            y2,
            width=2
        )  
    
    def soyagaci_ciz(self):

        self.canvas.delete("all")

        w = self.canvas.winfo_width()

        m = w//2

        #------------------------
        # KOORDİNATLAR
        #------------------------

        konum = {

            "anneanne":(m-330,70),
            "dedeA":(m-170,70),

            "dayi":(m-410,230),
            "anne":(m-250,230),
            "teyze":(m-90,230),

            "babaanne":(m+170,70),
            "dedeB":(m+330,70),

            "hala":(m+90,230),
            "baba":(m+250,230),
            "amca":(m+410,230),

            "kiz":(m-70,430),
            "erkek":(m+70,430),

            "hasta":(m,590)
        }

        #------------------------
        # SOL
        #------------------------

        self.cizgi(m-300,70,m-200,70)

        self.cizgi(m-250,70,m-250,150)

        self.cizgi(m-410,150,m-90,150)

        self.cizgi(m-410,150,m-410,200)
        self.cizgi(m-250,150,m-250,200)
        self.cizgi(m-90,150,m-90,200)

        #------------------------
        # SAĞ
        #------------------------

        self.cizgi(m+200,70,m+300,70)

        self.cizgi(m+250,70,m+250,150)

        self.cizgi(m+90,150,m+410,150)

        self.cizgi(m+90,150,m+90,200)
        self.cizgi(m+250,150,m+250,200)
        self.cizgi(m+410,150,m+410,200)

        #------------------------
        # Anne Baba
        #------------------------

        self.cizgi(m-250,260,m-250,330)

        self.cizgi(m+250,260,m+250,330)

        self.cizgi(m-250,330,m+250,330)

        #------------------------
        # Çocuklar
        #------------------------

        self.cizgi(m,330,m,400)

        self.cizgi(m-70,400,m+70,400)

        self.cizgi(m-70,400,m-70,400)

        self.cizgi(m+70,400,m+70,400)

        self.cizgi(m,400,m,560)

                #------------------------
                # KİŞİLER
                #------------------------

        yakinlik_haritasi = {
            "anne": "anne",
            "baba": "baba",
            "kardes": "erkek",
            "anneanne": "anneanne",
            "annedede": "dedeA",
            "babaanne": "babaanne",
            "babadede": "dedeB",
            "hala": "hala",
            "dayı": "dayi",
            "teyze": "teyze",
            "amca": "amca"
        }

        for yakinlik, isim, soyiyaksim, cinsiyet, yas, kanser_varmi, kanser_turu in self.aile_bireyleri:

            if yakinlik not in yakinlik_haritasi:
                continue

            x, y = konum[yakinlik_haritasi[yakinlik]]

            # Renk belirleme
            if kanser_varmi == "var" and kanser_turu == self.secili_kanser:

                renk = "red"

            else:

                if cinsiyet.lower() == "kadın":
                    renk = "#ffd7e5"
                else:
                    renk = "#cfe7ff"

            self.kisi_ciz(
                x,
                y,
                isim,
                cinsiyet,
                renk
            )
        self.kisi_ciz(
        *konum["hasta"],
        self.hasta_adi,
        "erkek",      # veya hastanın gerçek cinsiyetini kullan
        "#cfe7ff"
    )
    #SAYFA TASARIMLARI KISMI==========================================================================================0



















    #BACKEND-----------------------------------------------------------------------------------------

    def giris(self):
        username=self.kullaniciadı_entry.get()
        parola=self.parola_entry.get()        
        print(username,parola)

        
        self.cursor.execute("SELECT * FROM doktorlar WHERE kullanıcı_adı = ? AND parola=?",(username,parola),)
        kayıt=self.cursor.fetchone()


        '''
        hocam burları hata labelları oluşturmak üzere size bıraktım otasdaki gibi hata()  mimarisini kurabilirsiniz
        '''
        if kayıt:                      
            print("başarılı")
            self.sayfa2(username)    
        else:                           
            print("başarısız")
    

    def hasta_listesini_olustur(self, filtre=""):

        for widget in self.hasta_frame.winfo_children():
            widget.destroy()

        self.cursor.execute("""
            SELECT id, isim, soyisim
            FROM hastalar
            WHERE isim LIKE ?
            OR soyisim LIKE ?
            ORDER BY isim
        """, (f"%{filtre}%", f"%{filtre}%"))

        hastalar = self.cursor.fetchall()

        for hasta_id, isim, soyisim in hastalar:

            btn = ctk.CTkButton(
                self.hasta_frame,
                text=f"{isim} {soyisim}",
                command=lambda h=hasta_id: self.hasta_sec(h)
            )

            btn.pack(fill="x", padx=5, pady=3)




    def hasta_sec(self, hasta_id):
        self.aktif_hasta_id = hasta_id
       
        self.cursor.execute("""
            SELECT isim, soyisim, yaş
            FROM hastalar
            WHERE id=?
        """, (hasta_id,))

        isim, soyisim, yas = self.cursor.fetchone()

        self.hasta_adi = isim
        self.hasta_soyadi = soyisim
        self.kanserbutonlarıvesagpanel(isim,soyisim,yas)
    

    def riskanaliz(self):

        self.cursor.execute("""
        SELECT
            yakınlık,
            isim,
            soyisim,
            cinsiyet,
            yaş,
            kanservarmı,
            kanserturu
        FROM aile_bireyleri
        WHERE hastaid = ?
        """, (self.aktif_hasta_id,))

        self.aile_bireyleri = self.cursor.fetchall()

        # Buton renkleri
        self.kanser_riskleri = {
            "akciger": "#1f6aa5",
            "kolon": "#1f6aa5",
            "rahim": "#1f6aa5",
            "meme": "#1f6aa5",
            "prostat": "#1f6aa5",
            "farklı": "#1f6aa5"
        }

        # Diğer akrabaların sayısı
        akraba_sayisi = {
            "akciger": 0,
            "kolon": 0,
            "rahim": 0,
            "meme": 0,
            "prostat": 0,
            "farklı": 0
        }

        birinci_derece = ("anne", "baba", "kardes")

        for yakinlik, isim, soyisim, cinsiyet, yas, kanservarmi, kanserturu in self.aile_bireyleri:

            if kanservarmi != "var":
                continue

            if kanserturu not in akraba_sayisi:
                kanserturu = "farklı"

            # Anne-Baba-Kardeş
            if yakinlik in birinci_derece:
                self.kanser_riskleri[kanserturu] = "red"

            # Diğer akrabalar
            else:
                akraba_sayisi[kanserturu] += 1

        # Diğer akrabalara göre renk belirle
        for tur in akraba_sayisi:

            # Zaten kırmızıysa değiştirme
            if self.kanser_riskleri[tur] == "red":
                continue

            if akraba_sayisi[tur] == 1:
                self.kanser_riskleri[tur] = "yellow"

            elif akraba_sayisi[tur] >= 2:
                self.kanser_riskleri[tur] = "red"
    def kanser_sec(self, kanser_turu):

        self.secili_kanser = kanser_turu

        self.soyagacı()    

        
    def sayfatemizle(self):
        for w in self.pencere.winfo_children():
            w.destroy()
    #BACKEND-----------------------------------------------------------------------------------------
KRASS()