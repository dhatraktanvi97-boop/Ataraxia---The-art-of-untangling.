from ataraxia.context import create_context
from ataraxia.response import generate_response
from ataraxia.safety import validate_response, get_safe_fallback
from ataraxia.memory import ConversationMemory


def run_ataraxia(user_message: str, memory: ConversationMemory) -> str:
    recent_messages = memory.get_recent_messages()

    context = create_context(
        user_message,
        recent_messages
    )

    response = generate_response(context)

    safety_result = validate_response(response)

    if not safety_result.safe:
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
        
