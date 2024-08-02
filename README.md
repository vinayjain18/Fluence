# Fluence - Personalized Instagram Content Planner

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" />
  <img src="https://img.shields.io/badge/node-14%2B-green.svg" />
  <a href="https://twitter.com/vinayjn18" target="_blank">
    <img alt="Twitter: vinayjn18" src="https://img.shields.io/twitter/follow/vinayjn18.svg?style=social" />
  </a>
</p>


Fluence is an Instagram content planner that helps creators and businesses strategically plan, and generate personalized content based on their industry, niche, and profile details. Our goal is to empower you to unleash your creativity and boost your engagement with tailored content strategies.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [App Link](#app-link)
- [Contact](#contact)

## Features

- Personalized content plans based on your industry, niche, and Instagram profile.
- Industry insights to stay ahead of trends.
- Intuitive interface for easy content planning.
- Engagement-boosting content recommendations.

## Technologies Used

- **Frontend:** HTML, Tailwind CSS, TypeScript, Javascript
- **Backend:** Django
- **Database:** PostgreSQL
- **API Integration:** Instagram Graph API, OpenAI
- **Deployment:** Render

## Installation

### Prerequisites

- Node.js
- npm
- Python(version: 3.10+)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/vinayjain18/Fluence.git
   cd Fluence
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Build the tailwind CSS:
   ```bash
   npm run build-css
   ```

4. Now create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate #for windows -> venv/scripts/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Migrations and Static files:
   ```bash
   #For Database, you can either use the default sqlite or any of your choice 
   #but make sure to update it in fluence/settings.py file.
   
   #create database and tables
   python manage.py makemigrations
   python manage.py migrate

   #static files
   python manage.py collectstatic
   ```
6. Run the Django server:
   ```bash
   python manage.py runserver
   ```

## App Link
Access the live application here: https://fluence.azurewebsites.net/

## Contact
For any questions or feedback, please contact me at vinayjain449@gmail.com