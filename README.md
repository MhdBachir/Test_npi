# Reverse Polish Notation Solver

## Project Goal

The primary goal of this project is to provide a solution for evaluating mathematical expressions expressed in Reverse Polish Notation (RPN). Reverse Polish Notation, also known as postfix notation, is a mathematical notation in which every operator follows all of its operands. This notation eliminates the need for parentheses to indicate the order of operations.

## Features

- **Expression Evaluation**: The core feature of this project is the ability to evaluate expressions in RPN. Users can input mathematical expressions, and the application will provide the calculated result.

- **API Endpoint**: The project exposes an API endpoint `/evaluate/` where users can submit RPN expressions, and the server responds with the calculated result.

## How to Use

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/MhdBachir/Test_npi.git
    cd Test_npi
    ```

2. **Run the Application**:

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 7000
    ```

3. **Utiliser le point de terminaison de l'API**:

    Envoyez une requête POST à `http://localhost:7000/calculate/` avec une charge JSON contenant l'expression RPN. Par exemple :

    ```json
    {"expression": "3 4 + 2 *"}
    ```

    Le serveur répondra avec le résultat calculé. Vous pouvez également utiliser l'interface interactive de la documentation Swagger en accédant à `http://localhost:7000/api/v1/docs` pour tester l'API avec différentes expressions.

4. **Télécharger les opérations enregistrées au format CSV**:

    Pour récupérer toutes les opérations enregistrées dans la base de données sous forme de fichier CSV, envoyez une requête GET à `http://localhost:7000/download/`. Le serveur répondra avec un fichier CSV téléchargeable contenant les expressions et les résultats des opérations enregistrées.

    Par exemple, vous pouvez utiliser un outil tel que curl pour télécharger le fichier depuis la ligne de commande :

    ```bash
    curl -OJ http://localhost:7000/download/
    ```

    Assurez-vous d'avoir les autorisations appropriées pour accéder aux opérations enregistrées. Si nécessaire, ajustez les paramètres d'autorisation dans votre application FastAPI.


## API Endpoint Example

- **Endpoint**: `/evaluate/` , `/download/`

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
