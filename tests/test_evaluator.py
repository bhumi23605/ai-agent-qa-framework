from evaluators.accuracy import exact_match


def test_exact_match_passes_correct_answer():
    assert exact_match(
        "The capital of France is Paris.",
        "Paris"
    )


def test_exact_match_fails_wrong_answer():
    assert not exact_match(
        "The capital of France is London.",
        "Paris"
    )