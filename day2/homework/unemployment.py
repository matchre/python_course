# coding: utf-8 

data = [
    {"municipality":"Ale","unemployment_2009":5.5,"unemployment_2014":4.9},
    {"municipality":"Alingsås","unemployment_2009":5.7,"unemployment_2014":6},
    {"municipality":"Alvesta","unemployment_2009":4.7,"unemployment_2014":8.9},
    {"municipality":"Aneby","unemployment_2009":4.9,"unemployment_2014":6.2},
    {"municipality":"Arboga","unemployment_2009":6.5,"unemployment_2014":9.4},
    {"municipality":"Arjeplog","unemployment_2009":6.1,"unemployment_2014":5.6},
    {"municipality":"Arvidsjaur","unemployment_2009":7.8,"unemployment_2014":7.7},
    {"municipality":"Arvika","unemployment_2009":7,"unemployment_2014":6.9},
    {"municipality":"Askersund","unemployment_2009":5.7,"unemployment_2014":5.5},
    {"municipality":"Avesta","unemployment_2009":5.8,"unemployment_2014":8.1},
    {"municipality":"Bengtsfors","unemployment_2009":8,"unemployment_2014":8.3},
    {"municipality":"Berg","unemployment_2009":6.4,"unemployment_2014":7.3},
    {"municipality":"Bjurholm","unemployment_2009":5.7,"unemployment_2014":9.2},
    {"municipality":"Bjuv","unemployment_2009":7,"unemployment_2014":8.2},
    {"municipality":"Boden","unemployment_2009":6.7,"unemployment_2014":7.8},
    {"municipality":"Bollebygd","unemployment_2009":5.3,"unemployment_2014":4.4},
    {"municipality":"Bollnäs","unemployment_2009":8.6,"unemployment_2014":10.4},
    {"municipality":"Borgholm","unemployment_2009":4.6,"unemployment_2014":5.5},
    {"municipality":"Borlänge","unemployment_2009":6.2,"unemployment_2014":7.2},
    {"municipality":"Borås","unemployment_2009":6.3,"unemployment_2014":6.6},
    {"municipality":"Botkyrka","unemployment_2009":6.2,"unemployment_2014":9.6},
    {"municipality":"Boxholm","unemployment_2009":6.1,"unemployment_2014":6.4},
    {"municipality":"Bromölla","unemployment_2009":6.9,"unemployment_2014":9},
    {"municipality":"Bräcke","unemployment_2009":9.8,"unemployment_2014":8.4},
    {"municipality":"Burlöv","unemployment_2009":7.1,"unemployment_2014":9},
    {"municipality":"Båstad","unemployment_2009":4,"unemployment_2014":6},
    {"municipality":"Dals-Ed","unemployment_2009":7.3,"unemployment_2014":6.8},
    {"municipality":"Danderyd","unemployment_2009":1.6,"unemployment_2014":2},
    {"municipality":"Degerfors","unemployment_2009":7.2,"unemployment_2014":7.8},
    {"municipality":"Dorotea","unemployment_2009":9,"unemployment_2014":7.6},
    {"municipality":"Eda","unemployment_2009":5.5,"unemployment_2014":5.7},
    {"municipality":"Ekerö","unemployment_2009":1.8,"unemployment_2014":2.7},
    {"municipality":"Eksjö","unemployment_2009":4.5,"unemployment_2014":5.8},
    {"municipality":"Emmaboda","unemployment_2009":5.9,"unemployment_2014":7.5},
    {"municipality":"Enköping","unemployment_2009":4.4,"unemployment_2014":4.8},
    {"municipality":"Eskilstuna","unemployment_2009":9,"unemployment_2014":11.3},
    {"municipality":"Eslöv","unemployment_2009":4.8,"unemployment_2014":6.5},
    {"municipality":"Essunga","unemployment_2009":5.2,"unemployment_2014":5.1},
    {"municipality":"Fagersta","unemployment_2009":6.6,"unemployment_2014":9.7},
    {"municipality":"Falkenberg","unemployment_2009":5.7,"unemployment_2014":5.7},
    {"municipality":"Falköping","unemployment_2009":5.8,"unemployment_2014":7.2},
    {"municipality":"Falun","unemployment_2009":5.9,"unemployment_2014":5.8},
    {"municipality":"Filipstad","unemployment_2009":9.2,"unemployment_2014":9.5},
    {"municipality":"Finspång","unemployment_2009":5.6,"unemployment_2014":9.1},
    {"municipality":"Flen","unemployment_2009":7.1,"unemployment_2014":10.4},
    {"municipality":"Forshaga","unemployment_2009":7.5,"unemployment_2014":8.2},
    {"municipality":"Färgelanda","unemployment_2009":7.7,"unemployment_2014":7},
    {"municipality":"Gagnef","unemployment_2009":5.4,"unemployment_2014":4.7},
    {"municipality":"Gislaved","unemployment_2009":6.6,"unemployment_2014":7.2},
    {"municipality":"Gnesta","unemployment_2009":4.1,"unemployment_2014":5.4},
    {"municipality":"Gnosjö","unemployment_2009":7,"unemployment_2014":6.2},
    {"municipality":"Gotland","unemployment_2009":6.5,"unemployment_2014":7.9},
    {"municipality":"Grums","unemployment_2009":8.4,"unemployment_2014":8.7},
    {"municipality":"Grästorp","unemployment_2009":6,"unemployment_2014":6.9},
    {"municipality":"Gullspång","unemployment_2009":7.3,"unemployment_2014":9.9},
    {"municipality":"Gällivare","unemployment_2009":7.4,"unemployment_2014":6.8},
    {"municipality":"Gävle","unemployment_2009":8.6,"unemployment_2014":10.2},
    {"municipality":"Göteborg","unemployment_2009":6.1,"unemployment_2014":6.7},
    {"municipality":"Götene","unemployment_2009":5.5,"unemployment_2014":5.3},
    {"municipality":"Habo","unemployment_2009":4.1,"unemployment_2014":3.7},
    {"municipality":"Hagfors","unemployment_2009":9,"unemployment_2014":9.2},
    {"municipality":"Hallsberg","unemployment_2009":7.4,"unemployment_2014":7.8},
    {"municipality":"Hallstahammar","unemployment_2009":7,"unemployment_2014":8.5},
    {"municipality":"Halmstad","unemployment_2009":5.8,"unemployment_2014":7.2},
    {"municipality":"Hammarö","unemployment_2009":5.9,"unemployment_2014":5.5},
    {"municipality":"Haninge","unemployment_2009":4,"unemployment_2014":5.7},
    {"municipality":"Haparanda","unemployment_2009":15,"unemployment_2014":11.5},
    {"municipality":"Heby","unemployment_2009":5.2,"unemployment_2014":6.1},
    {"municipality":"Hedemora","unemployment_2009":4.9,"unemployment_2014":6.5},
    {"municipality":"Helsingborg","unemployment_2009":6.7,"unemployment_2014":8.5},
    {"municipality":"Herrljunga","unemployment_2009":5.9,"unemployment_2014":5.3},
    {"municipality":"Hjo","unemployment_2009":6.1,"unemployment_2014":5.8},
    {"municipality":"Hofors","unemployment_2009":7.8,"unemployment_2014":8.1},
    {"municipality":"Huddinge","unemployment_2009":4.4,"unemployment_2014":5.4},
    {"municipality":"Hudiksvall","unemployment_2009":7.7,"unemployment_2014":7.9},
    {"municipality":"Hultsfred","unemployment_2009":8.3,"unemployment_2014":8.4},
    {"municipality":"Hylte","unemployment_2009":4.6,"unemployment_2014":6.7},
    {"municipality":"Håbo","unemployment_2009":2.7,"unemployment_2014":3.9},
    {"municipality":"Hällefors","unemployment_2009":8.9,"unemployment_2014":9.1},
    {"municipality":"Härjedalen","unemployment_2009":5.5,"unemployment_2014":6.4},
    {"municipality":"Härnösand","unemployment_2009":7.9,"unemployment_2014":8.9},
    {"municipality":"Härryda","unemployment_2009":3.3,"unemployment_2014":3.7},
    {"municipality":"Hässleholm","unemployment_2009":7.1,"unemployment_2014":8.9},
    {"municipality":"Höganäs","unemployment_2009":4.6,"unemployment_2014":5.5},
    {"municipality":"Högsby","unemployment_2009":5.1,"unemployment_2014":8.1},
    {"municipality":"Hörby","unemployment_2009":4.5,"unemployment_2014":5.9},
    {"municipality":"Höör","unemployment_2009":4.8,"unemployment_2014":5.1},
    {"municipality":"Jokkmokk","unemployment_2009":7.1,"unemployment_2014":6.7},
    {"municipality":"Järfälla","unemployment_2009":3.6,"unemployment_2014":7},
    {"municipality":"Jönköping","unemployment_2009":5.3,"unemployment_2014":5.4},
    {"municipality":"Kalix","unemployment_2009":12.1,"unemployment_2014":8.7},
    {"municipality":"Kalmar","unemployment_2009":5.7,"unemployment_2014":6.5},
    {"municipality":"Karlsborg","unemployment_2009":4.7,"unemployment_2014":6.5},
    {"municipality":"Karlshamn","unemployment_2009":7,"unemployment_2014":8.4},
    {"municipality":"Karlskoga","unemployment_2009":7.6,"unemployment_2014":8.2},
    {"municipality":"Karlskrona","unemployment_2009":6.7,"unemployment_2014":8.3},
    {"municipality":"Karlstad","unemployment_2009":6.5,"unemployment_2014":7.1},
    {"municipality":"Katrineholm","unemployment_2009":8,"unemployment_2014":9.6},
    {"municipality":"Kil","unemployment_2009":7.6,"unemployment_2014":7.3},
    {"municipality":"Kinda","unemployment_2009":5.2,"unemployment_2014":7.1},
    {"municipality":"Kiruna","unemployment_2009":6.2,"unemployment_2014":3.5},
    {"municipality":"Klippan","unemployment_2009":6.7,"unemployment_2014":7.3},
    {"municipality":"Knivsta","unemployment_2009":2.7,"unemployment_2014":2.9},
    {"municipality":"Kramfors","unemployment_2009":9.5,"unemployment_2014":10},
    {"municipality":"Kristianstad","unemployment_2009":6.9,"unemployment_2014":8.9},
    {"municipality":"Kristinehamn","unemployment_2009":8,"unemployment_2014":9.7},
    {"municipality":"Krokom","unemployment_2009":5.8,"unemployment_2014":5.8},
    {"municipality":"Kumla","unemployment_2009":6.8,"unemployment_2014":6.1},
    {"municipality":"Kungsbacka","unemployment_2009":3.3,"unemployment_2014":3.4},
    {"municipality":"Kungsör","unemployment_2009":5.2,"unemployment_2014":8.7},
    {"municipality":"Kungälv","unemployment_2009":3.4,"unemployment_2014":2.9},
    {"municipality":"Kävlinge","unemployment_2009":3.9,"unemployment_2014":4.7},
    {"municipality":"Köping","unemployment_2009":7.2,"unemployment_2014":8.6},
    {"municipality":"Laholm","unemployment_2009":6,"unemployment_2014":6.2},
    {"municipality":"Landskrona","unemployment_2009":8.3,"unemployment_2014":11.8},
    {"municipality":"Laxå","unemployment_2009":7.3,"unemployment_2014":9.7},
    {"municipality":"Lekeberg","unemployment_2009":5.2,"unemployment_2014":4.8},
    {"municipality":"Leksand","unemployment_2009":5.4,"unemployment_2014":5},
    {"municipality":"Lerum","unemployment_2009":3.1,"unemployment_2014":3},
    {"municipality":"Lessebo","unemployment_2009":7.7,"unemployment_2014":11.7},
    {"municipality":"Lidingö","unemployment_2009":1.9,"unemployment_2014":3.3},
    {"municipality":"Lidköping","unemployment_2009":4.8,"unemployment_2014":6.6},
    {"municipality":"Lilla Edet","unemployment_2009":6.3,"unemployment_2014":7.3},
    {"municipality":"Lindesberg","unemployment_2009":8.2,"unemployment_2014":8.4},
    {"municipality":"Linköping","unemployment_2009":5.5,"unemployment_2014":5.4},
    {"municipality":"Ljungby","unemployment_2009":4.8,"unemployment_2014":5.6},
    {"municipality":"Ljusdal","unemployment_2009":8.8,"unemployment_2014":9.2},
    {"municipality":"Ljusnarsberg","unemployment_2009":7.4,"unemployment_2014":10.1},
    {"municipality":"Lomma","unemployment_2009":2.6,"unemployment_2014":3},
    {"municipality":"Ludvika","unemployment_2009":5.6,"unemployment_2014":6.6},
    {"municipality":"Luleå","unemployment_2009":7.6,"unemployment_2014":6.5},
    {"municipality":"Lund","unemployment_2009":3.5,"unemployment_2014":4.1},
    {"municipality":"Lycksele","unemployment_2009":7,"unemployment_2014":7.5},
    {"municipality":"Lysekil","unemployment_2009":5.7,"unemployment_2014":4.2},
    {"municipality":"Malmö","unemployment_2009":6.4,"unemployment_2014":10.5},
    {"municipality":"Malung-Sälen","unemployment_2009":5.5,"unemployment_2014":4.2},
    {"municipality":"Malå","unemployment_2009":7.2,"unemployment_2014":6.5},
    {"municipality":"Mariestad","unemployment_2009":7.8,"unemployment_2014":8.5},
    {"municipality":"Mark","unemployment_2009":4.5,"unemployment_2014":4.8},
    {"municipality":"Markaryd","unemployment_2009":5.4,"unemployment_2014":7.4},
    {"municipality":"Mellerud","unemployment_2009":6.2,"unemployment_2014":8.1},
    {"municipality":"Mjölby","unemployment_2009":6.6,"unemployment_2014":6.7},
    {"municipality":"Mora","unemployment_2009":6.5,"unemployment_2014":5.7},
    {"municipality":"Motala","unemployment_2009":8.1,"unemployment_2014":9},
    {"municipality":"Mullsjö","unemployment_2009":6.1,"unemployment_2014":4.4},
    {"municipality":"Munkedal","unemployment_2009":6.1,"unemployment_2014":5.1},
    {"municipality":"Munkfors","unemployment_2009":10.3,"unemployment_2014":9.6},
    {"municipality":"Mölndal","unemployment_2009":4.3,"unemployment_2014":4},
    {"municipality":"Mönsterås","unemployment_2009":5.7,"unemployment_2014":7.2},
    {"municipality":"Mörbylånga","unemployment_2009":4.7,"unemployment_2014":4.1},
    {"municipality":"Nacka","unemployment_2009":3,"unemployment_2014":3.8},
    {"municipality":"Nora","unemployment_2009":7.1,"unemployment_2014":6.9},
    {"municipality":"Norberg","unemployment_2009":6.3,"unemployment_2014":8.3},
    {"municipality":"Nordanstig","unemployment_2009":7.6,"unemployment_2014":7.2},
    {"municipality":"Nordmaling","unemployment_2009":7.7,"unemployment_2014":8.5},
    {"municipality":"Norrköping","unemployment_2009":8.1,"unemployment_2014":10.2},
    {"municipality":"Norrtälje","unemployment_2009":3,"unemployment_2014":4.1},
    {"municipality":"Norsjö","unemployment_2009":10,"unemployment_2014":8.2},
    {"municipality":"Nybro","unemployment_2009":6.2,"unemployment_2014":6.7},
    {"municipality":"Nykvarn","unemployment_2009":2.6,"unemployment_2014":3.4},
    {"municipality":"Nyköping","unemployment_2009":6.5,"unemployment_2014":6.7},
    {"municipality":"Nynäshamn","unemployment_2009":4.2,"unemployment_2014":5.5},
    {"municipality":"Nässjö","unemployment_2009":6.2,"unemployment_2014":7.8},
    {"municipality":"Ockelbo","unemployment_2009":7.6,"unemployment_2014":9.1},
    {"municipality":"Olofström","unemployment_2009":9.2,"unemployment_2014":10.6},
    {"municipality":"Orsa","unemployment_2009":8.1,"unemployment_2014":6.9},
    {"municipality":"Orust","unemployment_2009":4,"unemployment_2014":3.9},
    {"municipality":"Osby","unemployment_2009":6.4,"unemployment_2014":7.8},
    {"municipality":"Oskarshamn","unemployment_2009":3.7,"unemployment_2014":5.1},
    {"municipality":"Ovanåker","unemployment_2009":9.6,"unemployment_2014":9},
    {"municipality":"Oxelösund","unemployment_2009":6.5,"unemployment_2014":7.1},
    {"municipality":"Pajala","unemployment_2009":12.6,"unemployment_2014":6},
    {"municipality":"Partille","unemployment_2009":3.7,"unemployment_2014":4.1},
    {"municipality":"Perstorp","unemployment_2009":6.2,"unemployment_2014":10.6},
    {"municipality":"Piteå","unemployment_2009":7.2,"unemployment_2014":6.8},
    {"municipality":"Ragunda","unemployment_2009":9.3,"unemployment_2014":9.4},
    {"municipality":"Robertsfors","unemployment_2009":7.7,"unemployment_2014":5.4},
    {"municipality":"Ronneby","unemployment_2009":9.5,"unemployment_2014":10.5},
    {"municipality":"Rättvik","unemployment_2009":6.6,"unemployment_2014":6.2},
    {"municipality":"Sala","unemployment_2009":6,"unemployment_2014":8},
    {"municipality":"Salem","unemployment_2009":3.2,"unemployment_2014":4.6},
    {"municipality":"Sandviken","unemployment_2009":8.3,"unemployment_2014":10.4},
    {"municipality":"Sigtuna","unemployment_2009":3.8,"unemployment_2014":5.4},
    {"municipality":"Simrishamn","unemployment_2009":6.6,"unemployment_2014":6.4},
    {"municipality":"Sjöbo","unemployment_2009":5.2,"unemployment_2014":6.1},
    {"municipality":"Skara","unemployment_2009":6.3,"unemployment_2014":7.5},
    {"municipality":"Skellefteå","unemployment_2009":8.1,"unemployment_2014":7.4},
    {"municipality":"Skinnskatteberg","unemployment_2009":5.2,"unemployment_2014":7},
    {"municipality":"Skurup","unemployment_2009":5.5,"unemployment_2014":6.4},
    {"municipality":"Skövde","unemployment_2009":6.9,"unemployment_2014":6.4},
    {"municipality":"Smedjebacken","unemployment_2009":5.6,"unemployment_2014":4.9},
    {"municipality":"Sollefteå","unemployment_2009":9.7,"unemployment_2014":11.6},
    {"municipality":"Sollentuna","unemployment_2009":3.2,"unemployment_2014":4},
    {"municipality":"Solna","unemployment_2009":2.7,"unemployment_2014":4.1},
    {"municipality":"Sorsele","unemployment_2009":5.3,"unemployment_2014":5.8},
    {"municipality":"Sotenäs","unemployment_2009":3.6,"unemployment_2014":4.4},
    {"municipality":"Staffanstorp","unemployment_2009":3.4,"unemployment_2014":4.2},
    {"municipality":"Stenungsund","unemployment_2009":3.8,"unemployment_2014":3.6},
    {"municipality":"Stockholm","unemployment_2009":4,"unemployment_2014":5.1},
    {"municipality":"Storfors","unemployment_2009":9.1,"unemployment_2014":11.5},
    {"municipality":"Storuman","unemployment_2009":5.8,"unemployment_2014":6.3},
    {"municipality":"Strängnäs","unemployment_2009":5.2,"unemployment_2014":6.8},
    {"municipality":"Strömstad","unemployment_2009":4.1,"unemployment_2014":4.6},
    {"municipality":"Strömsund","unemployment_2009":11.3,"unemployment_2014":9.4},
    {"municipality":"Sundbyberg","unemployment_2009":3.9,"unemployment_2014":6.7},
    {"municipality":"Sundsvall","unemployment_2009":7.2,"unemployment_2014":8.1},
    {"municipality":"Sunne","unemployment_2009":7.4,"unemployment_2014":6.1},
    {"municipality":"Surahammar","unemployment_2009":6.3,"unemployment_2014":7.3},
    {"municipality":"Svalöv","unemployment_2009":5,"unemployment_2014":7.3},
    {"municipality":"Svedala","unemployment_2009":3.6,"unemployment_2014":4.8},
    {"municipality":"Svenljunga","unemployment_2009":5.6,"unemployment_2014":4.4},
    {"municipality":"Säffle","unemployment_2009":7.2,"unemployment_2014":10.7},
    {"municipality":"Säter","unemployment_2009":4.5,"unemployment_2014":4.8},
    {"municipality":"Sävsjö","unemployment_2009":6,"unemployment_2014":6.2},
    {"municipality":"Söderhamn","unemployment_2009":9.8,"unemployment_2014":10.4},
    {"municipality":"Söderköping","unemployment_2009":4.4,"unemployment_2014":5.9},
    {"municipality":"Södertälje","unemployment_2009":6.7,"unemployment_2014":11.3},
    {"municipality":"Sölvesborg","unemployment_2009":8.1,"unemployment_2014":8.3},
    {"municipality":"Tanum","unemployment_2009":5.5,"unemployment_2014":4.7},
    {"municipality":"Tibro","unemployment_2009":8.1,"unemployment_2014":8.6},
    {"municipality":"Tidaholm","unemployment_2009":6.6,"unemployment_2014":6.3},
    {"municipality":"Tierp","unemployment_2009":6.1,"unemployment_2014":7.6},
    {"municipality":"Timrå","unemployment_2009":8.9,"unemployment_2014":9},
    {"municipality":"Tingsryd","unemployment_2009":5.3,"unemployment_2014":6.4},
    {"municipality":"Tjörn","unemployment_2009":3.3,"unemployment_2014":3},
    {"municipality":"Tomelilla","unemployment_2009":6.7,"unemployment_2014":7.6},
    {"municipality":"Torsby","unemployment_2009":6.7,"unemployment_2014":6.1},
    {"municipality":"Torsås","unemployment_2009":6.4,"unemployment_2014":7.3},
    {"municipality":"Tranemo","unemployment_2009":4,"unemployment_2014":4.5},
    {"municipality":"Tranås","unemployment_2009":4.7,"unemployment_2014":7.4},
    {"municipality":"Trelleborg","unemployment_2009":6,"unemployment_2014":7.9},
    {"municipality":"Trollhättan","unemployment_2009":8.6,"unemployment_2014":11.5},
    {"municipality":"Trosa","unemployment_2009":3.7,"unemployment_2014":4.1},
    {"municipality":"Tyresö","unemployment_2009":2.8,"unemployment_2014":3.5},
    {"municipality":"Täby","unemployment_2009":1.8,"unemployment_2014":2.4},
    {"municipality":"Töreboda","unemployment_2009":8.2,"unemployment_2014":9},
    {"municipality":"Uddevalla","unemployment_2009":6.7,"unemployment_2014":7.5},
    {"municipality":"Ulricehamn","unemployment_2009":5,"unemployment_2014":4.5},
    {"municipality":"Umeå","unemployment_2009":5.3,"unemployment_2014":5.3},
    {"municipality":"Upplands Väsby","unemployment_2009":3.8,"unemployment_2014":5.1},
    {"municipality":"Upplands-Bro","unemployment_2009":3.9,"unemployment_2014":6.1},
    {"municipality":"Uppsala","unemployment_2009":3.7,"unemployment_2014":4.1},
    {"municipality":"Uppvidinge","unemployment_2009":6.8,"unemployment_2014":8.3},
    {"municipality":"Vadstena","unemployment_2009":5.5,"unemployment_2014":6},
    {"municipality":"Vaggeryd","unemployment_2009":6.4,"unemployment_2014":6.3},
    {"municipality":"Valdemarsvik","unemployment_2009":5.9,"unemployment_2014":7.4},
    {"municipality":"Vallentuna","unemployment_2009":1.7,"unemployment_2014":2.2},
    {"municipality":"Vansbro","unemployment_2009":6.9,"unemployment_2014":5.9},
    {"municipality":"Vara","unemployment_2009":5.2,"unemployment_2014":6.3},
    {"municipality":"Varberg","unemployment_2009":4,"unemployment_2014":4.1},
    {"municipality":"Vaxholm","unemployment_2009":1.5,"unemployment_2014":2.2},
    {"municipality":"Vellinge","unemployment_2009":2.8,"unemployment_2014":4},
    {"municipality":"Vetlanda","unemployment_2009":5.5,"unemployment_2014":5.5},
    {"municipality":"Vilhelmina","unemployment_2009":8.8,"unemployment_2014":10.8},
    {"municipality":"Vimmerby","unemployment_2009":7,"unemployment_2014":5.8},
    {"municipality":"Vindeln","unemployment_2009":7.5,"unemployment_2014":5.7},
    {"municipality":"Vingåker","unemployment_2009":6.3,"unemployment_2014":9.6},
    {"municipality":"Vårgårda","unemployment_2009":6,"unemployment_2014":5.7},
    {"municipality":"Vänersborg","unemployment_2009":6.5,"unemployment_2014":8.5},
    {"municipality":"Vännäs","unemployment_2009":4.4,"unemployment_2014":6},
    {"municipality":"Värmdö","unemployment_2009":2.7,"unemployment_2014":3.5},
    {"municipality":"Värnamo","unemployment_2009":5.7,"unemployment_2014":5.6},
    {"municipality":"Västervik","unemployment_2009":7.1,"unemployment_2014":7.5},
    {"municipality":"Västerås","unemployment_2009":6.7,"unemployment_2014":7.6},
    {"municipality":"Växjö","unemployment_2009":5.9,"unemployment_2014":7.2},
    {"municipality":"Ydre","unemployment_2009":4.8,"unemployment_2014":3.6},
    {"municipality":"Ystad","unemployment_2009":5.3,"unemployment_2014":5.6},
    {"municipality":"Åmål","unemployment_2009":9.4,"unemployment_2014":10},
    {"municipality":"Ånge","unemployment_2009":8.1,"unemployment_2014":9.5},
    {"municipality":"Åre","unemployment_2009":4.1,"unemployment_2014":4.4},
    {"municipality":"Årjäng","unemployment_2009":5.2,"unemployment_2014":6.2},
    {"municipality":"Åsele","unemployment_2009":9.2,"unemployment_2014":8.3},
    {"municipality":"Åstorp","unemployment_2009":7.6,"unemployment_2014":8.4},
    {"municipality":"Åtvidaberg","unemployment_2009":7.8,"unemployment_2014":6.4},
    {"municipality":"Älmhult","unemployment_2009":4.5,"unemployment_2014":4.9},
    {"municipality":"Älvdalen","unemployment_2009":7.3,"unemployment_2014":6.6},
    {"municipality":"Älvkarleby","unemployment_2009":6.8,"unemployment_2014":9.4},
    {"municipality":"Älvsbyn","unemployment_2009":8.9,"unemployment_2014":7.9},
    {"municipality":"Ängelholm","unemployment_2009":5.5,"unemployment_2014":6.3},
    {"municipality":"Öckerö","unemployment_2009":3.3,"unemployment_2014":3.2},
    {"municipality":"Ödeshög","unemployment_2009":6.9,"unemployment_2014":6.7},
    {"municipality":"Örebro","unemployment_2009":6.9,"unemployment_2014":7.2},
    {"municipality":"Örkelljunga","unemployment_2009":4.9,"unemployment_2014":7.5},
    {"municipality":"Örnsköldsvik","unemployment_2009":7.2,"unemployment_2014":7.8},
    {"municipality":"Östersund","unemployment_2009":6.5,"unemployment_2014":7},
    {"municipality":"Österåker","unemployment_2009":2.1,"unemployment_2014":3},
    {"municipality":"Östhammar","unemployment_2009":3,"unemployment_2014":4.2},
    {"municipality":"Östra Göinge","unemployment_2009":8.3,"unemployment_2014":9.9},
    {"municipality":"Överkalix","unemployment_2009":13,"unemployment_2014":10},
    {"municipality":"Övertorneå","unemployment_2009":13,"unemployment_2014":9.3}
]