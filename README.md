# Carbon Emissions Calculator

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Django](https://img.shields.io/badge/django-4.2-brightgreen)
![Docker](https://img.shields.io/badge/docker-compose-supported-important)

## 📦 Installation

### Prerequisites
- Docker Desktop
- Python 3.10+
- Climatiq API key ([Get one here](https://www.climatiq.io/api))

### Local Setup
```bash
# Clone repository
git clone https://github.com/Pradyumna-yes/carbon-tracker.git
cd carbon-tracker

# Create environment file
cat > .env <<EOL
CLIMATIQ_API_KEY=your_api_key_here
DEBUG=True
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
EOL

# Build and start containers
docker-compose up -d --build

```


🖥️ Usage
Access the application at:
http://localhost:8000

##  Features Preview

### 1. Energy Input Form
Users enter electricity consumption in kWh to calculate CO₂ emissions.

![Energy Input Form](<img width="940" height="449" alt="image" src="https://github.com/user-attachments/assets/964340c6-a205-456c-9fca-6d17ad48b00d" />
)  
*Figure 1: Form for entering energy consumption values*

### 2. Calculation Results
Instant CO₂ emissions calculation displayed with detailed breakdown.

![Results Page](<img width="940" height="502" alt="image" src="https://github.com/user-attachments/assets/761ba18d-1727-4bf0-80b3-1685a330e292" />)  
*Figure 2: Emissions calculation results with source data*

API Endpoint
POST /
Form Data: energy=[kWh value]

Example:
curl -X POST http://localhost:8000 -d "energy=1500"

🐳 Docker Configuration
Services
Service	Image	Port	Description
web	Custom Django	8000	Application server
db	postgres:13-alpine	5432	PostgreSQL database

Volumes
postgres_data: Persistent database storage

🌐 Network Architecture
<img width="1056" height="1458" alt="deepseek_mermaid_20250728_aae76d" src="https://github.com/user-attachments/assets/8abe755b-9d09-4132-859b-ef6fc5930e77" />

🔧 Technical Stack
Backend
Django 4.2
Gunicorn
PostgreSQL

Frontend
Bootstrap 5
HTML5
CSS3




