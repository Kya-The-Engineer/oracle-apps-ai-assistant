# oracle-apps-ai-assistant
**This hybrid AI Assistant was designed for support and communications related to OCI applications.**

## *What It Does*
This AI Assistant gives users access to two modes.
- **Support Mode** : Using the prefix "support:", ask questions about Oracle apps and get clear, step-by-step troubleshooting guidance.
- **Comms Mode** : Using the prefix "comms:", describe what you need to communicate and receive a professionally drafted response.

## *Built Using*
- **OCI GenAI:** Cohere Command R Plus model
- **OCI Python SDK:** for connecting to Oracle's AI inference service
- **python-dotenv:** for secure environment variable management

## *Skills*
- **Prompt Engineering:** designed prompts and message templates for 2 separate use cases.
- **Cloud API Intergration:** connected a Python application to a live Oracle GenAI service.
- **Modular Architecture:** separated concerns across 4 focused files. Helped greatly with organization.
- **Secure Configuration Management:** used environment variables to hold my OCI credentials and to keep from hardcoding sensitive data.
- **Python OOP:** implemented Protocol interfaces, dataclasses, and factory functions.
- **Error Handling:** defensive programming with input validation (allowlist) and descriptive error messages.

## *How To Run It*
- Python 3.9+
- Run python src/main.py
- 
## *Example*

Welcome to Oracle AI App Assistant!
Type 'support: your question' for support help.
Type 'comms: your request' for communication help.
Type 'quit' to exit.
----------------------------------------------------
You: support: How do I change my password in Oracle?

Assistant: 
Here are the general steps to change your password in Oracle Applications:

1. Log in to your Oracle Applications account
2. Click your profile icon in the top right corner
3. Select 'Account Settings' or 'My Profile'
4. Navigate to the Security or Password section
5. Click 'Change Password' and follow the prompts

## *Certs*
- Oracle Cloud Infrastructure AI Foundations
- Oracle Cloud Infrastructure GenAI Professional
- Oracle Cloud Infrastructure Foundations

I built this project to showcase practical skills in prompt engineering,  cloud API integration, and Python application development using OCI. The goal was to solve a real use case by helping others navigate Oracle applications through a conversational AI interface.
