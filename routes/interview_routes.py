from flask import Blueprint, render_template, request

from models.question_model import (
    get_random_questions,
    get_question_by_id
)

from services.interview_service import evaluate_answer


interview_bp = Blueprint(
    "interview",
    __name__,
    template_folder="../templates"
)


@interview_bp.route("/interview")
def interview_page():
    """
    Display interview questions.
    """

    questions = get_random_questions(limit=3)

    return render_template(
        "interview.html",
        questions=questions
    )


@interview_bp.route("/evaluate", methods=["POST"])
def evaluate():
    """
    Evaluate submitted answers.
    """

    results = []

    for key in request.form:

        if key.startswith("question_"):

            question_id = int(key.split("_")[1])

            user_answer = request.form[key]

            question = get_question_by_id(question_id)

            evaluation_result = evaluate_answer(
                question,
                user_answer
            )

            results.append(evaluation_result)
    print(results)
    return render_template(
        "result.html",
        results=results
    )