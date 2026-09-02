from agents.agent import SimpleAgent


def test_agent_answers_capital_question():
    agent = SimpleAgent()

    response = agent.ask("What is the capital of France?")

    assert "Paris" in response


def test_agent_answers_math_question():
    agent = SimpleAgent()

    response = agent.ask("What is 2 + 2?")

    assert "4" in response


def test_agent_handles_unknown_question():
    agent = SimpleAgent()

    response = agent.ask("What is the population of Mars?")

    assert response == "I don't know."