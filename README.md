
**System rekomendacji przepisów (NLP)**

Projekt implementuje system rekomendacji przepisów kulinarnych oparty na klasycznych technikach NLP.

- System rekomendacji oparty o **TF-IDF** i **cosine similarity** – użytkownik podaje składniki, a model zwraca najbardziej dopasowane przepisy.
- **Preprocessing tekstu** (normalizacja, usunięcie znaków specjalnych), wektorowa reprezentacja dokumentów i ranking podobieństwa.
- **Interfejs CLI (argparse)** do łatwego uruchamiania programu z poziomu terminala.
- **Ewaluacja modelu**: ranking prawdziwych przepisów (**MRR**, top-5 accuracy).
- Możliwość dalszej rozbudowy o embeddingi **SBERT** lub modele sekwencyjne.
