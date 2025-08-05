# AI Customer Support Chatbot 🤖

This project is a simple, AI-powered chatbot prototype built to support user onboarding and automate responses to common questions.

It uses LangChain and Python to simulate how businesses can integrate conversational AI into their onboarding or support flows — reducing repetitive queries, improving accessibility to key information, and saving time for both users and support teams.

---

## 🧠 What It Does

- Answers frequently asked questions about a product or service
- Provides structured onboarding guidance to new users
- Responds conversationally using prompt-based logic via LangChain
- Can be adapted to different domains by updating the prompt or input documents

---

## ⚙️ Tech Stack

- **LangChain** for prompt orchestration and chaining
- **Python** for core logic
- **PowerShell / Terminal** for local execution
- **VS Code** as the development environment

---

## 💡 Why This Exists

Chatbots are widely used — but this project shows how anyone can build a lightweight, adaptable version without needing a large team or infrastructure.

It's not about complexity. It's about:

- Reducing repetitive support overhead
- Making onboarding more accessible
- Experimenting with AI to solve real usability problems

---

## 📁 Project Structure

| Folder/File        | Description                                        |
| ------------------ | -------------------------------------------------- |
| `chatbot/`         | Contains the core logic and code that runs the bot |
| `data/`            | Onboarding documents used as the bot’s knowledge   |
| `README.md`        | Project overview and usage instructions            |
| `requirements.txt` | Python dependencies                                |
| `.gitignore`       | Files and folders ignored by Git                   |

---

## 🛠️ How to Run (PowerShell)

```bash
# Clone the repo
git clone https://github.com/Maryamkoga/ai-customer-support-bot.git

# Navigate into the folder
cd ai-customer-support-bot

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
python app.py

___

📝 Notes
The bot pulls its responses from onboarding materials stored in data/

You can swap in your own docs to suit different products or industries

Currently runs in a local terminal, ideal for testing or prototyping

```
