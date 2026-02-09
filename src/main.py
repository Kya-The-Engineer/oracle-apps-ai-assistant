#Importing functions from other files.

from config import get_settings 
from llm import get_llm_client
from prompts import (
    SUPPORT_PROMPT,
    COMMS_PROMPT,
    build_support_prompt,
    build_comms_prompt,
    parse_mode_and_text
)  

def main() -> None:

    settings = get_settings()
    client = get_llm_client(settings.llm_provider)

