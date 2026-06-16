from flask import Flask, render_template, request
import csv, os

app = Flask(__name__)

# ---------------- LANDING PAGE ----------------
@app.route('/')
def landing():
    return render_template('landing.html')


# ---------------- FORM PAGE ----------------
@app.route('/form')
def form():
    return render_template('index.html')


# ---------------- CHECK RESULT ----------------
@app.route('/check', methods=['POST'])
def check():

    company = request.form['company_name']
    website = request.form['website']
    email = request.form['email']
    linkedin = request.form['linkedin']
    fee = request.form['fee']

    score = 0
    score += 25 if website.strip() != "" else 0
    score += 25 if "@" in email else 0
    score += 25 if linkedin.lower() == "yes" else 0
    score += 25 if fee.lower() == "no" else 0

    if score >= 75:
        status = "PASS"
        color = "#10b981"
    elif score >= 50:
        status = "AVERAGE"
        color = "#f59e0b"
    else:
        status = "FAIL"
        color = "#ef4444"

    file_exists = os.path.isfile('internship_data.csv')

    with open('internship_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Company","Website","Email","LinkedIn","Fee","Score","Status"])
        writer.writerow([company, website, email, linkedin, fee, score, status])

    return render_template("dashboard.html",
        company=company,
        score=score,
        status=status,
        color=color
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=10000)
