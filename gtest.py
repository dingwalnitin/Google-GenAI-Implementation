from flask import Flask, request, render_template
import google.generativeai as palm
import time


app = Flask(__name__)


apikey= 'AIzaSyDpqKxMdAJYfn2_hmPTOkShkRzWJS0UBpQ'
palm.configure(api_key=apikey)
model_id = 'models/text-bison-001'




@app.route('/', methods=['GET', 'POST'])
def generate_text():
    output = ""
    elapsed_time = 0

    if request.method == 'POST':
        prompt = request.form['prompt'] + 'explain in detail'
        
        start_time = time.time()
        completion = palm.generate_text(model=model_id, prompt=prompt, temperature=0.8, max_output_tokens=1024, candidate_count=1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        output = completion.candidates[0]['output']

    

    return render_template('index.html', output=output, elapsed_time=elapsed_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
