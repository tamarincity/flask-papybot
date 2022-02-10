# flask_app/utilities/utils.py

from flask_app.constants import (
    LOCATION_WORDS,
)
from flask_app.utilities.utils import (
    extract_city_from_question,
    extract_question_from_text,
    extract_name_out_of_street,
    figure_out_city,
    remove_some_words_and_format_text,
    remove_accents,
    remove_punctuation,
)

def test_remove_accents():
    print("=> Remove all accents from question")
    text_to_format = "éèàù-normal  çie ë"
    assert remove_accents(text_to_format) == "eeau-normal  cie e"


def test_remove_punctuation():
    print("=> Remove punctuation from question")
    text_to_format = "Salut, comment vas-tu ?...;!:"
    assert remove_punctuation(text_to_format) == "Salut comment vastu "


def test_remove_some_words_and_format_text():
    print("=> Remove the provided words from the text and format the text")
    text_to_format = (
        "Salût, comment vas-tu l'ami, "
        "à l'approche de la fin du monde? 5 espaces entre la>     <et là !")
    words_to_remove = ["de la fin", "du monde"]
    assert remove_some_words_and_format_text(
        text_to_format, words_to_remove) == (
        "salut comment vas tu l'ami à l'approche 5 espaces entre la et la")


def test_extract_question_from_text():
    print("=> Select from the question the location to find")
    text_to_format = "quelle est l'adresse d'openclassrooms"
    text_to_format2 = "openclassrooms"
    STOP_WORDS = ["l'adresse d'"]
    assert extract_question_from_text(text_to_format, STOP_WORDS) == "openclassrooms"
    assert extract_question_from_text(text_to_format2, STOP_WORDS) == None


def test_extract_city_from_question():
    print("=> Select the city in the question thanks to specific words")
    question1 = "ou est le pont de la ville d'avignon"
    question2 = "ou est le pont d'avignon"
    assert extract_city_from_question(question1) == ("ou est le pont", "avignon")
    assert extract_city_from_question(question2) == ("ou est le pont d'avignon", None)


def test_figure_out_city():
    print('=> Try to determine the name of the city from the keyword "à", "a" and "de" ')
    question1 = "ou est le grand musée à rouen"
    question2 = "ou sont les ecluses a beziers"
    question3 = "ou est le musée de la peche de saint-pierre"
    question4 = "ou est le pont d'avignon"
    question5 = "ou se trouve le jardin des poetes"
    assert figure_out_city(question1) == (["ou est le grand musée", ""], ["rouen", ""])
    assert figure_out_city(question2) == (["ou sont les ecluses", ""], ["beziers", ""])
    assert figure_out_city(question3) == (["", "ou est le musée"], ["", "saint-pierre"])
    assert figure_out_city(question4) == (["", "ou est le pont"], ["", "avignon"])
    assert figure_out_city(question5) == (["", ""], ["", ""])


def test_extract_name_out_of_street():
    print("=> Get the number and the name of the street but not the type of street")
    street1 = "10 Avenue Robespierre"
    street2 = "10 avenue Robespierre"
    assert extract_name_out_of_street(street1, LOCATION_WORDS) == "10 Robespierre"
