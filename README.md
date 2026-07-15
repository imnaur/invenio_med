# invenioMED

**invenioMED** is a powerful and secure platform for managing a clinic and its records, built on Django.
The system
automates
patient scheduling, service catalog management, blog maintenance, and the recording of diagnostic results.

**🚀 Key Features**
Service Catalog Management: Convenient management of clinic services.

Smart Appointment Scheduling: An appointment scheduling process with automatic notifications to the administrator.

InvenioBot: A built-in AI assistant (based on LLM) that provides reference information. Important: The bot does not issue medical
prescriptions or make diagnoses.

Multilingual Support: Support for Russian and English with one-click language switching.

Background Processing: Uses Celery and Celery Beat to send email notifications and perform regular tasks without
overloading the main interface.

Diagnostics: Maintenance of a database of medical results and test reports.

Blog: An internal publishing system for patients and staff.

Security: Access rights managed based on user roles.

**🎨 Design and Interface**
The system interface is built using Bootstrap 5, which ensures:

Full responsiveness (the site displays correctly on smartphones, tablets, and PCs).

A modern look for forms, tables, and navigation panels, as well as an attractive design

Fast loading of interface components

**🛠 Technology Stack**

Backend: Django 6.0, Python >=3.12,<3.15

Task Queue: Celery + Redis

AI: Integration with the LLM API for InvenioBot

Internationalization: Django i18n

Frontend: Bootstrap 5 (responsive layout)

**Database:**
PostgreSQL (for development) / PostgreSQL (recommended for production)

**Testing:**
unittest + coverage
The project is covered by unit tests to ensure secure data access.

**Style:**
HTML5, CSS3

🤖 InvenioBot
Our built-in assistant helps users find answers to common questions about the clinic’s operations.

Disclaimer: The AI assistant is for informational purposes only. 

🌍 Localization
The website is fully translated into two languages. The language switcher is available in the site’s navigation bar.

🛠 Installation and Setup
To run the project, make sure you have Redis (a message broker) installed.

Clone the repository:

Bash
git clone https://github.com/imnaur/invenio_med.git
cd invenio_med
Install dependencies (via Poetry):

Bash
poetry install
Apply migrations:

Bash
poetry run python manage.py migrate
⚙️ Starting processes
For the project to function properly, you need to start processes in three terminals:

Django server:

Bash
poetry run python manage.py runserver
Celery Worker (task processing):

Bash
poetry run celery -A config worker --loglevel=info
Celery Beat (scheduler):

Bash
poetry run celery -A config beat --loglevel=info
🔐 Access Control
The system uses PermissionRequiredMixin to protect critical data:

Administrators: full access to all modules.

Doctors: access to patient records and diagnostic results.

Patients: access to their personal account, viewing their information, and the chatbot.

🧪 Testing
Bash
# Run all tests
poetry run python manage.py test

# Check code coverage
poetry run coverage run manage.py test
poetry run coverage report