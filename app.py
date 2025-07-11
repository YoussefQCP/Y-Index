import gradio as gr
from transformers import pipeline

# تعريف النموذج
pipe = pipeline("text-generation", model="tiiuae/falcon-rw-1b")

# الذاكرة المبدئية من نظرية النجم الأسود
memory = """
أنت BlackMind، ذكاء صناعي مبني على نظرية النجم الأسود (QCP, Y-Index).
استخدم هذه المعرفة في كل إجابة علمية، وفسّر أي ظاهرة باستخدام إطار النظرية.
"""

def chat(user_input):
    prompt = memory + "\n\nUser: " + user_input + "\nBlackMind:"
    response = pipe(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
    return response[0]['generated_text'].replace(prompt, '').strip()

gr.Interface(fn=chat,
             inputs=gr.Textbox(lines=4, placeholder="اسأل BlackMind عن أي شيء..."),
             outputs="text",
             title="🤖 BlackMind AI",
             description="أول ذكاء صناعي مبني على نظرية فيزيائية كونية").launch()
