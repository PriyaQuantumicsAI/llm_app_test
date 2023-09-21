import requests
import json
url = 'http://127.0.0.1:5000/jarvis_gen_ai_process_text'
final_prompt = "data_glossary: What is the business purpose of ADB CAUSTIC?"

project_details = {"project_name":"qs_edi","user_id":322,"db_schema":"qsai_edi_rawdb_322"}

data = {'prompt': final_prompt , 'project_details': project_details}
# data = {'prompt': "data_glossary: What is the business purpose of ADB CAUSTIC?" , 'project_details': project_details}

#print(json.dumps(data, indent=4))
response = requests.post(url, json=data)
print(json.dumps(response.json(), indent=4))
