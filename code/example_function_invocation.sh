echo "##########################"
echo "# 0. Load environments"
source ./venv/bin/activate
source .env

echo "##########################"
echo "# 1. Invoke application"
python3 function_calling_example.py
