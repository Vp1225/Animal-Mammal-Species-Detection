from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_dir = 'C:/Users/ADMIN/Desktop/Animal(mammal) species detection/mammals/train'

train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='sparse')

class_names = list(train_generator.class_indices.keys())
print(class_names)
