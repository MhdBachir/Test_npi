# Reverse Polish Notation Solver

## Project Goal

The primary goal of this project is to provide a solution for evaluating mathematical expressions expressed in Reverse Polish Notation (RPN). Reverse Polish Notation, also known as postfix notation, is a mathematical notation in which every operator follows all of its operands. This notation eliminates the need for parentheses to indicate the order of operations.

## Features

- **Expression Evaluation**: The core feature of this project is the ability to evaluate expressions in RPN. Users can input mathematical expressions, and the application will provide the calculated result.

- **API Endpoint**: The project exposes an API endpoint `/evaluate/` where users can submit RPN expressions, and the server responds with the calculated result.

## How to Use

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/reverse-polish-notation-solver.git
    cd reverse-polish-notation-solver
    ```

2. **Run the Application**:

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 7000
    ```

3. **Use the API Endpoint**:

    Send a POST request to `http://localhost:7000/evaluate/` with a JSON payload containing the RPN expression. For example:

    ```json
    {"expression": "3 4 + 2 *"}
    ```

    The server will respond with the calculated result.

## API Endpoint Example

- **Endpoint**: `/evaluate/`

- **Method**: POST

- **Request Payload**:

    ```json
    {"expression": "3 4 + 2 *"}
    ```

- **Response**:

    ```json
    {"result": 14}
    ```

## Docker Support

This project includes Docker support for easy deployment. Use the provided Dockerfiles and Docker Compose configuration to build and run the application within a containerized environment.

```bash
docker-compose build
docker-compose up
