# Geocoding log

Nominatim (OpenStreetMap), queried with each stop's `mapsQuery` (fallbacks: query without ', Japan', then stop name + city). A match is accepted only if it is a specific place (not a city/district polygon) within 2.5 km of the original pin.

## Could not match (11) — original approximate pin kept, please check

| Day | # | Stop | mapsQuery |
|---|---|---|---|
| 1 | 2 | BON Condominium Umeda | BON Condominium Umeda Osaka, Japan |
| 5 | 10 | Dinner: Kyoto Sumibi Kushiyaki Tsujiy | Kyoto Sumibi Kushiyaki Tsujiy, Japan |
| 6 | 9 | Dinner: Kyoto Gion Okaru | Gion Okaru Kyoto, Japan |
| 7 | 4 | Lunch: Miyota Matsumoto | Miyota Matsumoto soba, Japan |
| 9 | 4 | Takayama Nohi Bus Center | Takayama Nohi Bus Center, Japan |
| 11 | 1 | Takayama Nohi Bus Center | Takayama Nohi Bus Center, Japan |
| 12 | 5 | Gold-leaf workshop: Kanazawa Katani | Kanazawa Katani gold leaf, Japan |
| 12 | 7 | Dinner: Izakaya Gappa | Izakaya Gappa Kanazawa, Japan |
| 14 | 6 | Dinner: Koshu Houtou Kosaku | Koshu Houtou Kosaku Kawaguchiko, Japan |
| 16 | 4 | Galerie Dentsdelion | Galerie Dentsdelion Tokyo, Japan |
| 16 | 5 | Lunch: Mendokoro Honta, Akihabara | Mendokoro Honta Akihabara, Japan |

## Kept original pin on purpose (3)

| Day | # | Stop | Why |
|---|---|---|---|
| 5 | 5 | Nara Park deer | OSM centroid is far east of the deer area by Todai-ji |
| 6 | 1 | Fushimi Inari Taisha | OSM centroid is up the mountain; original pin is the main gate |
| 13 | 5 | Kawaguchiko Hotel | Nominatim returns other hotels (Kawaguchiko Park Hotel / Tominoko Hotel) |

## Matched but worth a glance (4)

| Day | # | Stop | Note |
|---|---|---|---|
| 2 | 1 | BON Condominium Umeda | Day 2 stop 1 is named BON Condominium but its mapsQuery is Hankyu Osaka-umeda Station, so the pin is the station |
| 13 | 6 | Dinner: Houtou Kura Funari | matched the Funari on Route 139 (Oarashi); confirm it is the branch you want |
| 15 | 3 | APA Hotel Kabukicho Tower (drop bags) | OSM only says 'APA Hotel' (Kabukicho 2-chome, Shokuan-dori); several APAs nearby |
| 17 | 1 | APA Hotel Kabukicho Tower | OSM only says 'APA Hotel' (Kabukicho 2-chome, Shokuan-dori); several APAs nearby |

## Matched (113) — pin moved by

| Day | # | Stop | Query used | OSM result | Moved (m) |
|---|---|---|---|---|---|
| 1 | 1 | Kansai Airport (KIX) | 関西国際空港 第1ターミナル | Terminal 1, Tajiri, Sennan County, Osaka Prefecture, 549-0011, Japan | 1292 |
| 1 | 3 | Dinner: Kinryu Ramen Midosuji | 金龍ラーメン | 金龍ラーメン, Hozenji Koisan Dori, Dotonbori 1, Chūō Ward, Osaka, Osaka Pref | 95 |
| 2 | 1 | BON Condominium Umeda | 大阪梅田駅 | Osaka-Umeda, National Highway Route 176, Shibata 1-chōme, Kita Ward, O | 144 |
| 2 | 2 | Minoh Station | Minoh Station Hankyu, Japan | Hankyu Minoh Station, Minoh Takimichi, Minoo 1-chome, Minoh, Osaka Pre | 949 |
| 2 | 3 | Katsuo-ji (daruma temple) | Katsuo-ji, Osaka | Katsuō Temple, Minoh, Osaka Prefecture, 562-8508, Japan | 205 |
| 2 | 4 | Minoh Falls + Ryuanji | 箕面大滝 | Minoh Waterfall, Minoh, Osaka Prefecture, 562-0002, Japan | 46 |
| 2 | 5 | Walk down to Minoh Station | Minoh Station Hankyu, Japan | Hankyu Minoh Station, Minoh Takimichi, Minoo 1-chome, Minoh, Osaka Pre | 949 |
| 2 | 6 | Osaka Castle (Otemon Gate) | Otemon Gate Osaka Castle, Japan | Otemon Gate, Uemachi Suji Street, Osakajo, Chūō Ward, Osaka, Osaka Pre | 253 |
| 2 | 7 | Shinsekai + Tsutenkaku | Tsutenkaku Shinsekai Osaka, Japan | Tsūtenkaku, 6, Shinsekai Market, Ebisu-Higashi 1, Naniwa Ward, Osaka,  | 4 |
| 2 | 8 | Dinner: Yaekatsu (kushikatsu) | 八重勝 | 株式会社 八重勝, 公園通, Ebisu-Higashi 3, Naniwa Ward, Osaka, Osaka Prefecture,  | 77 |
| 3 | 1 | Osaka-Namba (Kintetsu) | 大阪難波駅 | Ōsaka Namba, Sennichimae Dori Street, Minatomachi 1-chōme, Naniwa Ward | 323 |
| 3 | 2 | Iseshi Station | Iseshi Station, Japan | Iseshi Station, タクシープール, Fukiage 1-chome, Honmachi, Ise, Mie Prefectur | 156 |
| 3 | 3 | Ise Jingu Geku (Outer Shrine) | Ise Jingu Geku, Japan | Ise-Jingu Geku, Ise Nanto Line, Tokiwa 2-chome, Honmachi, Ise, Mie Pre | 28 |
| 3 | 4 | Ise Jingu Naiku (Inner Shrine) | 宇治橋 伊勢 | Uji Bridge, Ise Nansei Line, Ujiimazaikecho, Ise, Mie Prefecture, 516- | 431 |
| 3 | 5 | Lunch: Fukusuke + Okage Yokocho | Fukusuke Okage Yokocho Ise, Japan | おかげ横丁 ふくすけ, Okage Yokocho Ancient Street, Ujiurata 1-chome, Ujinakanok | 20 |
| 3 | 6 | Meoto Iwa (Wedded Rocks) | 二見興玉神社 | Futami Okitama Shrine, 禊橋, Futamichō-E, Ise, Mie Prefecture, 516-0037, | 61 |
| 3 | 7 | Iseshi Station | Iseshi Station, Japan | Iseshi Station, タクシープール, Fukiage 1-chome, Honmachi, Ise, Mie Prefectur | 156 |
| 3 | 8 | Dotonbori + Hozenji Yokocho | Hozenji Yokocho Osaka, Japan | Hozenji yokocho (alley w traditional restaurants, shops, bars), 坂町通, S | 94 |
| 4 | 1 | Osaka Station | Osaka Station JR, Japan | JR Osaka Station (Bus), 市道梅田線, Umeda 3-chōme, Kita Ward, Osaka, Osaka  | 150 |
| 4 | 2 | Saga-Arashiyama Station | Saga-Arashiyama Station, Japan | Saga Arashiyama Station, Marutamachi Street, Sagashakado-Monzensetogaw | 274 |
| 4 | 3 | Bamboo Grove | Arashiyama Bamboo Grove, Japan | Arashiyama Bamboo Grove, Ukyō Ward, Kyoto, Kyoto Prefecture, 616-0000, | 58 |
| 4 | 4 | Tenryu-ji | Tenryuji Temple Kyoto, Japan | Tenryuji Temple, Utano Arashiyama Yamada Line, Sagatenryuji-Tateishich | 291 |
| 4 | 5 | Gio-ji | Giouji Temple Kyoto, Japan | Giō Temple, Kyoto Hiyoshi Miyama Line, Saganisoninmonzen-Ojoincho, Uky | 22 |
| 4 | 6 | Adashino Nenbutsuji | 化野念仏寺 | Adashino-Nenbutsudera Temple, Kyoto Hiyoshi Miyama Line, Sagatoriimoto | 58 |
| 4 | 7 | Otagi Nenbutsuji | 愛宕念仏寺 | Otagi Nenbutsu Temple, Kiyotaki Toriimoto Line, Sagatoriimoto-Ikkahyoc | 241 |
| 4 | 8 | Lunch: Arashiyama Daizen | 大善 嵐山 | 大善, Sanjo Street, Saga-Isenokamicho, Ukyō Ward, Kyoto, Kyoto Prefectur | 470 |
| 4 | 9 | Rinn Kamiebisu (drop bags) | Rinn Kamiebisu | Rinn Kamiebisu, Kamiebisucho, Shimogyo Ward, Kyoto, Kyoto Prefecture,  | 373 |
| 4 | 10 | To-ji illumination | To-ji Temple Kyoto, Japan | To-ji Temple, Kujō Street, Nishikujo-Hieijocho, Minami Ward, Kyoto, Ky | 8 |
| 4 | 11 | Dinner: Hana-Tanuki | 花たぬき 京都 | 花たぬき, Higashinotōin Street, Shiokojicho, Shimogyo Ward, Kyoto, Kyoto P | 390 |
| 5 | 1 | Kintetsu Kyoto Station | Kintetsu Kyoto Station, Japan | Miyako City Kintetsu Kyoto Station, Hachijō Street, Nishikujo-Kitanouc | 58 |
| 5 | 2 | Kintetsu-Nara Station | Kintetsu Nara Station, Japan | Kintetsu Nara Station, 登大路, Nishimikadocho, Nara, Nara Prefecture, 630 | 32 |
| 5 | 3 | Nakatanidou (mochi pounding) | Nakatanidou Nara, Japan | Nakatanidou (fresh mochi & show), 29, Sanjō Dōri, Hashimotocho, Kawano | 105 |
| 5 | 4 | Todai-ji (Great Buddha Hall) | Todai-ji, Nara | Todai ji, 猫段, Suimoncho, Zoshicho, Nara, Nara Prefecture, 630-8211, Ja | 80 |
| 5 | 6 | Lunch: Mizuya Chaya | Mizuya Chaya Nara, Japan | Mizuya-Chaya, Mizuya Bridge, Kasuganochō, Nara, Nara Prefecture, 630-8 | 141 |
| 5 | 7 | Kasuga Taisha | Kasuga Taisha, Japan | Kasuga Taisha, 下の禰宜道（ささやきの小径）, Takabatakecho, Kasuganochō, Nara, Nara  | 128 |
| 5 | 8 | Naramachi | Naramachi Nara, Japan | Naramachi Museum, 上ツ道（上街道）, Nakanoshinyacho, Kawanokami-tsukinukecho,  | 78 |
| 5 | 9 | Kintetsu-Nara Station | Kintetsu Nara Station, Japan | Kintetsu Nara Station, 登大路, Nishimikadocho, Nara, Nara Prefecture, 630 | 32 |
| 6 | 2 | Kiyomizu-dera | Kiyomizu-dera, Japan | Kiyomizu-dera, Tokiwa Bridge, Kiyomizu 1-chōme, 辰巳町, Higashiyama Ward, | 84 |
| 6 | 3 | Mochi Mochi + Ninenzaka / Sannenzaka | Sannenzaka Kyoto, Japan | 鈴 三年坂夢子 Rinn Sannenzaka Yumeko, Three-year Slope, Kiyomizu 3-chome, 辰巳 | 59 |
| 6 | 4 | Lunch: Nishiki Market | Nishiki Market Kyoto, Japan | Nishiki Market, Nishikikōji Street, Higashiuoyachō, Nakagyo Ward, Kyot | 61 |
| 6 | 5 | Ginkaku-ji | Ginkakuji Temple Kyoto, Japan | Ginkaku-ji temple, Ginkakujichō, Sakyō Ward, Kyoto, Kyoto Prefecture,  | 19 |
| 6 | 6 | Philosopher's Path (south) | 哲学の道 | Philosopher's Walk, Shishigatani-Honeninnishimachi, 吉田上大路町, Sakyō Ward | 115 |
| 6 | 7 | Eikan-do | Eikando Zenrinji Kyoto, Japan | Eikando (Zenrin Temple), Shishigatani Street, Eikandōchō, 永観堂町飛地, Saky | 50 |
| 6 | 8 | Gion (Hanamikoji) | 花見小路通 | 花見小路通, Tominagacho, 辰巳町, Higashiyama Ward, Kyoto, Kyoto Prefecture, 60 | 86 |
| 6 | 10 | Kyoto Station: collect Klook tickets | Kyoto Station JR, Japan | Manneken JR Kyoto Station マネケン JR京都駅店, North-South Free Passage, Higas | 87 |
| 7 | 1 | Kyoto Station (Shinkansen) | 京都駅 | Kyoto, Hachijō Street, Nishikujo-Kitanouchicho, Minami Ward, Kyoto, Ky | 50 |
| 7 | 2 | Nagoya Station | Nagoya Station, Japan | Nagoya, Towers Terrace, Meieki 1-chome, Ushijimacho, Nakamura Ward, Na | 37 |
| 7 | 3 | Matsumoto Station | Matsumoto Station, Japan | Matsumoto, 松本駅, Fukashi 1-chome, Marunouchi, 葭町, Matsumoto, Nagano Pre | 22 |
| 7 | 5 | Matsumoto Castle (exterior) | Matsumoto Castle, Japan | Matsumoto Castle, Buried Bridge, Josei 2-chome, Marunouchi, 葭町, Matsum | 5 |
| 7 | 6 | Nakamachi + Nawate Streets | Nakamachi Street Matsumoto, Japan | Nakamachi Street, Nakamachi Dori, Chuo 3-chome, Marunouchi, 葭町, Matsum | 105 |
| 7 | 7 | Matsumoto Station | Matsumoto Station, Japan | Matsumoto, 松本駅, Fukashi 1-chome, Marunouchi, 葭町, Matsumoto, Nagano Pre | 22 |
| 7 | 8 | Kiso-Fukushima Station | Kiso-Fukushima Station, Japan | Kiso-Fukushima, 中山道, Kiso, Kiso District, Nagano Prefecture, 397-0001, | 89 |
| 7 | 9 | Kiso Mikawaya | Mikawaya Kiso | Kiso Mikawaya, 伊勢町小路, Kiso, Kiso District, Nagano Prefecture, 397-0001 | 1307 |
| 8 | 1 | Kiso-Fukushima Station | Kiso-Fukushima Station, Japan | Kiso-Fukushima, 中山道, Kiso, Kiso District, Nagano Prefecture, 397-0001, | 89 |
| 8 | 2 | Nakatsugawa Station | Nakatsugawa Station, Japan | Nakatsugawa Station, 中津川駅横断地下道, 太田町二丁目, 栄町, Nakatsugawa, Gifu Prefectu | 237 |
| 8 | 3 | Magome-juku | Magome-juku, Japan | Magome-juku, Magome, Nakatsugawa, Gifu Prefecture, 508-0502, Japan | 257 |
| 8 | 4 | Magome Pass | 馬籠峠 | Magome-tōge, 中津川南木曽線, Nagiso, Kiso District, Nagano Prefecture, 508-05 | 996 |
| 8 | 5 | Tsumago-juku + lunch at Otokichi | Tsumago-juku, Japan | Tsumago-juku, Tsumago, Azuma, Nagiso, Kiso District, Nagano Prefecture | 52 |
| 8 | 6 | Nagiso Station | Nagiso Station, Japan | Nagiso, 南木曽停車場線, Nagiso, Kiso District, Nagano Prefecture, 399-5301, J | 455 |
| 8 | 7 | Kiso-Fukushima + dinner Shirasagi | Kiso-Fukushima Station, Japan | Kiso-Fukushima, 中山道, Kiso, Kiso District, Nagano Prefecture, 397-0001, | 89 |
| 9 | 1 | Kiso-Fukushima Station | Kiso-Fukushima Station, Japan | Kiso-Fukushima, 中山道, Kiso, Kiso District, Nagano Prefecture, 397-0001, | 89 |
| 9 | 2 | Matsumoto Station | Matsumoto Station, Japan | Matsumoto, 松本駅, Fukashi 1-chome, Marunouchi, 葭町, Matsumoto, Nagano Pre | 22 |
| 9 | 3 | Matsumoto Bus Terminal | Matsumoto Bus Terminal, Japan | Matsumoto Bus Terminal, Shirakaba, Fukashi 1-chome, Marunouchi, 葭町, Ma | 22 |
| 9 | 5 | Sanmachi Suji old town | Sanmachi Suji Takayama, Japan | Takayama Old Town, Sanmachi Suji, Sanmachi-dori, Hidatakayama Sanmachi | 120 |
| 10 | 1 | Miyagawa Morning Market | Miyagawa Morning Market Takayama, Japan | Miyagawa Morning Market, National Highway Route 158, 本町三丁目, 相生町, Takay | 194 |
| 10 | 2 | Takayama Jinya | Takayama Jinya, Japan | Takayama Jinya, 中橋, 本町一丁目, 川原町, Takayama, Gifu Prefecture, 506-0846, J | 133 |
| 10 | 3 | Takayama Station | Takayama Station, Japan | Takayama, 高山停車場線, 花里町五丁目, 花川町, Takayama, Gifu Prefecture, 506-0026, Ja | 22 |
| 10 | 4 | Hida Furukawa + lunch | Hida-Furukawa Station, Japan | Hida-Furukawa Station, 岐阜県飛騨市古川町金森町８, 古川国府線, 古川町若宮二丁目, 古川町殿町, Hida, Gi | 151 |
| 10 | 5 | Sanmachi Suji + Hirase sake tasting | Sanmachi Suji Takayama, Japan | Takayama Old Town, Sanmachi Suji, Sanmachi-dori, Hidatakayama Sanmachi | 120 |
| 11 | 2 | Shirakawa-go bus terminal | Shirakawa-go bus terminal, Shirakawa | Shirakawa-go (Ogimachi), National Highway Route 156, Hatogaya, Shiraka | 20 |
| 11 | 3 | Shiroyama Viewpoint | 荻町城跡展望台 | Ogimachi Castle Observation Deck, National Highway Route 360, Hatogaya | 425 |
| 11 | 4 | Wada House + village | 和田家 白川村 | 国指定重要文化財 和田家, National Highway Route 156, Ogimachi, Shirakawa, Ono Cou | 233 |
| 11 | 5 | Lunch: Irori | いろり 白川村 | いろり, National Highway Route 156, Ogimachi, Shirakawa, Ono County, Gifu | 348 |
| 11 | 6 | Shirakawa-go bus terminal | Shirakawa-go bus terminal, Shirakawa | Shirakawa-go (Ogimachi), National Highway Route 156, Hatogaya, Shiraka | 20 |
| 11 | 7 | Kanazawa Station (West Exit) | Kanazawa Station, Japan | Kanazawa Station, 金沢駅西通り, Honmachi 2-chome, Hiyoshimachi, Kanazawa, Is | 89 |
| 11 | 8 | Hotel Forza Kanazawa | Hotel Forza Kanazawa, Japan | Hotel Forza Kanazawa, Prefectural Road 13, Honmachi 1-chome, Yasuecho, | 425 |
| 11 | 9 | Higashi Chaya + Kazuemachi | Higashi Chaya District Kanazawa, Japan | Higashi-chaya street (Geisha district), 愛宕二番丁, Kannonmachi 2-chome, Ha | 105 |
| 12 | 1 | Kenrokuen (early, free entry) | Kenrokuen | Kenroku-en Park, Kanazawa, Ishikawa Prefecture, 920-0936, Japan | 15 |
| 12 | 2 | Kanazawa Castle Park + Gyokusen-an | Gyokusen-an Kanazawa, Japan | Gyokusen-an, Ohori Street, Hirosaka 2-chome, Marunouchi, Kanazawa, Ish | 168 |
| 12 | 3 | Nagamachi + Nomura Samurai House | Nomura Samurai House Kanazawa, Japan | Nomura Samurai House, 長町三番丁, Korinbo 2-chome, Minamicho, Kanazawa, Ish | 123 |
| 12 | 4 | Lunch: Morimori Zushi, Omicho Market | もりもり寿し | Mori mori Sushi, 下近江町, Owaricho 2-chome, Shimoomicho, Kanazawa, Ishika | 102 |
| 12 | 6 | Myoryuji Ninja Temple | Myoryuji Ninja Temple Kanazawa, Japan | Myôryûji (Ninjadera Temple), 1-2-12, 蛤坂, Nomachi 1-chome, Jusangenmach | 443 |
| 13 | 1 | Kanazawa Station | Kanazawa Station, Japan | Kanazawa Station, 大階段, Honmachi 2-chome, Kinoshinbomachi, Kanazawa, Is | 71 |
| 13 | 2 | Tokyo Station | Tokyo Station, Japan | Tokyo Station;Exit M12, Marunouchi 1, Marunouchi, Chiyoda, Tokyo, 100- | 175 |
| 13 | 3 | Shinjuku Station (Platform 9) | Shinjuku Station, Japan | Shinjuku, JR新宿駅, Shinjuku 3, Shinjuku, Tokyo, 160-0022, Japan | 74 |
| 13 | 4 | Kawaguchiko Station | Kawaguchiko Station, Japan | Kawaguchiko Station, misaka road, Funatsu, Fujikawaguchiko, Minamitsur | 45 |
| 13 | 6 | Dinner: Houtou Kura Funari | 歩成 河口湖 | 歩成, National Highway Route 139, Oarashi, Fujikawaguchiko, Minamitsuru  | 1410 |
| 14 | 1 | Oishi Park | 大石公園 | Ōishi Park, Oishi, Fujikawaguchiko, Minamitsuru County, Yamanashi Pref | 880 |
| 14 | 2 | Chureito Pagoda | Chureito Pagoda, Japan | Chureito Pagoda, 1, Arakura, Fujiyoshida, Yamanashi Prefecture, 403-00 | 25 |
| 14 | 3 | Lunch: Koubaiya / Kitchen Fujiyama View | 大石公園 | Ōishi Park, Oishi, Fujikawaguchiko, Minamitsuru County, Yamanashi Pref | 796 |
| 14 | 4 | Oshino Hakkai | Oshino Hakkai, Japan | Oshino Hakkai, 八海2号橋, Shibokusa, Oshino, Minamitsuru County, Yamanashi | 32 |
| 14 | 5 | Kachi Kachi Ropeway | Kachi Kachi Ropeway, Japan | Lake Kawaguchi Mt. Tenjō Ropeway, misaka road, Funatsu, Azagawa, Fujik | 177 |
| 15 | 1 | Kawaguchiko Station | Kawaguchiko Station, Japan | Kawaguchiko Station, misaka road, Funatsu, Fujikawaguchiko, Minamitsur | 45 |
| 15 | 2 | Busta Shinjuku (South Exit) | Busta Shinjuku, Japan | Shinjuku Expressway Bus Terminal, 55, Sendagaya 5, Sendagaya, Shibuya, | 37 |
| 15 | 3 | APA Hotel Kabukicho Tower (drop bags) | APA Hotel Higashi Shinjuku Kabukicho Tower, Japan | APA Hotel, Shokuan Street, Kabukichō 2, Kabukichō, Shinjuku, Tokyo, 16 | 273 |
| 15 | 4 | Meiji Jingu | Meiji Jingu, Japan | Meiji Jingu Main Shrine, 1, Yoyogi Kamizono-chō, Shibuya, Tokyo, 151-8 | 176 |
| 15 | 5 | Lunch: Sakuratei | さくら亭 神宮前 | Sakura Okonomiyaki, 旧渋谷川遊歩道路（キャットストリート）, Jingumae 3, Jingumae, Shibuya | 211 |
| 15 | 6 | Takeshita Street | Takeshita Street Harajuku | Takeshita Exit of Harajuku Sta., Takeshita Street, Jingūmae 1, Jinguma | 7 |
| 15 | 7 | Omotesando + Cat Street | Cat Street Harajuku | Creative Space Akademeia 21 Harajuku, Cat Street, Jingumae 5, Jingumae | 340 |
| 15 | 8 | Shibuya Crossing at sunset | Shibuya Scramble Crossing, Japan | Shibuya Scramble Crossing, Jingu-dori Street, Dōgenzaka 2, Dōgenzaka,  | 1 |
| 15 | 9 | Dinner: Tori Take Souhonten | 鳥竹 | Toritake, Plaza-dori Street, Dōgenzaka 1, Dōgenzaka, Shibuya, Tokyo, 1 | 67 |
| 15 | 10 | Omoide Yokocho / Golden Gai / Don Quijote | Omoide Yokocho Shinjuku, Japan | Omoide-yokochō, Nishi-Shinjuku 1, Nishi-Shinjuku, Shinjuku, Tokyo, 160 | 6 |
| 16 | 1 | APA Hotel / Higashi-Shinjuku Station | Higashi-shinjuku Station, Japan | Higashi-shinjuku, Nukebenten Street, Shinjuku 6, Shinjuku, Tokyo, 160- | 4 |
| 16 | 2 | Ueno Park + Ameyoko | Ameyoko Ueno, Japan | Ameya-Yokocho, Ameyoko Street, Ueno 6, Ueno, Taito, Tokyo, 110-0005, J | 9 |
| 16 | 3 | Kappabashi Kitchen Town | かっぱ橋道具街 | 犬印鞄製作所 合羽橋道具街, Kappabashi Dogugai Street, Nishi-Asakusa 2, Matsugaya,  | 68 |
| 16 | 6 | Akihabara: Animate / Mandarake / Radio Kaikan | Akihabara Radio Kaikan, Japan | Akihabara Radio Kaikan, 16, Soto-Kanda 1, Soto-Kanda, Chiyoda, Tokyo,  | 47 |
| 16 | 7 | Hara Shobo, Jimbocho | Hara Shobo Jimbocho, Japan | Hara Shobo Japanese Ukiyo-e Prints, 22, Kanda-Jimbocho 2, Kanda-Jimboc | 160 |
| 16 | 8 | Ginza | 銀座四丁目交差点 | Ginza Crossing, Ginza, Ginza 5, Ginza, Chuo, Tokyo, 104-0061, Japan | 54 |
| 16 | 9 | Dinner, then pack | Shinjuku Kakekomi Gyoza, Japan | Shinjuku Kakekomi Gyoza, Central Road, Kabukichō 1, Kabukichō, Shinjuk | 421 |
| 17 | 1 | APA Hotel Kabukicho Tower | APA Hotel Higashi Shinjuku Kabukicho Tower, Japan | APA Hotel, Shokuan Street, Kabukichō 2, Kabukichō, Shinjuku, Tokyo, 16 | 273 |
| 17 | 2 | Tokyu Kabukicho Tower bus stop | Tokyu Kabukicho Tower, Japan | Tokyu Kabukicho Tower, 1, Kabukichō 1, Kabukichō, Shinjuku, Tokyo, 160 | 21 |
| 17 | 3 | Narita Airport Terminal 2 | Narita Airport Terminal 2, Japan | Narita Airport Terminal 2, Central Square, Furugome, Narita, Chiba Pre | 56 |
| 17 | 4 | Depart CX527 → HKG → CX663 | Narita Airport Terminal 2, Japan | Narita Airport Terminal 2, Central Square, Furugome, Narita, Chiba Pre | 56 |
