<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reverse Life Simulator - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.7;
            max-width: 900px;
            margin: auto;
            padding: 30px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #4B0082;
        }
        code {
            background-color: #eee;
            padding: 2px 6px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 15px;
            overflow-x: auto;
            border-left: 5px solid #4B0082;
        }
        a {
            color: #4B0082;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        hr {
            border: none;
            border-top: 2px solid #ccc;
            margin: 30px 0;
        }
    </style>
</head>
<body>

    <h1>🌀 Reverse Life Simulator</h1>
    <p>A fun and inspiring Flask-based web application that imagines an alternate version of your life. Simply fill in the form with your current and alternate life details, and get a unique story generated using OpenAI or a creative fallback if the API is unavailable.</p>

    <hr>

    <h2>🔧 Features</h2>
    <ul>
        <li>🌍 Collects current and alternate life details (city, education, job)</li>
        <li>✨ Generates personalized alternate life stories using OpenAI GPT-3.5</li>
        <li>💾 Saves generated stories to a local history (<code>history.json</code>)</li>
        <li>📜 Displays all previous user stories on the <code>/history</code> page</li>
        <li>🔐 Uses <code>.env</code> file for secure API key management</li>
    </ul>

    <hr>

    <h2>🚀 Getting Started</h2>

    <h3>1. Clone the Repository</h3>
    <pre><code>git clone https://github.com/yourusername/reverse-life-simulator.git
cd reverse-life-simulator</code></pre>

    <h3>2. Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>3. Set Environment Variables</h3>
    <p>Create a <code>.env</code> file in the root directory with the following:</p>
    <pre><code>OPENAI_API_KEY=your_openai_api_key
FLASK_SECRET_KEY=your_secret_key</code></pre>
    <p><strong>Note:</strong> If you don't have an OpenAI API key, the app will still work using a fallback story generator.</p>

    <h3>4. Run the App</h3>
    <pre><code>python app.py</code></pre>
    <p>Then open your browser and visit: <a href="http://localhost:5000" target="_blank">http://localhost:5000</a></p>

    <hr>

    <h2>📁 Project Structure</h2>
    <pre><code>reverse-life-simulator/
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
├── app.py
├── history.json
├── .env
├── requirements.txt
└── README.html</code></pre>

    <hr>

    <h2>🧠 How It Works</h2>
    <p>When a user submits the form, the app sends a prompt to OpenAI’s Chat API to generate a story. If OpenAI is not available or fails, a default story template is used instead. All results are saved in a <code>history.json</code> file and can be viewed on the <code>/history</code> page.</p>

    <hr>

    <h2>📜 License</h2>
    <p>This project is open-source and available under the <strong>MIT License</strong>.</p>

    <hr>

    <h2>💡 Future Improvements</h2>
    <ul>
        <li>Add user login to personalize story histories</li>
        <li>Enhance prompt for richer storytelling</li>
        <li>Add image generation using DALL·E for visual storytelling</li>
    </ul>

    <hr>

    <h2>🙌 Author</h2>
    <p><strong>Fatima Raza</strong><br>
    MPhil in Zoology | Web Developer | Python Enthusiast<br>
    📧 <a href="mailto:your-email@example.com">Contact Me</a></p>

</body>
</html>
