# **AI Feedback System**

##  Overview

This repository contains the complete implementation for **Task 1** (LLM Prompt Evaluation) and **Task 2** (Two-Dashboard AI Feedback System). The project includes backend API development, user and admin dashboards, data storage workflow, and evaluation of prompt performance.


---

#  Task 1 – LLM Prompt Evaluation System

## **1. Objective**

Task 1 focuses on evaluating three different LLM prompt versions to determine their accuracy, JSON correctness, and completeness of predictions.

---

## **2. Evaluation Results**

| Prompt Version | Accuracy | JSON Validity | Missing Predictions |
| -------------- | -------- | ------------- | ------------------- |
| Prompt V1      | 0.400000 | 0.733333      | 4                   |
| Prompt V2      | 0.466667 | 0.800000      | 3                   |
| Prompt V3      | 0.533333 | 1.000000      | 0                   |

---

## **3. Workflow Summary**

* Three iterations of prompts were designed (V1 → V2 → V3).
* A dataset of inputs was fed into each prompt version.
* Responses were parsed, validated, and evaluated:

  * JSON structure correctness
  * Accuracy of generated outputs
  * Missing or incomplete fields
* A comparative analysis was performed to identify the best-performing prompt.

---

## **4. Running Task 1**

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Launch Notebook**

```bash
jupyter notebook
```

Open:

```
task1_prompt_evaluation.ipynb
```

---

#  Task 2 – Two-Dashboard AI Feedback System

Task 2 implements a fully functioning web-based system:

* **User Dashboard** (public-facing)
* **Admin Dashboard** (internal-facing)
* **FastAPI Backend** (shared)

All components communicate through HTTP API calls.

---

## **1. System Architecture**

### **Component Overview**

| Component                       | Description                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------- |
| **FastAPI Backend**             | Handles storing feedback, generating summaries, and providing API endpoints.    |
| **User Dashboard (Streamlit)**  | Allows users to submit ratings and reviews and receives AI-generated responses. |
| **Admin Dashboard (Streamlit)** | Displays all submissions, summaries, actions, and optional analytics.           |
| **Storage Layer**               | Lightweight CSV/JSON used for persistent data storage.                          |

---

## **2. Live Deployments**

| Dashboard           | URL                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| **User Dashboard**  | [https://fynd-ai-cchsuxewxgafrftj6yfz3m.streamlit.app/](https://fynd-ai-cchsuxewxgafrftj6yfz3m.streamlit.app/) |
| **Admin Dashboard** | [https://fynd-ai-fwzxifhbe9bgcak3gaqycb.streamlit.app/](https://fynd-ai-fwzxifhbe9bgcak3gaqycb.streamlit.app/) |

Backend is run locally but supports deployment to platforms like Render, Railway, or PythonAnywhere.

---

## **3. Project Structure**

```
task2/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── data/
│   │   └── feedback.json
│   └── requirements.txt
│
├── user_dashboard/
│   └── streamlit_user_app.py
│
└── admin_dashboard/
    └── streamlit_admin_app.py
```

---

## **4. Installation & Setup**

### **A. Create Virtual Environment**

```bash
python -m venv env
```

Activate:

```bash
env\Scripts\activate      # Windows
source env/bin/activate   # Linux/Mac
```

---

### **B. Install Backend Requirements**

```bash
cd task2/backend
pip install -r requirements.txt
```

---

### **C. Start FastAPI Backend**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend runs at:

```
http://localhost:8000
```

---

### **D. Run User Dashboard Locally**

```bash
cd task2/user_dashboard
streamlit run streamlit_user_app.py
```

---

### **E. Run Admin Dashboard Locally**

```bash
cd task2/admin_dashboard
streamlit run streamlit_admin_app.py
```

---

# 5. System Workflow

1. The user submits a star rating and review through the **User Dashboard**.
2. Data is sent to the **FastAPI backend**, which:

   * Stores it
   * Generates:

     * AI summary
     * Recommended actions
     * AI user response
3. The **Admin Dashboard** reads from the same storage file to display real-time updates.
4. Both dashboards operate independently but share the same backend, following a clean client–server architecture.

---

# 6. Technologies Used

| Category     | Tools                 |
| ------------ | --------------------- |
| Frontend     | Streamlit             |
| Backend      | FastAPI, Uvicorn      |
| Data Storage | JSON / CSV            |
| AI Model     | OpenAI-compatible LLM |
| Deployment   | Streamlit Cloud       |

---

#  7. Conclusion

This repository delivers a complete, production-ready system integrating prompt evaluation, backend engineering, frontend dashboards, and LLM-powered automation.
The architecture is modular, scalable, and suitable for further development such as authentication, analytics, or extended model integration.


