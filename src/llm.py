from dataclasses import dataclass
from typing import Protocol
import oci

@dataclass(frozen=True)
class LLMResponse:
    text: str
    provider: str

class LLMClient(Protocol):
    """
    Interface that all LLM clients must follow.
    """
    def generate(self, system: str, user: str) -> LLMResponse:
        ...

class OCIClient:
    """
    Real LLM client that connects to Oracle Cloud
    Generative AI service.
    """
    def __init__(
        self,
        compartment_id: str,
        model_id: str,
        service_endpoint: str,
    ):
        self.compartment_id = compartment_id
        self.model_id = model_id
        self.client = oci.generative_ai_inference.GenerativeAiInferenceClient(
            config=oci.config.from_file(),
            service_endpoint=service_endpoint,
        )

    def generate(self, system: str, user: str) -> LLMResponse:
        """
        Sends the prompt to Oracle's AI and returns the response.
        """
        response = self.client.chat(
            oci.generative_ai_inference.models.ChatDetails(
                compartment_id=self.compartment_id,
                serving_mode=oci.generative_ai_inference.models.OnDemandServingMode(
                    model_id=self.model_id
                ),
                chat_request=oci.generative_ai_inference.models.CohereChatRequest(
                    message=user,
                    preamble_override=system,
                )
            )
        )
        text = response.data.chat_response.text
        return LLMResponse(text=text, provider="OCI")

def get_llm_client(
    provider: str,
    compartment_id: str = "",
    model_id: str = "",
    service_endpoint: str = "",
) -> LLMClient:
    """
    Factory function that returns the correct LLM client
    based on the configured provider.
    """
    provider = provider.strip().upper()

    if provider == "OCI":
        return OCIClient(
            compartment_id=compartment_id,
            model_id=model_id,
            service_endpoint=service_endpoint,
        )

    raise ValueError(f"Unknown LLM_PROVIDER: {provider}")
