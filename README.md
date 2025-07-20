# Portfolio Website

A personal portfolio website built with Flask, HTML, CSS, and JavaScript to showcase my projects, skills, and experience.

## Features

- Responsive design with both desktop and mobile navigation

- Project showcase with detailed individual project pages

- Sections for About, Experience, Projects, and Contact

- Interactive UI elements and smooth transitions

## Project Structure

```text
portfolio-website/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── mediaqueries.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── assets/
│   │       └── images and other static files
│   ├── templates/
│   │   ├── index.html
│   │   ├── python_project.html
│   │   ├── web_dev.html
│   │   ├── android_development.html
│   │   └── cybersecurity_project.html
│   └── routes.py
├── venv/
├── run.py
├── requirements.txt
└── README.md
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/portfolio-website.git
cd portfolio-website
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python run.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Deployment

This project is designed to be deployed on PythonAnywhere, which provides hosting for Flask applications.

## Routes

- / - Home page
- /python_projects - Python project showcase
- /web_dev - Web development projects
- /android_development - Android development projects
- /cyber_security - Cybersecurity projects

## Technologies Used

- Backend: Flask/Python
- Frontend: HTML, CSS, JavaScript
- Responsive Design: Custom CSS with media - queries
- Hosting: PythonAnywhere

## Upcomming

I am planning to add more projects on Android Development where I learned a lot about Java and Kotlin. Stay Tuned!

## License

This project is open source and available under the MIT License.
