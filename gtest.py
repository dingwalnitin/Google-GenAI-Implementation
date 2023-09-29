from flask import Flask, request, render_template
import google.generativeai as palm
import time
import os

app = Flask(__name__)

# Replace with your actual API key and model ID

apikey = os.environ.get("API_KEY") 
palm.configure(api_key=apikey)
model_id = 'models/text-bison-001'

# Function to count unique visitors based on unique IP addresses in the text file
def count_unique_visitors():
    unique_ips = set()  # Use a set to store unique IP addresses
    try:
        with open('unique_ips.txt', mode='r') as file:
            for line in file:
                ip_address = line.strip()
                unique_ips.add(ip_address)
        unique_visitors = len(unique_ips)
    except FileNotFoundError:
        unique_visitors = 0

    return unique_visitors


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

    unique_visitors = count_unique_visitors()

    return render_template('index.html', output=output, elapsed_time=elapsed_time, unique_visitors=unique_visitors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
