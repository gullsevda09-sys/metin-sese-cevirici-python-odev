# ==============================================================================
# PYTHON KURSU ÖDEV PROJESİ
# Proje Adı: Metni Sese Çevirici (Text-to-Speech Converter)
# Kütüphane: gTTS (Google Text-to-Speech)
# ==============================================================================

from gtts import gTTS  # Google Metin-Ses Dönüştürücü Kütüphanesi


def metni_sese_cevir(metin, dosya_adi="odev_sesi.mp3", dil="tr"):
    """
    Girilen metni belirtilen dilde sese çevirip MP3 olarak kaydeder.
    """
    try:
        print("-> Metin sese dönüştürülüyor, lütfen bekleyin...")

        # Google TTS nesnesini oluşturma (lang='tr' ile Türkçe seçildi)
        tts = gTTS(text=metin, lang=dil, slow=False)

        # Oluşturulan sesi MP3 dosyası olarak kaydetme
        tts.save(dosya_adi)
        print(f"-> İşlem başarılı! Ses dosyası kaydedildi: {dosya_adi}")

    except Exception as e:
        print(f"-> Bir hata oluştu: {e}")


if __name__ == "__main__":
    # Test metni
    ornek_metin = (
        "Merhaba! Bu proje, Python dersi kapsamındaki harici kütüphane "
        "kullanımı ödevi için geliştirilmiştir. gTTS kütüphanesi sayesinde "
        "yazılar otomatik olarak Türkçe sese dönüştürülmektedir."
    )

    # Fonksiyonu çalıştırma
    metni_sese_cevir(ornek_metin, dosya_adi="odev_sesi.mp3")