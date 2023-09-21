# Quantumics Generative AI APP
Quantumics.AI LLM application

## Installation and running the code locally

### Prerequisites
1. Pycharm/Visual Studio Code
2. Anaconda (Python 3.10) 
3. Git

### Steps
1. Clone the repository
2. Open the project in Pycharm/Visual Studio Code
3. Create a virtual environment in Pycharm with Python 3.10
4. Install the requirements.txt file using the following command in the terminal
``` pip install -r requirements.txt ```
5. Run the app.py file
6. Open temp/test_api and run the test_api.py file


### Steps for running the code on the server Docker
1. Clone the repository
2. Go inside the repository
3. Run the following command
``` docker build -t llm_app_test:v1 . ```
``` docker run -p 5000:5000 llm_app_test:v1 ```
4. Open temp/test_api and run the test_api.py file


### Author
1. Priyadharshini Devarajan

### Contributors
1. Priyadharshini Devarajan
2. Diksha
3. Somto
4. Sai Kumar
5. Kishore Kumar
6. Karthick Subbaraman
