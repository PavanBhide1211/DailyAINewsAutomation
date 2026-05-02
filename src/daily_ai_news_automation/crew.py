import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerplyNewsSearchTool
)






@CrewBase
class DailyAiNewsAutomationCrew:
    """DailyAiNewsAutomation crew"""

    
    @agent
    def ai_news_researcher(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["ai_news_researcher"],
            
            
            tools=[				SerplyNewsSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def document_manager(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["document_manager"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            apps=[
                    "microsoft_word/create_document",
                    
                    "microsoft_word/get_documents",
                    
                    "microsoft_word/get_document_content",
                    ],
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def file_repository_manager(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["file_repository_manager"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            apps=[
                    "microsoft_onedrive/list_files",
                    
                    "microsoft_onedrive/share_item",
                    
                    "microsoft_onedrive/search_files",
                    ],
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def email_communication_manager(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["email_communication_manager"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            apps=[
                    "microsoft_outlook/send_email",
                    ],
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    

    
    @task
    def gather_daily_ai_news(self) -> Task:
        return Task(
            config=self.tasks_config["gather_daily_ai_news"],
            markdown=False,
            
            
        )
    
    @task
    def update_monthly_ai_news_document(self) -> Task:
        return Task(
            config=self.tasks_config["update_monthly_ai_news_document"],
            markdown=False,
            
            
        )
    
    @task
    def generate_document_share_link(self) -> Task:
        return Task(
            config=self.tasks_config["generate_document_share_link"],
            markdown=False,
            
            
        )
    
    @task
    def send_daily_ai_news_email(self) -> Task:
        return Task(
            config=self.tasks_config["send_daily_ai_news_email"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the DailyAiNewsAutomation crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


