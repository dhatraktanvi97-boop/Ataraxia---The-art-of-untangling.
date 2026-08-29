from dataclasses import dataclass, field


@dataclass
class ConversationMemory:
    messages: list[str] = field(default_factory=list)

    def add_message(self, message: str) -> None:
        self.messages.append(message.strip())

    def get_recent_messages(self, limit: int = 5) -> list[str]:
        return self.messages[-limit:]

    def clear(self) -> None:
        self.messages.clear()
        