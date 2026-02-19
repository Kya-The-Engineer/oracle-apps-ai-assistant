import os 
from dataclasses import dataclass 
from dotenv import load_dotenv 


load_dotenv()

@dataclass(frozen=True) 
class Settings:  
    llm_provider: str  #Which backend to use for LLM.
    debug: bool   #Debug information

    def get_settings() -> Settings:
        """
        Read environment variables and return a Settings object.
        """

        provider = (os.getenv("LLM_PROVIDER") or "STUB").strip().upper()

        debug_raw = (os.getenv("DEBUG") or "false").strip().lower()
        debug = debug_raw in {"1", "true", "yes" , "y"}  #Allowlist
  
        return Settings ( 
            llm_provider=provider,
            debug=debug
        )
    
    