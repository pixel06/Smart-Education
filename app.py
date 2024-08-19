from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Ensure this is kept secret and secure

# Define all questions
all_questions = [
    {"question": "What is the capital of Maharashtra?", "options": ["Mumbai", "Pune", "Nagpur", "Aurangabad"], "answer": "Mumbai"},
    {"question": "What is the capital of Tamil Nadu?", "options": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli"], "answer": "Chennai"},
    {"question": "What is the capital of Karnataka?", "options": ["Bengaluru", "Mysuru", "Hubli", "Davanagere"], "answer": "Bengaluru"},
    {"question": "What is the capital of Uttar Pradesh?", "options": ["Lucknow", "Agra", "Kanpur", "Varanasi"], "answer": "Lucknow"},
    {"question": "What is the capital of West Bengal?", "options": ["Kolkata", "Siliguri", "Durgapur", "Asansol"], "answer": "Kolkata"},
    {"question": "Who is known as the 'Father of the Nation' in India?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "Bhagat Singh"], "answer": "Mahatma Gandhi"},
    {"question": "Which Indian leader is known for the slogan 'Give me blood, and I shall give you freedom'?", "options": ["Lal Bahadur Shastri", "Bhagat Singh", "Sardar Patel", "Jawaharlal Nehru"], "answer": "Bhagat Singh"},
    {"question": "What is the largest river in India by volume of water?", "options": ["Ganga", "Yamuna", "Godavari", "Brahmaputra"], "answer": "Brahmaputra"},
    {"question": "Which city is known as the 'Pink City' of India?", "options": ["Jaipur", "Delhi", "Mumbai", "Bengaluru"], "answer": "Jaipur"},
    {"question": "In which year did India gain independence from British rule?", "options": ["1942", "1947", "1950", "1965"], "answer": "1947"},
    {"question": "What is the capital of Andhra Pradesh?", "options": ["Amaravati", "Hyderabad", "Vijayawada", "Visakhapatnam"], "answer": "Amaravati"},
    {"question": "Which Indian state is known as the 'Land of the Rising Sun'?", "options": ["Arunachal Pradesh", "Assam", "Nagaland", "Meghalaya"], "answer": "Arunachal Pradesh"},
    {"question": "Who was the first President of India?", "options": ["Rajendra Prasad", "Jawaharlal Nehru", "Sardar Patel", "Dr. B.R. Ambedkar"], "answer": "Rajendra Prasad"},
    {"question": "Which Indian state is the largest by area?", "options": ["Rajasthan", "Madhya Pradesh", "Uttar Pradesh", "Maharashtra"], "answer": "Rajasthan"},
    {"question": "What is the national flower of India?", "options": ["Rose", "Lotus", "Sunflower", "Marigold"], "answer": "Lotus"},
    {"question": "Which Indian leader is known for the Dandi March?", "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Bhagat Singh"], "answer": "Mahatma Gandhi"},
    {"question": "What is the capital of Himachal Pradesh?", "options": ["Shimla", "Manali", "Dharamshala", "Kullu"], "answer": "Shimla"},
    {"question": "Which Indian state is known as 'God's Own Country'?", "options": ["Kerala", "Goa", "Tamil Nadu", "Karnataka"], "answer": "Kerala"}
]

@app.route('/')
def index():
    # Randomly select 10 questions and shuffle their options
    questions = random.sample(all_questions, 10)
    for question in questions:
        random.shuffle(question['options'])
    
    # Store questions in session
    session['questions'] = questions
    return render_template('index.html', questions=questions, user_answers={})

@app.route('/submit', methods=['POST'])
def submit():
    questions = session.get('questions', [])
    score = 0
    results = []
    
    # Collect user responses from form
    user_answers = {f'question_{i}': request.form.get(f'question_{i}') for i in range(len(questions))}
    
    for i, question in enumerate(questions):
        user_answer = user_answers.get(f'question_{i}')
        correct_answer = question['answer']
        
        # Calculate score
        if user_answer == correct_answer:
            score += 1
        
        # Prepare result for rendering
        result = {
            'question': question['question'],
            'options': question['options'],
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'status': 'Correct' if user_answer == correct_answer else 'Incorrect'
        }
        results.append(result)
    
    return render_template('result.html', score=score, total=len(questions), results=results, user_answers=user_answers)

if __name__ == '__main__':
    app.run(debug=True)
