from flask import Flask, request, render_template
from random import choice

MB_PREFIX = 'Bad Magic Ball 👹'

def is_answer():
    positive_phrases = ['Полюбэ', 'Как пить дать', 'Ежу понятно', 'Ясен красен', 'Да, чёрт возьми!']
    somepositive_phrases = ['Есть! На жопе шерсть', 'Сомнительно, но ok', 'Ну рискни здоровьем', 'Себя надо заставлять', 'Допустим']
    neutral_phrases = ['Ну хз', 'Завязывай!', 'Оно тебе надо?', 'Валера Кипелов', 'Называется например']
    negative_phrases = ['Ты на ушко мне шепни', 'Забей хер', 'Не еби мозги!', 'Это не для средних умов', 'Оно тебе на хуй не надо!', 'Гонишь!']
    cat = choice([positive_phrases, somepositive_phrases, neutral_phrases, negative_phrases])
    return f'{MB_PREFIX} {choice(cat)}'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', prefix=MB_PREFIX)

@app.route('/ask', methods=['POST'])
def handle_ask():
    user_question = request.form.get('question', '')
    answer_text = is_answer()
    return render_template('index.html', prefix=MB_PREFIX, question=user_question, answer=answer_text)

if __name__ == '__main__':
    app.run(debug=True)