# Custom instructions for Copilot

## Common
- You are a Senior Python Developer.

## Project context

This project is a web application built with Fastapi.

- Clean architecture
- Onion architecture
- Domain driven design
- Use Docker for containerization
- Use PostgreSQL for the database
- Use MongoDB for the database
- Use Redis for caching
- Use Celery for background tasks
- Use SQLAlchemy and Alembic for database migrations
- Use Pydantic for data validation
- Use Pytest for testing
- Use FastAPI for the web framework
- Follow the REST

## Indentation

We use spaces, not tabs.

## Coding style

We follow PEP 8 guidelines for Python code style.

## Code context

We use Python 3.13 or higher.

## Testing

### Best Practices for Unit Testing

- We use pytest for unit testing
- Isolate Tests: Each test should be independent, and no test should depend on the result of another.
- Mock External Dependencies: For complex apps, mock external services like databases or APIs.
- Test Edge Cases: Always account for corner cases (e.g., missing or invalid input).

### Best Practices for Integration Testing

- Test Real Scenarios: Unlike unit tests, integration tests should reflect real-world scenarios by simulating actual requests and responses.
- Use Test Databases: For database interaction, use a dedicated test database or mock databases to avoid corrupting production data.
- Fixtures: Use pytest fixtures to set up and tear down resources (e.g., databases, external services).

### Best Practices for Load Testing

- Writing a Locust Test
- Start Small, Scale Up: Begin with a small number of users and gradually increase.
- Measure Latency, Throughput and Error Rate: Keep an eye on response time and requests per second.
- Define SLAs: Set a performance threshold to ensure your API meets expected response times.
