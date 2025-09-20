from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jobs')
def jobs():
    # Sample job data for the careers website
    jobs_data = [
        {
            'id': 1,
            'title': 'Senior Python Developer',
            'department': 'Engineering',
            'location': 'Remote',
            'type': 'Full-time',
            'description': 'Join our engineering team to build scalable web applications using Python and Flask.'
        },
        {
            'id': 2,
            'title': 'Data Scientist',
            'department': 'Analytics',
            'location': 'San Francisco, CA',
            'type': 'Full-time',
            'description': 'Analyze large datasets and build machine learning models to drive business insights.'
        },
        {
            'id': 3,
            'title': 'UX Designer',
            'department': 'Design',
            'location': 'New York, NY',
            'type': 'Full-time',
            'description': 'Create intuitive and beautiful user experiences for our products.'
        },
        {
            'id': 4,
            'title': 'Marketing Coordinator',
            'department': 'Marketing',
            'location': 'Remote',
            'type': 'Part-time',
            'description': 'Coordinate marketing campaigns and help grow our brand presence.'
        }
    ]
    return render_template('jobs.html', jobs=jobs_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Configure for Replit environment
    app.run(host='0.0.0.0', port=5000, debug=True)