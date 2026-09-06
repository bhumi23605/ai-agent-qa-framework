class SimpleAgent:
    """
    A simple rule-based agent used for testing
    the QA framework before connecting a real LLM.
    """

    def ask(self, question: str) -> str:
        question = question.lower().strip()

        if "capital of france" in question:
            return "The capital of France is Paris."

        if "2 + 2" in question or "2+2" in question:
            return "The answer is 4."

        return "I don't know."