from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class LLMResponse:
    text: str
    provider : str

class LLMClient(Protocol):
    """
    Interface that all LLM clients must follow.
    """
    def generate(self, system: str, user: str) -> LLMResponse:
        ...


        class StubClient:
            """
            Fake LLM client used for development and testing.
            Returns a predictable response so we can validate workflow without calling a real API.
            """
            def generate(self, system: str, user: str) -> LLMResponse:
                text = (
                    "1) Summary\n"
                    "This is a stubbed response used to test the assistant workflow.\n\n"
                    "2) Likely Causes\n"
                    "- Missing configuration\n"
                    "- Incomplete context\n\n"
                    "3) Troubleshooting Steps\n"
                    "1. Confirm the affect module and process.\n"
                    "2. Capture the exact error message.\n"
                    "3. Attempt to reproduce the issue.\n\n"
                    "4) What I Need From You\n"
                    "- Module name\n"
                    "- Error text or screenshot\n"
                )
                return LLMResponse(text=text, provider = "STUB")
            
            def get_llm_client(provider: str) -> LLMClient:
                """
                Factory function that returns the correct LLM client based on the configured provider.
                """
                provider = provider.strip().upper()

                if provider == "STUB":
                    return StubClient()
                
                if provider == "OCI":
                    raise NotImplementedError("OCI client not wired yet. Use STUB for now.")
                if provider == "OPENAI":
                    raise NotImplementedError("OpenAI client not wired yet. Use STUB for now.")
                raise ValueError(f"Uknown LLM_PROVIDER: {provider}")
            


