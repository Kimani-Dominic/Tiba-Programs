## Tiba-Programs Documentation

- A short program that simulates a basic health information system for managing clients and health programs built in django.

## App Properties

### 1. User Authentication and Authorization
- Secure login and authentication using OAuth 2.0.
- Role-based access control for **Patients & Doctors**.

### 2. Appointment Scheduling
- Patients can book, reschedule, or cancel appointments.
- Doctors can book appointments for patients after enrolling them in a program.

### 3. Medical Report Management

The **Medical Records** module allows doctors and authorized users to maintain and access patients' medical history.

- Create and manage patient medical records
- Secure access control (only authorized users can view/edit)
- Store past appointment notes and programs history
- Integrated with appointments


### 4. API Documentation
- API endpoints are documented using **Swagger**.
- Available at `http://localhost:8000/swagger` for interactive API testing.

---

## System Architecture

### 1. Technology Stack
| Component       | Technology Used |
|----------------|----------------|
| Backend        | Django |
| Database       | PostgreSQL      |
| Authentication | Token-based Auth |
| API Docs       | Swagger & Redoc |

### 2. System Design
- **Client-Server Model:** Uses a REST API Development to handle requests.
- **Role-based Access Control (RBAC):** Manages access levels for Patients and Doctors
- **Database Design:** Uses PostgreSQL with well-structured models for **Users, Programs Management, Appointments, and Medical Records**.


### 3. Database Schema

### Tables & Relationships

#### **Auth**
- **id**: Primary Key
- **username**: Unique username for the user
- **email**: unique email
- **password**: Encrypted password
- **role**: Boolean to get either a doctor or patient, default for patient

#### **appointments**
- **id**: Primary Key
- **patient**: ForeignKey to `Patient` (one-to-many relationship)
- **doctor**: ForeignKey to `Doctor` (one-to-many relationship)
- **program**: ForeignKey to `Programs` (one-to-many relationship)
- **appointment_time**: Date and time of the appointment
- **status**: Status of the appointment (pending, confirmed, completed, canceled)


#### **MedicalRecords**
- **patient**: ForeignKey to `Patient` (one-to-many relationship)
- **appointment**: ForeignKey to `Appointment` 
- **program**: ForeignKey to `Programs` (one-to-many relationship)
- **notes**: Additional notes
---

### 4. Design Decisions

#### Role-Based Access Control (RBAC):

- Patient Role: normal users.

- Doctor Role: Only users with the doctor role can create programs and medical records linked to specific appointments.


#### Appointment Model:

- Links appointments to a specific program

- Doctors can book appointments for patients after enrolling them in a program.


#### MedicalRecord Model:

- Linked medical records to their profile information i.e appointments and programs.

- Ensured access to sensitive medical information only by authorized roles.

#### Authentication & Access Control:

- Enforced that only authenticated users can create appointments or get medical records & users.

- Doctors can only create medical records and specific programs for patients and their specific appointments.

#### Data Integrity:

- Used Django model relationships (ForeignKey, OneToOneField) to ensure programs, appointments and medical records are properly linked.

#### Security:

- Sensitive medical information is only accessible by authorized users, i.e, doctors.

- Password and email validation ensure secure user registration.


#### Experience with DHIS2 programs
Having worked with **DHIS2**, a comprehensive opensource healthcare platform, the design leverages similar concepts to programs and inking them with patients medical records:

- **DHIS2 Programs**: Just like DHIS2, links programs to various metadata
ients can book appointments, and only doctors can manage medical records.