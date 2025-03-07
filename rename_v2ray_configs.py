import sys
import requests
import json

def fetch_subscription(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to fetch subscription")

def modify_labels(subscription_content, new_label):
    configs = json.loads(subscription_content)
    for config in configs:
        config["remark"] = new_label
    return json.dumps(configs, indent=4)

def main(url, new_label):
    try:
        subscription_content = fetch_subscription(url)
        modified_content = modify_labels(subscription_content, new_label)

        # ذخیره محتوا به فایل جدید
        with open("modified_subscription.json", "w") as f:
            f.write(modified_content)

        # چاپ لینک جدید (می‌توانید این را به لینک واقعی هاست خود تغییر دهید)
        print("http://your-host-address/modified_subscription.json")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = sys.argv[1]
    new_label = sys.argv[2]
    main(url, new_label)
