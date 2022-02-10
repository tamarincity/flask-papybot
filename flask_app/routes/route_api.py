from turtle import clear
from flask import request, jsonify  # jsonify: To render json (API REST)


from ..logic.papybot import PapyBot

def routes_api(app):
    """
    Routes to consumn the api.
    """

    @app.route("/api", methods=["GET"])
    def papybot():
        question = request.args.get('question')
        if not question:
            return (
                jsonify({"message": "Il faut me poser une question"}),
                400)

        response_from_papybot, status = PapyBot.start(question)

        return jsonify({"message": response_from_papybot}), status
