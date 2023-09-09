# FastAPI Form 1

![FastAPI logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

This project implements a simple web form using FastAPI with Python and SQL

## Features

- Web form with name, email, message inputs
- Form data validation on both frontend and backend
- Submitting the form saves the data to a JSON file  
- List submitted messages on a separate page

The backend will be available at http://localhost:8000

### Frontend

The frontend will be available at http://localhost:3000

- `POST /submit`: Validates and saves form data
- `GET /messages`: Returns submitted messages 

Validation is done with Pydantic models. Data is saved to `backend/messages.json`


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or issues, please email sebajgodoy@gmail.com
