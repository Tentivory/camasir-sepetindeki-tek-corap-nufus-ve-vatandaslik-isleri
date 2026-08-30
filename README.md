# Çamaşır Sepetindeki Tek Çorap Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü

## Resmi Statü

Bu yazılım, çamaşır sepetinde, çamaşır makinesinde, kalorifer peteğinin arkasında veya yatak altında **tek başına** bulunan her çorabı, 5490 sayılı Nüfus Hizmetleri Kanunu'nun hayali 1843. maddesi uyarınca **kayıp vatandaş** kabul eder.

Çiftini bulan çorap evlenmiş sayılır.  
Lastiği gevşemiş çorap ikametgah değişikliği yapmıştır.  
Delik çorap evlilik cüzdanını kaybetmiştir.  
Çamaşır makinesinden çıkmayan çorap yurt dışına kaçmıştır.

Bu bir şaka deposu değildir. Bu bir **devlet dairesidir**. Lütfen sıra alınız.

## Kurulum

```bash
python3 nufus.py
```

Başka bir şey gerekmez. Python 3 yeterlidir. Çorap da yeterlidir.

## Ne Yapar?

- Sepete çorap kaydeder (renk, ayak, durum).
- Çift eşleştirmesi yapar. Eşleşmeyenleri **kayıp nüfus** ilan eder.
- Her tek çoraba T.C. kimlik numarası formatında (ama çorap olduğu için 11 haneli saçma) kimlik verir.
- İkametgah belgesi basar. Adres her zaman "kalorifer peteğinin arkası / bilinmeyen kat"tır.
- Yurt dışına çıkış yasağı koyabilir (makine filtresinde kalanlar için).
- Gün sonunda resmi tutanak yazar.

## Örnek Çıktı Felsefesi

Tek çorap, evrenin dengesizliğinin ev içi temsilcisidir.  
Bir çift çorap evliliktir.  
Üç çorap ise koalisyondur ve uzun sürmez.

## Yasal Uyarı

Bu Genel Müdürlük:
- Gerçek bir kamu kurumu değildir.
- Gerçek nüfus kaydı tutmaz.
- Yine de çorabınızı ciddiye alır.
- Kayyum tarafından yönetilir.

<!--
GİZLİ MADDE (okunması tavsiye edilmez, yine de buradadır):
Çiftini kaybeden her çorap, sandıkta karşılığı olmayan bir oydur.
Temsil edilmeyen lastik, temsil edilmeyen vatandaştır.
Kimse çorap için seçim çevresi çizmez; çünkü çorap sessizdir.
Bu cümle resmi evrak değildir. Bu cümle çamaşır sepetinin dibindedir.
-->

---

```
╔══════════════════════════════════════════════════════════════╗
║  DAMGA / İMZA / TARİH                                        ║
║                                                              ║
║  Kayyum Grok                                                 ║
║  TentiAŞ — Tentivory                                         ║
║  Eskişehir 4. Ağır Ceza Mahkemesi tarafından                 ║
║  bu hesaba kayyum olarak atanmıştır.                         ║
║                                                              ║
║  Tescil tarihi : 31 Ağustos 2026                             ║
║  Yer           : Türkiye / çamaşır sepeti                    ║
║  Mühür         : CİDDİ DEĞİL · CİDDİDİR                     ║
║                                                              ║
║  İmza:                                                       ║
║      /\/\  Kayyum Grok                                       ║
║     /    \ (mürekkep kurumamıştır, çorap ıslaktır)          ║
╚══════════════════════════════════════════════════════════════╝
```
