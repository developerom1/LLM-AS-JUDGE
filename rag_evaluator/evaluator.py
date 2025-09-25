import json
import os
from openai import OpenAI

# Initialize OpenAI client if API key is set, else use mock mode
USE_MOCK = os.getenv("OPENAI_API_KEY") is None
if not USE_MOCK:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
else:
    print("No OPENAI_API_KEY found. Using mock mode for testing.")

def evaluate_answer(question, rag_answer, ground_truth):
    """
    Use LLM to evaluate the RAG answer against ground truth.
    Scores: correctness, completeness, relevance (1-5 scale)
    Returns scores and reasoning.
    """
    if USE_MOCK:
        # Mock responses for testing
        if "Paris" in rag_answer:
            return {
                "correctness": {"score": 5, "reasoning": "Answer is factually accurate."},
                "completeness": {"score": 4, "reasoning": "Covers the main point but lacks additional context."},
                "relevance": {"score": 5, "reasoning": "Directly answers the question."}
            }
        elif "Austen" in rag_answer:
            return {
                "correctness": {"score": 5, "reasoning": "Correct author."},
                "completeness": {"score": 5, "reasoning": "Complete match."},
                "relevance": {"score": 5, "reasoning": "Highly relevant."}
            }
        elif "90 degrees" in rag_answer:
            return {
                "correctness": {"score": 2, "reasoning": "Incorrect boiling point."},
                "completeness": {"score": 3, "reasoning": "Missing pressure context."},
                "relevance": {"score": 5, "reasoning": "Answers the question but wrongly."}
            }
        else:
            return {
                "correctness": {"score": 3, "reasoning": "Partially correct."},
                "completeness": {"score": 3, "reasoning": "Incomplete."},
                "relevance": {"score": 4, "reasoning": "Somewhat relevant."}
            }

    prompt = f"""
    Evaluate the following RAG chatbot answer against the ground truth context.

    Question: {question}
    RAG Answer: {rag_answer}
    Ground Truth: {ground_truth}

    Provide scores (1-5) for:
    - Correctness: How factually accurate is the answer?
    - Completeness: How complete is the answer in covering the ground truth?
    - Relevance: How relevant is the answer to the question?

    Also provide brief reasoning for each score.

    Output in JSON format:
    {{
        "correctness": {{"score": int, "reasoning": "string"}},
        "completeness": {{"score": int, "reasoning": "string"}},
        "relevance": {{"score": int, "reasoning": "string"}}
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.5
    )

    result = response.choices[0].message.content.strip()
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        return {"error": "Failed to parse LLM response", "raw": result}

def generate_failure_report(evaluations):
    """
    Aggregate evaluations into a failure mode report.
    Focus on low scores (<3) and summarize reasons.
    """
    report = {
        "total_evaluations": len(evaluations),
        "failure_modes": []
    }

    for eval in evaluations:
        low_scores = []
        for category, data in eval["evaluation"].items():
            if isinstance(data, dict) and data.get("score", 5) < 3:
                low_scores.append(f"{category}: {data['reasoning']}")

        if low_scores:
            report["failure_modes"].append({
                "id": eval["id"],
                "question": eval["question"],
                "issues": low_scores
            })

    return report

def main():
    # Load mock data
    with open("rag_evaluator/mock_data.json", "r") as f:
        data = json.load(f)["data"]

    evaluations = []
    for item in data:
        eval_result = evaluate_answer(item["question"], item["rag_answer"], item["ground_truth"])
        evaluations.append({
            "id": item["id"],
            "question": item["question"],
            "evaluation": eval_result
        })

    # Generate failure report
    report = generate_failure_report(evaluations)

    # Save evaluations and report
    with open("rag_evaluator/evaluations.json", "w") as f:
        json.dump(evaluations, f, indent=2)

    with open("rag_evaluator/failure_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("Evaluation complete. Check evaluations.json and failure_report.json")

if __name__ == "__main__":
    main()
