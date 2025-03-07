from flask import Flask, request, jsonify, render_template_string
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>V2Ray Config Renamer</title>
          </head>
          <body>
            <h1>V2Ray Config Renamer</h1>
            <form action="/rename" method="post">
              <label for="url">Subscription URL:</label><br>
              <input type="text" id="url" name="url" required><br><br>
              <label for="new_label">New Label:</label><br>
              <input type="text" id="new_label" name="new_label" required><br><br>
              <input type="submit" value="Rename">
            </form>
          </body>
        </html>
    ''')

@app.route('/rename', methods=['POST'])
def rename():
    subscription_url = request.form['url']
    new_label = request.form['new_label']

    try:
        response = requests.get(subscription_url)
        if response.status_code == 200:
            configs = json.loads(response.text)
            for config in configs:
                config["remark"] = new_label
            modified_content = json.dumps(configs, indent=4)
            return jsonify({"modified_subscription": modified_content})
        else:
            return jsonify({"error": "Failed to fetch subscription"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
