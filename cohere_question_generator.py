import cohere

co = cohere.Client("YOUR_API_KEY")  # Replace with your API key

def generate_questions(text, question_type="long", num_questions=5):
    if question_type == "mcq_with_answers":
        prompt = (
            f"Generate exactly {num_questions} multiple-choice questions based on the following text. "
            "Each question should have 4 options (A, B, C, D), followed by the correct answer and a brief explanation.\n\n"
            f"Text:\n{text}\n\n"
            "Format:\n"
            "Q1. ...?\nA. ...\nB. ...\nC. ...\nD. ...\nAnswer: C\nExplanation: ...\n\n"
        )
    elif question_type == "mcq":
        prompt = (
            f"Generate exactly {num_questions} multiple-choice questions based on the following text. "
            "Each question should have 4 options (A, B, C, D). Do not include answers or explanations.\n\n"
            f"Text:\n{text}\n\n"
            "Format:\n"
            "Q1. ...?\nA. ...\nB. ...\nC. ...\nD. ...\n\n"
        )
    elif question_type == "long_with_answers":
        prompt = (
            f"Generate exactly {num_questions} descriptive questions and their answers based on the following text.\n\n"
            f"Text:\n{text}\n\n"
            "Format:\nQ1. ...?\nAnswer: ...\n\n"
        )
    elif question_type == "long":
        prompt = (
            f"Generate exactly {num_questions} descriptive questions based on the following text. "
            "Do not include answers.\n\n"
            f"Text:\n{text}\n\n"
            "Format:\nQ1. ...?\nQ2. ...?\n\n"
        )
    else:
        return "❌ Unsupported question type."

    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=2000,
        temperature=0.6
    )

    return response.generations[0].text.strip()
