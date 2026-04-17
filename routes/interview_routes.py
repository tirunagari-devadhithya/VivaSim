from flask import Blueprint, render_template, request

from models.question_model import (
    get_question_by_id,
    get_questions_by_difficulty,
    get_random_questions
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
    Show interview page based on selected difficulty.
    Default = easy
    """

    level = request.args.get("level", "easy").lower()

    # Fetch difficulty-based questions
    questions = get_questions_by_difficulty(
        level,
        limit=3
    )

    # Safety fallback
    if not questions:
        questions = get_random_questions(limit=3)

    print("Selected difficulty:", level)
    print("Questions loaded:", len(questions))

    return render_template(
        "interview.html",
        questions=questions,
        level=level
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

            user_answer = request.form[key].strip()

            # Skip blank answers
            if not user_answer:
                continue

            question = get_question_by_id(question_id)

            if question is None:
                continue

            evaluation_result = evaluate_answer(
                question,
                user_answer
            )

            results.append(evaluation_result)

    print("Evaluation results:", results)

    return render_template(
        "result.html",
        results=results
    )