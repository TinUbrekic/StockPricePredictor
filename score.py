import os
import joblib
import json
import pandas as pd

def init():
    global models
    models = {}
    tickers = ['Nike', 'Adobe', 'Ebay', 'Electronic_Arts', 'Bank_of_America'] 
    
    base_path = os.getenv("AZUREML_MODEL_DIR")
    
    for ticker in tickers:
        try:
            model_name = f"{ticker.lower()}_stock_price_model"
            model_file_path = os.path.join(base_path, model_name, f"best_model_{ticker}.pkl")
            
            if not os.path.exists(model_file_path):
                 model_file_path = os.path.join(base_path, f"best_model_{ticker}.pkl")

            models[ticker] = joblib.load(model_file_path)
            print(f"Uspješno učitan model za: {ticker}")
        except Exception as e:
            print(f"Greška pri učitavanju modela za {ticker}: {e}")

def run(raw_data):
    try:
        input_data = json.loads(raw_data)
        company = input_data.get("company", "Nike") 
        data = input_data["data"]
        
        df = pd.DataFrame(data)
        
        #provjera postoji li za odredenu tvrtku
        if company in models:
            prediction = models[company].predict(df)
            return {"prediction": prediction.tolist(), "company": company}
        else:
            return {"error": f"Model za tvrtku '{company}' nije učitan."}
            
    except Exception as e:
        return {"error": str(e)}
