from app.services.llm_service import generate_response

response = generate_response("What is the capital of France?")
print(response)