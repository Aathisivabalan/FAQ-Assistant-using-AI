# FAQ Assistant using AI

An AI-powered chatbot designed to answer technical queries with high accuracy and low latency.  
Built using **Python**, **FastAPI**, and **OpenAI API**, the system is capable of handling over 1,000 queries while reducing manual support workload by 40%.

---

## 📸 Demo

![FAQ Assistant Demo](demo.gif)  
*Above: Example of chatbot handling multiple queries with instant responses.*

---

## 🚀 Features
- **AI-Powered Q&A**: Understands context and provides accurate answers.
- **High Performance**: Caching and latency optimization improve response time by 25%.
- **Scalable Backend**: FastAPI-based architecture for high concurrency.
- **User Satisfaction**: Maintains 90%+ satisfaction rate.
- **Modular Architecture**: Easily add new features and integrations.

---

## 🛠 Tech Stack
- **Programming Language**: Python
- **Framework**: FastAPI
- **AI Service**: OpenAI API
- **Database/Storage**: (Optional — specify if used: SQLite, MongoDB, PostgreSQL, etc.)
- **Tools**: Uvicorn, Pydantic, Requests

---

## 📂 Project Structure
```
FAQ-Assistant/
│
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── routes.py         # API endpoints
│   ├── services.py       # Chatbot business logic
│   ├── cache.py          # Caching mechanism
│   └── utils.py          # Helper functions
│
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables (API keys)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/FAQ-Assistant.git
cd FAQ-Assistant
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API Key
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the application
```bash
uvicorn app.main:app --reload
```
Visit: `http://127.0.0.1:8000/docs` for the interactive API documentation.

---

## 📡 API Usage

### **Endpoint:** `/ask`
**Method:** `POST`  
**Request Body:**
```json
{
  "question": "What is a REST API?"
}
```

**Response:**
```json
{
  "answer": "A REST API is an application programming interface that conforms to the constraints of REST architecture..."
}
```

---

## 📊 Performance
- Handles **1,000+ queries** efficiently.
- **25% faster** response time via caching and optimization.
- Reduced manual support by **40%**.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
