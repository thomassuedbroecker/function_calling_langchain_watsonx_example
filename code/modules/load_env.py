import os

##################################
# Configure Logging

def load_ibmcloud_env():
       if (os.environ.get("IBMCLOUD_APIKEY") == None):
            IBMCLOUD_APIKEY = ''
       else:
            IBMCLOUD_APIKEY = os.environ.get("IBMCLOUD_APIKEY")
        
       if (os.environ.get("IBMCLOUD_URL") == None):
            IBMCLOUD_URL = ''
       else:
            IBMCLOUD_URL = os.environ.get("IBMCLOUD_URL")

       if ((IBMCLOUD_APIKEY=='') or (IBMCLOUD_URL=='')):
            configurationStatus = False
       else:
            configurationStatus = True
    
       configurationJSON = { "IBMCLOUD_APIKEY": IBMCLOUD_APIKEY,
                             "IBMCLOUD_URL": IBMCLOUD_URL}
       
       return configurationJSON, configurationStatus

def load_instructlab_env():
    if (os.environ.get("INSTRUCTLAB_URL") == None):
            INSTRUCTLAB_URL = ''
    else:
            INSTRUCTLAB_URL = os.environ.get("INSTRUCTLAB_URL")

    if (os.environ.get("INSTRUCTLAB_PROMPT_FILE") == None):
            INSTRUCTLAB_PROMPT_FILE = ''
    else:
            INSTRUCTLAB_PROMPT_FILE = os.environ.get("INSTRUCTLAB_PROMPT_FILE")

    if (os.environ.get("INSTRUCTLAB_MAX_NEW_TOKENS") == None):
            INSTRUCTLAB_MAX_NEW_TOKENS = ''
    else:
            INSTRUCTLAB_MAX_NEW_TOKENS = os.environ.get("INSTRUCTLAB_MAX_NEW_TOKENS")


    
    if ((INSTRUCTLAB_PROMPT_FILE=='') or
        (INSTRUCTLAB_URL=='') or
        (INSTRUCTLAB_MAX_NEW_TOKENS=='')):
            configurationStatus = False
    else:
            configurationStatus = True
    
    configurationJSON = { "INSTRUCTLAB_PROMPT_FILE": INSTRUCTLAB_PROMPT_FILE,
                          "INSTRUCTLAB_URL":INSTRUCTLAB_URL,
                          "INSTRUCTLAB_MAX_NEW_TOKENS":INSTRUCTLAB_MAX_NEW_TOKENS
                        }

    return configurationJSON, configurationStatus

def load_watson_x_env_min():
    if (os.environ.get("WATSONX_URL") == None):
            WATSONX_URL = ''
    else:
            WATSONX_URL = os.environ.get("WATSONX_URL")

    if (os.environ.get("WATSONX_PROJECT_ID") == None):
            WATSONX_PROJECT_ID = ''
    else:
            WATSONX_PROJECT_ID = os.environ.get("WATSONX_PROJECT_ID")

    if (os.environ.get("WATSONX_LLM_NAME") == None):
            WATSONX_LLM_NAME = ''
    else:
            WATSONX_LLM_NAME = os.environ.get("WATSONX_LLM_NAME")
    
    if ((WATSONX_URL=='') or
        (WATSONX_LLM_NAME=='') or 
        (WATSONX_PROJECT_ID=='')):
            configurationStatus = False
    else:
            configurationStatus = True
    
    configurationJSON = { "WATSONX_URL": WATSONX_URL,
                          "WATSONX_LLM_NAME":WATSONX_LLM_NAME,
                          "WATSONX_PROJECT_ID":WATSONX_PROJECT_ID,
                        }

    return configurationJSON, configurationStatus

def load_watson_x_env():
    if (os.environ.get("WATSONX_URL") == None):
            WATSONX_URL = ''
    else:
            WATSONX_URL = os.environ.get("WATSONX_URL")

    if (os.environ.get("WATSONX_VERSION") == None):
            WATSONX_VERSION = ''
    else:
            WATSONX_VERSION = os.environ.get("WATSONX_VERSION")

    if (os.environ.get("WATSONX_PROJECT_ID") == None):
            WATSONX_PROJECT_ID = ''
    else:
            WATSONX_PROJECT_ID = os.environ.get("WATSONX_PROJECT_ID")

    if (os.environ.get("WATSONX_LLM_NAME") == None):
            WATSONX_LLM_NAME = ''
    else:
            WATSONX_LLM_NAME = os.environ.get("WATSONX_LLM_NAME")

    if (os.environ.get("WATSONX_MIN_NEW_TOKENS") == None):
            WATSONX_MIN_NEW_TOKENS = ''
    else:
            WATSONX_MIN_NEW_TOKENS = os.environ.get("WATSONX_MIN_NEW_TOKENS")

    if (os.environ.get("WATSONX_MAX_NEW_TOKENS") == None):
            WATSONX_MAX_NEW_TOKENS = ''
    else:
            WATSONX_MAX_NEW_TOKENS = os.environ.get("WATSONX_MAX_NEW_TOKENS")

    if (os.environ.get("WATSONX_PROMPT_FILE") == None):
            WATSONX_PROMPT_FILE = ''
    else:
            WATSONX_PROMPT_FILE = os.environ.get("WATSONX_PROMPT_FILE")

    if (os.environ.get("WATSONX_USERNAME") == None):
            WATSONX_USERNAME = ''
    else:
            WATSONX_USERNAME = os.environ.get("WATSONX_USERNAME")

    if (os.environ.get("WATSONX_INSTANCE_ID") == None):
            WATSONX_INSTANCE_ID = ''
    else:
            WATSONX_INSTANCE_ID = os.environ.get("WATSONX_INSTANCE_ID")
    
    if ((WATSONX_URL=='') or
        (WATSONX_LLM_NAME=='') or 
        (WATSONX_MIN_NEW_TOKENS=='') or 
        (WATSONX_MAX_NEW_TOKENS=='') or 
        (WATSONX_PROMPT_FILE=='') or
        (WATSONX_VERSION=='') or
        (WATSONX_PROJECT_ID=='') or 
        (WATSONX_USERNAME=='') or 
        (WATSONX_INSTANCE_ID=='')):
            configurationStatus = False
    else:
            configurationStatus = True
    
    configurationJSON = { "WATSONX_URL": WATSONX_URL,
                          "WATSONX_LLM_NAME":WATSONX_LLM_NAME,
                          "WATSONX_MIN_NEW_TOKENS":WATSONX_MIN_NEW_TOKENS,
                          "WATSONX_MAX_NEW_TOKENS":WATSONX_MAX_NEW_TOKENS,
                          "WATSONX_PROMPT_FILE":WATSONX_PROMPT_FILE,
                          "WATSONX_PROJECT_ID":WATSONX_PROJECT_ID,
                          "WATSONX_VERSION":WATSONX_VERSION,
                          "WATSONX_USERNAME":WATSONX_USERNAME,
                          "WATSONX_INSTANCE_ID":WATSONX_INSTANCE_ID
                        }

    return configurationJSON, configurationStatus