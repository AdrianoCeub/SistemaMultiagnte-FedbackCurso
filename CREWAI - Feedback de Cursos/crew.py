from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())


def get_gemini_api_key():
    load_env()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    return gemini_api_key

LLModel = LLM(
model="gemini/gemini-1.5-flash", 
temperature=0.5,
api_key=get_gemini_api_key(),
)

# Uncomment the following line to use an example of a custom tool
# from sistema_multi_agentes.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class SistemaMultiAgentesCrew():
	"""SistemaMultiAgentes crew"""

	@agent
	def analista(self) -> Agent:
		return Agent(
			config=self.agents_config['analista'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
		    allow_delegation=False,
			llm=LLModel
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
		    allow_delegation=False,
			llm=LLModel
		)
	
	@agent
	def analista_graficos(self) -> Agent:
		return Agent(
			config=self.agents_config['analista_graficos'],
			verbose=True,
		    allow_delegation=False,
			llm=LLModel
		)

	@agent
	def desenvolvedor(self) -> Agent:
		return Agent(
			config=self.agents_config['desenvolvedor'],
			verbose=True,
		    allow_delegation=False,
			allow_code_execution=True,
			llm=LLModel
		)

	@task
	def classification_task(self) -> Task:
		return Task(
			config=self.tasks_config['classification_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='results/report.md'
		)
	
	@task
	def grafico_task(self) -> Task:
		return Task(
			config=self.tasks_config['grafico_task'],
			output_file='results/graficos.py'
		)



	@crew
	def crew(self) -> Crew:
		"""Creates the SistemaMultiAgentes crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			#process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)