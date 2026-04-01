from models.response_model import save_response
from models.profile_model import update_profile_scores
from nlp_engine.text_preprocessing import preprocess_text
from nlp_engine.keyword_analysis import analyze_keywords
from nlp_engine.structure_analysis import analyze_structure
from nlp_engine.scoring_engine import calculate_total_score
from nlp_engine.feedback_generator import generate_feedback

def evaluate_answer(question, user_answer):
    """
    Evaluates a single answer using the NLP engine, saves it, and returns the results.
    """
    
    # Process the text
    tokens = preprocess_text(user_answer)

    # Analyze keywords
    keyword_result = analyze_keywords(
        tokens,
        question["keywords"]
    )

    # Analyze structure
    structure_result = analyze_structure(user_answer)

    # Calculate overall score
    total_score = calculate_total_score(
        keyword_result,
        structure_result
    )
    update_profile_scores(
        "demo_user",
        keyword_score=keyword_result.get("score", 0),
        structure_score=structure_result.get("score", 0),
        final_score=total_score
    )

    # Generate constructive feedback
    feedback = generate_feedback(
        keyword_result,
        structure_result
    )

    # Save to the database
    save_response(
        question_id=question["id"],
        answer_text=user_answer,
        total_score=total_score,
        feedback=feedback
    )

    # Return structured result
    return {
        "question_text": question["question_text"],
        "user_answer": user_answer,
        "score": total_score,
        "feedback": feedback,
        "keyword_score": keyword_result.get("score", 0),
        "structure_score": structure_result.get("score", 0)
    }
