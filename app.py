from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    company = request.form['company_name']
    website = request.form['website']
    email = request.form['email']
    linkedin = request.form['linkedin']
    fee = request.form['fee']

    score = 0

    if website:
        score += 25

    if "@" in email:
        score += 25

    if linkedin == "Yes":
        score += 25

    if fee == "No":
        score += 25

    if score >= 80:
        result = " Low Risk"
    elif score >= 50:
        result = " Medium Risk"
    else:
        result = " High Risk"
    # Save the details into internship_data.csv
    with open('internship_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            company,
            website,
            email,
            linkedin,
            fee,
            score,
            result
        ])
    return render_template(
        "result.html",
        company=company,
        website=website,
        email=email,
        linkedin=linkedin,
        fee=fee,
        score=score,
        result=result
    )

if __name__ == '__main__':
    app.run(debug=True)