from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class PostWriter():
    """PostWriter crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'], 
            verbose=True
        )

    @task
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['writer_task'], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PostWriter crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
