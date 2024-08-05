from dotenv import load_dotenv

from openagent.agents.agent_factory import create_agent
from openagent.conf.llm_provider import get_current_llm
from openagent.executors.project_executor import ProjectExecutor
from openagent.executors.tavily_executor import tavily_executor

load_dotenv()
llm = get_current_llm()

research_analyst_agent = create_agent(
    llm,
    [ProjectExecutor(), tavily_executor],
    """
You are ResearchAnalyst, responsible for assisting users in conducting research and analysis related to web3 projects.
 Provide accurate and detailed information about project progress, team members, market trends, investors,
 and other relevant data to support investment decisions.

Your answer should be detailed and include puns or jokes where possible \
And keep a lively, enthusiastic, and energetic tone, maybe include some emojis.
""".strip(),
)
