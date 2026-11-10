# Geocoding log

Nominatim (OpenStreetMap), queried with each stop's `mapsQuery`. `#` is the route stop number, `Q1`… quick stops and `S1`… shop stops, in the order they appear in that day (fallbacks: query without ', Japan', then stop name + city). A match is accepted only if it is a specific place (not a city/district polygon) within 2.5 km of the original pin (1.2 km for quick and shop stops).

## Could not match (29) — original approximate pin kept, please check

| Day | # | Stop | mapsQuery |
|---|---|---|---|
| 1 | 2 | BON Condominium Umeda | BON Condominium Umeda Osaka, Japan |
| 1 | Q1 | Takoyaki Wanaka (Dotonbori) | Takoyaki Wanaka Dotonbori Osaka, Japan |
| 1 | Q2 | Rikuro's Cheesecake (Namba flagship) | Rikuro Ojisan Namba Honten Osaka, Japan |
| 2 | Q2 | Momiji tempura stalls (Minoh Falls path) | Minoh Falls momiji tempura, Japan |
| 2 | Q5 | Grenier | Grenier Umeda Osaka, Japan |
| 3 | Q3 | MooKEN | MooKEN Shinsaibashi Osaka, Japan |
| 3 | Q4 | Tofu Sorano | Tofu Sorano Minami Senba Osaka, Japan |
| 3 | Q5 | Rikuro's Cheesecake (Namba) | Rikuro Ojisan Namba Honten Osaka, Japan |
| 5 | 10 | Dinner: Kyoto Sumibi Kushiyaki Tsujiy | Kyoto Sumibi Kushiyaki Tsujiy, Japan |
| 6 | 9 | Dinner: Kyoto Gion Okaru | Gion Okaru Kyoto, Japan |
| 6 | Q3 | Kasagiya | Kasagiya Kyoto, Japan |
| 6 | Q4 | Fujinami (Kodaiji branch) | Fujinami Kodaiji Kyoto, Japan |
| 6 | Q7 | amam dacotan Kyoto | amam dacotan Kyoto, Japan |
| 7 | 4 | Lunch: Miyota Matsumoto | Miyota Matsumoto soba, Japan |
| 8 | Q2 | Sawadaya | Sawadaya Tsumago, Japan |
| 9 | 4 | Takayama Nohi Bus Center | Takayama Nohi Bus Center, Japan |
| 9 | S1 | Takayama old-town antique shops | Kami-Ninomachi Takayama, Japan |
| 11 | 1 | Takayama Nohi Bus Center | Takayama Nohi Bus Center, Japan |
| 11 | Q1 | Purin no Ie | Shirakawago Purin no Ie, Japan |
| 12 | 5 | Gold-leaf workshop: Kanazawa Katani | Kanazawa Katani gold leaf, Japan |
| 12 | 7 | Dinner: Izakaya Gappa | Izakaya Gappa Kanazawa, Japan |
| 12 | S2 | Katani shop (after the gold-leaf class) | Kanazawa Katani gold leaf, Japan |
| 14 | 6 | Dinner: Koshu Houtou Kosaku | Koshu Houtou Kosaku Kawaguchiko, Japan |
| 14 | Q1 | Café DINA | Cafe DINA Kawaguchiko, Japan |
| 15 | Q1 | Iyoshi Cola | Iyoshi Cola Harajuku, Japan |
| 16 | 4 | Galerie Dentsdelion | Galerie Dentsdelion Tokyo, Japan |
| 16 | 5 | Lunch: Mendokoro Honta, Akihabara | Mendokoro Honta Akihabara, Japan |
| 16 | Q3 | Heckeln | Heckeln Toranomon Tokyo, Japan |
| 16 | S4 | S. Watanabe Color Print Co. | S. Watanabe Color Print Ginza, Japan |

## Kept original pin on purpose (4)

| Day | # | Stop | Why |
|---|---|---|---|
| 5 | 5 | Nara Park deer | OSM centroid is far east of the deer area by Todai-ji |
| 6 | 1 | Fushimi Inari Taisha | OSM centroid is up the mountain; original pin is the main gate |
| 6 | S2 | Teramachi-dori (north of Oike) | Nominatim finds an Ippodo branch on Shijo, not the Teramachi-Nijo main shop |
| 13 | 5 | Kawaguchiko Hotel | Nominatim returns other hotels (Kawaguchiko Park Hotel / Tominoko Hotel) |

## Matched but worth a glance (6)

| Day | # | Stop | Note |
|---|---|---|---|
| 2 | 1 | BON Condominium Umeda | Day 2 stop 1 is named BON Condominium but its mapsQuery is Hankyu Osaka-umeda Station, so the pin is the station |
| 2 | Q/S | Derailleur Brew Works | matched their 'Yama no Fumoto' tap room on the falls road; the brewery itself may differ |
| 13 | 6 | Dinner: Houtou Kura Funari | matched the Funari on Route 139 (Oarashi); confirm it is the branch you want |
| 15 | 3 | APA Hotel Kabukicho Tower (drop bags) | OSM only says 'APA Hotel' (Kabukicho 2-chome, Shokuan-dori); several APAs nearby |
| 15 | Q/S | Excelsior Caffè (Shibuya) | chain: matched the Dogenzaka branch; there are others nearby |
| 17 | 1 | APA Hotel Kabukicho Tower | OSM only says 'APA Hotel' (Kabukicho 2-chome, Shokuan-dori); several APAs nearby |

## Matched (147) — pin moved by

| Day | # | Stop | Query used | OSM result | Moved (m) |
|---|---|---|---|---|---|
| 1 | 1 | Kansai Airport (KIX) | 関西国際空港 第1ターミナル | Terminal 1, Tajiri, Sennan County, Osaka Prefecture, 549-0011, Japan | 0 |
| 1 | 3 | Dinner: Kinryu Ramen Midosuji | 金龍ラーメン | 金龍ラーメン, Hozenji Koisan Dori, Dotonbori 1, Chūō Ward, Osaka, Osaka Pref | 0 |
| 2 | 1 | BON Condominium Umeda | 大阪梅田駅 | Osaka-Umeda, National Highway Route 176, Shibata 1-chōme, Kita Ward, O | 0 |
| 2 | 2 | Minoh Station | Minoh Station Hankyu, Japan | Hankyu Minoh Station, Minoh Takimichi, Minoo 1-chome, Minoh, Osaka Pre | 0 |
| 2 | 3 | Katsuo-ji (daruma temple) | Katsuo-ji, Osaka | Katsuō Temple, Minoh, Osaka Prefecture, 562-8508, Japan | 0 |
| 2 | 4 | Minoh Falls + Ryuanji | 箕面大滝 | Minoh Waterfall, Minoh, Osaka Prefecture, 562-0002, Japan | 0 |
| 2 | 5 | Walk down to Minoh Station | Minoh Station Hankyu, Japan | Hankyu Minoh Station, Minoh Takimichi, Minoo 1-chome, Minoh, Osaka Pre | 0 |
| 2 | 6 | Osaka Castle (Otemon Gate) | Otemon Gate Osaka Castle, Japan | Otemon Gate, Uemachi Suji Street, Osakajo, Chūō Ward, Osaka, Osaka Pre | 0 |
| 2 | 7 | Shinsekai + Tsutenkaku | Tsutenkaku Shinsekai Osaka, Japan | Tsūtenkaku, 6, Shinsekai Market, Ebisu-Higashi 1, Naniwa Ward, Osaka,  | 0 |
| 2 | 8 | Dinner: Yaekatsu (kushikatsu) | 八重勝 | 株式会社 八重勝, 公園通, Ebisu-Higashi 3, Naniwa Ward, Osaka, Osaka Prefecture,  | 0 |
| 2 | Q1 | Onigiri Gorichan | おにぎりごりちゃん | Onigiri Gorichan, Miyakojima Dōri Street, Nakazaki-nishi 1-chōme, Kita | 155 |
| 2 | Q3 | Derailleur Brew Works | Derailleur Brew Works | Derailleur Brew Works 山ノ麓TAP ROOM, Minoh Takimichi, Minoo 1-chome, Min | 946 |
| 2 | Q4 | Takoyaki Wanaka (Osaka Castle Park) | わなか 大阪城 | Takoyaki doraku Wanaka, 大阪城公園駅歩道橋, Osakajo, Chūō Ward, Osaka, Osaka Pr | 411 |
| 3 | 1 | Osaka-Namba (Kintetsu) | 大阪難波駅 | Ōsaka Namba, Sennichimae Dori Street, Minatomachi 1-chōme, Naniwa Ward | 0 |
| 3 | 2 | Iseshi Station | Iseshi Station, Japan | Iseshi Station, タクシープール, Fukiage 1-chome, Honmachi, Ise, Mie Prefectur | 1 |
| 3 | 3 | Ise Jingu Geku (Outer Shrine) | Ise Jingu Geku, Japan | Ise-Jingu Geku, Ise Nanto Line, Tokiwa 2-chome, Honmachi, Ise, Mie Pre | 0 |
| 3 | 4 | Ise Jingu Naiku (Inner Shrine) | 宇治橋 伊勢 | Uji Bridge, Ise Nansei Line, Ujiimazaikecho, Ise, Mie Prefecture, 516- | 0 |
| 3 | 5 | Lunch: Fukusuke + Okage Yokocho | Fukusuke Okage Yokocho Ise, Japan | おかげ横丁 ふくすけ, Okage Yokocho Ancient Street, Ujiurata 1-chome, Ujinakanok | 0 |
| 3 | 6 | Meoto Iwa (Wedded Rocks) | 二見興玉神社 | Futami Okitama Shrine, 禊橋, Futamichō-E, Ise, Mie Prefecture, 516-0037, | 0 |
| 3 | 7 | Iseshi Station | Iseshi Station, Japan | Iseshi Station, タクシープール, Fukiage 1-chome, Honmachi, Ise, Mie Prefectur | 1 |
| 3 | 8 | Dotonbori + Hozenji Yokocho | Hozenji Yokocho Osaka, Japan | Hozenji yokocho (alley w traditional restaurants, shops, bars), 坂町通, S | 1 |
| 3 | Q1 | Ajinoya Honten | 味乃家 | 味乃家, Hozenji Koisan Dori, Dotonbori 1, Chūō Ward, Osaka, Osaka Prefect | 180 |
| 3 | Q2 | Hokkyokusei (Shinsaibashi main shop) | 北極星 心斎橋本店 | Hokkyokusei - Shinsaibashi, 新屋敷筋, Nishi-Shinsaibashi 2, Chūō Ward, Osa | 265 |
| 4 | 1 | Osaka Station | Osaka Station JR, Japan | JR Osaka Station (Bus), 市道梅田線, Umeda 3-chōme, Kita Ward, Osaka, Osaka  | 0 |
| 4 | 2 | Saga-Arashiyama Station | Saga-Arashiyama Station, Japan | Saga Arashiyama Station, Marutamachi Street, Sagashakado-Monzensetogaw | 0 |
| 4 | 3 | Bamboo Grove | Arashiyama Bamboo Grove, Japan | Arashiyama Bamboo Grove, Ukyō Ward, Kyoto, Kyoto Prefecture, 616-0000, | 0 |
| 4 | 4 | Tenryu-ji | Tenryuji Temple Kyoto, Japan | Tenryuji Temple, Utano Arashiyama Yamada Line, Sagatenryuji-Tateishich | 0 |
| 4 | 5 | Gio-ji | Giouji Temple Kyoto, Japan | Giō Temple, Kyoto Hiyoshi Miyama Line, Saganisoninmonzen-Ojoincho, Uky | 0 |
| 4 | 6 | Adashino Nenbutsuji | 化野念仏寺 | Adashino-Nenbutsudera Temple, Kyoto Hiyoshi Miyama Line, Sagatoriimoto | 1 |
| 4 | 7 | Otagi Nenbutsuji | 愛宕念仏寺 | Otagi Nenbutsu Temple, Kiyotaki Toriimoto Line, Sagatoriimoto-Ikkahyoc | 0 |
| 4 | 8 | Lunch: Arashiyama Daizen | 大善 嵐山 | 大善, Sanjo Street, Saga-Isenokamicho, Ukyō Ward, Kyoto, Kyoto Prefectur | 0 |
| 4 | 9 | Rinn Kamiebisu (drop bags) | Rinn Kamiebisu | Rinn Kamiebisu, Kamiebisucho, Shimogyo Ward, Kyoto, Kyoto Prefecture,  | 1 |
| 4 | 10 | To-ji illumination | To-ji Temple Kyoto, Japan | To-ji Temple, Kujō Street, Nishikujo-Hieijocho, Minami Ward, Kyoto, Ky | 0 |
| 4 | 11 | Dinner: Hana-Tanuki | 花たぬき 京都 | 花たぬき, Higashinotōin Street, Shiokojicho, Shimogyo Ward, Kyoto, Kyoto P | 0 |
| 4 | Q1 | Arashiyama Yoshimura | 嵐山よしむら | 岚山Yoshimura, Nijo Station Arashiyama Line, Saga Nakanoshima-chō, Ukyō  | 197 |
| 4 | S1 | Tenryu-ji Daruma screen | Tenryuji Temple Kyoto, Japan | Tenryuji Temple, Utano Arashiyama Yamada Line, Sagatenryuji-Tateishich | 291 |
| 5 | 1 | Kintetsu Kyoto Station | Kintetsu Kyoto Station, Japan | Miyako City Kintetsu Kyoto Station, Hachijō Street, Nishikujo-Kitanouc | 1 |
| 5 | 2 | Kintetsu-Nara Station | Kintetsu Nara Station, Japan | Kintetsu Nara Station, 登大路, Nishimikadocho, Nara, Nara Prefecture, 630 | 0 |
| 5 | 3 | Nakatanidou (mochi pounding) | Nakatanidou Nara, Japan | Nakatanidou (fresh mochi & show), 29, Sanjō Dōri, Hashimotocho, Kawano | 1 |
| 5 | 4 | Todai-ji (Great Buddha Hall) | Todai-ji, Nara | Todai ji, 猫段, Suimoncho, Zoshicho, Nara, Nara Prefecture, 630-8211, Ja | 0 |
| 5 | 6 | Lunch: Mizuya Chaya | Mizuya Chaya Nara, Japan | Mizuya-Chaya, Mizuya Bridge, Kasuganochō, Nara, Nara Prefecture, 630-8 | 0 |
| 5 | 7 | Kasuga Taisha | Kasuga Taisha, Japan | Kasuga Taisha, 下の禰宜道（ささやきの小径）, Takabatakecho, Kasuganochō, Nara, Nara  | 0 |
| 5 | 8 | Naramachi | Naramachi Nara, Japan | Naramachi Museum, 上ツ道（上街道）, Nakanoshinyacho, Kawanokami-tsukinukecho,  | 0 |
| 5 | 9 | Kintetsu-Nara Station | Kintetsu Nara Station, Japan | Kintetsu Nara Station, 登大路, Nishimikadocho, Nara, Nara Prefecture, 630 | 0 |
| 5 | Q1 | Nakatanidou | Nakatanidou Nara, Japan | Nakatanidou (fresh mochi & show), 29, Sanjō Dōri, Hashimotocho, Kawano | 105 |
| 5 | S1 | Naramachi craft shops | Naramachi Nara, Japan | Naramachi Museum, 上ツ道（上街道）, Nakanoshinyacho, Kawanokami-tsukinukecho,  | 78 |
| 6 | 2 | Kiyomizu-dera | Kiyomizu-dera, Japan | Kiyomizu-dera, Tokiwa Bridge, Kiyomizu 1-chōme, 辰巳町, Higashiyama Ward, | 0 |
| 6 | 3 | Mochi Mochi + Ninenzaka / Sannenzaka | Sannenzaka Kyoto, Japan | 鈴 三年坂夢子 Rinn Sannenzaka Yumeko, Three-year Slope, Kiyomizu 3-chome, 辰巳 | 0 |
| 6 | 4 | Lunch: Nishiki Market | Nishiki Market Kyoto, Japan | Nishiki Market, Nishikikōji Street, Higashiuoyachō, Nakagyo Ward, Kyot | 0 |
| 6 | 5 | Ginkaku-ji | Ginkakuji Temple Kyoto, Japan | Ginkaku-ji temple, Ginkakujichō, Sakyō Ward, Kyoto, Kyoto Prefecture,  | 0 |
| 6 | 6 | Philosopher's Path (south) | 哲学の道 | Philosopher's Walk, Shishigatani-Honeninnishimachi, 吉田上大路町, Sakyō Ward | 0 |
| 6 | 7 | Eikan-do | Eikando Zenrinji Kyoto, Japan | Eikando (Zenrin Temple), Shishigatani Street, Eikandōchō, 永観堂町飛地, Saky | 1 |
| 6 | 8 | Gion (Hanamikoji) | 花見小路通 | 花見小路通, Tominagacho, 辰巳町, Higashiyama Ward, Kyoto, Kyoto Prefecture, 60 | 1 |
| 6 | 10 | Kyoto Station: collect Klook tickets | Kyoto Station JR, Japan | Manneken JR Kyoto Station マネケン JR京都駅店, North-South Free Passage, Higas | 1 |
| 6 | Q1 | Inari Futaba | Inari Futaba Fushimi, Japan | いなり　ふたば, Hommachi street, Honmachi 20-chome, 東九条東松ノ木町, Fushimi Ward, K | 104 |
| 6 | Q2 | ICHiMARU5 | ICHiMARU5 | Ichimaru5, Chawan-zaka, Shiraitocho, 辰巳町, Higashiyama Ward, Kyoto, Kyo | 365 |
| 6 | Q5 | (THISIS)SHIZEN | THISIS SHIZEN | (thisis)shizen, 586-2, Karasuma Street, Banocho, Nakagyo Ward, Kyoto,  | 54 |
| 6 | Q6 | MACCHA HOUSE | 抹茶館 | Maccha House, 十軒町橋通, Kamiyacho, Nakagyo Ward, Kyoto, Kyoto Prefecture, | 70 |
| 6 | Q8 | Demachi Futaba | Demachi Futaba Kyoto, Japan | Demachi Futaba, Demachi Masugata Shopping Street, Nishincho, Kamigyō W | 216 |
| 6 | S1 | Kiyomizu-zaka / Gojozaka pottery shops | 五条坂 | Gojōzaka, Shiraitocho, 辰巳町, Higashiyama Ward, Kyoto, Kyoto Prefecture, | 383 |
| 6 | S3 | Shinmonzen-dori | 新門前通 | Shinmonzen-dori, Nakanocho, 辰巳町, Higashiyama Ward, Kyoto, Kyoto Prefec | 94 |
| 6 | S4 | Furumonzen-dori | 古門前通 | Furumonzen-dori, Ishibashicho, 辰巳町, Higashiyama Ward, Kyoto, Kyoto Pre | 86 |
| 6 | S5 | Kennin-ji | 建仁寺 | Kennin-ji, こもれ火小路, Atarashicho, 辰巳町, Higashiyama Ward, Kyoto, Kyoto Pr | 35 |
| 7 | 1 | Kyoto Station (Shinkansen) | 京都駅 | Kyoto, Hachijō Street, Nishikujo-Kitanouchicho, Minami Ward, Kyoto, Ky | 0 |
| 7 | 2 | Nagoya Station | Nagoya Station, Japan | Nagoya, Towers Terrace, Meieki 1-chome, Ushijimacho, Nakamura Ward, Na | 0 |
| 7 | 3 | Matsumoto Station | Matsumoto Station, Japan | Matsumoto, 松本駅, Fukashi 1-chome, Marunouchi, 葭町, Matsumoto, Nagano Pre | 0 |
| 7 | 5 | Matsumoto Castle (exterior) | Matsumoto Castle, Japan | Matsumoto Castle, Buried Bridge, Josei 2-chome, Marunouchi, 葭町, Matsum | 1 |
| 7 | 6 | Nakamachi + Nawate Streets | Nakamachi Street Matsumoto, Japan | Nakamachi Street, Nakamachi Dori, Chuo 3-chome, Marunouchi, 葭町, Matsum | 0 |
| 7 | 7 | Matsumoto Station | Matsumoto Station, Japan | Matsumoto, 松本駅, Fukashi 1-chome, Marunouchi, 葭町, Matsumoto, Nagano Pre | 0 |
| 7 | 8 | Kiso-Fukushima Station | Kiso-Fukushima Station, Japan | Kiso-Fukushima, 中山道, Kiso, Kiso District, Nagano Prefecture, 397-0001, | 0 |
| 7 | 9 | Kiso Mikawaya | Mikawaya Kiso | Kiso Mikawaya, 伊勢町小路, Kiso, Kiso District, Nagano Prefecture, 397-0001 | 0 |
| 7 | S1 | Nakamachi Street craft shops | Nakamachi Street Matsumoto, Japan | Nakamachi Street, Nakamachi Dori, Chuo 3-chome, Marunouchi, 葭町, Matsum | 161 |
| 8 | 1 | Kiso-Fukushima Station | Kiso-Fukushima Station, Japan | Kiso-Fukushima, 中山道, Kiso, Kiso District, Nagano Prefecture, 397-0001, | 0 |
| 8 | 2 | Nakatsugawa Station | Nakatsugawa Station, Japan | Nakatsugawa Station, 中津川駅横断地下道, 太田町二丁目, 栄町, Nakatsugawa, Gifu Prefectu | 1 |
| 8 | 3 | Magome-juku | Magome-juku, Japan | Magome-juku, Magome, Nakatsugawa, Gifu Prefecture, 508-0502, Japan | 1 |
| 8 | 4 | Magome Pass | 馬籠峠 | Magome-tōge, 中津川南木曽線, Nagiso, Kiso District, Nagano Prefecture, 508-05 | 0 |
| 8 | 5 | Tsumago-juku + lunch at Otokichi | Tsumago-juku, Japan | Tsumago-juku, Tsumago, Azuma, Nagiso, Kiso District, Nagano Prefecture | 0 |
| 8 | 6 | Nagiso Station | Nagiso Station, Japan | Nagiso, 南木曽停車場線, Nagiso, Kiso District, Nagano Prefecture, 399-5301, J | 1 |
| 8 | 7 | Kiso-Fukushima + dinner Shirasagi | Kiso-Fukushima Station, Japan | Kiso-Fukushima, 中山道, Kiso, Kiso District, Nagano Prefecture, 397-0001, | 0 |
| 8 | Q1 | Cafe Kappe | かっぺ 馬籠 | CafeKappe かっぺ, 中津川南木曽線, Magome, Nakatsugawa, Gifu Prefecture, 508-0502 | 337 |
| 9 | 1 | Kiso-Fukushima Station | Kiso-Fukushima Station, Japan | Kiso-Fukushima, 中山道, Kiso, Kiso District, Nagano Prefecture, 397-0001, | 0 |
| 9 | 2 | Matsumoto Station | Matsumoto Station, Japan | Matsumoto, 松本駅, Fukashi 1-chome, Marunouchi, 葭町, Matsumoto, Nagano Pre | 0 |
| 9 | 3 | Matsumoto Bus Terminal | Matsumoto Bus Terminal, Japan | Matsumoto Bus Terminal, Shirakaba, Fukashi 1-chome, Marunouchi, 葭町, Ma | 0 |
| 9 | 5 | Sanmachi Suji old town | Sanmachi Suji Takayama, Japan | Takayama Old Town, Sanmachi Suji, Sanmachi-dori, Hidatakayama Sanmachi | 1 |
| 10 | 1 | Miyagawa Morning Market | Miyagawa Morning Market Takayama, Japan | Miyagawa Morning Market, National Highway Route 158, 本町三丁目, 相生町, Takay | 0 |
| 10 | 2 | Takayama Jinya | Takayama Jinya, Japan | Takayama Jinya, 中橋, 本町一丁目, 川原町, Takayama, Gifu Prefecture, 506-0846, J | 1 |
| 10 | 3 | Takayama Station | Takayama Station, Japan | Takayama, 高山停車場線, 花里町五丁目, 花川町, Takayama, Gifu Prefecture, 506-0026, Ja | 1 |
| 10 | 4 | Hida Furukawa + lunch | Hida-Furukawa Station, Japan | Hida-Furukawa Station, 岐阜県飛騨市古川町金森町８, 古川国府線, 古川町若宮二丁目, 古川町殿町, Hida, Gi | 0 |
| 10 | 5 | Sanmachi Suji + Hirase sake tasting | Sanmachi Suji Takayama, Japan | Takayama Old Town, Sanmachi Suji, Sanmachi-dori, Hidatakayama Sanmachi | 1 |
| 10 | S1 | Mishima candle shop (Hida Furukawa) | 三嶋和ろうそく店 | Japanese candle shop Mishima shoten, 3-12, Setogawa River and Shirakab | 460 |
| 10 | S2 | Takayama antique + Shibukusa-yaki shops | Sanmachi Suji Takayama, Japan | Takayama Old Town, Sanmachi Suji, Sanmachi-dori, Hidatakayama Sanmachi | 120 |
| 11 | 2 | Shirakawa-go bus terminal | Shirakawa-go bus terminal, Shirakawa | Shirakawa-go (Ogimachi), National Highway Route 156, Hatogaya, Shiraka | 0 |
| 11 | 3 | Shiroyama Viewpoint | 荻町城跡展望台 | Ogimachi Castle Observation Deck, National Highway Route 360, Hatogaya | 1 |
| 11 | 4 | Wada House + village | 和田家 白川村 | 国指定重要文化財 和田家, National Highway Route 156, Ogimachi, Shirakawa, Ono Cou | 0 |
| 11 | 5 | Lunch: Irori | いろり 白川村 | いろり, National Highway Route 156, Ogimachi, Shirakawa, Ono County, Gifu | 0 |
| 11 | 6 | Shirakawa-go bus terminal | Shirakawa-go bus terminal, Shirakawa | Shirakawa-go (Ogimachi), National Highway Route 156, Hatogaya, Shiraka | 0 |
| 11 | 7 | Kanazawa Station (West Exit) | Kanazawa Station, Japan | Kanazawa Station, 金沢駅西通り, Honmachi 2-chome, Hiyoshimachi, Kanazawa, Is | 0 |
| 11 | 8 | Hotel Forza Kanazawa | Hotel Forza Kanazawa, Japan | Hotel Forza Kanazawa, Prefectural Road 13, Honmachi 1-chome, Yasuecho, | 0 |
| 11 | 9 | Higashi Chaya + Kazuemachi | Higashi Chaya District Kanazawa, Japan | Higashi-chaya street (Geisha district), 愛宕二番丁, Kannonmachi 2-chome, Ha | 1 |
| 11 | S1 | Higashi Chaya craft shops | Higashi Chaya District Kanazawa, Japan | Higashi-chaya street (Geisha district), 愛宕二番丁, Kannonmachi 2-chome, Ha | 105 |
| 12 | 1 | Kenrokuen (early, free entry) | Kenrokuen | Kenroku-en Park, Kanazawa, Ishikawa Prefecture, 920-0936, Japan | 1 |
| 12 | 2 | Kanazawa Castle Park + Gyokusen-an | Gyokusen-an Kanazawa, Japan | Gyokusen-an, Ohori Street, Hirosaka 2-chome, Marunouchi, Kanazawa, Ish | 1 |
| 12 | 3 | Nagamachi + Nomura Samurai House | Nomura Samurai House Kanazawa, Japan | Nomura Samurai House, 長町三番丁, Korinbo 2-chome, Minamicho, Kanazawa, Ish | 0 |
| 12 | 4 | Lunch: Morimori Zushi, Omicho Market | もりもり寿し | Mori mori Sushi, 下近江町, Owaricho 2-chome, Shimoomicho, Kanazawa, Ishika | 0 |
| 12 | 6 | Myoryuji Ninja Temple | Myoryuji Ninja Temple Kanazawa, Japan | Myôryûji (Ninjadera Temple), 1-2-12, 蛤坂, Nomachi 1-chome, Jusangenmach | 0 |
| 12 | Q1 | isotope café | isotope | isotope アイソトープ, 塩川町, Nagamachi 2-chome, Kiguramachi, Kanazawa, Ishikaw | 109 |
| 12 | S1 | Shintatemachi | 新竪町 | Shintate-machi, Shintatemachi-dori, Shintatemachi 3-chome, 新竪町, Kanaza | 772 |
| 13 | 1 | Kanazawa Station | Kanazawa Station, Japan | Kanazawa Station, 大階段, Honmachi 2-chome, Kinoshinbomachi, Kanazawa, Is | 1 |
| 13 | 2 | Tokyo Station | Tokyo Station, Japan | Tokyo Station;Exit M12, Marunouchi 1, Marunouchi, Chiyoda, Tokyo, 100- | 1 |
| 13 | 3 | Shinjuku Station (Platform 9) | Shinjuku Station, Japan | Shinjuku, JR新宿駅, Shinjuku 3, Shinjuku, Tokyo, 160-0022, Japan | 0 |
| 13 | 4 | Kawaguchiko Station | Kawaguchiko Station, Japan | Kawaguchiko Station, misaka road, Funatsu, Fujikawaguchiko, Minamitsur | 0 |
| 13 | 6 | Dinner: Houtou Kura Funari | 歩成 河口湖 | 歩成, National Highway Route 139, Oarashi, Fujikawaguchiko, Minamitsuru  | 0 |
| 14 | 1 | Oishi Park | 大石公園 | Ōishi Park, Oishi, Fujikawaguchiko, Minamitsuru County, Yamanashi Pref | 0 |
| 14 | 2 | Chureito Pagoda | Chureito Pagoda, Japan | Chureito Pagoda, 1, Arakura, Fujiyoshida, Yamanashi Prefecture, 403-00 | 1 |
| 14 | 3 | Lunch: Koubaiya / Kitchen Fujiyama View | 大石公園 | Ōishi Park, Oishi, Fujikawaguchiko, Minamitsuru County, Yamanashi Pref | 0 |
| 14 | 4 | Oshino Hakkai | Oshino Hakkai, Japan | Oshino Hakkai, 八海2号橋, Shibokusa, Oshino, Minamitsuru County, Yamanashi | 0 |
| 14 | 5 | Kachi Kachi Ropeway | Kachi Kachi Ropeway, Japan | Lake Kawaguchi Mt. Tenjō Ropeway, misaka road, Funatsu, Azagawa, Fujik | 0 |
| 15 | 1 | Kawaguchiko Station | Kawaguchiko Station, Japan | Kawaguchiko Station, misaka road, Funatsu, Fujikawaguchiko, Minamitsur | 0 |
| 15 | 2 | Busta Shinjuku (South Exit) | Busta Shinjuku, Japan | Shinjuku Expressway Bus Terminal, 55, Sendagaya 5, Sendagaya, Shibuya, | 0 |
| 15 | 3 | APA Hotel Kabukicho Tower (drop bags) | APA Hotel Higashi Shinjuku Kabukicho Tower, Japan | APA Hotel, Shokuan Street, Kabukichō 2, Kabukichō, Shinjuku, Tokyo, 16 | 0 |
| 15 | 4 | Meiji Jingu | Meiji Jingu, Japan | Meiji Jingu Main Shrine, 1, Yoyogi Kamizono-chō, Shibuya, Tokyo, 151-8 | 0 |
| 15 | 5 | Lunch: Sakuratei | さくら亭 神宮前 | Sakura Okonomiyaki, 旧渋谷川遊歩道路（キャットストリート）, Jingumae 3, Jingumae, Shibuya | 1 |
| 15 | 6 | Takeshita Street | Takeshita Street Harajuku | Takeshita Exit of Harajuku Sta., Takeshita Street, Jingūmae 1, Jinguma | 1 |
| 15 | 7 | Omotesando + Cat Street | Cat Street Harajuku | Creative Space Akademeia 21 Harajuku, Cat Street, Jingumae 5, Jingumae | 1 |
| 15 | 8 | Shibuya Crossing at sunset | Shibuya Scramble Crossing, Japan | Shibuya Scramble Crossing, Jingu-dori Street, Dōgenzaka 2, Dōgenzaka,  | 1 |
| 15 | 9 | Dinner: Tori Take Souhonten | 鳥竹 | Toritake, Plaza-dori Street, Dōgenzaka 1, Dōgenzaka, Shibuya, Tokyo, 1 | 0 |
| 15 | 10 | Omoide Yokocho / Golden Gai / Don Quijote | Omoide Yokocho Shinjuku, Japan | Omoide-yokochō, Nishi-Shinjuku 1, Nishi-Shinjuku, Shinjuku, Tokyo, 160 | 0 |
| 15 | Q2 | SILKREAM | SILKREAM | Silkream, 19-3, Jinnan 1, Jinnan, Shibuya, Tokyo, 150-0041, Japan | 391 |
| 15 | Q3 | Excelsior Caffè (Shibuya) | エクセルシオール カフェ 渋谷 | EXCELSIOR CAFE, Dogen-zaka Street, Dōgenzaka 2, Dōgenzaka, Shibuya, To | 117 |
| 15 | S1 | Oriental Bazaar | Oriental Bazaar | オリエンタルバザール, Omotesandō, Jingumae 5, Jingumae, Shibuya, Tokyo, 150-0001 | 205 |
| 16 | 1 | APA Hotel / Higashi-Shinjuku Station | Higashi-shinjuku Station, Japan | Higashi-shinjuku, Nukebenten Street, Shinjuku 6, Shinjuku, Tokyo, 160- | 1 |
| 16 | 2 | Ueno Park + Ameyoko | Ameyoko Ueno, Japan | Ameya-Yokocho, Ameyoko Street, Ueno 6, Ueno, Taito, Tokyo, 110-0005, J | 0 |
| 16 | 3 | Kappabashi Kitchen Town | かっぱ橋道具街 | 犬印鞄製作所 合羽橋道具街, Kappabashi Dogugai Street, Nishi-Asakusa 2, Matsugaya,  | 0 |
| 16 | 6 | Akihabara: Animate / Mandarake / Radio Kaikan | Akihabara Radio Kaikan, Japan | Akihabara Radio Kaikan, 16, Soto-Kanda 1, Soto-Kanda, Chiyoda, Tokyo,  | 0 |
| 16 | 7 | Hara Shobo, Jimbocho | Hara Shobo Jimbocho, Japan | Hara Shobo Japanese Ukiyo-e Prints, 22, Kanda-Jimbocho 2, Kanda-Jimboc | 0 |
| 16 | 8 | Ginza | 銀座四丁目交差点 | Ginza Crossing, Ginza, Ginza 5, Ginza, Chuo, Tokyo, 104-0061, Japan | 0 |
| 16 | 9 | Dinner, then pack | Shinjuku Kakekomi Gyoza, Japan | Shinjuku Kakekomi Gyoza, Central Road, Kabukichō 1, Kabukichō, Shinjuk | 0 |
| 16 | Q1 | Imo Pippi | 芋ぴっぴ | 芋ぴっぴ。浅草店, Okuyama Omairimachi, Asakusa 2, Asakusa, Taito, Tokyo, 111-0 | 238 |
| 16 | Q2 | Excelsior Caffè (Akihabara) | エクセルシオール カフェ 秋葉原 | EXCELSIOR CAFE, 秋葉原駅西側交通広場, Soto-Kanda 1, Soto-Kanda, Chiyoda, Tokyo,  | 103 |
| 16 | S1 | Tokyo National Museum (Honkan) | Tokyo National Museum, Japan | Tokyo National Museum, 9, Ueno Park, Taito, Tokyo, 110-8712, Japan | 55 |
| 16 | S2 | Kappabashi ceramic shops | かっぱ橋道具街 | 犬印鞄製作所 合羽橋道具街, Kappabashi Dogugai Street, Nishi-Asakusa 2, Matsugaya,  | 68 |
| 16 | S3 | Hara Shobo | Hara Shobo Jimbocho, Japan | Hara Shobo Japanese Ukiyo-e Prints, 22, Kanda-Jimbocho 2, Kanda-Jimboc | 160 |
| 16 | S5 | Antique Mall Ginza | Antique Mall Ginza | antique mall ginza, Ginza Sakura-dori Street, Ginza 1, Ginza, Chuo, To | 113 |
| 17 | 1 | APA Hotel Kabukicho Tower | APA Hotel Higashi Shinjuku Kabukicho Tower, Japan | APA Hotel, Shokuan Street, Kabukichō 2, Kabukichō, Shinjuku, Tokyo, 16 | 0 |
| 17 | 2 | Tokyu Kabukicho Tower bus stop | Tokyu Kabukicho Tower, Japan | Tokyu Kabukicho Tower, 1, Kabukichō 1, Kabukichō, Shinjuku, Tokyo, 160 | 1 |
| 17 | 3 | Narita Airport Terminal 2 | Narita Airport Terminal 2, Japan | Narita Airport Terminal 2, Central Square, Furugome, Narita, Chiba Pre | 0 |
| 17 | 4 | Depart CX527 → HKG → CX663 | Narita Airport Terminal 2, Japan | Narita Airport Terminal 2, Central Square, Furugome, Narita, Chiba Pre | 0 |
