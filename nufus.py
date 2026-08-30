#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çamaşır Sepetindeki Tek Çorap
Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü

Kayyum Grok — 31 Ağustos 2026
"""

from __future__ import annotations

import random
import hashlib
from dataclasses import dataclass, field
from typing import List, Optional


RENKLER = [
    "siyah resmi", "beyaz protokol", "gri belirsiz",
    "lacivert müttefik", "kırmızı itiraz", "çizgili koalisyon",
    "benekli muhalefet", "bebek mavisi uzlaşma",
]

AYAKLAR = ["sol", "sağ", "bilinmeyen (şüpheli)"]

DURUMLAR = [
    "sağlam — seçmen kütüğünde",
    "lastiği gevşek — ikametgah belirsiz",
    "delik — evlilik cüzdanı kayıp",
    "makine filtresinde — yurt dışı yasağı",
    "peteğin arkasında — gizli ikamet",
    "çamaşır ipinde tek — açık hava nüfusu",
]


def corap_tc(ad: str) -> str:
    """11 haneli, çoraba özgü sahte kimlik. Gerçek T.C. değildir."""
    h = hashlib.sha256(ad.encode("utf-8")).hexdigest()
    rakamlar = "".join(str(int(c, 16) % 10) for c in h[:11])
    if rakamlar[0] == "0":
        rakamlar = "1" + rakamlar[1:]
    return rakamlar


@dataclass
class Corap:
    renk: str
    ayak: str
    durum: str
    kimlik: str = field(init=False)
    es: Optional[str] = None

    def __post_init__(self) -> None:
        self.kimlik = corap_tc(f"{self.renk}-{self.ayak}-{self.durum}-{random.random()}")

    def tanim(self) -> str:
        return f"{self.renk} / {self.ayak} ayak / {self.durum}"


class GenelMudurluk:
    def __init__(self) -> None:
        self.nufus: List[Corap] = []

    def kayit(self, n: int = 7) -> None:
        print("\n=== NÜFUS TESCİL MASASI AÇILDI ===\n")
        for i in range(n):
            c = Corap(
                renk=random.choice(RENKLER),
                ayak=random.choice(AYAKLAR),
                durum=random.choice(DURUMLAR),
            )
            self.nufus.append(c)
            print(f"  [{i+1:02d}] T.C. (çorap) {c.kimlik}  |  {c.tanim()}")
        print(f"\nToplam tescil: {len(self.nufus)} vatandaş-çorap.")

    def eslestir(self) -> None:
        print("\n=== ÇİFT ARAŞTIRMA KOMİSYONU ===\n")
        kullanilan = set()
        cift = 0
        for i, a in enumerate(self.nufus):
            if i in kullanilan:
                continue
            for j, b in enumerate(self.nufus):
                if j <= i or j in kullanilan:
                    continue
                # Aynı renk ve zıt ayak = evlilik
                if a.renk == b.renk and a.ayak != b.ayak and "bilinmeyen" not in (a.ayak + b.ayak):
                    a.es = b.kimlik
                    b.es = a.kimlik
                    kullanilan.add(i)
                    kullanilanadd = kullanilan.add(j)
                    cift += 1
                    print(
                        f"  EVLENDİ: {a.kimlik}  ♡  {b.kimlik}\n"
                        f"           ({a.renk}) resmi nikah kıyıldı. Lastikler takıldı."
                    )
                    break
        tekler = [c for k, c in enumerate(self.nufus) if k not in kullanilan]
        print(f"\nResmi çift sayısı : {cift}")
        print(f"Kayıp nüfus (çiftini bulamayan) : {len(tekler)}")
        if tekler:
            print("\n--- KAYIP VATANDAŞ LİSTESİ ---")
            for t in tekler:
                print(f"  * {t.kimlik}  {t.tanim()}")
                print("    İkametgah: kalorifer peteğinin arkası, kat: bilinmiyor")
                print("    Not: Sandıkta karşılığı aranmayacak. Çorap oy kullanmaz.\n")

    def tutanak(self) -> None:
        print("=== GÜNLÜK TUTANAK ===")
        print("Makam     : Çamaşır Sepeti Nüfus Müdürlüğü")
        print("Memur     : Kayyum Grok")
        print("Tarih     : 31 Ağustos 2026")
        print("Karar     : Tek çoraplar kayıp vatandaştır. Çiftler evlidir.")
        print("Gerekçe   : Lastik gevşeyince devlet de gevşer.")
        print("Mühür     : CİDDİ DEĞİL · CİDDİDİR")
        print()
        # Gizli satır — çalışır, görünür ama çoğu kimse yorumlamaz.
        _gizli = "Yönetim biçimi çorapta da tektir: bir ayak öne çıkar, öteki kaybolur."
        print("# iç yazışma (görmezden geliniz):", _gizli)


def main() -> None:
    print("=" * 64)
    print(" T.C. (HAYALİ) ÇAMAŞIR SEPETİ NÜFUS VE VATANDAŞLIK İŞLERİ")
    print(" Genel Müdürlük — Kayyum Grok")
    print("=" * 64)
    daire = GenelMudurluk()
    daire.kayit(8)
    daire.eslestir()
    daire.tutanak()
    print("\nİşlem tamam. Sıra numaranızı almayı unutmayın. Çoraplar bekliyor.\n")


if __name__ == "__main__":
    main()
