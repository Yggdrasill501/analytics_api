# Google Analytics 4 API

## Overview

This project is a full-stack application integrating a Django backend with a Next.js frontend. The backend interacts with the Google Analytics 4 API to fetch and serve analytics data, while the frontend displays this data in a user-friendly manner.

## Features

- **Google Analytics 4 Integration**: Connects to the Google Analytics 4 API using OAuth 2.0 for secure data access.
- **Data Fetching**: Retrieves a variety of metrics and dimensions from Google Analytics.
- **Customizable Reports**: Supports the creation of custom reports and endpoints for specific data needs.
- **Next.js Frontend**: Utilizes Next.js for a modern, responsive user interface.
- **JSON Responses**: Backend serves data in JSON format, making it easy to integrate with the frontend or other applications.

## Prerequisites

Before starting, ensure you have the following:

- Python 3.x and Node.js installed on your machine.
- Django and necessary Python packages installed.
- A Google Cloud project with the Google Analytics API enabled.
- OAuth 2.0 credentials (Client ID and Client Secret) from Google Cloud Console.
- A Google Analytics 4 property with appropriate permissions.
- Next.js and necessary Node.js packages installed.

## Setup and Installation

### Backend (Django)

1. **Clone the Repository**: Clone the repository to your local machine.
2. **Install Dependencies**: Install required Python packages.
3. **Google Cloud Credentials**: Place the `credentials.json` file in your project directory.
4. **Configuration**: Update the Django `settings.py` file with the path to your credentials and any other necessary settings.
5. **Run Migrations**: Apply any database migrations required by Django.
6. **Start the Server**: Launch the Django development server.

### Frontend (Next.js)

1. **Create Next.js Project**: Create a new Next.js project.
2. **Install Dependencies**: Install necessary Node.js packages like `axios`.
3. **Fetch and Display Data**: Implement pages and components to fetch data from the Django backend and display it.
4. **Run the Development Server**: Start the Next.js development server.

## Usage

- **Endpoints**: Access predefined endpoints in the Django backend to fetch various reports and analytics data.
- **Customization**: Modify or add new views and endpoints in Django and Next.js to tailor the data fetching and display to your specific needs.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Ensure that your code adheres to the project's coding standards and includes appropriate tests.
---
