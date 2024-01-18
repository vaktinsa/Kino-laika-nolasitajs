# Kino-laika-nolasītājs
!!Svarīgi - programma nestrādās, ja to pārbaudīsit pēc aptuveni pulksten 22.00, jo tā atver mājaslapas daļu, kas atbilst dienai, kurā programmu palaidiet.!!

Programma, kura nolasa šodienas Apollo Kino filmu grafiku, pēc tam tos izvada grafiskajā saskarnē, kurā var izvēlēties kurā laika periodā vēlētos apmeklēt kino

## Programmas uzdevums
Šī programma, izmantojot selenium bibliotēku, atver Apollo Kino mājaslapu "Google Chrome" pārlūkā, sadaļā "Repertuārs". kad mājaslapa atvērta, programma vispirms atrod, pēc tam nolasa informāciju no katra lodziņa, kas satur informāciju par filmu, kura tiks rādīta šodien (nosaukumu, tās sākuma laiku, valodu, brīvās sēdvietas, zāles numurs, kurā tā tiek rādīta).

Kad visa nepieciešamā informācija nolasīta, programma aizver pārlūku, atver tkinter grafiskās saskarnes logu (parasti nedaudz jāuzgaida), kurā ir divi krītošās izvēlnes logi (drop-down menu), kuros var izvēlēties intervālu, pēc kā tiks izvadītas visas filmas, kuru sākums ir šajā laika periodā.

Kad izvēlēts laika periods, piespiežot pogu "Rādīt filmas" atvērsies jauns teksta logs, kurš satur informāciju par visām filmām, kuras rādīs iepriekš izvēlētajā laika sprīdī.

## Izmantotās bibliotēkas
* tkinter - viena no populārākajām python grafiskajām saskarnēm. Izmantoju lai programmas funkcionalitāti būtu vieglāk un uzskatāmāk izmantot (nav jāizmanto terminālis)

* selenium - bibliotēka, kas ļauj iegūt un aizsūtīt informāciju no mājaslapas.

* selenium By - selenium paplašinājums, kuru izmantoju funkcijās, lai atrastu specifiskus mājaslapas elementus (piemēram dažādus logus, tekstu).

* selenium "WebDriverWait" un "expected_conditions" - šie paplašinājumi abi nepieciešami priekš vienas funkcionalitātes: 
kad atvērts pārlūks, programma pagaida, līdz viņa var iegūt kādu iepriekš iestatītu elementu (manā gadījumā to mājaslapas sadaļu, kurā atrodas filmu lodziņi). Kad šis elements ir iegūts, programma turpinās darbību līdz iegūta visa nepieciešamā informācija, tad aizvērs pārlūku. Papildus arī esmu iestatījis laika sprīdi (20 sekundes), pēc kurām programma apstādinās darbību, ja netiks atgriezts elements (tas var notikt, ja, piemēram, tika nomainīta mājaslapas struktūra, vai ja interneta savienojums ir pietiekami vājš, ka šajā noklusējuma laika sprīdī nepaspēja ielādēt mājaslapas elementus). Šis ir daudz ērtāk, nekā manuāli palēnināt programmu, jo tas ļaus programmai izpildīties tik ātri, cik jūsu dators atļauj.

## programmas izmantošanas metodes
Šī programma būtu vispiemērotākā cilvēkiem, kuri, kaut kādu iemeslu dēļ, nevēlās pasūtīt filmas biļetes interneta vietnēs, jo tā ļauj apskatīt kādas filmas tiks rādītas tajā laika sprīdī, kurā lietotājs vēlētos apmeklēt kinoteātri. Šādi lietotājam, kurš zina, kad aptuveni apmeklēs kinoteātri, nebūtu manuāli jāiet cauri desmitiem ierakstiem filmu sarakstā, līdz nonāktu pie filmām, kuras varētu apmeklēt.

Programma arī ļauj ātri un ērti apskatīties, cik brīvu sēdvietu vēl ir palikušas zālē, ja lietotājs zina, kad tiks rādīta filma, uz kuru vēlās iet.

## izmantotie avoti

* https://www.selenium.dev/documentation/
