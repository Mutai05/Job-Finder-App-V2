from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def home_page():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='JobFinder Website')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)
    if job:
        return render_template('jobpage.html', job=job)
    else:
        return "Job Not Found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
