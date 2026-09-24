import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from agents.agent import SimpleAgent
from evaluators.accuracy import exact_match


def load_test_cases(file_path: str) -> list:
    """Load evaluation test cases from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


def evaluate_agent(agent, test_cases: list) -> list:
    """Run the agent against every test case."""
    results = []

    for test_case in test_cases:
        response = agent.ask(test_case["input"])

        passed = exact_match(
            response,
            test_case["expected"]
        )

        results.append({
            "id": test_case["id"],
            "category": test_case["category"],
            "input": test_case["input"],
            "expected": test_case["expected"],
            "response": response,
            "passed": passed
        })

    return results


def calculate_accuracy(results: list) -> float:
    """Calculate the percentage of passed test cases."""
    if not results:
        return 0.0

    passed = sum(result["passed"] for result in results)

    return (passed / len(results)) * 100


if __name__ == "__main__":
    agent = SimpleAgent()

    test_cases = load_test_cases(
        "datasets/evaluation_cases.json"
    )

    results = evaluate_agent(agent, test_cases)

    accuracy = calculate_accuracy(results)

    for result in results:
        status = "PASS" if result["passed"] else "FAIL"

        print(
            f'{result["id"]}: {status} '
            f'| {result["input"]}'
        )

    print("\n--------------------")
    print(f"Overall Accuracy: {accuracy:.2f}%")