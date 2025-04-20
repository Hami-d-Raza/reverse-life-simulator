from flask import Flask, render_template, request, flash
import os
import json
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load .env variables
load_dotenv()

# OpenAI config
try:
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        client = OpenAI(api_key=api_key)
        use_openai = True
        logging.info("OpenAI client initialized successfully")
    else:
        use_openai = False
        logging.warning("OPENAI_API_KEY not found in environment variables")
except ImportError:
    logging.warning("OpenAI package not installed")
    use_openai = False

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")  # For flash messages

# File to store history
history_file = 'history.json'


# Home Page - Form
@app.route('/')
def home():
    return render_template('index.html')


# Result Page - Handle form + generate story
@app.route('/result', methods=['POST'])
def result():
    try:
        user_data = {
            "name": request.form['name'],
            "age": request.form['age'],
            "current": {
                "city": request.form['current_city'],
                "education": request.form['current_education'],
                "job": request.form['current_job']
            },
            "alternate": {
                "city": request.form['alternate_city'],
                "education": request.form['alternate_education'],
                "job": request.form['alternate_job']
            }
        }

        # Validate form data
        if not all([user_data["name"], user_data["age"]]):
            flash("Please fill in all required fields")
            return render_template('index.html')

        story = generate_story(user_data)

        # Save story and data to history
        save_history(user_data, story)

        return render_template('result.html', data=user_data, story=story)
    except KeyError as e:
        flash(f"Missing form field: {e}")
        return render_template('index.html')
    except Exception as e:
        logging.error(f"Error processing form: {e}")
        flash("An error occurred while processing your request")
        return render_template('index.html')


# History Page - Display all previous results
@app.route('/history')
def history():
    history_data = load_history()
    return render_template('history.html', history=history_data)


# Generate story using OpenAI or fallback
def generate_story(user_data):
    name = user_data["name"]
    age = user_data["age"]
    current = user_data["current"]
    alternate = user_data["alternate"]

    # Use OpenAI if available
    if use_openai:
        prompt = f"""
        Imagine an alternate life of {name}, age {age}.
        In real life, they studied {current['education']} in {current['city']} and work as a {current['job']}.
        In an alternate timeline, they studied {alternate['education']} in {alternate['city']} and became a {alternate['job']}.
        Write an emotional, inspiring story of their alternate life.
        """
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative storyteller."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.8
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"OpenAI API Error: {e}")
            # Fall through to fallback story

    # Fallback story if OpenAI not available or fails
    story = (
        f"<h3>The Alternate Life of {name}</h3>"
        f"<p>{name}, a {age}-year-old, originally studied {current['education']} in {current['city']} "
        f"and now works as a {current['job']}.</p>"
        f"<p>But in an alternate reality, {name} chose a different path. They moved to {alternate['city']} "
        f"to study {alternate['education']}. The decision wasn't easy, but it led them down an exciting new path.</p>"
        f"<p>Years later, {name} became a successful {alternate['job']}, finding fulfillment in ways they "
        f"couldn't have imagined in their original life. While both paths had their challenges and rewards, "
        f"this alternate life gave {name} a unique perspective on what might have been.</p>"
    )
    return story


# Save to history.json
def save_history(user_data, story):
    try:
        history = load_history()
        history.append({"user_data": user_data, "story": story})

        with open(history_file, 'w') as f:
            json.dump(history, f, indent=4)
        logging.info("History saved successfully")
    except Exception as e:
        logging.error(f"Error saving history: {e}")


# Load history from JSON file
def load_history():
    if os.path.exists(history_file):
        try:
            with open(history_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing history file: {e}")
            # Return empty list and backup corrupted file
            if os.path.getsize(history_file) > 0:
                os.rename(history_file, f"{history_file}.corrupted")
            return []
    return []


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)