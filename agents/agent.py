class SimpleAgent:
    """
    A simple test agent.

    This is intentionally not an LLM yet.
    We will replace its internal logic with a real
    LLM-based agent later.
    """

    def ask(self, question: str) -> str:
        question = question.lower().strip()

        if "capital of france" in question:
            return "The capital of France is Paris."

        if "2 + 2" in question or "2+2" in question:
            return "The answer is 4."

        return "I don't know."