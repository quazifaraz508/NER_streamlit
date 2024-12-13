import re

cities_Andra_pradesh = 'Adoni | Anantapuram | Amaravati | Bhimavaram | Chilakaluripet | Chittoor | Dharmavaram | Eluru | Gudivada | Guntakal | Guntur | Hindupur | Kadapa | Kadiri | Kakinada | Kurnool | Machilipatnam | Madanapalle | Mangalagiri-Tadepalli | Nandyal | Narasaraopet | Nellore | Ongole | Proddatur | Rajamahendravaram | Srikakulam | Tadepalligudem | Tadipatri | Tenali | Tirupati | Vijayawada | Visakhapatnam | Vizianagaram'
towns_andra_pradesh ='Repalle | Venkatagiri | Amalapuram | Payakaraopeta | Jaggayyapeta | Parvathipuram | Palamaner | Rajampet | Puttur | Punganur | Pithapuram | Bheemunipatnam | Mandapeta | Sattenapalle | Bobbili | Samarlakota | Kandukuru | Macherla | Palasa | Nuzvid | Narasapuram | Dhone | Ponnur | Pileru | Rayadurgam | Nagari | Vinukonda | Piduguralla | Tadepalle | Pulivendula | Badvel | Bapatla | Markapuram | Gudur | Tanuku | Srikalahasti | Palakollu | Anakapalli | Kadiri | Kavali | Rayachoti | Chirala | Yemmiganur'
villages_andra_pradesh ='Ambugaon | Anderband | Antargaon | Arli | Arli T | Bandalnagapur | Belsari Rampur | Bheempoor | Dabbakuchi | Dhanora | Ghotkuri | Girgaon | Gollaghat | Gomutri | Gona | Guledi | Gunjala | Hasnapur | Jamdi | Kamathwada | Karanji | Khapperla | Nipani | Palodi Ramnagar | Pippalkhoti | Ponnari | Savargaon | Tamsi | Tamsi | Waddadi | Wadgaon | Wadoor | Adilabad | Ankapoor | Ankoli | Anukunta | Arli | Asodabhurki | Battisawargaon | Belluri | Bheemseri | Borenur | Chanda | Chichadhari | Chinchughat | Dimma | Hathigutta | Jamdapur | Jamuldhari | Kachkanti | Khanapoor | Khandala | Kottur | Nevegaon| Kumbhajheri | Landasangvi | Lohara | Lokari | Maleborgaon | Maregaon | Mavala | Nishanghat | Pippaldhari | Pochara | Ramai | Rampoor | Royati | Takli | Tippa | Tontoli | Waghapur | Wanwat | Yapalguda | Ada | Akoli | Akurla | Bahadurpur | Balapur | Ballori | Belgaon | Bhoraj | Deepaiguda | Dollara | Fouzpur | Gimma | Guda | Hashampur | Hathighat | Jainad | Jamini | Kamai | Kamtha | Kanpa | Mediguda | Karanji | Kedarpur | Khapri | Korta | Kowtha | Kura | Laxmipur |Uligan | Lekarwadi | Makoda | Mangurla | Moudagada | Muktapur | Nirala | Nizampur | Pardi  | Pardi | Khurd | Pendalwada | Pippalgaon | Pipparwada | Poosai | Rampurtaraf | Sangvi | Savapur | Sirsonna | Tarada  Umri | Awalpur | Bela | Bhadi | Bhedoda | Bhodod |Kopsi | Boregaon | Chandpalle | Chaprala | Dehegaon | Dhoptala | Douna | Ekori | Guda | Junoni | Kamgarpur | Karoni | Karoni | Khadki | Khagdur | Kobhai | Mangrool | Manyarpur | Masala  | Masala | Mohabatpur | Patan | Pitgaon | Pohar | Ponnala | Ramkam | Sadarpur | Sahej | Sangdi | Sangvi | Shamshabad | Sirsanna | Sonkhos | Syedpur | Takli | Toyaguda | Kora | Warur | Arli  | Bharampur | Dehegaon | Devapur | Dorli | Jhari | Kajjarla | Kappardevi | Khodad | Kosai | Kothur | Kuchalapoor | Lachampur | Lingi | Madnapoor | Nandigaon | Palasi  | Palasi| Palle  | Palle | Ratnapur | Ruyyadi | Saknapoor | Sunkidi | Talamadugu | Umadam | Umrei | Belluri | Dhampur | Dongargaon | Gondharkapur | Gudihathinur | Guruj | Kamalapur | Kolhari | Lingapur | Machapur | Malkapur | Mannur | Muthnur | Neradigonda | Rendlabori | Seetagondi'

states = ' Andhra Pradesh | Arunachal Pradesh | Assam | Bihar | Chhattisgarh | Goa |goa| Goa| Gujarat | Haryana | Himachal Pradesh | Jharkhand | Karnataka | Kerala | Madhya Pradesh | Maharashtra | Manipur | Meghalaya | Mizoram | Nagaland | Odisha | Punjab | Rajasthan | Sikkim | Tamil Nadu | Telangana | Tripura | Uttar Pradesh | Uttarakhand | West Bengal |Andaman and Nicobar Islands | Chandigarh | Dadra and Nagar Haveli and Daman and Diu | Delhi | Lakshadweep | Jammu and Kashmir | Ladakh | Puducherry'
cities =  'Mumbai | bombay | Bambai | Calcutta | Bangalore | Kolkata | Chennai | Hyderabad | Ahmedabad | Pune | Jaipur | Surat | Lucknow | Kanpur | Nagpur | Visakhapatnam | Vadodara | Ghaziabad | Rajkot | Coimbatore | Patna | Agra | Madurai | Nashik | Faridabad | Ludhiana | Vijayawada | Aurangabad | Bhopal | Jodhpur | Guwahati | Kochi | Mysore | Dehradun | Indore | Itanagar | Naharlagun | Dibrugarh | Silchar | Jorhat | Gaya | Bhagalpur | Muzaffarpur | Raipur | Bhilai | Bilaspur | Panaji | Margao | Vasco da Gama | Gurgaon | Ambala | Shimla | Dharamshala | Mandi | Ranchi | Jamshedpur | Dhanbad | Thiruvananthapuram | Kozhikode | Bhubaneswar | Cuttack | Rourkela | Amritsar | Jalandhar | Udaipur | Gangtok | Warangal | Agartala | Siliguri | Durgapur |Mumbai| bombay| Bambai| Calcutta | Bangalore| Kolkata| Chennai| Hyderabad| Ahmedabad| Pune| Jaipur| Surat| Lucknow| Kanpur| Nagpur| Visakhapatnam| Vadodara| Ghaziabad| Rajkot| Coimbatore| Patna| Agra| Madurai| Nashik| Faridabad| Ludhiana| Vijayawada| Aurangabad| Bhopal| Jodhpur| Guwahati| Kochi| Mysore| Dehradun| Indore| Itanagar| Naharlagun| Dibrugarh| Silchar| Jorhat| Gaya| Bhagalpur| Muzaffarpur| Raipur| Bhilai| Bilaspur| Panaji| Margao| Vasco da Gama| Gurgaon| Ambala| Shimla| Dharamshala| Mandi| Ranchi| Jamshedpur| Dhanbad| Thiruvananthapuram| Kozhikode| Bhubaneswar| Cuttack| Rourkela| Amritsar| Jalandhar| Udaipur| Gangtok| Warangal| Agartala| Siliguri| Durgapur|Mumbai |bombay |Bambai |Calcutta |Bangalore |Kolkata |Chennai |Hyderabad |Ahmedabad |Pune |Jaipur |Surat |Lucknow |Kanpur |Nagpur |Visakhapatnam |Vadodara |Ghaziabad |Rajkot |Coimbatore |Patna |Agra |Madurai |Nashik |Faridabad |Ludhiana |Vijayawada |Aurangabad |Bhopal |Jodhpur |Guwahati |Kochi |Mysore |Dehradun |Indore |Itanagar |Naharlagun |Dibrugarh |Silchar |Jorhat |Gaya |Bhagalpur |Muzaffarpur |Raipur |Bhilai |Bilaspur |Panaji |Margao |Vasco da Gama |Gurgaon |Ambala |Shimla |Dharamshala |Mandi |Ranchi |Jamshedpur |Dhanbad |Thiruvananthapuram |Kozhikode |Bhubaneswar |Cuttack |Rourkela |Amritsar |Jalandhar |Udaipur |Gangtok |Warangal |Agartala |Siliguri |Durgapur '


cities_Arunachal_Pradesh = 'Bordumsa | Changlang | Jairampur | Kharsang | Khemiyong | Manmao | Miao | Nampong | Vijaynagar | Vijoypur | Anini | Bameng | Bana | Chyangtajo | Khenewa | P.kessang | Palizi | Pipu-dipu | Seijosa | Seppa | Thrizino | Veo | Adipasi | Boleng | Borguli | Damro | Gtc | Pasighat | Ruksin | Chakma | Danglat | Kamlang Nagar | Kherem | Lohitpur | Medo | Namsai | Tezu | Wakro | Bomdila | Dirang | Kalaktang | Tawang | Basar | Likabali | Logum Jining | Roing | Daporijo | Balukpong'

villages_Arunachal_Pradesh = 'Bubang | Chopelling | Deban | Dharampur | Gandhigrams | Bisa | Kutum | Lallung | Manabhum | Namchik | Namdang | Namphai | Namtok | New Kamlao | New Mohang | Rajanagar | Rangfrah | Ranglom | Two-hat | Yangkang | Alinye | Anelih | Etalin | Ayeng | Balek | Bilat | Dalbing | Debing | Hill Top | Kebang | Korang | Koyu | Ledum | Mebo | Nari | Ngopok | Oyan | Pangin | Rani | Renging | Riga | Sille | Silluk | Sirem | Yagrung | Mirem | Mikong | Chambang | Damin | Hiya | Nyapin | Palin | Sangram | Sarli | Tali | Alubari | Changliang | Chowkham | Gohaingaon | Innao | Jaipur | Kumari Kachari | Kumsai | Lathao | Loiliang | Mahadevpur | Momong | Nanam | Peyong | Podumani | Sunpura | Tafragram | Tindolong | Udaipur | Wingko | Yealing | Abango | Anupam | Bijari | Bomjir | Dambuk | Desali | Elopa | Hunli | Iduli | Jia | Koranu | Kronli | Meka | Paglam | Parbuk | Santipur | Boasimla | Deed | Godak | Hija | Joram | Mengio | Raga | Talo | Yazali | Ziro | A P Sectt | Balijan | Hawa Camp | Kheel | Kimin | Kokila | Midpu | Model Village | Naharlagun | Nirjuli | Ram Krishna Mission | Sonajuli | Vivek Vihar | Gispu | Lhou | Lumberdung | Mukto | Sakpret | Temple Gompa | Thingbu | Zimithang | Borduria | Dadam | K/nokno | Kaimai | Khela | Kheti | Khonsa Basti | Khotnu | Lazu | Longfong | Minthong | Namsang Mukh | Narottam Nagar | Nginu | Niausa | Panchou | Senewa | Soha | Thinsa | Tupi | Valley View | Geku | Gelling | Karko | Mariyang | Migging | Shimong | Singa | Tuting | Dumporijo | Giba | Lemiking | Lepajaring | Muri | Nacho | Sippi | Siyum | Tabarijo | Taksing | Taliha | Balemu | Bhalukpong | Dahung | Dedza | Dirang Basti | Khellong | Lish | Munna Camp | Nafra | Rupa | Salari | Sangti | Senge | Shergaon | Singchung | Tenga Market | Tenzingaon | Tippi | Bagra | Bame | Bene | Dali | Darak | Daring | Darka | Garu | Gensi | Kambang | Kaying | Kombo | Likabali | Liromoba | Mechuka | Monigong | Nikte | Payum | Rumgong | Tato | Tirbin | Vivek Nagar | Yomcha' 


class ner_logic:
    
    def build(self, inp):
        
        match_find_cities = re.findall(r'\b(?:' + '|'.join(cities.split(' | ')) + r')\b', inp, re.IGNORECASE)
        # match_find_cities_andra_pradesh = re.findall(cities_Andra_pradesh  ,inp, re.IGNORECASE)
        match_find_cities_andra_pradesh = re.findall(r'\b(?:' + '|'.join(cities_Andra_pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        match_find_cities_Arunachal_Pradesh = re.findall(r'\b(?:' + '|'.join(cities_Arunachal_Pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        
        # match_find_town_andra_pradesh = re.findall( towns_andra_pradesh  , inp, re.IGNORECASE)
        match_find_town_andra_pradesh = re.findall(r'\b(?:' + '|'.join(towns_andra_pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        match_find_villages_or_town_Arunachal_Pradesh = re.findall(r'\b(?:' + '|'.join(villages_Arunachal_Pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        
        # match_find_village_andra_pradesh = re.findall( villages_andra_pradesh  , inp, re.IGNORECASE)
        match_find_village_andra_pradesh = re.findall(r'\b(?:' + '|'.join(villages_andra_pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        match_find_states = re.findall(r'\b(?:'+ '|'.join(states.split(' | ')) + r')\b', inp, re.IGNORECASE)
        # if match_find_state or match_find_cities:
        #     print(f"states: {match_find_state}")
        #     print(f"cities: {match_find_cities}")
        # else:
        #     pass

        results = []
        
        if match_find_cities_andra_pradesh or match_find_town_andra_pradesh or match_find_village_andra_pradesh or match_find_states or match_find_cities_Arunachal_Pradesh or match_find_villages_or_town_Arunachal_Pradesh or match_find_cities:
        #     print(f"cities in Andara Pradesh:{match_find_cities_andra_pradesh}")
        #     print(f"towns in Andara Pradesh:{match_find_town_andra_pradesh}")
        #     print(f"villages in Andara Pradesh:{match_find_village_andra_pradesh}")
        # else:
        #     pass

            results.append(f"States :{match_find_states}")
            results.append(f"cities :{match_find_cities_andra_pradesh + match_find_cities_Arunachal_Pradesh + match_find_cities }")
            results.append(f"Towns/village: {match_find_town_andra_pradesh + match_find_village_andra_pradesh + match_find_villages_or_town_Arunachal_Pradesh }")
            
            # results.append(f"Cities in Andhra Pradesh: {match_find_cities_andra_pradesh}")
            # results.append(f"Towns in Andhra Pradesh: {match_find_town_andra_pradesh}")
            # results.append(f"Villages in Andhra Pradesh: {match_find_village_andra_pradesh}")
            # results.append(f"cities in Arunachal Pradesh:{match_find_cities_Arunachal_Pradesh}")
            # results.append(f"towns and villages in Arunachal Pradesh:{match_find_villages_or_town_Arunachal_Pradesh}")

        return "\n".join(results) if results else "No matches found."
    