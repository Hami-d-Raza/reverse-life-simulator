# 🌀 Reverse Life Simulator

> A creative and inspiring Flask web app that generates stories based on your real and alternate life choices.

---

## 🔧 Features
- 🌍 Collects your current and alternate life data (city, education, job)
- ✨ Generates emotional, personalized stories using OpenAI GPT-3.5
- 💾 Saves your stories to a local history.json file
- 📜 Browse all previous stories on the /history page
- 🔐 Secure API key management using .env

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/reverse-life-simulator.git
cd reverse-life-simulator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key
FLASK_SECRET_KEY=your_secret_key
```
📝 If no OpenAI API key is set, the app gracefully uses a fallback story generator.

### 4. Run the App
```bash
python app.py
```
Then go to: http://localhost:5000

IF you want to check this project online
Go to this URL = https://hamid8659.pythonanywhere.com/ and test it.<br>
**Disclaimer:** Use alternative demo names and passions for testing, as your history will be saved and visible to everyone.

## 📁 Project Structure
```
reverse-life-simulator/
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
├── app.py
├── history.json
├── .env
├── requirements.txt
└── README.md
```

## 🧠 How It Works
1. You fill out a form with your real and alternate life details.
2. The app sends a prompt to OpenAI's GPT-3.5 to craft a story.
3. If the API fails or is not configured, a default inspirational story is created.
4. All entries are saved and viewable on the `/history` route.

## 💡 Future Plans
* User login and authentication
* Richer story generation prompts
* AI-generated character portraits via DALL·E

## 📜 License
This project is licensed under the MIT License.

## 🙌 Author
**Muhammad Hamid Raza**  
Computer Science | Python Dev | Web Enthusiast  
📧 Email Me ( hamidraza9182@gmail.com )
