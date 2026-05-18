from flask import Flask, render_template
import os

app = Flask(
    __name__,
    template_folder="../templates"
)

LOG_FILE = "../logs/alerts.log"

# =========================
# HOME PAGE
# =========================

@app.route("/")

def home():

    logs = []

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r", encoding="utf-8") as f:

            logs = f.readlines()

    logs.reverse()

    attack_count = len(logs)

    return render_template(
        "index.html",
        logs=logs,
        attack_count=attack_count
    )

# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":

    app.run(
        debug=True
    )