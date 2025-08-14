# 🧠 AI Text Summarizer

A modern web application that uses AI to automatically summarize long text using Hugging Face's Transformers library. Built with Flask backend and vanilla JavaScript frontend.

![AI Text Summarizer Demo](https://img.shields.io/badge/demo-live-brightgreen) ![Python](https://img.shields.io/badge/python-3.7+-blue) ![Flask](https://img.shields.io/badge/flask-2.0+-green) ![Transformers](https://img.shields.io/badge/transformers-4.0+-orange)

## ✨ Features

- **AI-Powered Summarization**: Uses pre-trained transformer models from Hugging Face
- **Real-time Processing**: Instant text summarization with loading indicators
- **Clean UI**: Responsive design with modern styling
- **Error Handling**: Comprehensive error handling for empty inputs and network issues
- **Customizable**: Easily adjustable summary length parameters
- **Lightweight**: Minimal dependencies and fast loading

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-text-summarizer.git
   cd ai-text-summarizer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask transformers torch
   ```

4. **Create the templates directory and HTML file**
   ```bash
   mkdir templates
   ```
   Save the provided HTML code as `templates/index.html`

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
ai-text-summarizer/
│
├── app.py                 # Flask backend application
├── templates/
│   └── index.html        # Frontend HTML template
├── README.md            # Project documentation
```

## 🔧 Usage

1. **Enter Text**: Paste or type the text you want to summarize in the text area
2. **Click Summarize**: Press the "Summarize" button to process your text
3. **View Results**: The AI-generated summary will appear in the summary box below
4. **Adjust Length**: Modify `max_length` and `min_length` parameters in `app.py` for different summary lengths

## ⚙️ Configuration

### Summary Parameters

You can customize the summarization behavior by modifying parameters in `app.py`:

```python
summary = summarizer(text, 
    max_length=60,      # Maximum summary length
    min_length=25,      # Minimum summary length
    do_sample=False     # Deterministic output
)
```

### Available Parameters:
- `max_length`: Maximum number of tokens in the summary (default: 60)
- `min_length`: Minimum number of tokens in the summary (default: 25)
- `do_sample`: Whether to use sampling for generation (default: False)
- `temperature`: Controls randomness when do_sample=True
- `top_k`: Limits vocabulary for sampling
- `top_p`: Nucleus sampling parameter

## 🛠️ API Endpoints

### POST `/summarize`

Summarizes the provided text.

**Request Body:**
```json
{
    "text": "Your long text to be summarized..."
}
```

**Success Response:**
```json
{
    "summary": "The generated summary of your text."
}
```

**Error Response:**
```json
{
    "error": "No text provided"
}
```

## 🔍 Model Information

This application uses Hugging Face's default summarization pipeline, which typically loads the `facebook/bart-large-cnn` model. This model is specifically fine-tuned for summarization tasks and provides high-quality results for news articles, documents, and general text.

### Model Features:
- **Architecture**: BART (Bidirectional and Auto-Regressive Transformers)
- **Training Data**: CNN/DailyMail dataset
- **Strengths**: Excellent for news articles, formal documents, and structured text
- **Languages**: English

## 🚀 Deployment

### Local Development
```bash
python app.py
```

## 📦 Dependencies

```txt
Flask==2.3.3
transformers==4.33.2
torch==2.0.1
```



## 🐛 Troubleshooting

### Common Issues

1. **Model Loading Takes Time**: The first run may take a few minutes to download the model
   ```bash
   # Pre-download models (optional)
   python -c "from transformers import pipeline; pipeline('summarization')"
   ```

2. **Memory Issues**: Large texts or models may require more RAM
   ```python
   # Use a smaller model for lower memory usage
   summarizer = pipeline("summarization", model="t5-small")
   ```

3. **CORS Issues**: If deploying with separate frontend
   ```bash
   pip install flask-cors
   ```
   ```python
   from flask_cors import CORS
   CORS(app)
   ```

### Performance Tips

- **GPU Acceleration**: Install PyTorch with CUDA for faster processing
- **Model Caching**: Models are cached after first load
- **Batch Processing**: Process multiple texts together for better efficiency

## 🔗 Useful Links

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [BART Model Card](https://huggingface.co/facebook/bart-large-cnn)

## 📊 Example Usage

**Input Text:**
```
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".
```

**Generated Summary:**
```
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to natural intelligence displayed by humans and animals. The term is often used to describe machines that mimic cognitive functions like learning and problem solving.
```

---

**⭐ If you found this project helpful, please give it a star!**
