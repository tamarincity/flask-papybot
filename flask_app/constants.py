CENTER_OF_FRANCE = "46.6937342,2.9800691"
FRENCH = "fr"
LOCATION_WORDS = [
    "avenue de la ",
    "avenue des ",
    "avenue du ",
    "avenue d'",
    "avenue ",
    "place de la ",
    "place des ",
    "place du ",
    "place d'",
    "place ",
    "boulevard de la ",
    "boulevard des ",
    "boulevard du ",
    "boulevard d'",
    "boulevard ",
    "rue de la ",
    "rue des ",
    "rue du ",
    "rue d'",
    "rue ",
    "impasse de la ",
    "impasse des ",
    "impasse du ",
    "impasse d'",
    "impasse ",
    "chemin de la ",
    "chemin des ",
    "chemin du ",
    "chemin d'",
    "chemin ",
    "voie de la ",
    "voie des ",
    "voie du ",
    "voie d'",
    "voie ",
    "site du ",
    "site de ",
    "cite de ",
    "cite du ",
    "cite ",
    "cité de ",
    "cité du ",
    "cité ",
    "cité",
    "Cité",
    'Cit"',
]

STOP_WORDS = [
    "where is the ",
    "where is ",
    "where are the ",
    "where are ",
    "where is located the ",
    "where is located ",
    "where are located the ",
    "where are located ",
    " find the ",
    " find ",
    " get to the ",
    " get to ",
    "location of the ",
    "location of ",
    " take place",
    "adress du ",
    "adresse du ",
    " address of the ",
    " address of ",
    " adress of the ",
    " adress of ",
    " addres of the ",
    " addres of ",
    " adres of the ",
    " adres of ",
    " addresse of the ",
    " addresse of ",
    " addresses of the ",
    " addresses of ",
    " que sais tu sur les ",
    " que sais tu sur la ",
    " que sais tu sur le ",
    " que sais tu sur l'",
    " que sais tu sur ",
    " que tu sais sur les ",
    " que tu sais sur la ",
    " que tu sais sur le ",
    " que tu sais sur l'",
    " que tu sais sur ",
    " l'adresse de la ",
    " l'adresse de ",
    " l'adresse d'",
    " l'adresse des ",
    " adresse est le ",
    " adresse est la ",
    " adresse est l'",
    " adresse du ",
    " adresses sont les ",
    " adresse sont les ",
    " adresses sont ",
    " adresse sont ",
    " adresse est ",
    " l'address de la ",
    " l'address de ",
    " l'address d'",
    " l'address des ",
    " address est le ",
    " address est la ",
    " address est l'",
    " addresss sont les ",
    " address sont les ",
    " addresss sont ",
    " address sont ",
    " address est ",
    " l'addresse de la ",
    " l'addresse de ",
    " l'addresse d'",
    " l'addresse des ",
    " addresse est le ",
    " addresse est la ",
    " addresse est l'",
    " addresses sont les ",
    " addresse sont les ",
    " addresses sont ",
    " addresse sont ",
    " addresse est ",
    " l'addresse de la ",
    " l'addresse de ",
    " l'addresse d'",
    " l'addresse des ",
    " addresse est le ",
    " addresse est la ",
    " addresse est l'",
    " addresses sont les ",
    " addresse sont les ",
    " addresses sont ",
    " addresse sont ",
    " addresse est ",
    "l'adress de la ",
    "l'adress de ",
    "l'adress d'",
    "l'adress des ",
    " adress est le ",
    " adress est la ",
    " adress est l'",
    " adresss sont les ",
    " adress sont les ",
    " adresss sont ",
    " adress sont ",
    " adress est ",
    "a propos de la ",
    "a propos des ",
    "a propos du ",
    "a propos de ",
    " a propos d'",
    "emplacement des ",
    "emplacement de la ",
    "emplacement du ",
    "emplacement d'",
    "emplacement de ",
    "parler de la ",
    "parler du ",
    "parler des ",
    "parler de ",
    "parler d'",
    "parle moi des ",
    "parle moi de la ",
    "parle moi du ",
    "parle moi d'",
    "parles moi des ",
    "parles moi de la ",
    "parles moi du ",
    "parles moi d'",
    "dire sur les ",
    "dire sur le ",
    "dire sur la ",
    "dire sur l'",
    "dire sur ",
    " tu sur les ",
    " tu sur le ",
    " tu sur la ",
    " tu sur l'",
    " se trouvent les ",
    " se trouve les ",
    " se trouve le ",
    "se trouvent la ",
    " se trouve l'",
    " se trouve la ",
    "se trouve ",
    " ce trouvent les ",
    "ce trouve les ",
    "ce trouve le ",
    "ce trouvent la ",
    "ce trouve l'",
    "ce trouve",
    "se situent les ",
    "se situe les ",
    "se situe le ",
    "se situe la ",
    "se situe l'",
    "se situe ",
    "ce situent les ",
    "ce situe les ",
    "ce situe le ",
    "ce situe la ",
    "ce situe l'",
    "ce situe ",
    "se cituent les ",
    "se citue les ",
    "se citue le ",
    "se citue la ",
    "se citue l'",
    "se citue ",
    "ce cituent les ",
    "ce citue les ",
    "ce citue le ",
    "ce citue  ",
    "ce citue l'",
    "ce citue ",
    "sont situes les ",
    "sont situe les ",
    "son situes les ",
    "son situe les ",
    "est situe les ",
    "est situe le ",
    "est situe la ",
    "est situe l'",
    "est situe ",
    "sont situes ",
    "son situes ",
    "sont situees les ",
    "sont situee les ",
    "son situees les ",
    "son situee les ",
    "est situee les ",
    "est situee le ",
    "est situee la ",
    "est situee l'",
    "est situee ",
    "sont situees ",
    "son situees ",
    "et situe les ",
    "et situe le ",
    "et situe la ",
    "et situe l'",
    "es situe les ",
    "es situe le ",
    "es situe la ",
    "es situe l'",
    "est citue les ",
    "est citue le ",
    "est citue la ",
    "est citue l'",
    "et citue les ",
    "et citue le ",
    "et citue la ",
    "et citue l'",
    "es citue les ",
    "es citue le ",
    "es citue la ",
    "es citue l'",
    "ou sont les ",
    "ou son les ",
    "ou est les ",
    "ou est le ",
    "ou est la ",
    "ou sont la  ",
    "ou sont le ",
    "ou et les ",
    "ou et le ",
    "ou et la ",
    "ou et l'",
    "ou es les ",
    "ou es le ",
    "ou es la ",
    "ou es l'",
    "ou sont ",
    "ou est ",
    "ou es ",
    "localiser les ",
    "localiser le ",
    "localiser la ",
    "localiser l'",
    "localise les ",
    "localise le ",
    "localise la ",
    "localise l'",
    "localises les ",
    "localises le ",
    "localises la ",
    "localises l'",
    "geolocaliser les ",
    "geolocaliser le ",
    "geolocaliser la ",
    "geolocaliser l'",
    "geolocalise les ",
    "geolocalise le ",
    "geolocalise la ",
    "geolocalise l'",
    "geolocalises les ",
    "geolocalises le ",
    "geolocalises la ",
    "geolocalises l'",
    "geo-localiser les ",
    "geo-localiser le ",
    "geo-localiser la ",
    "geo-localiser l'",
    "geo-localise les ",
    "geo-localise le ",
    "geo-localise la ",
    "geo-localise l'",
    "geo-localises les ",
    "geo-localises le ",
    "geo-localises la ",
    "geo-localises l'",
    "geo localiser les ",
    "geo localiser le ",
    "geo localiser la ",
    "geo localiser l'",
    "geo localise les ",
    "geo localise le ",
    "geo localise la ",
    "geo localise l'",
    "geo localises les ",
    "geo localises le ",
    "geo localises la ",
    "geo localises l'",
    "geolocaliser ",
    "geo-localiser ",
    "geo localiser",
    "coordonnees gps de la ",
    "coordonnees gps du ",
    "coordonnees gps des ",
    "coordonnees gps de l'",
    "coordonnees gps d'",
    "coordonee gps de la ",
    "coordonee gps du ",
    "coordonee gps des ",
    "coordonee gps de l'",
    "coordonee gps d'",
    "coordonnee gps de la ",
    "coordonnee gps du ",
    "coordonnee gps des ",
    "coordonnee gps de l'",
    "coordonnee gps d'",
    "coordonnes gps de la ",
    "coordonnes gps du ",
    "coordonnes gps des ",
    "coordonnes gps de l'",
    "coordonnes gps d'",
    "coordonees gps de la ",
    "coordonees gps du ",
    "coordonees gps des ",
    "coordonees gps de l'",
    "coordonees gps d'",
    "coordonnees de la ",
    "coordonnees du ",
    "coordonnees des ",
    "coordonnees de l'",
    "coordonnees d'",
    "coordonnees gps ",
    "coordonnee gps ",
    "coordonees gps ",
    "coordonee gps ",
    "coordonnees gps de ",
    "coordonnees ",
    "coordonnes",
    "coordones",
    "coordonees",
    "coordonnee",
    "localisation gps de la ",
    "localisation gps du ",
    "localisation gps des ",
    "localisation gps de l'",
    "localisation gps d'",
    "geo-localisation gps de la ",
    "geo-localisation gps du ",
    "geo-localisation gps des ",
    "geo-localisation gps de l'",
    "geo-localisation gps d'",
    "geo-localisation de la ",
    "geo-localisation du ",
    "geo-localisation des ",
    "geo-localisation de l'",
    "geo-localisation d'",
    "geo localisation gps de la ",
    "geo localisation gps du ",
    "geo localisation gps des ",
    "geo localisation gps de l'",
    "geo localisation gps d'",
    "geo localisation de la ",
    "geo localisation du ",
    "geo localisation des ",
    "geo localisation de l'",
    "geo localisation d'",
    "geolocalisation gps de la ",
    "geolocalisation gps du ",
    "geolocalisation gps des ",
    "geolocalisation gps de l'",
    "geolocalisation du ",
    "geolocalisation des ",
    "geolocalisation de l'",
    "geolocalisation d'",
    "geolocalisation ",
    "geo localisation ",
    "geo-localisation ",
    "donnees gps de la ",
    "donnees gps du ",
    "donnees gps des ",
    "donnees gps de l'",
    "donnees gps d'",
    "donnee gps de la ",
    "donnee gps du ",
    "donnee gps des ",
    "donnee gps de l'",
    "donnee gps d'",
    "position geographique des ",
    "position geographique de la ",
    "position geographique du ",
    "position geographique de le ",
    "position geographique d'",
    "position gps des ",
    "position gps du ",
    "position gps de le ",
    "position gps de la ",
    "position gps de l'",
    "position gps d'",
    "position des ",
    "position de la ",
    "position de le ",
    "position du ",
    "position d'",
    "position de l'",
    "latitude et longitude des ",
    "latitude et longitude de la ",
    "latitude et longitude du ",
    "latitude et longitude d'",
    "latitude et longitude de l'",
    "latitude et la longitude des ",
    "latitude et la longitude de la ",
    "latitude et la longitude du ",
    "latitude et la longitude d'",
    "latitude et la longitude de l'",
    "longitude et latitude des ",
    "longitude et latitude de la ",
    "longitude et latitude du ",
    "longitude et latitude d'",
    "longitude et latitude de l'",
    "longitude et la latitude des ",
    "longitude et la latitude de la ",
    "longitude et la latitude du ",
    "longitude et la latitude d'",
    "longitude et la latitude de l'",
    "longitude et la latitude ",
    "latitude et la longitude ",
    "longitude et latitude ",
    "latitude et longitude ",
    "longitude latitude ",
    "latitude longitude ",
    "localise moi la ",
    "localise moi le ",
    "localise moi les ",
    "trouve moi la ",
    "trouve moi le ",
    "trouve moi les ",
    "cherche moi la ",
    "cherche moi le ",
    "cherche moi les ",
    "x y de la ",
    "x y des ",
    "x y du ",
    "x y d'",
    "trouver les ",
    "trouver le ",
    "trouver la ",
    "trouver l'",
    "trouve les ",
    "trouve le ",
    "trouve la ",
    "trouve l'",
    "quel endroit sont les ",
    "quel endroit est la ",
    "quel endroit est le ",
    "quel endroi sont les ",
    "quel endroi est la ",
    "quel endroi est le ",
    "quel endrois sont les ",
    "quel endrois est la ",
    "quel endrois est le ",
    "quel endroit est l'",
    "quel endroi est l'",
    "quel endrois est l'",
    "quels endroits sont les ",
    "quels endrois sont les ",
]

URL_GEOLOCATION_API = "https://places.ls.hereapi.com/places/v1/autosuggest/?"
URL_GET_CITY_GEOLOC_API = (
    "https://geocoder.ls.hereapi.com/6.2/geocode.json?&city=")

URL_GET_INTERESTING_POINTS_AROUND = (
    "https://places.sit.ls.hereapi.com/places/v1/discover/"
    "around?lang=fr-fr&pretty&at=")

URL_SUGGESTED_ITEMS_FROM_WIKIPEDIA = (
    "https://fr.wikipedia.org/w/api.php?action=query&list=search"
    "&inprop=url&utf8=&format=json&origin=*&srlimit=3&srsearch=")

URL_ITEM_INFO_FROM_WIKIPEDIA = (
    "https://fr.wikipedia.org/w/api.php?action=query"
    "&prop=extracts&format=json&exintro=1&titles=")

WORDS_OF_COURTESY = [
    "s'il te plait",
    "sil te plait",
    "s'il vous plait",
    "sil vous plait",
    "stp",
    "svp",
    "merci beaucoup",
    "merci bien",
    "merci d'avance",
    "merci",
    "mon papi cheri",
    "mon papy cheri",
    "mon papi d'amour",
    "mon papy d'amour",
    "mon papi robot cheri",
    "mon papy robot cheri",
    "mon papi robot d'amour",
    "mon papy robot d'amour",
    "mon papi robot",
    "mon papy robot",
    "mon cher papi robot",
    "mon cher papy robot",
    "mon papi",
    "mon papy",
    "mon cher papi",
    "mon cher papy",
    "mon papibot",
    "mon papybot",
    "mon papi_bot",
    "mon papy_bot",
    "mon papi bot",
    "mon papy bot",
    "mon grandpy",
    "mon grandpi",
    "mon grand py",
    "mon grand pi",
    "mon cher grandpy",
    "mon cher grandpi",
    "mon cher grand py",
    "mon cher grand pi",
    "cher grandpy",
    "cher grandpi",
    "cher grand py",
    "cher grand pi",
    "mon grandpy d'amour",
    "papi grandpy",
    "papy grandpy",
    "papi grandpi",
    "papi grand py",
    "papi grand pi",
    "papibot",
    "papybot",
    "papi_bot",
    "papy_bot",
    "papi bot",
    "papy bot",
    "papi",
    "papy",
    "grandpy",
    "grand py",
    "grandpi",
    "grand pi",
    "please",
]
