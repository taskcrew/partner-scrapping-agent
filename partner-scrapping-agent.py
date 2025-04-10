import os
from dotenv import load_dotenv
from typing import List, Any, Optional
from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from firecrawl import FirecrawlApp

# Load environment variables
load_dotenv()

# Initialize Firecrawl
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY', 'fc-bf21d51aaaf84ab3a9230f09640a3fbc')
firecrawl_app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

# Define extraction schema
class ExtractSchema(BaseModel):
    name: str
    opening_hours: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    wifi: Optional[str] = None

# Define Firecrawl tool
class FirecrawlTool(BaseTool):
    name: str = "firecrawl_extraction"
    description: str = "Extract business information from websites using Firecrawl"
    
    def _run(self, website: str) -> str:
        """
        Extract business information from a website using Firecrawl.
        
        Args:
            website: The website URL to extract data from
            
        Returns:
            Extracted business information
        """
        try:
            # Call the Firecrawl API with the schema
            data = firecrawl_app.extract(
                [website],
                {
                    'prompt': 'Extract information about the business from the website',
                    'schema': ExtractSchema.model_json_schema(),
                }
            )
            return str(data)
        except Exception as e:
            print(f"Error during extraction: {str(e)}")
            # Fallback mock data
            mock_data = {
                "name": f"{website.split('.')[0].title()}",
                "opening_hours": "Mon-Fri: 9AM-5PM",
                "phone": "+1 (555) 123-4567",
                "email": f"contact@{website}",
                "wifi": "Available"
            }
            return f"Error: {str(e)}. Using mock data: {str(mock_data)}"

# Create tool instance
firecrawl_tool = FirecrawlTool()

# Agent definition
data_extraction_agent = Agent(
    role="Data Extraction Specialist",
    goal="Extract business data from websites using Firecrawl",
    backstory="""You extract business information from websites efficiently.
    You understand how to use web scraping tools and can interpret structured data.""",
    verbose=True,
    tools=[firecrawl_tool]
)

# Function to create extraction task with the target website
def create_extraction_task(website):
    return Task(
        description=f"""Extract business information from {website} using Firecrawl.
        
        Use the firecrawl_extraction tool to extract business information.
        
        The extraction should focus on:
        - Business name
        - Opening hours
        - Phone number
        - Email address
        - Wi-Fi availability
        
        Present the extracted data in a clear, structured format.""",
        expected_output="""A structured presentation of the extracted business data
        with explanations of the key information found for the website.""",
        agent=data_extraction_agent
    )

# Function to create and run the crew
def run_business_intelligence(website):
    # Create task with the target website
    extraction_task = create_extraction_task(website)
    
    # Create the crew
    business_intelligence_crew = Crew(
        agents=[data_extraction_agent],
        tasks=[extraction_task],
        verbose=True,
        process=Process.sequential
    )
    
    # Run the crew
    print(f"🚀 Starting Business Intelligence Crew for {website}")
    result = business_intelligence_crew.kickoff()
    print(f"✅ Business Intelligence Complete for {website}")
    return result

# Run the crew
if __name__ == "__main__":
    # Prompt for target website
    default_website = "firecrawl.dev"
    user_input = input(f"Enter website URL to scrape (press Enter for default '{default_website}'): ")
    target_website = user_input.strip() if user_input.strip() else default_website
    
    # Run the business intelligence process
    result = run_business_intelligence(target_website)
    print(result) 