from dataclasses import dataclass

@dataclass(frozen=True)
class Prompt:
    system: str
    template: str

# Sets prompt for support requests.
SUPPORT_PROMPT = Prompt(
    system=(
        "You are an Oracle Apps Support Assistant. You help users troubleshoot issues with Oracle Applications. "
        "Be clear, professional, and give step by step instructions in your responses."
    ),
    template=(
        "The user has the following support question: \n\n\""
        "{question}\n\n\""
        "Please provide a helpful and accurate response."
    ),
)
    
# Sets prompt for communication requests.
COMMS_PROMPT = Prompt(
    system=(
        "You are an Oracle Apps Communication Assistant. "
        "You help users draft communications related to Oracle Applications."
    ),
    template=(
        "The user needs help with the following communication: \n\n\""
        "{context}\n\n\""
        "Please draft a clear and professional response."
    ),
)


def build_support_prompt(question: str) -> str:
    q = question.strip()
    if not q:
        raise ValueError("Support question cannot be empty.")
    return SUPPORT_PROMPT.template.format(question=q)


def build_comms_prompt(context: str) -> str:
    c = context.strip()
    if not c:
        raise ValueError("Comms context cannot be empty.")
    return COMMS_PROMPT.template.format(context=c)


def parse_mode_and_text(raw: str) -> tuple[str, str]:
    cleaned = raw.strip().lower()

    if cleaned.startswith("support:"):
        text = raw[len("support:"):].strip()
        return ("support", text)

    if cleaned.startswith("comms:"):
        text = raw[len("comms:"):].strip()
        return ("comms", text)

    return ("support", raw.strip())
    
      
    

