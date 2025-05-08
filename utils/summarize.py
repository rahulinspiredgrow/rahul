from transformers import pipeline

summarizer_en = pipeline("summarization", model="facebook/bart-large-cnn")
summarizer_hi = pipeline("summarization", model="ai4bharat/indicbart", tokenizer="ai4bharat/indicbart")

def summarize_text(text, lang='en'):
    if lang == 'hi':
        return summarizer_hi(text[:512])[0]['summary_text']
    else:
        return summarizer_en(text[:1024])[0]['summary_text']
