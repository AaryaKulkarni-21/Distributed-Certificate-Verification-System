Distributed Cloud-Based Certificate Verification System



A centralized certificate verification platform designed to enable organizations and HR professionals to validate academic credentials through a distributed architecture of simulated institutional services.



Project Overview



The Distributed Cloud-Based Certificate Verification System aims to simplify and improve the reliability of academic certificate verification.



The platform allows an HR professional or authorized verifier to validate a certificate using its unique Certificate ID. A central verification portal communicates with multiple simulated institution services to retrieve and validate certificate records.



The project follows a distributed architecture in which institutional data is maintained across separate services rather than relying on a single centralized institution database.



Key Features



\* Centralized Verification Portal: Provides a unified interface for certificate verification.

\* Distributed Institution Services: Integrates three independently simulated institutions.

\* Certificate ID Verification: Enables certificate validation using a unique identification number.

\* REST API Communication: Facilitates communication between the central portal and institution services.

\* Verification Results: Displays verification outcomes such as Verified or Invalid / Not Found.

\* Database Integration: Uses SQLite databases to maintain institutional certificate records.



System Architecture



The system consists of the following components:



1\. Central Portal – Handles verification requests and coordinates communication with institutional services.

2\. Institution A – Simulated academic institution service.

3\. Institution B – Simulated academic institution service.

4\. Institution C – Simulated academic institution service.

5\. Database Layer – Stores sample certificate records for each institution.



The central portal communicates with the institutional services through API requests to validate certificate information.



Technology Stack



Category	Technologies

Programming Language	Python

Backend Framework	Flask

Frontend	HTML, CSS

Database	SQLite

API Communication	REST APIs

Development Environment	Visual Studio Code

Cloud Platform	Amazon Web Services (AWS) – Planned



Project Structure



Distributed-Certificate-Verification/

│

├── central\_portal/

│   ├── app.py

│   ├── static/

│   └── templates/

│

├── institution\_a/

│   └── app.py

│

├── institution\_b/

│   └── app.py

│

├── institution\_c/

│   └── app.py

│

├── database/

│   ├── init\_db.py

│   ├── institution\_a.db

│   ├── institution\_b.db

│   └── institution\_c.db

│

├── .gitignore

└── README.md



Development Status



Component	Status

Project Architecture	Completed

Central Verification Portal	Completed

Simulated Institution Services	Completed

Database Setup	Completed

API Communication	Completed

Certificate Verification Workflow	Completed

AWS Cloud Deployment	Planned / In Progress



Cloud Deployment Roadmap



The next phase of development focuses on deploying the application on Amazon Web Services (AWS).



Planned activities include:



\* Preparing the application for cloud deployment.

\* Configuring the required AWS infrastructure.

\* Deploying the central portal and institutional services.

\* Configuring network communication between services.

\* Testing application availability and verification workflows in the cloud environment.



Note: AWS deployment is a planned development phase and has not yet been completed.



Project Scope



This project uses simulated institutional services and sample academic certificate records to demonstrate the distributed verification workflow. It does not currently connect to real university databases or external academic verification APIs.



Future Enhancements



\* Integration with authorized institutional verification systems.

\* Enhanced authentication and access control.

\* Improved data integrity and security mechanisms.

\* Scalable cloud infrastructure and monitoring.

\* Production-ready deployment on AWS.



Project Purpose



This project is developed as part of the Master of Computer Applications (MCA) academic curriculum, with a focus on distributed systems, cloud computing, API integration, and practical application development.

