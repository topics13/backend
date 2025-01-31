import pickle
from utility import generate_dataset, resources

def crop_predict(crop_attributes):
    crop_to_predict_dataset = generate_dataset.generate_dataset(crop_attributes)

    model = pickle.load(open(resources.CROP_PREDICT_MODEL, 'rb'))

    prediction = model.predict((crop_to_predict_dataset))

    return prediction

    