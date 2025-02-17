# Project Name

This project is a FastAPI-based application for plate number recognition using PaddleOCR.

## 1. Setup Virtual Environment

To set up the project environment, follow these steps:

1. **Create a virtual environment**:

   ```bash
   python3.10 -m venv venv
   ```

2. **Activate the virtual environment**:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

## 2. Install Dependencies

After activating the virtual environment, install the required packages by running:

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies for the project.

## 3. Run the Application

To run the FastAPI app with auto-reload, execute the following command:

```bash
uvicorn app.main:app --reload
```

This will start the server, and your application will be accessible locally.

## 4. Test the API

Once the server is running, open a web browser and go to the following URL:

```
http://127.0.0.1:8000/docs
```

This will open the Swagger UI where you can test the API endpoints.
