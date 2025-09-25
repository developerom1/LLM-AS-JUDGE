# RAG Chatbot Evaluator MVP

This is a minimal viable product for evaluating RAG chatbot answers against ground-truth context using a judge LLM.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY="your-api-key-here"
   ```
   On Windows, use `set OPENAI_API_KEY="your-api-key-here"`

## Usage

Run the evaluator script:
```
python evaluator.py
```

This will:
- Load mock data from `mock_data.json`
- Evaluate each RAG answer using GPT-4 for correctness, completeness, and relevance (1-5 scale)
- Save detailed evaluations to `evaluations.json`
- Generate a failure mode report to `failure_report.json` (focusing on scores <3)

## Output

- `evaluations.json`: Detailed scores and reasoning for each answer
- `failure_report.json`: Aggregated report of failure modes (low scores with reasons)

## Mock Data

The `mock_data.json` contains sample questions, RAG answers, and ground-truth contexts for testing.

## Scope

- Limited to 3 sample evaluations
- Uses OpenAI GPT-4 as the judge LLM
- Simple JSON input/output
- No front-end
