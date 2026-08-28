from ataraxia.response import generate_response
from ataraxia.safety import validate_response, get_safe_fallback


def run_ataraxia(user_message: str) -> str:
    response = generate_response(user_message)

    safety_result = validate_response(response)

    if not safety_result.safe:
        return get_safe_fallback()

    return response


if __name__ == "__main__":
    message = input("You: ")
    print("Ataraxia:", run_ataraxia(message))
