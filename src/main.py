from ataraxia.context import create_context
from ataraxia.response import generate_response
from ataraxia.safety import (
    check_user_input,
    validate_response,
    get_safe_fallback,
)
from ataraxia.memory import ConversationMemory


def run_ataraxia(user_message: str, memory: ConversationMemory) -> str:
    input_safety = check_user_input(user_message)

    if not input_safety.safe:
        return get_safe_fallback()

    recent_messages = memory.get_recent_messages()

    context = create_context(
        user_message,
        recent_messages
    )

    response = generate_response(context)

    response_safety = validate_response(response)

    if not response_safety.safe:
        response = get_safe_fallback()

    memory.add_message(user_message)

    return response


if __name__ == "__main__":
    memory = ConversationMemory()

    while True:
        message = input("You: ")

        if message.lower().strip() in ["exit", "quit"]:
            print("Ataraxia: Conversation ended.")
            break

        response = run_ataraxia(message, memory)
        print("Ataraxia:", response)