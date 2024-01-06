# LeNs

## Overview

This repository contains the codebase for a comprehensive school dashboard system designed to streamline administrative tasks, facilitate communication, track student progress, and provide insightful data analysis. It comprises features for user authentication, student and teacher record management, performance analysis, intervention tracking, goal setting, communication tools, customizable views, data analysis, parent access, gamification, integration with existing systems, data privacy, and feedback mechanisms.

## Features

### <span style="color:blue">User Authentication</span>
- Secure login and signup processes
- Storage of user information (name, email, hashed password) in a database
- Credential validation upon login

### <span style="color:green">Student Records</span>
- Management and display of student details (name, grade, test scores, attendance, disciplinary actions)
- Database storage and retrieval based on user permissions

### <span style="color:orange">Teacher Records</span>
- Management and display of teacher information (name, subjects taught, performance reviews, professional development)
- Separate database storage and retrieval based on user permissions

### <span style="color:purple">Performance Analysis</span>
- Visual representation of student and teacher performance data through charts and graphs
- Examples: average test scores by grade, attendance trends over time

### <span style="color:brown">Intervention Tracking</span>
- Monitoring and recording of interventions for struggling students
- Includes parent meetings, tutoring sessions, assigned remedial work
- Data storage and display in table format

### <span style="color:#ff00ff">Goal Setting</span>
- Assistance in setting and tracking goals for both students and teachers
- Storage and tracking of individual goals, showcasing progress

### <span style="color:red">Communication</span>
- Facilitation of communication among teachers, administrators, and parents
- Messaging system, announcements, and event calendar integration
- Compatibility with email or text messaging platforms

### <span style="color:#4CAF50">Customizable Views</span>
- Personalized dashboard views based on user preferences
- Tailoring data display for various needs (behavioral, academic focus)

### <span style="color:#2196F3">Data Analysis Tools</span>
- Integration of tools for data insights and analysis
- Report generation, correlation analysis, predictive analytics

### <span style="color:#FF5722">Parent Access</span>
- Parental access to monitor child's progress and interact with teachers
- Real-time grade updates, messaging, and progress reports

### <span style="color:#795548">Gamification</span>
- Implementation of gamification elements for student and teacher engagement
- Badges, points, and academic challenges for motivation

### <span style="color:#607D8B">Integration with Other Systems</span>
- Seamless integration with existing school systems (e.g., learning management, student information)
- Streamlining data collection and enhancing usability

### <span style="color:#673AB7">Data Privacy and Security</span>
- Implementation of robust data privacy measures (encryption, access controls)
- Regular data backup and recovery procedures

### <span style="color:#FF9800">Feedback Mechanisms</span>
- User-friendly feedback mechanisms (surveys, user testing)
- Continuous improvement based on user input

## Tech Stack

### Front-end
- React: JavaScript library for building user interfaces
- Redux: Predictable state management for data flow in the application
- Chart.js: JavaScript library for creating various charts and graphs
- Material-UI: React component library following Material Design guidelines

### Back-end
- FastAPI: Python web framework for building high-performance APIs
- SQLAlchemy: Python library for working with relational databases
- MariaDB: Open-source relational database management system

### Infrastructure
- AWS (Amazon Web Services): Cloud computing platform for hosting, storage, and networking
- Terraform: Infrastructure as code tool for provisioning and managing resources
- Jenkins: Continuous Integration/Continuous Deployment (CI/CD) tool for automating build and deployment processes

## Installation and Deployment

### Prerequisites
- Node.js, Python, Docker
- AWS account, Terraform, Jenkins setup

### Installation Steps
1. Clone this repository
2. Set up front-end and back-end environments
3. Configure databases and API endpoints
4. Deploy using Docker containers
5. Utilize Terraform for AWS infrastructure provisioning
6. Implement CI/CD with Jenkins for automated deployment

For detailed installation instructions, refer to individual component READMEs.

## Contributors
- [Rohit Jain](https://github.com/rohitjain25)
- [Ronak Jain](https://github.com/jainr5668)
