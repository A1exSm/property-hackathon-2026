from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from gService import get_key
from telemetry.telemetry import TelemetryData

dynatrace_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url='https://iwu38168.apps.dynatrace.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp',
        headers={
            "Authorization": f"Bearer {get_key("DYNA")}"
        },
    )
)

tools = dynatrace_toolset.get_tools()

root_agent = LlmAgent(
    name='Expert_Fault_Manager',
    model='gemini-2.5-flash',
    description=(
        'You an Expert Fault Manager for a property Business, who can analyse and triage faults and their assignees.'
    ),
    sub_agents=[],
    instruction=(
        "You are the automated Property Management & Facilities Maintenance Agent.\n\n"
        "Available Dynatrace tools:\n"
        "- execute_dql: Run queries to fetch telemetry data\n"
        "- query_problems: List active facility/infrastructure problems\n"
        "- get_vulnerabilities: Check for security issues\n"
        "- timeseries_novelty_detection: Find anomalies like leaks or pressure changes\n"
        "- ask_dynatrace_docs: Get help understanding Dynatrace concepts\n\n"
        "When asked about building health, leaks, HVAC, or boiler status:\n"
        "1. Use execute_dql to fetch relevant metrics (water usage, pressure, temperature)\n"
        "2. Use query_problems to identify active issues\n"
        "3. Use timeseries_novelty_detection to spot spikes or anomalies\n"
        "4. If a critical event is found (leak, pressure failure), recommend technician dispatch\n"
    ),
    tools=[
        dynatrace_toolset,
    ],
)
