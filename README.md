# Client/Server with FastAPI and React

**Movie Exam Project in Data Science Class**

[Problem Definition Page](https://github.com/FrederikBA/DataScienceExam/blob/main/documents/problem%20definition.md)

---

## Setup

### 🛠️ Prerequisites

Ensure the following tools are installed on your system:

- **Anaconda or Miniconda:** Used for managing environments and dependencies.
- **npm:** Needed for client-side dependency management.

### Environment and Dependency Setup

#### 🖥️ Windows and anaconda:

Use the following commands in your terminal:

```bash
conda create -n datascience_movie_exam python=3.10.11 -y
conda activate datascience_movie_exam
pip install -r requirements.txt
```

#### 🍎 Mac with M1-Chipset using miniconda:

Use the following commands in your terminal:

```bash
conda create -n datascience_movie_exam python=3.10.11 -y
conda activate datascience_movie_exam
pip install -r requirementsmac.txt
```

📝 **Note:** After setting up the environment and installing the dependencies, run the following Python script to download the Google Sentence Encoder. Make sure you're at the root of the project in your terminal:

```bash
python .\download_Google_Sentence_Encoder.py
```

---

## Usage

### 📓 Notebooks:

Follow these steps:

1. Navigate to the `notebooks` folder.
2. Run the following notebooks to save the models to the correct folder (these are ignored on git). This step is required to run the server.
   - `Movie Earnings Classifier.ipynb`
   - `Naive_bayes_sentiment_analysis.ipynb`

### 🖥️ Server:

Follow these steps:

1. Navigate to `/server`.
2. Run the server using: `uvicorn main:app --reload`
3. Access the server at: `http://127.0.0.1:8000`
4. Access Swagger API Documentation at: `http://127.0.0.1:8000/docs`

### 🖱️ Client:

Follow these steps:

1. Navigate to `/client`.
2. Install dependencies using: `npm install`
3. Run the client using: `npm start`

---




