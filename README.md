# MongoDB + Flask + Azure App Services Demo

This project is a simple Flask application that connects to a MongoDB Atlas database and implements CRUD (Create, Read, Update, and Delete) functionality. The application is designed to be hosted on Azure App Services.

## Project Structure

The project has the following structure:

- `app.py`: This is the main Python script of the application. It sets up the Flask application and handles the routing for the application.
- `templates/index.html`: This is the HTML template for the application's homepage.
- `requirements.txt`: This file lists the Python dependencies that need to be installed for the application to run.
- `.gitignore`: This file specifies the files and directories that Git should ignore.

## How It Works

The application connects to a MongoDB Atlas database using the connection string specified in the environment variable `CONNECTION_STRING`. It then uses this database to perform CRUD operations on a collection of books.

The application has the following endpoints:

- `/`: The homepage of the application, which displays a list of tasks that the application can perform.
- `/books`: This endpoint is used to create a new book (POST request) or retrieve all books (GET request).
- `/books/<book_id>`: This endpoint is used to update (PUT request) or delete (DELETE request) a specific book.

## Setup and Installation

1. Clone the repository to your local machine.
2. Install the required Python dependencies by running `pip install -r requirements.txt`.
3. Set the `CONNECTION_STRING` environment variable to your MongoDB Atlas connection string.
4. Run the application by executing `python app.py`.

## Hosting on Azure

To host this application on Azure App Services, follow the official Azure documentation for deploying a Flask application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
