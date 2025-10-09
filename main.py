import requests
import gradio as gr


def echo(message, history):
    payload = {"human_says": message, "history": history}
    try:
        # Assuming FastAPI is running on http://127.0.0.1:8000
        response = requests.post("http://127.0.0.1:8000/interact", json=payload)
        response.raise_for_status()
        json_response = response.json()
        return json_response
    except requests.exceptions.RequestException as e:
        print(e)
        return f"Error connecting to backend: {e}"

demo = gr.ChatInterface(fn=echo, type="messages", examples=["hello", "hola", "merhaba"], title="Echo Bot")
demo.launch()