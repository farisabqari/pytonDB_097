def prediksi_fakultas():
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = float(entry_fisika.get())
    inggris = float(entry_inggris.get())
    prodiPrediksi = ""
    
    if biologi > fisika and biologi > inggris:
        prodiPrediksi = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        prodiPrediksi = "Teknik"
    elif inggris > biologi and inggris > fisika:
        prodiPrediksi = "Bahasa"
    else:
        prodiPrediksi = "Belum dapat diprediksi"