from dataclasses import dataclass

@dataclass(frozen=True)
class Prompt:
    system: str
    template: str

# Sets prompt for support requests.
    SUPPORT_PROMPT = Prompt( 

    )   
    
    # Sets prompt for communication requests.
    COMMS_PROMPT = Prompt(
        system=(
            "You are an Oracle Apps Communication Assistant",
             ),
        template=(
        
        ),

    )

    def build_support_prompt(question: str) -> str:
        q = question.strip()
        if not q:
            raise ValueError("Support question cannot be empty.")  # Returns this ValueError if the question is empty.
        return Prompt.SUPPORT_PROMPT.template.format(question=q)
    
    def build_comms_prompt(context: str) -> str:
        c = context.strip()
        if not c:
            raise ValueError("Comms context cannot be empty.")
        return Prompt.COMMS_PROMPT.template.format(context=c)
    
    def parse_mode_and_text(raw: str) -> tuple[str, str]:
    
      
    

