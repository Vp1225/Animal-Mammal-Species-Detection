import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint

train_dir = r'C:\Users\ADMIN\Desktop\backup - backup\Animal(mammal) species detection\mammals\train'
validation_dir = r'C:\Users\ADMIN\Desktop\backup - backup\Animal(mammal) species detection\mammals\validation'
model_dir = r'C:\Users\ADMIN\Desktop\backup - backup\Animal(mammal) species detection\Final_MODELS'  # Model directory

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(160, 160),
    batch_size=32,  
    class_mode='sparse')

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(160, 160),
    batch_size=32,
    class_mode='sparse')

base_model = MobileNetV2(input_shape=(160, 160, 3),
                         include_top=False,
                         weights='imagenet')
base_model.trainable = False

model = Sequential([
    base_model,
    Conv2D(32, 3, activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(308, activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model_checkpoint_callback = ModelCheckpoint(
    filepath=model_dir + "/best_model_{epoch:02d}_{val_accuracy:.2f}.h5",
    save_best_only=True,
    monitor='val_accuracy',
    mode='max',
    verbose=1)

history = model.fit(
    train_generator,
    steps_per_epoch=256,
    epochs=20,
    validation_data=validation_generator,
    validation_steps=64,
    callbacks=[model_checkpoint_callback])

final_model_path = model_dir + "/mammal_species.h5"
model.save(final_model_path)
print(f"Model saved to {final_model_path}")