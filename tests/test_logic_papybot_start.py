# flask_app/controller/papybot.py
# test the start method of the class PapyBot

import pytest

from flask_app.logic import papybot

GeolocApi = papybot.GeolocApi
PapyBot = papybot.PapyBot


questions = (
    "Où est le théatre de Béziers, s'il te plaît ?",
    "ou se trouve le parc des Princes",
    "quelle est l'adresse d'openclassrooms?",
    "À quel endroit se situe la cathédrale de fort de france",
)

returns_from_function_remove_some_words_and_format_text = (
    "ou est le theatre de beziers",
    )
returns_from_function_extract_question_from_text = (
    "theatre de beziers",
)
returns_from_function_extract_city_from_question = (
    ("theatre de beziers" ,  None),
)
returns_from_function_figure_out_city = (
    (['', 'theatre'] ,  ['', 'beziers'])
)
returns_from_function_check_if_city_exists = (
    ({'Response': {
        'View': [
            {'Result': [
                {
                'Location': {
                    'Address': {
                        'Label': 'Béziers, Occitanie, France',
                        'Country': 'FRA', 'State': 'Occitanie',
                        'County': 'Hérault',
                        'City': 'Béziers',
                        'PostalCode': '34500'}}}
            ]}]}}),
)
returns_from_function_get_geolocation = (
    ({'item': {
        'title': 'Theatre Municipal de Beziers',
        'highlightedTitle': '<b>Theatre</b> Municipal <b>de</b> <b>Beziers</b>',
        'vicinity': 'Place Jean Jaurès<br/>34500 Béziers',
        'highlightedVicinity': 'Place Jean Jaurès<br/>34500 Béziers',
        'position': [43.3418, 3.21703],
        'category': 'theatre-music-culture',
        'categoryTitle': 'Theatre, Music & Culture'},
    'location_title': 'Theatre Municipal de Beziers',
    'full_address': 'Place Jean Jaurès<br/>34500 Béziers',
    'extracted_city': 'B',
    'street': 'Place Jean Jaurès',
    'name_out_of_street': 'Jean Jaurès',
    'position_list': [43.3418, 3.21703],
    'latitude': 43.3418,
    'longitude': 3.21703,
    'message_from_papy': ''}),
)
returns_from_function_check_response_validity_of_geoloc = (
    "Theatre Municipal de Beziers",
)
returns_from_function_get_interesting_points_around = (
    ([
        {'position': [43.3418, 3.21703],
        'distance': 0,
        'title': 'Theatre Municipal de Beziers',
        'averageRating': 0.0,
        'category': {'title': 'Theatre, Music & Culture'},
        'icon': 'https://.../icons/categories/05.icon',
        'vicinity': 'Place Jean Jaurès<br/>34500 Béziers'},
        {'position': [43.34202, 3.21669],
        'distance': 37,
        'title': 'Cafe de la Bourse',
        'averageRating': 0.0,
        'category': {'title': 'Restaurant'},
        'icon': 'https://.../icons/categories/03.icon',
        'vicinity': '32 Place Jean Jaurès<br/>34500 Béziers'}
    ]),
)
returns_from_function_translate_points_categories = (
    ([
        {'position': [43.3418, 3.21703],
        'title': 'Theatre Municipal de Beziers',
        'category': {
            'title': 'Théâtre, musique et culture'},
        'icon': 'https://.../icons/categories/05.icon',
        'vicinity': 'Place Jean Jaurès<br/>34500 Béziers'},
        {'position': [43.34202, 3.21669],
        'title': 'Cafe de la Bourse',
        'category': {
            'title': 'Le restaurant'},
        'icon': 'https://.../icons/categories/03.icon',
        'vicinity': '32 Place Jean Jaurès<br/>34500 Béziers'}
    ])
)
returns_from_function_turn_interesting_points_into_html_version = (
    ("""<strong>Theatre Municipal de Beziers</strong> """
    """<img src="https://.../icons/categories/05.icon" """
    """alt="icon for catégorie: Théâtre, musique et culture" """
    """title="catégorie: Théâtre, musique et culture"width="50" />, """
    """<strong>Cafe de la Bourse</strong> """
    """<img src="https://.../icons/categories/03.icon" """
    """alt="icon for catégorie: Le restaurant" """
    """title="catégorie: Le restaurant"width="50" />"""),
)
returns_from_function_get_info_from_wikipedia = (
    ([
        "<p><b>Béziers</b> est une commune française située dans ...</p>",
        "<p><b>Jean-Jaurès</b> est une station de correspondance ...</p>",
        "<p><b>Jean Jaurès</b>, né le 3 septembre 1859 à Castres ...</p>"
    ]),
)
expected_values = (
    (("Pour tout de dire...<br />L'adresse de "
    "<< Theatre Municipal de Beziers >> est: "
    "Place Jean Jaurès<br/>34500 Béziers.<br />"
    "Les coordonnées sont: (43.3418, 3.21703)."        
    "<end_of_bubble />Pour ton information :<br/>"
    "<p><b>Béziers</b> est une commune française située dans ...</p>"
    "<end_of_bubble />J'ai bien envie de te parler de ceci :<br/>"
    "<p><b>Jean-Jaurès</b> est une station de correspondance ...</p>"
    "<end_of_bubble />En bonus pour ta culture générale apprends ça:<br/><br/>"
    "<p><b>Jean Jaurès</b>, né le 3 septembre 1859 à Castres ...</p>"
    "<end_of_bubble />Je t'ai fait une petite liste des endroits qui pourraient"
    " t'intéresser autour de l'adresse que tu m'as demandé :<br/><br/>"
    """<strong>Theatre Municipal de Beziers</strong> """
    """<img src="https://.../icons/categories/05.icon" """
    """alt="icon for catégorie: Théâtre, musique et culture" """
    """title="catégorie: Théâtre, musique et culture"width="50" />, """
    """<strong>Cafe de la Bourse</strong> """
    """<img src="https://.../icons/categories/03.icon" """
    """alt="icon for catégorie: Le restaurant" """
    """title="catégorie: Le restaurant"width="50" />"""
    """<br/><br>Je sais, je parle beaucoup. 😁<br/><br/>"""
    """<end_of_bubble />Pour finir, voici la carte ...<br />"""
    """<img src="https://image.maps.ls.hereapi.com/mia/1.6/mapview"""
    """?apiKey=xxx&z=17&w=1000&h=700&c=43.3418,3.21703" />""") ,  200 ),
)



@pytest.mark.parametrize(
    (
        "question, "
        "return_from_function_remove_some_words_and_format_text, "
        "return_from_function_extract_question_from_text, "
        "return_from_function_extract_city_from_question, "
        "return_from_function_figure_out_city, "
        "return_from_function_check_if_city_exists, "
        "return_from_function_get_geolocation, "
        "return_from_function_check_response_validity_of_geoloc, "
        "return_from_function_get_interesting_points_around, "
        "return_from_function_translate_points_categories, "
        "return_from_function_turn_interesting_points_into_html_version, "
        "return_from_function_get_info_from_wikipedia, "
        "expected_value"
    ),
    [
        (questions[0],
        returns_from_function_remove_some_words_and_format_text[0],
        returns_from_function_extract_question_from_text[0],
        returns_from_function_extract_city_from_question[0],
        returns_from_function_figure_out_city[0],
        returns_from_function_check_if_city_exists[0],
        returns_from_function_get_geolocation[0],
        returns_from_function_check_response_validity_of_geoloc[0],
        returns_from_function_get_interesting_points_around[0],
        returns_from_function_translate_points_categories[0],
        returns_from_function_turn_interesting_points_into_html_version[0],
        returns_from_function_get_info_from_wikipedia[0],
        expected_values[0])
    ]
    )
def test_start(
    monkeypatch,
    question,
    return_from_function_remove_some_words_and_format_text,
    return_from_function_extract_question_from_text,
    return_from_function_extract_city_from_question,
    return_from_function_figure_out_city,
    return_from_function_check_if_city_exists,
    return_from_function_get_geolocation,
    return_from_function_check_response_validity_of_geoloc,
    return_from_function_get_interesting_points_around,
    return_from_function_translate_points_categories,
    return_from_function_turn_interesting_points_into_html_version,
    return_from_function_get_info_from_wikipedia,
    expected_value
    ):
    
    Sut = PapyBot

    def mock_remove_some_words_and_format_text(text_to_format, WORDS_OF_COURTESY):
        return return_from_function_remove_some_words_and_format_text

    def mock_extract_question_from_text(formated_text, STOP_WORDS):
        return return_from_function_extract_question_from_text

    def mock_extract_city_from_question(question):
        return return_from_function_extract_city_from_question

    def mock_figure_out_city(question):
        return return_from_function_figure_out_city

    def mock_check_if_city_exists(city):
        return return_from_function_check_if_city_exists

    def mock_get_geolocation(question, city, message_from_papy):
        return return_from_function_get_geolocation

    def mock_check_response_validity_of_geoloc(question, location_title, full_address, city):
        return return_from_function_check_response_validity_of_geoloc

    def mock_get_interesting_points_around(latitude, longitude):
        return return_from_function_get_interesting_points_around

    def mock_translate_points_categories(interesting_points_list, FRENCH):
        return return_from_function_translate_points_categories

    def mock_turn_interesting_points_into_html_version(interesting_points_list):
        return return_from_function_turn_interesting_points_into_html_version

    def mock_get_info_from_wikipedia(topic):
        if "theatre de beziers" in topic:
            return return_from_function_get_info_from_wikipedia[0]
        elif "Place Jean Jaurès" in topic:
            return return_from_function_get_info_from_wikipedia[1]
        elif "Jean Jaurès" in topic:
            return return_from_function_get_info_from_wikipedia[2]

    def mock_very_first_words_of_papy():
        return "Pour tout de dire...<br />"

    def mock_display_map(api_key, latitude, longitude):
        return (
            """<end_of_bubble />Pour finir, voici la carte ...<br />"""
            """<img src="https://image.maps.ls.hereapi.com/mia/1.6/mapview"""
            """?apiKey=xxx&z=17&w=1000&h=700&c=43.3418,3.21703" />""")

    monkeypatch.setattr(
        papybot,
        "remove_some_words_and_format_text",
        mock_remove_some_words_and_format_text
    )

    monkeypatch.setattr(
        papybot,
        "extract_question_from_text",
        mock_extract_question_from_text
    )

    monkeypatch.setattr(
        papybot,
        "extract_city_from_question",
        mock_extract_city_from_question
    )

    monkeypatch.setattr(
        papybot,
        "figure_out_city",
        mock_figure_out_city
    )

    monkeypatch.setattr(
        GeolocApi,
        "check_if_city_exists",
        mock_check_if_city_exists
    )

    monkeypatch.setattr(
        Sut,
        "get_geolocation",
        mock_get_geolocation
    )

    monkeypatch.setattr(
        Sut,
        "get_geolocation",
        mock_get_geolocation
    )

    monkeypatch.setattr(
        Sut,
        "check_response_validity_of_geoloc",
        mock_check_response_validity_of_geoloc
    )

    monkeypatch.setattr(
        GeolocApi,
        "get_interesting_points_around",
        mock_get_interesting_points_around
    )

    monkeypatch.setattr(
        Sut,
        "translate_points_categories",
        mock_translate_points_categories
    )

    monkeypatch.setattr(
        Sut,
        "turn_interesting_points_into_html_version",
        mock_turn_interesting_points_into_html_version
    )

    monkeypatch.setattr(
        Sut,
        "get_info_from_wikipedia",
        mock_get_info_from_wikipedia
    )

    monkeypatch.setattr(
        Sut,
        "very_first_words_of_papy",
        mock_very_first_words_of_papy
    )

    monkeypatch.setattr(
        Sut,
        "display_map",
        mock_display_map
    )
    
    assert Sut.start(question) == expected_value

             