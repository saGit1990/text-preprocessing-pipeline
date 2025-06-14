from utils.utils import DataCleaner

def clean_text(text: str):
    cleaner = DataCleaner(text)
    cleaned = cleaner.cleaned_text()
    
    output = {
        "original_text": text,
        "cleaned_text": cleaned
    }
    
    with open('cleaned_text.json', 'w') as f:
        import json
        json.dump(output, f)
        
    print("Text cleaned and saved to cleaned_text.json")
    
if __name__ == "__main__":
    sample_text = "This is a sample text with some noise! @#%$^&*()_+{}|:\"<>?[];',./`~"
    clean_text(sample_text)
    print("Cleaning process completed.")


