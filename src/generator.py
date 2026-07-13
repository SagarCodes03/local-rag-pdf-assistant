import ollama

def generated_answer(query,context):

    prompt = f"""
you are a healpfull AI assistant.
Answer ONLY using the provided context. 
if the answer is not in the context, say:
"i couldn't find that information in your context."

context:
{context}

question:
{query}
"""
    response = ollama.chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role":"user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"]