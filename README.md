# function_calling_langchain_watsonx_example

This repository is an example using the `langchain_ibm` implementation for function calling with watsonx.

Related blog post: [Integrating langchain_ibm with watsonx and LangChain: Example and Tutorial](https://wp.me/paelj4-20d)

## Setup and run the example

The following steps are instructions on how to run the example on your local machine.

### Step 1: Clone the repository to your local machine
```sh
git clone https://github.com/thomassuedbroecker/function_calling_langchain_watsonx_example.git
```

### Step 2: Generate a virtual Python environment

```sh
cd code
python3 -m venv --upgrade-deps venv
source venv/bin/activate
```

### Step 3: Install the needed libraries

```sh 
python3 -m pip install -qU langchain-ibm
python3 -m pip install python-weather
```

### Step 4: Generate a `.env` file for the needed environment variables

```sh
cat env_example_template > .env
```

Insert the values for the two environment variables: 

* `WATSONX_PROJECT_ID=YOUR_WATSONX_PROJECT_ID`
* `IBMCLOUD_APIKEY=YOUR_KEY`

Content of the environment file.

```sh
export IBMCLOUD_APIKEY=YOUR_KEY
export IBMCLOUD_URL="https://iam.cloud.ibm.com/identity/token"

# Watsonx
export WATSONX_URL="https://eu-de.ml.cloud.ibm.com"
export WATSONX_VERSION=2023-05-29
export WATSONX_PROJECT_ID=YOUR_PROJECT_ID

export WATSONX_MIN_NEW_TOKENS=1
export WATSONX_MAX_NEW_TOKENS=300
export WATSONX_LLM_NAME=mistralai/mixtral-8x7b-instruct-v01
export WATSONX_INSTANCE_ID=YOUR_WATSONX_INSTANCE_ID
```

### Step 5: Run the example

```sh
bash example_function_invocation.sh
```

* Output of the invocation:

```
##########################
# 0. Load environments
##########################
# 1. Invoke application
1. Load environment
{'project_id': 'YOUR_PROJECT_ID', 'url': 'https://eu-de.ml.cloud.ibm.com', 'model_id': 'mistralai/mixtral-8x7b-instruct-v01', 'apikey': 'YOUR_APIKEY'}

2. Prepare model parameters
{'decoding_method': 'greedy', 'max_new_tokens': 400, 'min_new_tokens': 1, 'temperature': 1.0}

3. Create a ChatWatsonx instance

4. Bind tools to chat

5. Run the weather example

- Weather_messages:
[('system', "You are a weather expert. If the question is not about the weather, say: I don't know."), ('human', 'Which city is hotter today: LA or NY?')]

- Weather_aimessage:
content='' additional_kwargs={'tool_calls': {'type': 'function', 'function': {'name': 'weather_service', 'arguments': {'city': 'LA, NY'}}}} response_metadata={'token_usage': {'generated_token_count': 65, 'input_token_count': 723}, 'model_name': 'mistralai/mixtral-8x7b-instruct-v01', 'system_fingerprint': '', 'finish_reason': 'stop_sequence'} id='run-6893b0a4-85cb-44fd-8500-fd44c35def5e-0' tool_calls=[{'name': 'weather_service', 'args': {'city': 'LA, NY'}, 'id': '1723450740.908', 'type': 'tool_call'}] usage_metadata={'input_tokens': 723, 'output_tokens': 65, 'total_tokens': 788}

- Weather_tools:
[{'name': 'weather_service', 'args': {'city': 'LA, NY'}, 'id': '1723450740.908', 'type': 'tool_call'}]

- Invoke real weather endpoint:
[{'city': 'LA', 'temperature': '11 celsius'}, {'city': ' NY', 'temperature': '13 celsius'}]


6. Run the finance example

- Finance_messages:
[('system', 'You are a finance expert tasked with analyzing the questions and selecting the most relevant title from a specified table. Find the finance topic and finance category that best match the content of the sentence.\n        **Dictionary:**\n        {categories}\n        **Instructions:**\n        - Determine the correct table from the dictionary.\n        - Use this table to find the finance topic and finance category values that are most relevant to the finance sentence\n        - Ensure that the values retrieved are the best match to the content of the sentence.\n        **Conclusion:**\n        Provide the result in the following format, only return following information not add any other word or sentence in response, give answer only in JSON Object format, only return answer with the following format do not use different format:\n        {{"category": "found_category", "id": category_id}}\n        '), ('human', 'What percentage of total Debit Card and Credit Card expenditures were made in the Airlines and Accommodation sectors in 2023?')]

- Finance_aimessage:
content='' additional_kwargs={'tool_calls': {'type': 'function', 'function': {'name': 'finance_service', 'arguments': {'startdate': '01-01-2023', 'enddate': '31-12-2023'}}}} response_metadata={'token_usage': {'generated_token_count': 393, 'input_token_count': 902}, 'model_name': 'mistralai/mixtral-8x7b-instruct-v01', 'system_fingerprint': '', 'finish_reason': 'stop_sequence'} id='run-f5865bca-48b5-49ba-b285-adb15235d79d-0' tool_calls=[{'name': 'finance_service', 'args': {'startdate': '01-01-2023', 'enddate': '31-12-2023'}, 'id': '1723450746.65', 'type': 'tool_call'}] usage_metadata={'input_tokens': 902, 'output_tokens': 393, 'total_tokens': 1295}

- Finance_tools:
[{'name': 'finance_service', 'args': {'startdate': '01-01-2023', 'enddate': '31-12-2023'}, 'id': '1723450746.65', 'type': 'tool_call'}]

- Invoke example finance endpoint:
 Your finance request is from 01-01-2023 to 31-12-2023
```