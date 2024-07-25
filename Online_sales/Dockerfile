# STEP 1: Install Base image. Optimized for Python
FROM python:3.12-slim

# STEP 2: Upgrading pip
RUN pip install --upgrade pip

# STEP 3: Copying all the files to the app directory
COPY . /usr/ML/app

# STEP 4: Expose port 5000 of Docker to run this application
EXPOSE 5000

# STEP 5: Set working directory for the app
WORKDIR /usr/ML/app

# STEP 5: Giving permissions to python file
RUN chmod +x app.py

# STEP 6: Install required python dependencies from the requirements file
RUN pip install -r requirements.txt

# STEP 7: Run the app.py file
ENTRYPOINT [ "python" ]

CMD [ "flask_api.py" ]