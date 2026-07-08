# Hospital Management System – Backend CRUD API (Django + DRF)

A REST API-based Hospital Management System built with Django, Django REST Framework,
Models, Serializers (ModelSerializer), and function-based views, using SQLite by default.
Manages three modules: **Doctors**, **Patients**, and **Appointments**.

## Project Structure
```
HospitalManagement/
├── manage.py
├── HospitalManagement/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── doctor/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── patient/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
└── appointment/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── migrations/
```

## Setup Instructions

1. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install django djangorestframework
   ```

3. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

5. The API will be available at `http://127.0.0.1:8000/`

---

## Module 1 – Doctor Management

### Doctor Model

| Field            | Type                        |
|-------------------|------------------------------|
| doctor_name       | CharField (max_length=100)  |
| specialization    | CharField (max_length=100)  |
| experience        | IntegerField                |
| phone             | CharField (max_length=10)   |
| email             | EmailField                  |
| consultation_fee  | FloatField                  |

### API Endpoints

| Method | Endpoint                    | Description          |
|--------|-------------------------------|------------------------|
| POST   | `/doctors/add/`               | Add a new doctor       |
| GET    | `/doctors/`                   | Retrieve all doctors   |
| PUT    | `/doctors/update/<id>/`       | Update doctor details  |
| DELETE | `/doctors/delete/<id>/`       | Delete a doctor        |

### Sample Request — POST `/doctors/add/`
```json
{
    "doctor_name": "Dr. Ramesh Kumar",
    "specialization": "Cardiologist",
    "experience": 12,
    "phone": "9876543210",
    "email": "ramesh@gmail.com",
    "consultation_fee": 700
}
```
Response:
```json
{
    "message": "Doctor Added Successfully",
    "doctor": {
        "id": 1,
        "doctor_name": "Dr. Ramesh Kumar",
        "specialization": "Cardiologist",
        "experience": 12,
        "phone": "9876543210",
        "email": "ramesh@gmail.com",
        "consultation_fee": 700
    }
}
```

---

## Module 2 – Patient Management

### Patient Model

| Field         | Type                        |
|----------------|------------------------------|
| patient_name   | CharField (max_length=100)  |
| age            | IntegerField                |
| gender         | CharField (max_length=10)   |
| phone          | CharField (max_length=10)   |
| disease        | CharField (max_length=100)  |
| address        | CharField (max_length=255)  |

### API Endpoints

| Method | Endpoint                     | Description            |
|--------|---------------------------------|--------------------------|
| POST   | `/patients/add/`                | Add a new patient       |
| GET    | `/patients/`                    | Retrieve all patients   |
| PUT    | `/patients/update/<id>/`        | Update patient details  |
| DELETE | `/patients/delete/<id>/`        | Delete a patient        |

### Sample Request — POST `/patients/add/`
```json
{
    "patient_name": "Rahul Sharma",
    "age": 28,
    "gender": "Male",
    "phone": "9123456789",
    "disease": "Fever",
    "address": "Hyderabad"
}
```
Response:
```json
{
    "message": "Patient Added Successfully",
    "patient": {
        "id": 1,
        "patient_name": "Rahul Sharma",
        "age": 28,
        "gender": "Male",
        "phone": "9123456789",
        "disease": "Fever",
        "address": "Hyderabad"
    }
}
```

---

## Module 3 – Appointment Management

### Appointment Model

| Field              | Type                        |
|---------------------|------------------------------|
| patient_name        | CharField (max_length=100)  |
| doctor_name         | CharField (max_length=100)  |
| appointment_date    | DateField                   |
| appointment_time    | TimeField                   |
| status              | CharField (max_length=50)   |

> **Note:** `patient_name` and `doctor_name` are kept as plain CharFields per the
> project spec (ForeignKey relationships to Doctor/Patient models are a later topic).

### API Endpoints

| Method | Endpoint                         | Description                |
|--------|-------------------------------------|-------------------------------|
| POST   | `/appointments/add/`                | Add a new appointment        |
| GET    | `/appointments/`                    | Retrieve all appointments    |
| PUT    | `/appointments/update/<id>/`        | Update appointment details   |
| DELETE | `/appointments/delete/<id>/`        | Delete an appointment        |

### Sample Request — POST `/appointments/add/`
```json
{
    "patient_name": "Rahul Sharma",
    "doctor_name": "Dr. Ramesh Kumar",
    "appointment_date": "2026-07-20",
    "appointment_time": "10:30:00",
    "status": "Confirmed"
}
```
Response:
```json
{
    "message": "Appointment Added Successfully",
    "appointment": {
        "id": 1,
        "patient_name": "Rahul Sharma",
        "doctor_name": "Dr. Ramesh Kumar",
        "appointment_date": "2026-07-20",
        "appointment_time": "10:30:00",
        "status": "Confirmed"
    }
}
```

---

## Full API Summary (12 APIs)

| # | Module      | Method | Endpoint                       | Description              |
|---|-------------|--------|----------------------------------|-----------------------------|
| 1 | Doctor      | POST   | `/doctors/add/`                  | Add a new doctor           |
| 2 | Doctor      | GET    | `/doctors/`                      | Retrieve all doctors       |
| 3 | Doctor      | PUT    | `/doctors/update/<id>/`          | Update doctor details      |
| 4 | Doctor      | DELETE | `/doctors/delete/<id>/`          | Delete a doctor            |
| 5 | Patient     | POST   | `/patients/add/`                 | Add a new patient          |
| 6 | Patient     | GET    | `/patients/`                     | Retrieve all patients      |
| 7 | Patient     | PUT    | `/patients/update/<id>/`         | Update patient details     |
| 8 | Patient     | DELETE | `/patients/delete/<id>/`         | Delete a patient           |
| 9 | Appointment | POST   | `/appointments/add/`             | Add a new appointment      |
| 10| Appointment | GET    | `/appointments/`                 | Retrieve all appointments  |
| 11| Appointment | PUT    | `/appointments/update/<id>/`     | Update appointment details |
| 12| Appointment | DELETE | `/appointments/delete/<id>/`     | Delete an appointment      |

## Notes
- All 12 endpoints have been tested end-to-end (add, list, update, delete for
  each module) and confirmed to return the exact response shapes described in
  the project spec.
- Each model (`Doctor`, `Patient`, `Appointment`) is also registered in Django
  Admin (`/admin/`) for easy inspection (create a superuser with
  `python manage.py createsuperuser`).
- Time values (`appointment_time`) accept `HH:MM:SS` 24-hour format, e.g.
  `"14:00:00"` for 2:00 PM.
