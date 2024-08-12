import argparse
import python_weather
import asyncio

from langchain_ibm import ChatWatsonx
from langchain_core.messages.ai import AIMessage
from modules.load_env import load_ibmcloud_env, load_watson_x_env_min

# ******************************************
# Functions

async def getweather(args):
  
  temperature_list = []
  cities = args['city'].split(",")

  for city in cities:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
        temperature_list.append({"city":city, "temperature": str(weather.temperature) + " celsius"})
  return temperature_list

def load_env():
        
        ibmcloud_apikey , validation = load_ibmcloud_env()
        if( validation == False):
            return {  "apikey" : "ERROR",
                      "project_id" : "ERROR",
                      "url": "ERROR",
                      "model_id": "ERROR",
                    }
        else:
             apikey = ibmcloud_apikey['IBMCLOUD_APIKEY']
             
        watson_x_env, validation = load_watson_x_env_min()
        
        if validation == False:
            return { "apikey" : "ERROR",
                     "project_id" : "ERROR",
                     "url": "ERROR",
                     "model_id": "ERROR",
                    }
        else:
             project_id = watson_x_env['WATSONX_PROJECT_ID']
             url = watson_x_env['WATSONX_URL']
             model_id = watson_x_env['WATSONX_LLM_NAME']
                        
        return { "project_id" : project_id,
                 "url": url,
                 "model_id": model_id,
                 "apikey": apikey }

def categories_load():
       categories = [
                {
                    "category": "Exchange_Rates",
                    "id": 1
                },
                {   "category": "International_Investment_Position", 
                    "id": 2
                },
                {   "category": "Bank_and_Credit_Card_Sectoral_Expenditure_Statistics", 
                    "id": 3
                }
            ]
       return categories

def tools_load():
      tools = [{
                "type": "function",
                "function": {
                    "name": "finance_service",
                    "description": "finance advisor api provide all of the financial needs and information in that api, it serve financial instructions, international finance statuses, money transactions, loans, debits, banking operations or etc, you can found everything for financial area in this api",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "startdate": {
                                "type": "string",
                                "description": "requested transaction start date or time with format dd-MM-yyyy, it is required parameter you must find and return begin date value. If query not contains any start date, you can alternatively set start date as 01-01-2024"
                            },
                            "enddate": {
                                "type": "string",
                                "description": "requested transaction end date or time with format dd-MM-yyyy, it is required parameter you must find and return last date value. If query not contains any end date, you can alternatively set end date as 31-12-2024"
                            }
                        },
                        "required": [
                            "startdate",
                            "enddate"
                        ]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "weather_service",
                    "description": "weather advisor api provide all of the weather needs and information in that api, it serve weather information",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA"
                            }
                        },
                        "required": [
                            "location"
                        ]
                    }
                }
            }
            ]
      return tools

def watsonx_tools_calling():
        #weather_aimessage = AIMessage()
        #finance_aimessage = AIMessage()

        environment = load_env()
        print(f"1. Load environment variables\n{environment}\n")
              
        parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": 400,
            "min_new_tokens": 1,
            "temperature": 1.0
        }
        print(f"2. Prepare model parameters\n{parameters}\n")
        
        print(f"3. Create a ChatWatsonx instance\n")
        watsonx_chat =  ChatWatsonx( model_id=environment['model_id'],
            url=environment['url'],
            project_id=environment['project_id'],
            apikey= environment['apikey'],
            params=parameters
        )
        
        print(f"4. Bind tools to chat\n")
        watsonx_chat_with_tools = watsonx_chat.bind_tools(tools_load())

        # Weather example
        print(f"5. Run the weather example\n")
        weather_system_prompt = """You are a weather expert. If the question is not about the weather, say: I don't know."""
        weather_question="Which city is hotter today: LA or NY?"
        weather_messages = [
            ("system", weather_system_prompt),
            ("human", weather_question)
        ]
        print(f"- Weather_messages:\n{weather_messages}\n")
        weather_aimessage = watsonx_chat_with_tools.invoke(input=weather_messages)
        
        print(f"- Weather_aimessage:\n{weather_aimessage}\n")
        print(f"- Weather_tools:\n{weather_aimessage.tool_calls}\n")
        print(f"- Invoke real weather endpoint:\n{asyncio.run(getweather(weather_aimessage.tool_calls[0]['args']))}\n")
        
        # Finance example
        print(f"\n6. Run the finance example\n")
        finance_system_prompt = """You are a finance expert tasked with analyzing the questions and selecting the most relevant title from a specified table. Find the finance topic and finance category that best match the content of the sentence.
        **Dictionary:**
        {categories}
        **Instructions:**
        - Determine the correct table from the dictionary.
        - Use this table to find the finance topic and finance category values that are most relevant to the finance sentence
        - Ensure that the values retrieved are the best match to the content of the sentence.
        **Conclusion:**
        Provide the result in the following format, only return following information not add any other word or sentence in response, give answer only in JSON Object format, only return answer with the following format do not use different format:
        {{"category": "found_category", "id": category_id}}
        """
        finance_system_prompt.format(categories=categories_load())
        finance_question = "What percentage of total Debit Card and Credit Card expenditures were made in the Airlines and Accommodation sectors in 2023?"
        finance_messages = [
            ("system", finance_system_prompt),
            ("human", finance_question)
        ]
        print(f"- Finance_messages:\n{finance_messages}\n")
        
        finance_aimessage = watsonx_chat_with_tools.invoke(input=finance_messages)
        
        print(f"- Finance_aimessage:\n{finance_aimessage}\n")
        print(f"- Finance_tools:\n{finance_aimessage.tool_calls}\n")
        print(f"- Invoke example finance endpoint:\n Your finance request is from {finance_aimessage.tool_calls[0]['args']['startdate']} to {finance_aimessage.tool_calls[0]['args']['enddate']}")
        return 

# ******************************************
# Execution
def main(args):

     watsonx_tools_calling()
     
     
if __name__ == "__main__":  
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)