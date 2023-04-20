# Logging API
This is a REST API that allows legacy systems to log to the centralized logging system. Each log entry must have the following metadata:

- Application ID (source of log entry)
- Trace ID
- Severity
- Timestamp
- Message
- Optional metadata:

- Component name
- Request ID

The API supports multiple log destinations, such as Kafka topic, Flat file, MQ topic.

## Tech Stack
- Python 3.9
- FastAPI
- Kafka
- Pydantic
- pytest
This section lists the technologies used in the project, including the programming language, web framework, messaging system, and libraries.

## Getting Started
### Prerequisites
Python 3.9 or later installed on your system
This section lists the prerequisites required to run the project, which is Python 3.9 or later.

### Installation
1. Clone the repository:
`git clone https://github.com/<username>/logging-api.git`
2. Install the dependencies:
`pip install -r requirements.txt`
3. Start the server:
`uvicorn app.main:app --reload`
4. Open your browser and go to http://localhost:8000/docs to access the Swagger UI.
Sure, here's the README.md in Markdown format with explanations for each section:

Logging API
This is a REST API that allows legacy systems to log to the centralized logging system. Each log entry must have the following metadata:

Application ID (source of log entry)
Trace ID
Severity
Timestamp
Message
Optional metadata:

Component name
Request ID
The API supports multiple log destinations, such as Kafka topic, Flat file, MQ topic.

Tech Stack
Python 3.9
FastAPI
Kafka
Pydantic
pytest
This section lists the technologies used in the project, including the programming language, web framework, messaging system, and libraries.

Getting Started
Prerequisites
Python 3.9 or later installed on your system
This section lists the prerequisites required to run the project, which is Python 3.9 or later.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/<username>/logging-api.git
Install the dependencies:

Copy code
pip install -r requirements.txt
Start the server:

lua
Copy code
uvicorn app.main:app --reload
Open your browser and go to http://localhost:8000/docs to access the Swagger UI.

This section provides the steps required to install and run the project, including cloning the repository, installing dependencies, starting the server, and accessing the Swagger UI.
 
## Usage
  ### Logging an Entry
  To log a new entry, send a POST request to the /log endpoint with the following data:
  `{
    "application_id": "myapp",
    "trace_id": "123456",
    "severity": "INFO",
    "timestamp": "2023-04-19T12:34:56Z",
    "message": "User logged in successfully"
}
`
You can also include optional metadata such as component_name and request_id.

This section explains how to log an entry by sending a POST request to the /log endpoint with required and optional metadata.
  
### Retrieving Logs
To retrieve logs, send a GET request to the /log endpoint. You can filter the logs by various parameters such as application_id, trace_id, severity, and timestamp.

This section explains how to retrieve logs by sending a GET request to the /log endpoint with filter parameters.

### Changing the Log Destination
To change the log destination, modify the LOG_DESTINATION constant in app/config.py. The options are "kafka", "file", and "mq".

This section explains how to change the log destination by modifying the LOG_DESTINATION constant in app/config.py.
  
## Running Tests
To run the tests, use the following command:  
`pytest app/tests`  
  
 ## Below is a brief explanation of each code module:

1. `app/main.py`: This is the main entry point for the application. It imports the FastAPI framework and sets up the endpoints and routes for the logging API.

2. `app/models.py`: This module defines the data models used by the application. In this case, we have a LogEntry model which represents a single log entry in the system.

3. `app/services.py`: This module defines the services used by the application. In this case, we have a LogService which handles the business logic of creating and retrieving log entries.

4. `app/destinations.py`: This module defines the different log destinations supported by the application. In this case, we have a KafkaDestination, FileDestination, and MQDestination.

5. `app/config.py`: This module defines the configuration settings for the application, such as the log level and log format.

6. `app/utils.py`: This module defines utility functions used by the application, such as generating trace IDs and timestamps.

7. `tests/test_logging.py´: This module defines the unit tests for the logging API and services. We are using the pytest framework to run our tests.

Overall, the code we wrote follows SOLID principles and uses a TDD approach to ensure that it is well-designed and tested. The code is modular and easy to understand, with clear separation of concerns between the different components. By following these best practices, we can ensure that the logging API is reliable, scalable, and maintainable.
