def exact_match(response: str, expected: str) -> bool:
    """
    Basic evaluator that checks whether the expected
    answer appears in the agent response.
    """
    return expected.lower() in response.lower()