Stock Price Predictor
Ovaj projektni zadatak predstavlja model za predviđanje cijena dionica pet tvrtki (Adobe, Bank of America, Ebay, Nike i Electronic Arts).

Arhitektura sustava
Arhitektura projekta sastoji se od tri ključna dijela:

AzureML: Modeli su trenirani, optimizirani i registrirani na Azure cloud platformi.

Flask API: Služi kao komunikacijski sloj koji prima zahtjeve od korisnika, komunicira s modelima i vraća predviđanja u JSON formatu.

Gradio Interface: Web aplikacija koja korisniku omogućuje unos podataka i vizualizaciju trendova kretanja cijena.

Korišteni modeli i metode
U projektu su testirani i implementirani sljedeći algoritmi strojnoga učenja:

Random Forest Regressor

Support Vector Regression (SVR)

K-Nearest Neighbors (KNN)

Decision Tree Regressor

Za evaluaciju modela korištena je metrika MAE (Mean Absolute Error), a optimizacija je provedena pomoću GridSearchCV.


Tehnologije
Jezik: Python 3.10.19

Biblioteke: Pandas, Scikit-learn, Matplotlib, Joblib

Cloud: Microsoft Azure Machine Learning

UI/API: Gradio, Flask
