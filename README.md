# Predikcija kategorije proizvoda na osnovu naslova

**Kurs:** Introduction to Machine Learning using Python  
**Zadatak:** Task 3 (platforma 947) — automatska klasifikacija proizvoda po `Product Title`  
**Autor:** Nebojša Simović

Model predlaže kategoriju (npr. Mobile Phones, Laptops) na osnovu naziva proizvoda — za online trgovinu sa 30.000+ artikala u `products.csv`.

> **ITA-ML** (ovaj folder): vođeni primer kroz lekcije modula 4 (ML projekat). **Finalni Task 3 (947)** ide u **novi repo** kasnije — link na platformu neće biti ITA-ML. Task 1/2 i `_lokalno/` su van gita.

## Struktura projekta

```
├── data/
│   └── products.csv          # skup za treniranje (obavezno u repou)
├── notebooks/
│   └── *.ipynb               # EDA, feature engineering, poređenje modela
├── model/
│   └── *.pkl                 # trenirani model (generisati train_model.py)
├── train_model.py            # treniranje i čuvanje modela
├── predict_category.py       # interaktivno: unos naslova → kategorija
├── requirements.txt
└── README.md
```

## Podaci

Kolone u `products.csv`: Product ID, Product Title, Merchant ID, Category Label, Product Code, Number of Views, Merchant Rating, Listing Date.

Preuzimanje (ako nemaš fajl lokalno):

https://www.link-elearning.com/linkdl/coursefiles/1956/IMLP4_TASK_03-products.csv

Stavi fajl u `data/products.csv`.

## Okruženje

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Pokretanje

**1. Treniranje** (kreira/ ažurira model u `model/`):

```powershell
python train_model.py
```

**2. Predikcija** (interaktivno):

```powershell
python predict_category.py
```

**3. Analiza** (notebook):

Otvori `notebooks/` u Jupyteru i pokreni sve ćelije redom.

## Test naslovi (iz zadatka)

| Naziv proizvoda | Očekivana kategorija |
|-----------------|----------------------|
| iphone 7 32gb gold,4,3,Apple iPhone 7 32GB | Mobile Phones |
| olympus e m10 mark iii geh use silber | Digital Cameras |
| kenwood k20mss15 solo | Microwaves |
| bosch wap28390gb 8kg 1400 spin | Washing Machines |
| bosch serie 4 kgv39vl31g | Fridge Freezers |
| smeg sbs8004po | Fridge Freezers |

## Kloniranje

```bash
git clone https://github.com/Newbluewood/ITA-ML.git
cd ITA-ML
```

SSH (ovaj računar):

```bash
git clone git@github.com-blw:Newbluewood/ITA-ML.git
```

## Status

- [ ] Notebook: analiza, FE, poređenje ≥2 modela, evaluacija
- [ ] `train_model.py` + `.pkl` u `model/`
- [ ] `predict_category.py`
- [ ] Link repozitorijuma na platformi (947)
