# LLM as Judge - RAG Evaluator

This repository contains the code and resources for the "LLM as Judge" project, specifically the RAG (Retrieval-Augmented Generation) Evaluator. The evaluator assesses the performance of LLM-based systems in judging and evaluating responses.

## Project Structure

- **rag_evaluator/**: Core directory containing the evaluation scripts, data, and documentation.
  - `evaluator.py`: Main evaluation script for running assessments.
  - `mock_data.json`: Sample data for testing the evaluator.
  - `generate_doc.py`: Script for generating documentation and reports.
  - `README.md`: Detailed instructions for the RAG evaluator.
  - `requirements.txt`: Python dependencies required to run the project.
  - `evaluations.json`: JSON file storing evaluation results.
  - `failure_report.json`: Reports on evaluation failures.
  - `feedback_details.docx`: Detailed feedback document.
  - `rag_evaluator_detailed_report.docx`: Comprehensive report on evaluations.

## Setup and Usage

1. Clone the repository:
   ```
   git clone https://github.com/developerom1/LLM-AS-JUDGE.git
   cd LLM-AS-JUDGE
   ```

2. Navigate to the rag_evaluator directory:
   ```
   cd rag_evaluator
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the evaluator:
   ```
   python evaluator.py
   ```

For more details, refer to `rag_evaluator/README.md`.

## License

This project is open-source. Feel free to contribute!
