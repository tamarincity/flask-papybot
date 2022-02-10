from typing import List
import unicodedata
import re
import logging


def remove_accents(text_to_format):
    return "".join(
        char
        for char in unicodedata.normalize("NFD", text_to_format)
        if unicodedata.category(char) != "Mn"
    )


def remove_punctuation(text_to_format):
    return re.sub(r"[^\w\s]", "", text_to_format)


def remove_some_words_and_format_text(text_to_format, words_to_remove: List[str]):
    """
    Remove words from the given text and format the text
    """
    text_to_format = text_to_format.lower() if text_to_format else ""

    # save appostrophy and replace minus sign by space
    text_to_format = text_to_format.replace("'", "75dhzkgf85h").replace("-", " ")

    # save " à " because it can help to determine the city
    text_to_format = text_to_format.replace(" à ", "75dhdhfk753f85h")

    text_to_format = remove_accents(text_to_format)
    text_to_format = remove_punctuation(text_to_format)
    # Re-inject the appostrophy
    text_to_format = text_to_format.replace("75dhzkgf85h", "'")

    # Re-inject the " à "
    text_to_format = text_to_format.replace("75dhdhfk753f85h", " à ")

    # Remove courtesy words
    for word in words_to_remove:
        text_to_format = text_to_format.replace(word, "")

    # Remove double space
    while "  " in text_to_format:
        text_to_format = text_to_format.replace("  ", " ")

    text_to_format = text_to_format.strip()
    return text_to_format


def extract_question_from_text(text_to_format, STOP_WORDS: List[str]):
    for word in STOP_WORDS:
        if word in text_to_format:
            return text_to_format.split(word)[1].strip()
    return None


def extract_city_from_question(question):
    """
    Extract the city from the question if
    "ville de " is in the question.

    Args:
        question (string): the question including the city

    Returns:
        tuple: question: string, city: string
    """

    city_stop_words = [
        " de la ville de ",
        " de la ville d'",
        " de la ville ",
        "ville de ",
        "ville d'",
        " ville:",
        " ville :",
        " ville ",
    ]

    for stop_word in city_stop_words:
        if stop_word in question:
            elements_of_question = question.split(stop_word)
            return elements_of_question[0].strip(), elements_of_question[-1].strip()

    return question, None


def figure_out_city(question):
    """
    Try to figure out what is the city from the question.
    This function uses keywords such as " à ", " de ".

    Args:
        question (string): the question including the city

    Returns:
        tuple: questions_without_city: [string], possible_cities: [string]
    """
    question1 = ""
    question2 = ""
    city1 = ""
    city2 = ""

    if " à " in question:
        elements_of_question = question.split(" à ")
        question1 = elements_of_question[0].strip()
        city1 = elements_of_question[-1].strip()

    elif " a " in question:
        elements_of_question = question.split(" a ")
        question1 = elements_of_question[0].strip()
        city1 = elements_of_question[-1].strip()

    if " de " in question:
        elements_of_question = question.split(" de ")
        question2 = elements_of_question[0].strip()
        city2 = elements_of_question[-1].strip()

    elif " d'" in question:
        elements_of_question = question.split(" d'")
        question2 = elements_of_question[0].strip()
        city2 = elements_of_question[-1].strip()

    return [question1, question2], [city1, city2]


def extract_name_out_of_street(street, LOCATION_WORDS):
    try:
        for word in LOCATION_WORDS:
            street = street.replace(word, "").replace(word.title(), "")

    except Exception as e:
        logging.exception(str(e))
    return street.strip()
