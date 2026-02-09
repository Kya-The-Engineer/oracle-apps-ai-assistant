import os  # Used to store setting and secrets w/o hardcoding them.
from dataclasses import dataclass # Creatrs container for settings.
from dotenv import load_dotenv #Loads variables from a .env file.

# Load envirnoment variables from a .env file. Allows variables to be read using os.getenv().
load_dotenv()

@dataclass(frozen=True) #Keeps settings from being changed after it runs.
class Settings:  #Creates container for Settings.
    llm_provider: str  #Which backend to use for LLM.
    debug: bool   #Whether to print debug information

    def get_settings() -> Settings: #Main funtion. Keeps env from being read multiple times.
        """
        Read environment variables and return a Settings object.
        """

        #Determine the provider to use. STUB gurantees the app runs even if no provider is set.
        # Strip removes extra spacees. Makes all variations of the provider name UPPERCASE.
        provider = (os.getenv("LLM_PROVIDER") or "STUB").strip().upper()

        # Determines if debug mode is on. 
        debug_raw = (os.getenv("DEBUG") or "false").strip().upper()
        debug = debug_raw in {"1", "true", "yes" , "y"}

        return Settings (
            llm_provider=provider,
            debug=debug
        )
    