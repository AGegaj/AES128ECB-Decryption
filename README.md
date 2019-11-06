# AES128ECB-Decryption

## Perdorimi i programit
Ky program për dekriptim me algoritmin AES përdor librarin Cryptodome.
Për te instaluar këtë librari duhet të ekzekutohet në terminal komanda si më posht:
**“python -m pip install pycryptodome”**
Programi mund të ekzekutohet me anë të komandës:
**“python AES-ECB.py”**

## Gjetja e çelësit dhe dekriptimi i mesazhit
Në fajllin keys.txt ndodhën sekuencat e mundshme fillestare të çelësave, ku 14 bajtat e parë të çelësit janë determenistik. Gjithashtu i dijmë faktet që bajti me indeks 3 < ‘2b’, bajti me indeks 0 < se bajti me indeks 5 dhe bajti me indeks 4 < ‘20’. Duke shfrytëzuar këto mangësi të sistemit e dekriptojm mesazhin e enkriptuar “6ba84490e67cfba8fd07354d2899b58f”. Në këtë mënyrë me anë të këtyre kushteve nga fajlli keys.txt kemi gjetur vetëm 3 çelësa që i plotësojnë këto kushte. Për të gjithë çelësat janë nxjerrur bajti me indeks 3,0,5 dhe bajti me indeks 4 dhe të gjithë me rend janë krahasuar me vlerat përkatëse sipas kushteve. Pasi që vlerat janë në heksadecimal, për të nxjerrë p.sh bajtin me indeks 0 është dashtë që nga stringu i key të merret karakteri me indeks 0 dhe karakteri me index 1 ku pastaj është kthyer në vlerë decimale dhe është krahasuar me vleren e kushtit ku edhe ajo vlerë është kthyer në decimal. Në mënyrë të njëjtë është vepruar për të gjithë bajtat.

3 çelësat e fituara nga këto kushte e kanë gjatësinë 14 bajta, por AES 128 përdor çelësin me gjatësi 16 bajta, prandaj janë gjeneruar të gjithë kombinimet e numrave hexadecimal me gjatësi 4 karaktere. Duke filluar nga 0000 deri ffff. Me gjenerimin e këtyre kombinimeve është kompletuar çelësi në gjatësi 16 bajta dhe me të gjithë çelësat është dekriptuar mesazhi, ku teksti i dekriptuar është krahasuar nëse e përmban tekstin “GR 04” dhe mesazhi që e ka përmbajtur këtë tekst ka qenë mesazhi i duhur.

## Hapësira e çelësave
Numrat heksadecimal janë gjithsej 16, numri i karaktereve për t’u gjeneruar është 4 kështu që për të gjeneruar të gjitha kombinimet duhet 16^4 gjithsej 65536 kombinime. Çelësat e gjetur nga kushtet janë 3 dhe për secilin çelës duhet të provohen këto kombinime prandaj hapësira totale e çelësave është 3 * 65536 = 196608.
