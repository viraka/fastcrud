# FastAPI CRUD Project

This project is a simple FastAPI application that demonstrates how to create a CRUD (Create, Read, Update, Delete) API for managing categories and products. The project uses SQLAlchemy for database interactions and Pydantic for data validation.

## Project Structure

```plaintext
my_fastapi_project/

├── app/
|   ├── __init__.py           # Initializes the app package
|   ├── main.py                   # Entry point of the application  
│   ├── database.py           # Database configuration and session management
│   ├── models.py             # SQLAlchemy models for Category and Product
│   ├── schemas.py            # Pydantic schemas for data validation
│   ├── routers/
│   │   ├── __init__.py       # Initializes the routers package
│   │   ├── categories.py     # API routes for category management
│   │   └── products.py       # API routes for product management
└── README.md                 # Project documentation

```

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite (or any other SQL database)

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    In this project, an SQLite database is used by default, which will be created automatically when you run the application for the first time. If you are using a different database, configure the `DATABASE_URL` in `app/database.py`.

5. **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

6. **Access the API**:
    The API will be available at `http://127.0.0.1:8000`.

7. **API Documentation**:
    FastAPI automatically generates interactive API documentation:
    - Swagger UI: `http://127.0.0.1:8000/docs`
    - ReDoc: `http://127.0.0.1:8000/redoc`

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

Please ensure your code adheres to the coding standards and that you have included relevant tests.

## Contact

For any inquiries, please reach out at [virajprabhup@gmail.com](mailto:virajprabhup@gmail.com).
