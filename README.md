
# MSC Workflow Project

This project is a Django application for managing data for students, teachers, coordinators, experts, proposals, defense notices, and assigning marks to student projects. The project is containerized using Docker to ensure consistent environments for development and deployment.

## Prerequisites

Make sure you have the following installed on your system:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Installation

1. Clone the repository:
   git clone https://github.com/JanardanBhetwal/MSC_Workflow.git

2. Navigate to the project directory:
   cd msc_workflow

3. Build and run the Docker containers:
   docker-compose up --build

### Accessing the Application

Open a web browser and go to:
http://localhost:7188


## Troubleshooting

If you encounter issues, make sure the Docker service is running on your machine. You can check the Docker service status by running:
docker info
If Docker is not running, start it from the Docker Desktop application or restart the Docker service.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
