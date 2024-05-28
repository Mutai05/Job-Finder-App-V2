from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

# Define the company name once
COMPANY_NAME = 'JobFinder Website'

@app.route("/")
def home_page():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name=COMPANY_NAME)

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)
    if job:
        return render_template('jobpage.html', job=job, company_name=COMPANY_NAME)
    else:
        return "Job Not Found", 404
    
@app.route("/job/<int:id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    # store in the db
    # send an email
    # display acknowledgement
    return render_template('application-submitted.html',
                           application=data,
                           job=job)
                         

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
