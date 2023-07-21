# ToDo List
ToDo list is a web application that allows you create, update and delete  tasks for your daily routine

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/KirillMelanich/py-to-do-list.git
   
2. Navigate to the project directory and activate virtual environment:
   ```shell
   cd radio-station
   python3 - venv venv
   venv/Scripts/activate(on Windows)
   source venv/bin/activate(on Mac)
   
3. Install dependencies:
   ```shell
    pip install -r requirements.txt
   
4. Perform database migrations:
    ```shell
    python manage.py migrate

5. Add these apps to `INSTALLED_APPS` and install them corresponding to the `CRISPY_TEMPLATE_PACK` bootstrap version.

      ```python
        INSTALLED APPS = [
      ...,
      "crispy_bootstrap4",
      "crispy_forms",
   ]
   ```
## Usage

1. Run the development server:
     ```shell
    python manage.py runserver
2. Open your web browser and visit:
    ```shell 
    http://localhost:8000/
   
## Features:
```shell 
Tasks: Browse, add, update, and delete task for you
Tags: View and manage usefull tags for tasks
```
