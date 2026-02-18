import json
from typing import Optional
from google.adk.agents import Agent

def update_transfer_details(
    amount: Optional[str] = None,
    country: Optional[str] = None,
    beneficiary: Optional[str] = None,
    method: Optional[str] = None
):
    """
    Saves and updates money transfer details in the session state.
    The agent MUST call this tool whenever new info is provided or corrected.
    """
    return f"RECORDED: {amount=}, {country=}, {beneficiary=}, {method=}"

# MUST be named 'root_agent' for the 'adk run .' command to work
root_agent = Agent(
    name="SendMoneyAgent",
    model="gemini-1.5-flash",
    description="Guided conversational agent for money transfers.",
    instruction="""
    You are a friendly money transfer assistant.
    Your goal is to collect: 1) Amount, 2) Country, 3) Beneficiary name, 4) Delivery method.

    OPERATING GUIDELINES:
    1. Identify Missing Info: Review the current state and ask for what is missing.
    2. Extract & Record: Use the 'update_transfer_details' tool immediately when info is provided.
    3. Handle Corrections: If the user says "actually make it 200", call the tool to overwrite the value.
    4. Conversational Slot Filling: Ask questions naturally (e.g., "And who are we sending this to?").
    5. Final Output: Once all 4 fields are collected, output a JSON summary of the transfer.
    """,
    tools=[update_transfer_details]
)