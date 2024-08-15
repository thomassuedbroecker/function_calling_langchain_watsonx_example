#############################
# Environment variables
echo "##########################"
echo "# 0. Load environments"
source ./venv/bin/activate
source .env

# Optional for get watsonx instance id
export IBMCLOUD_REGION="YOUR REGION example 'eu-de'"
export IBMCLOUD_GROUP="YOUR GROUP example 'default'"
export WATSONMACHINELEARNING_SERVICE_NAME=YOUR_SERVICE_NAME

#############################
# Functions
function get_watsonx_instance_id() {
    echo "##########################"
    echo "# -Get Watson Machine Learning Instance ID"
    ibmcloud login --apikey ${IBMCLOUD_APIKEY}
    ibmcloud target -r $IBMCLOUD_REGION -g $IBMCLOUD_GROUP
    export WATSONX_INSTANCE_ID=$(ibmcloud resource service-instance ${WATSONMACHINELEARNING_SERVICE_NAME} | grep "GUID" | awk '{print $2;}')
    echo "** Log: WATSONX_INSTANCE_ID: ${WATSONX_INSTANCE_ID}"
}

##############################
# Execution
echo "##########################"
echo "# 1. Invoke application"
python3 function_calling_example.py
