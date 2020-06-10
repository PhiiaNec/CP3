from ludwig.api import LudwigModel
import pandas as pd
import pprint
# Тренируем модель
model_definition = {'input_features': [{'name':'meanfun' , 'type': 'numerical'},{'name':'IQR' , 'type': 'numerical'}],
                    'output_features': [{'name': 'label', 'type': 'category'},]}
model = LudwigModel(model_definition)
training_dataframe=pd.read_csv("voice.csv",sep=",")
train_stats = model.train(training_dataframe)

# или загружаем модель 
# model = LudwigModel.load('results/api_experiment_run/model')

# Получаем предсказания 
test_dataframe=pd.read_csv("voice_to_predict.csv",sep=",")

predictions = model.predict(test_dataframe)
print(predictions)
model.close()
pass