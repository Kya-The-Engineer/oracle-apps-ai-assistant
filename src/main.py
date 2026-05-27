# Importing functions from the other files.
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
    """
    Main function that runs the Oracle AI App Assistant.
    """
    # Load settings from .env file
    settings = get_settings()

    # Get the correct AI client based on config
    client = get_llm_client(
        provider=settings.llm_provider,
        compartment_id=settings.oci_compartment_id,
        model_id=settings.oci_model_id,
        service_endpoint=settings.oci_service_endpoint,
    )

    print("Welcome to the Oracle AI App Assistant!")
    print("Type 'support: your question' for support help.")
    print("Type 'comms: your request' for communication help.")
    print("Type 'quit' to exit.")
    print("-" * 50)

    # Main interaction loop
    while True:
        # Get input from the user
        raw_input = input("\nYou: ").strip()

        # Exit if user types quit
        if raw_input.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break

        # Skip empty input
        if not raw_input:
            print("Please enter a question or request.")
            continue

        # Figure out mode and clean the input
        mode, text = parse_mode_and_text(raw_input)

        # Build the correct prompt based on mode
        if mode == "support":
            system = SUPPORT_PROMPT.system
            user = build_support_prompt(text)
        else:
            system = COMMS_PROMPT.system
            user = build_comms_prompt(text)

        # Send to Oracle AI and get response
        print("\nAssistant: thinking...")
        response = client.generate(system=system, user=user)

        # Display the response
        print(f"\nAssistant: {response.text}")
        print(f"(Powered by: {response.provider})")
        print("-" * 50)

if __name__ == "__main__":
    main()
