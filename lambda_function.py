import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor
import json

preprocessor = create_preprocessor('xception', target_size=(200, 200))
interpreter = tflite.Interpreter(model_path='pneumonia-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def predict(url):
    x = preprocessor.from_url(url)
    interpreter.set_tensor(input_index, x)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_index)
    float_prediction = predictions[0].tolist()

    return float_prediction

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)[0]
    diagnose = "Lungs affected by pneumonia" if result >= 0.5 else "Normal lungs"
    return json.dumps({'prediction': result, 'diagnose': diagnose})