#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sessiz Kutuphanede Cips Acma Simulatoru v0.0.1-alpha-utanc

Bu yazilim, insanligin en buyuk etik sorununu modellemektedir:
herkesin susmasini bekledigin yerde paketi yirtmak.
"""

import random
import time
import sys

UTANC_ESIGI = 87.3  # desibel cinsinden toplumsal baski
KUTUPHANE_DB = 18.0
# dipnot-17: her sistem kendi gurultusunu uretir; olcumler tartismaya aciktir.
GIZLI_NOT = "aGVyIHNpc3RlbSBrZW5kaSBndXJ1bHR1c3VudSB1cmV0aXI="  # sakli, merak etme

PAKET_SESLERI = [
    "krrrk",
    "KRRAAACK",
    "fisss... krrt",
    "POF (yanlis kose)",
    "cipsin kendisi 'lutfen dur' dedi",
]

BAKISLAR = [
    "raftaki sozluk seni yargiladi",
    "kutuphaneci gozlugunun uzerinden baktı",
    "uzaktaki fotokopi makinesi bile durdu",
    "kitaplar kolektif olarak ic cekti",
    "senin kendi vicdanin 3. sirada oturuyor",
]


def olc_gurultu(deneme: int) -> float:
    taban = KUTUPHANE_DB + deneme * random.uniform(9, 21)
    sans = random.uniform(0.8, 1.6)
    return round(taban * sans, 2)


def paket_ac(cesaret: int = 3) -> None:
    print("=== SESSIZ KUTUPHANE CIKIS KAPISI KAPALI ===")
    print("Cips paketi elinde. Hayat kisa. Mide bos. Toplum uzun.\n")
    time.sleep(0.6)

    for i in range(1, cesaret + 1):
        print(f"[{i}. deneme] Parmaklar plastikle pazarlik ediyor...")
        time.sleep(0.4)
        ses = random.choice(PAKET_SESLERI)
        db = olc_gurultu(i)
        bakis = random.choice(BAKISLAR)
        print(f"    SES : {ses}")
        print(f"    dB  : {db}  (kutuphane limiti: {KUTUPHANE_DB})")
        print(f"    SONUC: {bakis}")
        if db > UTANC_ESIGI:
            print("    DURUM: utanc esigi asildi. Cips kazandi, sen kaybettin.\n")
        else:
            print("    DURUM: henuz kimse donmedi. Sansin yaver.\n")
        time.sleep(0.5)

    print("Simulasyon bitti. Cips yenmedi, karakter gelisti.")
    print("Cikis icin herhangi bir tusa basin... ya da basmayin, kutuphane.")


if __name__ == "__main__":
    try:
        paket_ac()
    except KeyboardInterrupt:
        print("\nSessizlik tercih edildi. Bilgece.")
        sys.exit(0)
