"""Internal imports"""

import requests
import re
import string
import random
from api import KEY


class DataExtractor:

    """ 
    To extract the datas from different API
    """

    @staticmethod
    def get_papybot_quote():
        papybot_quote_list = ["Voici l'endroit que tu cherches, mon poussin !", "Mais bien sûr mon petit ! Voici : ",
                              "C'est comme si c'était fait :", "A ton service mon petit !"]
        papybot_quote = random.choice(papybot_quote_list)
        return papybot_quote

    @staticmethod
    def get_key_words(question):

        stop_words = [
            "a", "abord", "absolument", "afin", "ah", "ai", "aie", "ailleurs", "ainsi", "ait", "allaient",
            "allo", "allons", "allô", "alors", "anterieur", "anterieure", "anterieures", "apres", "après",
            "as", "assez", "attendu", "au", "aucun", "aucune", "aujourd", "aujourd'hui", "aupres", "auquel",
            "aura", "auraient", "aurait", "auront", "aussi", "autre", "autrefois", "autrement", "autres",
            "autrui", "aux", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avoir",
            "avons", "ayant", "b", "bah", "bas", "basee", "bat", "beau", "beaucoup", "bien", "bigre", "boum",
            "bravo", "brrr", "c", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles",
            "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "cent", "cependant", "certain",
            "certaine", "certaines", "certains", "certes", "ces", "cet", "cette", "ceux", "ceux-ci",
            "ceux-là", "chacun", "chacune", "chaque", "cher", "chers", "chez", "chiche", "chut", "chère",
            "chères", "ci", "cinq", "cinquantaine", "cinquante", "cinquantième", "cinquième", "clac", "clic",
                      "combien", "comme", "comment", "comparable", "comparables", "compris", "concernant", "contre",
                      "couic", "crac", "d", "da", "dans", "de", "debout", "dedans", "dehors", "deja", "delà", "depuis",
                      "dernier", "derniere", "derriere", "derrière", "des", "desormais", "desquelles", "desquels",
                      "dessous", "dessus", "deux", "deuxième", "deuxièmement", "devant", "devers", "devra", "different",
                      "differentes", "differents", "différent", "différente", "différentes", "différents", "dire",
                      "directe", "directement", "dit", "dite", "dits", "divers", "diverse", "diverses", "dix",
                      "dix-huit", "dix-neuf", "dix-sept", "dixième", "doit", "doivent", "donc", "dont", "douze",
                      "douzième", "dring", "du", "duquel", "durant", "dès", "désormais", "e", "effet", "egale",
                      "egalement", "egales", "eh", "elle", "elle-même", "elles", "elles-mêmes", "en", "encore", "enfin",
                      "entre", "envers", "environ", "es", "est", "et", "etant", "etc", "etre", "eu", "euh", "eux",
                      "eux-mêmes", "exactement", "excepté", "extenso", "exterieur", "f", "fais", "faisaient", "faisant",
                      "fait", "façon", "feront", "fi", "flac", "floc", "font", "g", "gens", "h", "ha", "hein", "hem",
                      "hep", "hi", "ho", "holà", "hop", "hormis", "hors", "hou", "houp", "hue", "hui", "huit",
                      "huitième", "hum", "hurrah", "hé", "hélas", "i", "il", "ils", "importe", "j'", "je", "jusqu'",
                      "jusque", "juste", "k", "l'", "la", "laisser", "laquelle", "las", "le", "lequel", "les",
                      "lesquelles", "lesquels", "leur", "leurs", "longtemps", "lors", "lorsque", "lui", "lui-meme",
                      "lui-même", "là", "lès", "m", "ma", "maint", "maintenant", "mais", "malgre", "malgré", "maximale",
                      "me", "meme", "memes", "merci", "mes", "mien", "mienne", "miennes", "miens", "mille", "mince",
                      "minimale", "moi", "moi-meme", "moi-même", "moindres", "moins", "mon", "moyennant", "multiple",
                      "multiples", "même", "mêmes", "n", "na", "naturel", "naturelle", "naturelles", "ne", "neanmoins",
                      "necessaire", "necessairement", "neuf", "neuvième", "ni", "nombreuses", "nombreux", "non", "nos",
                      "notamment", "notre", "nous", "nous-mêmes", "nouveau", "nul", "néanmoins", "nôtre", "nôtres", "o",
                      "oh", "ohé", "ollé", "olé", "on", "ont", "onze", "onzième", "ore", "ou", "ouf", "ouias", "oust",
                      "ouste", "outre", "ouvert", "ouverte", "ouverts", "o|", "où", "p", "paf", "pan", "par", "parce",
                      "parfois", "parle", "parlent", "parler", "parmi", "parseme", "partant", "particulier",
                      "particulière", "particulièrement", "pas", "passé", "pendant", "pense", "permet", "personne",
                      "peu", "peut", "peuvent", "peux", "pff", "pfft", "pfut", "pif", "pire", "plein", "plouf", "plus",
                      "plusieurs", "plutôt", "possessif", "possessifs", "possible", "possibles", "pouah", "pour",
                      "pourquoi", "pourrais", "pourrait", "pouvait", "prealable", "precisement", "premier", "première",
                      "premièrement", "pres", "probable", "probante", "procedant", "proche", "près", "psitt", "pu",
                      "puis", "puisque", "pur", "pure", "q", "qu", "quand", "quant", "quant-à-soi", "quanta",
                      "quarante", "quatorze", "quatre", "quatre-vingt", "quatrième", "quatrièmement", "que", "quel",
                      "quelconque", "quelle", "quelles", "quelqu'un", "quelque", "quelques", "quels", "qui",
                      "quiconque", "quinze", "quoi", "quoique", "r", "rare", "rarement", "rares", "relative",
                      "relativement", "remarquable", "rend", "rendre", "restant", "reste", "restent", "restrictif",
                      "retour", "revoici", "revoilà", "rien", "s'", "sa", "sacrebleu", "sais", "sait", "sans",
                      "sapristi", "sauf", "se", "sein", "seize", "selon", "semblable", "semblaient", "semble",
                      "semblent", "sent", "sept", "septième", "sera", "seraient", "serait", "seront", "ses", "seul",
                      "seule", "seulement", "si", "sien", "sienne", "siennes", "siens", "sinon", "six", "sixième",
                      "soi", "soi-même", "soit", "soixante", "son", "sont", "sous", "souvent", "specifique",
                      "specifiques", "speculatif", "stop", "strictement", "subtiles", "suffisant", "suffisante",
                      "suffit", "suis", "suit", "suivant", "suivante", "suivantes", "suivants", "suivre", "superpose",
                      "sur", "surtout", "t", "ta", "tac", "tant", "tardive", "te", "tel", "telle", "tellement",
                      "telles", "tels", "tenant", "tend", "tenir", "tente", "tes", "tic", "tien", "tienne", "tiennes",
                      "tiens", "toc", "toi", "toi-même", "ton", "touchant", "toujours", "tous", "tout", "toute",
                      "toutefois", "toutes", "treize", "trente", "tres", "trois", "troisième", "troisièmement", "trop",
                      "trouve", "très", "tsoin", "tsouin", "tu", "té", "u", "un", "une", "unes", "uniformement",
                      "unique", "uniques", "uns", "v", "va", "vais", "vas", "vers", "via", "vif", "vifs", "vingt",
                      "vivat", "vive", "vives", "vlan", "voici", "voilà", "vont", "vos", "votre", "vous", "vous-mêmes",
                      "vu", "vé", "vôtre", "vôtres", "w", "x", "y", "z", "zut", "à", "â", "ça", "ès", "étaient",
                      "étais", "était", "étant", "été", "être", "ô"
        ]

        question_in_lower_case = question.lower()

        remove_punctuation = string.punctuation
        remove_punctuation = remove_punctuation.replace("-", "")

        pattern = r"[{}]".format(remove_punctuation)

        word_results = re.sub(pattern, "", question_in_lower_case)

        word_results = word_results.split()

        for word in word_results:
            if word not in stop_words:
                print(word)

        return word

    @staticmethod
    def get_gm_data(name_place):
        
        """
        Return the json datas of the place from GoogleMaps API

            Parameter
            ----------
            name_place : type str
                The name of the place.
        """
        
        gm_base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        gm_api_url = gm_base_url + "address=" + name_place + "&key=" + KEY
        response = requests.get(gm_api_url)
        response = response.json()

        lat = response["results"][0]["geometry"]["location"]["lat"]
        lng = response["results"][0]["geometry"]["location"]["lng"]
        address = response["results"][0]["formatted_address"]
        return [{
            "address": address,
            "lat": lat,
            "lng": lng
            }]

    @staticmethod
    def get_mw_data(name_place):
        
        """
        Return the json datas of the place from wikimedia API

            Parameter
            ----------
            name_place : type str
                The name of the place.
        """

        # To fetch coordinates of the place 
        mw_base_url = "https://fr.wikipedia.org/w/rest.php/v1/search/page?"

        requests.get(mw_base_url + "q=" + name_place + "&limit=1")

        # To fetch some extract of the place
        mw_description_url = \
            "https://fr.wikipedia.org/w/api.php?action=query" \
            "&prop=extracts&exsentences=5&exlimit=1&explaintext=1" \
            "&formatversion=2&format=json"

        description_place = mw_description_url + "&titles=" + name_place

        print(description_place)

        description_requests = requests.get(description_place)

        description_quote = description_requests.json() 
        
        print(description_quote)

        extract = description_quote["query"]["pages"][0]["extract"]

        print("Voici ce que je sais sur cet endroit mon jeune padawan:", extract)
        
        print("L'adresse de cet endroit est :", name_place)
        
        return {
            "extract": extract
        }
