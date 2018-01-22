from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('.well-known/acme-challenge/uN9MCASIEgwfuLWpLVLswYtzOSEgSJvjMC8MGJSLkow')
def letsencrypt():
    return 'uN9MCASIEgwfuLWpLVLswYtzOSEgSJvjMC8MGJSLkow.H5iM88zVcyI6quHQsgAP59M0DguawF5twO6AZrVdz6w'

if __name__ == '__main__':
    app.run(port=8889,debug=True)
