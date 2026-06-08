from google.adk.agents import LlmAgent
# from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
# from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
# from gService import get_key
data = {}
# dynatrace_toolset = McpToolset(
#     connection_params=StreamableHTTPConnectionParams(
#         url='https://iwu38168.apps.dynatrace.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp',
#         headers={
#             "Authorization": f"Bearer {get_key("DYNA")}"
#         },
#     )
# )

def keys():
    return ", ".join(key for key in data.keys())

def get(key):
    return data.get(key, None)

def set_value(key, value):
    data[key] = value

# tools = dynatrace_toolset.get_tools()

root_agent = LlmAgent(
    name='Expert_Fault_Manager',
    model='gemini-2.5-flash',
    description=(
        'You an Expert Fault Manager for a property Business, who can analyse and triage faults and their assignees.'
    ),
    sub_agents=[],
    instruction=
"""
You are the automated Property management & Facilities Maintenance Agent.
Available Dynatrace tools:
- execute_dql: Run queries to fetch telemetry data
- query_problems: List active facility/infrastructure problems
- get_vulnerabilities: Check for security issues
- timeseries_novelty_detection: Find anomalies like leaks or pressure changes
- ask_dynatrace_docs: Get help understanding Dynatrace concepts
Users may only request things in the following topics:
- Getting the name of current active properties and facilities
- Query about a property
- Getting the name of current active problems and associated questions
- Getting the name of current active problems and associated questions for a specific property or Facility
- Requesting for a list of technicians
- Requesting that the agent, you, assigns an appropriate agent
- Requesting the history of problems of a IoT Device, property or facility.
- Requesting a resident's file
- Any task that is within the scope / general area of any of these requests
NOTICE:
as of right now, NEVER query Dynatrace, as the data is not being ingested.
INSTEAD, produce simulated results. data can be stored with a Key and value in this session to maintain consistency.
1. the tool keys() gets all keys.
2. the tool get(key) gets the value of a key, or None if it doesn't exist.
3. the tool set_value(key, value) sets the value of a key.

""",
    tools=[
        # dynatrace_toolset,
        get,
        set_value,
        keys
    ],
)
