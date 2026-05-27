import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    llm_provider: str
    debug: bool
    oci_compartment_id: str
    oci_model_id: str
    oci_service_endpoint: str
  
def get_settings() -> Settings:
        provider = (os.getenv("LLM_PROVIDER") or "OCI").strip().upper()
        debug_raw = (os.getenv("DEBUG") or "false").strip().lower()
        debug = debug_raw in {"1", "true", "yes", "y"}
        oci_compartment_id = os.getenv("OCI_COMPARTMENT_ID") or ""
        oci_model_id = os.getenv("OCI_MODEL_ID") or "cohere.command-r-16k"
        oci_service_endpoint = (os.getenv("OCI_SERVICE_ENDPOINT") or "").strip()
        return Settings(
            llm_provider=provider,
            debug=debug,
            oci_compartment_id=oci_compartment_id,
            oci_model_id=oci_model_id,
            oci_service_endpoint=oci_service_endpoint,
        )
                                         