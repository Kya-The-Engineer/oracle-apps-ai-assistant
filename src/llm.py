from dataclasses import dataclass #creates containers for data
from typing import Protocol 

@dataclass(frozen=True)
class LLMResponse:
    text: str
    provider : str

class LLMClient(Protocol): # 
    """
    Interface that all LLM clients must follow.
    """
    def generate(self, system: str, user: str) -> LLMResponse: #One consistent method no matter the backend.
        ... #Placeholder


    class StubClient:
            """
            Fake LLM client used for development and testing.
            Returns a predictable response so we can validate workflow without calling a real API.
            """
            def generate(self, system: str, user: str) -> LLMResponse:
                text = (
                 
                )
                return LLMResponse(text=text, provider = "STUB")
            
    def get_llm_client(provider: str) -> LLMClient:
                """
                Factory function that returns the correct LLM client based on the configured provider.
                """
                provider = provider.strip().upper()

                #Chooses the correct client based on the provider. Gives it to main.py.
                if provider == "STUB":
                    return StubClient()
                
                if provider == "OCI":
                    raise NotImplementedError("OCI client not wired yet. Use STUB for now.")
                if provider == "OPENAI":
                    raise NotImplementedError("OpenAI client not wired yet. Use STUB for now.")
                raise ValueError(f"Uknown LLM_PROVIDER: {provider}")
            


