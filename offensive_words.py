
offensive_words = [
    # English offensive words (with common variations)
    "abuse", "idiot", "stupid", "dumb", "fool", 
    "bastard", "moron", "loser", "jerk", "trash",
    "scum", "psycho", "dirtbag", "weirdo", "clown",
    "crazy", "lazy", "douche", "pervert", "creep",
    "scumbag", "useless", "annoying", "lame", 
    "disgusting", "filthy", "gross", "pathetic", 
    "worthless", "unworthy", "cheater", "liar", 
    "backstabber", "snake", "traitor", 
    "cuss", "curse", "damn", "hell", "piss", 
    "suck", "crap", "bull", "garbage", "dirt", 

    # Highly offensive English words (censored versions)
    "f***", "fck", "fk", "f**k", 
    "sh*t", "sh1t", "sht", 
    "b***h", "b!tch", "b1tch", 
    "c**k", "c0ck", "cok", 
    "a**", "a$$", "assh***", "ashole", 
    "p***", "p*rn", "p0rn", 
    "d***", "d**k", "d1ck", 
    "s**t", "sht", "sc*mb*g", 
    "wh***", "w***e", "wh0re", "hoe", 
    "sl*t", "sl**", "s1ut", 
    "m***", "mf", "m*therf*cker", 
    "r**ard", "r3tard", "idi*t", 
    "d***head", "douchebag", "a**hole", "ashole", 

    # Hinglish abusive words (common in India/Pakistan region)
    "chutiya", "ch*tiya", "chutiye", "c#utiya", 
    "madarchod", "m**c", "m@darchod", 
    "bhenchod", "b**c", "b#nchod", 
    "bhosdike", "bh0sdike", "bh0sdi", 
    "randi", "r@ndi", "randwa", 
    "gandu", "ga**u", "g@ndu", 
    "suar", "s**r", "s*ar", 
    "chinal", "ch**al", "ch#nal", 
    "harami", "h**rami", "h@rami", 
    "kutta", "k#tta", "kutti", "k*tti", 
    "launde", "la**de", "l@unde", 
    "kamina", "k*mina", "k@mina", 
    "tatti", "ta**i", "t@tti", 
    "ghatiya", "ghat*ya", "g@tiya", 
    "nalayak", "n@layak", "n*layak", 
    "lafanga", "l@fanga", "laf*nga", 
    "bevda", "b#vda", "bev**a", 
    "bhikhari", "b#khari", "bh*khari", 

    # Variations of known Hinglish terms
    "chut", "choot", "ch0ot", 
    "bhosda", "bh0sda", 
    "mc", "bc", 
    "r**di", "r@ndi", 
    "bkl", "bekar", 
    "gaand", "g**nd", "g@and", 
    "chu", "choo", "ch0o", 
    "chodu", "chodu", "chod**", 
    "tatte", "ta**e", 
    "katwa", "k@twa", 
    "kameena", "k@m**na", 
    "chutiyapa", "ch*t**pa", 
    "bakchod", "b@kchod", 
    "ullu", "ul**u", 
    "kutta", "kutya", "kut**", 
    "bevakoof", "bev*koof", 

    # Internet/online disguised versions (used to avoid censorship)
    "f4ck", "phuck", "phk", "p0rn", "p@rn", 
    "fuk", "fuc*", "fu*k", 
    "sux", "scks", "sck", 
    "c*ck", "c0ck", "c@ck", 
    "sht", "sh1t", "sh*t", 
    "b1tch", "b*tch", "b!tch", 
    "s1ut", "sl*t", "s|ut", 
    "a$$", "4$$", "a55", 
    "h3ll", "h3ll", "he||", 
    "cr@p", "cr4p", "sh1t", 
    "f*ck", "f*ck", "f|ck", 
    "a**", "a55", "4$$", 
    "p*rn", "p0rn", "p@rn", 

    # Offensive animal references
    "pig", "p!g", "dog", "d0g", "donkey", 
    "ass", "coward", "chicken", "goat", 
    "rat", "snitch", "monkey", 
    "buffalo", "bhains", "bhais", "bhandar", 

    # Offensive words related to social status or race
    "slave", "servant", "dog", 
    "beggar", "bhikhari", "pest", 
    "cheap", "gutter", "sewer", 
    "untouchable", "unclean", "low-class", 
    "trash", "poor", "beg", 
    "downtrodden", "peasant", "serf", 
    "drunkard", "alcoholic", "addict", 
    "sinner", "infidel", "heretic", 

    # 🚨 **Extreme English Offensive Words**
    "f***", "f**k", "fck", "f*ck", "f4ck", 
    "b***h", "b*tch", "b1tch", "b!tch", "b!t", 
    "sh*t", "sh1t", "sht", "s**t", "sh!t", 
    "d***", "d1ck", "d!ck", "d!k", "dic*", 
    "c**k", "c0ck", "cok", "c*ck", 
    "a**", "a55", "a$$", "ashole", 
    "wh***", "wh0re", "wh*re", "w***e", "w**re", 
    "p***", "p0rn", "p*rn", "p@rn", "p0rn0", 
    "s**t", "sht", "s!ht", "s**tbag", 
    "d***head", "d**khead", "d*ckhead", 
    "a**hole", "a$$hole", "a**h**e", 
    "r***rd", "r3tard", "r*tard", 
    "f*g", "f@g", "f4g", "f*ggot", 
    "c***", "c*nt", "c@nt", "c*nt", 
    "d***face", "d*ckface", "d1ckface", 
    "m***erf***er", "m*therf*cker", "mf", "m*f", 
    "bastard", "jerk", "scum", "trash", 
    "douche", "douchebag", "creep", "pervert", 
    "lame", "loser", "psycho", "scumbag", 
    "a**wipe", "a**clown", "a**hat", 
    "sucker", "dirtbag", "clown", "filth", 

    # 🚨 **Extreme Hinglish Offensive Words**
    "chutiya", "ch*tiya", "chutiyapa", "ch#tiya", 
    "madarchod", "m**c", "m@darchod", "mc", 
    "bhenchod", "b**c", "bc", 
    "bhosdike", "bh0sdike", "b#sdike", 
    "randi", "r@ndi", "randiwa", 
    "gandu", "g@ndu", "ga**u", "gndu", 
    "launde", "la**de", "la#nde", 
    "kamina", "k@mina", "k*mina", 
    "harami", "h@rami", "h*rmi", 
    "kutta", "k#tta", "k*tta", 
    "chodu", "chodu", "ch0du", 
    "tatte", "ta**e", "tat**", 
    "gaand", "g*nd", "g@and", 
    "tatti", "ta**i", "tat*i", 
    "chut", "choot", "cho*t", 
    "bevda", "b#vda", "bev*da", 
    "lafanga", "laf*nga", "l@fnga", 
    "bhikhari", "b#khari", "b!khari", 
    "chinal", "ch*nal", "chinali", 
    "ullu", "ul**u", "ul#u", 
    "katwa", "k*twa", "k@tw@", 
    "bekar", "b@kar", "b*kar", 
    "nalayak", "nal*yak", "n@layak", 
    "bakchod", "b@kchod", "bak**od", 
    "bhosda", "bh0sda", "bh0sd", 

    # 🚨 **Animal-based Insults**
    "pig", "p!g", "swine", "dog", "d0g", 
    "kutta", "kutti", "k@tti", "rat", "snake", 
    "monkey", "donkey", "buffalo", "bhains", 
    "bhondar", "bhandar", "bakri", "goat", 
    "chuha", "ch*ha", "billi", "cat", 
    "gadha", "ghada", "g*dha", "coward", 

    # 🚨 **Racial and Discriminatory Words**
    "slave", "s*ave", "servant", 
    "beggar", "bhikhari", "pest", 
    "cheap", "ch*p", "gutter", 
    "trash", "poor", "beg", 
    "peasant", "serf", "drunkard", 
    "alcoholic", "addict", 
    "sinner", "infidel", "heretic", 
    "low-class", "unclean", 
    "untouchable", "unworthy", 

    # 🚨 **Offensive Variations Used Online (Bypassing Filters)**
    "f4ck", "phuck", "phk", "fuk", 
    "sux", "scks", "sck", 
    "c*ck", "c0ck", "c@ck", 
    "sh1t", "b1tch", "sl*t", 
    "s|ut", "4$$", "a55", 
    "he||", "h3ll", "cr@p", 
    "cr4p", "sh1t", "a55", 
    "p*rn", "p0rn", "p@rn", 
    "c**k", "c0ck", "a55h0le", 
    "d0uche", "duche", "f***er", 
    "f|ck", "f*ck", "fu*k", 
    "w|tch", "b*tch", "b!tch", 

    # 🚨 **Insults Related to Looks, Intelligence, or Status**
    "ugly", "stupid", "idiot", 
    "dumb", "moron", "retard", 
    "weirdo", "freak", "clown", 
    "disgusting", "pathetic", "filthy", 
    "worthless", "garbage", "trash", 
    "lazy", "slow", "dummy", 
    "worthless", "unworthy", 
    "backstabber", "liar", 
    "snake", "traitor", "two-faced", 
    "waste", "annoying", 
    "loser", "psycho", "useless", 


    # Common Hinglish abusive words
    "chutiya", "chutiyapa", "chutiye", 
    "madarchod", "maderchod", "madarchod", 
    "bhenchod", "bhenchod", "bhencho", 
    "bhosdike", "bhosdi", "bhosda", 
    "randi", "randwa", 
    "gandu", "gandu", 
    "suar", "suar", 
    "chinal", "chinal", 
    "harami", "haramkhor", 
    "kutta", "kutti", 
    "launde", "launda", 
    "kamina", "kamina", 
    "tatti", "tatti", 
    "ghatiya", "ghatiya", 
    "nalayak", "nalayak", 
    "lafanga", "lafanga", 
    "bevda", "bevda", 
    "bhikhari", "bhikhari", 

    # Variations of Hinglish offensive words
    "chut", "choot", 
    "bhosda", "bhoda", 
    "mc", "bc", 
    "randi", "rand", 
    "bekar", 
    "gaand", "gand", 
    "chu", "choo", 
    "chodu", "chodu", 
    "tatte", "tatte", 
    "katwa", 
    "kameena", "kameena", 
    "chutiyapa", 
    "bakchod", 
    "ullu", 
    "kutya", 
    "bevakoof", 

    # Animal references used as insults
    "kutta", "kutti", 
    "suar", "bhains", "bhais", "bhandar", 
    "gadha", "gadhi", 
    "ullu", 

    # Words targeting social status or class
    "bhikhari", "beggar", 
    "gutter", "gandagi", 
    "cheap", "nalayak", 
    "bevda", 
    "peasant", 
    "lafanga", 

    # Blended Hinglish slang used online
    "mc", "bc", "chut", 
    "gandu", "harami", 
    "kutta", "kameena", 
    "madarchod", "bhenchod", 
    "chinal", 
    "nalayak", 
    "launda", "launde", 
    "bakchod", 
    "bevkuf", "bevakoof", 
    "chutiyapa", 
    "ullu"

]

import re
def offencive_word_detect(text):
    words= offensive_words
    patterns = r'\b(' + '|'.join(map(re.escape, words)) + r')\b'
    matches = re.findall(patterns, text.lower())
    
    if matches:
        print("Offensive words detected.")
    else:
        print("No offensive words detected.")
        
    return matches
