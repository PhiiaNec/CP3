hw_ludwig.py учится на файле voice.csv, кладет свои знания в папку results/api_experiment_run/model  и предсказывает пол по данным в файле voice_to_predict.csv
Это файл для обучения voice.csv и для предсказания voice_to_predict.csv .
файл для обучения - dataset c Kaglee, а файл для предсказания первая и две последние строки из него

label_predictions  ...  label_probability
0              male  ...           0.685111
1              male  ...           0.514323
2            female  ...           0.523106

Это результат предсказания 2 из 3х - правильно