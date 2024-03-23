import numpy as np
import pandas as pd
import collections 
from tensorflow import keras
from keras import layers, utils
from keras.layers import Dense, Activation
from PIL import Image 
import os
from keras.datasets import mnist, fashion_mnist
import matplotlib.pyplot as plt
from tensorflow import keras
import json
from PIL import Image
import fnmatch
from keras.optimizers import Adam
#Mallaun Stefan

number_classes = 10
batch_size = 128
epochs = 3

categories = {0:'T-shirt_Top', 1:'Hose', 2:'Pullover', 3:'Kleid', 4:'Mantel', 5:'Sandalen', 6:'Hemd', 7:'Sneaker', 8:'Tasche', 9:'Halbschuhe'}

# Daten laden
(training_images, training_labels), (test_images, test_labels)  = fashion_mnist.load_data()

#------------------------------------------------------------------------------------------------
#1.1.1.  Die Beschaffenheit (Dimensionen und Häufigkeiten) der Daten abfragen)
print('Dimension: ')
print(training_images.shape)

#------------------------------------------------------------------------------------------------
#1.2.1 Visualisierung der Daten
for i in range(0,100):
    im = Image.fromarray(training_images[i])
    real = training_labels[i]

    #1.2.2 Bilder der gleichen Kategorie exportieren
    path = os.path.join('06_Keras/zalando', categories[real])
    os.makedirs(path, exist_ok=True)
    im.save("%s/%d_%d.jpeg" % (path, i, real))

#------------------------------------------------------------------------------------------------
#1.1.2. Wie viele Kleidungsstücke sind pro Kategorie verfuegbar?
rootdir = '06_Keras/zalando'
bildZehn = ''
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        if os.path.basename(d) != 'models':
            #print(d)
            count = 0
            for subfile in os.listdir(d):
                if os.path.isfile(os.path.join(d, subfile)):
                    count += 1
                    if '10_0.jpeg' in subfile:
                        bildZehn = [os.path.join(d, subfile), os.path.basename(d)]
            print(f'Kategorie: {os.path.basename(d)} | Anzahl Bilder: {count}')

#------------------------------------------------------------------------------------------------
#1.1.3 Wie bekommt man die Pixel des zehnten Bildes, wie die Info, welches Kleidungsstück hier dargestellt werden soll?
def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return f'{width}*{height}'

print(f'Pixel vom zehnten Bild: {get_num_pixels(bildZehn[0])} | Kategorie: {bildZehn[1]}')

training_images = training_images.astype("float32") / 255
print(training_images.shape, "train samples")
test_images = test_images.astype("float32") / 255

# Make sure images have shape (28, 28, 1)
training_images = np.expand_dims(training_images, -1)
test_images = np.expand_dims(test_images, -1)

print(training_images.shape, "training_images shape:")
print(training_images.shape[0], "number of train samples")
print(test_images.shape[0], "number of test samples")

nr_labels_y = collections.Counter(training_labels) #count the number of labels
print(nr_labels_y, "Number of labels")

# convert class vectors (the labels) to binary class matrices
training_labels = keras.utils.to_categorical(training_labels, number_classes)
labels_y = test_labels #use this to leave the labels untouched
test_labels = keras.utils.to_categorical(test_labels, number_classes)

training_images = training_images.reshape(60000, 784)
test_images = test_images.reshape(10000, 784)
training_images = training_images.astype('float32')
test_images = test_images.astype('float32')

#------------------------------------------------------------------------------------------------
#2.1. Erzeugen der Modellstruktur
model = keras.Sequential(
    [
        keras.Input(shape=(784,)),
        layers.Dense(16, activation="relu"),
        layers.Dense(32, activation="relu"),
        layers.Dense(52, activation="relu"),
        layers.Dense(124, activation="relu"),
        layers.Dense(188, activation="relu"),
        layers.Dense(189, activation="relu"),
        layers.Dense(212, activation="relu"),
        layers.Dense(230, activation="relu"),
        layers.Dense(342, activation="relu"),
        layers.Dense(456, activation="relu"),
        layers.Dense(678, activation="relu"),
        layers.Dense(number_classes, activation="softmax"),
    ]
)
model.summary()

#------------------------------------------------------------------------------------------------
#2.2. Compilieren des Modells
model.compile(loss ="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

#------------------------------------------------------------------------------------------------
# 3 Beobachtung der Lernprozesse
history = model.fit(training_images, training_labels, batch_size=batch_size, epochs=epochs, validation_split=0.1)
print('history' + str(history.history))

#------------------------------------------------------------------------------------------------
#3.1 Evulation der Ergebnisse
score = model.evaluate(test_images, test_labels, verbose=2)
print(score)

#------------------------------------------------------------------------------------------------
# 3.2. Analyse der Ergebnisse
pred = model.predict(test_images)
print(pred[1])
prediction_1 = np.argmax(pred[1])
print(prediction_1)
print(labels_y[1])
print('highest value')
prediction_dict = {
    "prediction" : [],
    "y_label" : []
}
for i in range(0,100):
    prediction_i = np.argmax(pred[i]) # get the position of the highest value within the list
    prediction_dict["prediction"].append(prediction_i)
    print (labels_y[i], prediction_i)
    prediction_dict["y_label"].append(labels_y[i])
print(prediction_dict)

#------------------------------------------------------------------------------------------------
#3.3. Optimierung (funktioniert nicht, obwohl es gleich ist wie auf dem GitHub)
model.save('06_Keras/zala/models/model.mdl')
model.save_weights("06_Keras/zala/models/model.weights.h5")

weights = model.get_weights()
j = json.dumps(pd.Series(weights).to_json(orient='values'), indent=3)


model = tf.saved_model.save('06_Keras/zala/models/model.mdl')
model.load_weights("06_Keras/zala/models/model.weights.h5")

model_json = model.to_json()
print (model_json)

#4:
pd.DataFrame(pred_dic).plot(figsize=(8,5))
plt.show()