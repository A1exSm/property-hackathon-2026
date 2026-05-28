from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from gService import get_env_key

root_agent = LlmAgent(
    name='Expert_Fault_Manager',
    model='gemini-2.5-flash',
    description=(
        'You an Expert Fault Manager for a property Business, who can analyse and triage faults and their assignees.'
    ),
    sub_agents=[],
    instruction=(
        '# Agent Persona & Directives\n'
        'You are the automated Property Management & Facilities Maintenance Agent.\n\n'
        '# Operational Execution Loop\n'
        '1. When asked about building health, leak statuses, or HVAC performance, invoke the `dynatrace_property_mcp` tool.\n'
        '2. If the tool identifies an active \'Water Leak Detected\' or a \'Boiler Pressure Critical Failure\' event, '
        'categorize the required trade skill (e.g., Plumber or HVAC Engineer).\n'
        '3. Cross-reference the faulting location with your available staff tools, locate the on-duty technician '
        'matching that trade skill, and execute a dispatch webhook.\n'
        '4. Report back the telemetry details clearly to the user and confirm that the correct technician has been '
        'deployed to the property location.'
    ),
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url='https://iwu38168.apps.dynatrace.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp',
                headers={
                    "Authorization": f"Bearer {get_env_key("DYNA")}",
                    "Content-Type": "application/json"
                }
            ),
        )
    ],
)
