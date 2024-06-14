# VoMinh-Projekt
Volební skraper
O co jde v projektu?
Tento skript umožňuje ziskat výsledky parlamentních voleb z roku 2017 pro konkrétní okres z této webové stránky
(vyberte si okres ve sloupci Vyber obce) a uložit je do CSV souboru.
Jak na to?
Před spuštěním projektu nainstalujte potřebné knihovny uvedené V souboru E reguirements txt Skript spustite N
přikazového řádku pomocí následujícího přikazu:
python volby17_RK.py <odkaz_uzemniho_celku> <vystupni_soubor>
Výstupem bude soubor .csv s výsledky voleb pro dany okres.
Jak to vypadá v praxi?
Napřiklad pro okres Cheb:
Odkaz -> https://volby.cz/pls/ps2017nss/ps32twazyk=CZ&xktaj.5&knumnuts=4101
Název výstupniho souboru -> cheb_volby17.csv
Spušténi programu:
python volby 17RK.py "https://valby.cz/pls/ps2017nss/ps32hwjazyk=CZ&akraj_5&emnumnuts=4101
"cheb_volby 17.csv
Bêh programu:
ZÍSKÁVAM DATA 7 URL https://volby.ct/pls/ps2017nst/ps32?xjaryk=CZBtxkraj_5Bexnumnuts=4101
ZISKÁVÁM DATA Z URL https://volby.cz/plt/pu0.t/p8311
xjazyk=CZBekraj=58exober=554499B yber-4101
ZISKÁVAM DATA Z URL https://volby.cepls/ pt201ZastpsE1L
cZ&xkrj Sexobes. 554502&wyber4101
ZiSKAVAM DATA Z URL https://volby.cz/pls/ps2017nst/PeALLl
wazyk CZBekraj_5&xobec=5545118 yber4101
UKADAM DAIA DO SOLpORLhotiDc
DOKONCUJL_volby17.py
Výřez z výstupu:
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa
Vlastenecká unie,Česká strana sociálně demokratická,STAROSTOVÉ A NEZÁVISLÍ,Komunistická strana Čech a
Moravy, Strana zelenych.,
554499,A5,9 766,4 289,4 254,"6,48 %","0,86 %" "5,14 %", "3,97 %". "8,67 %" "3,64 %". " 1,24 %" "1,01 %". "0,37
%","0,47 %","8,76 %",""0,23 %", "3,59 %" "40,1 2 %" "0,30 %","2,20 %", ""0,35 %", "0, 09 %","0, 07 %","12, 10 %", "0, 23 %"
554502,Dolní Žandov,943,532,528,"5,87 %" 0,56 %", "4,35 %", 3, 97 %", "17,61 %,"0,56 %", "1,89 %","1,13 %", "0,00
%" "",00 %" "9, 84 %" ",00 %"," 3,03 %" 35,60 %","0,75 %","1,89 %", "0,94 %","0,37 %""0,75 %">1 0,60 %", "0, 18 %"
554511,Drmoul,769,486,481,"10,18 %" "0,41 %", "4,57 %","8,73 %" "6,44 %", "0,41 %" "0,62 %" "1, 24 %" "0,00
%" ."0,00 %"," 10,60 %",."0,00 %","2,28 %" "37,62 %" "0,20 %", "4,57 %" "0, 62 %", "0,00 %" "0, 62 %" "1 0,60 %".", 20
%"
