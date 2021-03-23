from flask import Flask, request, jsonify, render_template, Markup

# importing needed functions from gibberish_generator_v2.py 
from gibberish_generator_v2 import gibberish_generate, return_sample_gibberish

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', examples=return_sample_gibberish())

@app.route('/Generate Gibberish',methods=['POST'])
def GenerateGibberish():
    '''
    For rendering results on HTML GUI
    '''
    sentence = [x for x in request.form.values()]
    return render_template(        'index.html', 
    gibberish_text=Markup('Original text: {0} <br/> <br/> &nbsp; &nbsp; &nbsp; &nbsp; gibberish generated: {1}'.format(
            sentence[0], gibberish_generate(sentence[0]))), examples=return_sample_gibberish())

# for running in local machine
# if __name__ == "__main__":
#     app.run(debug=True)

# for hosting in AWS
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080)
