# CutSession-Pipeline-Project

A Python API for scheduling studio (photo and video) sessions built with FastAPI.

## Installation

This project requires [Python](https://www.python.org/downloads/) v3.9+ to run.

1. Clone the project from the repository and then cd into the root directory.

  ```sh
  
  git clone https://github.com/DonTee-Why/CutSession-Pipeline-Project.git
  cd CutSession-Pipeline-Project
  
  ```
  
2. To avoid alterating global packages, I suggest using a virtual environment. Create a virtual environment

  ```sh
  python -m venv env
  ```
  
  And then activate it.
  
  On linux:
  
  ```sh
  source ./env/bin/activate
  ```
  
  On windows:
  
  ```sh
  env\Scripts\activate.bat
  ```

3. Install the dependencies in the virtual environment.

  ```sh
  cd CutSession-Pipeline-Project
  pip install -r requirements.txt
  ```
  
4. Run the project

  ```sh
  uvicorn main:app --reload
  ```
  
## Testing

The project includes unit tests written with `unittest`.

- To run all the tests:

  ```sh
  python -m unittest
  ```
  
- To run individual test suites:

  ```sh
  python -m unittest tests.<TEST SUITE>
  ```
  
## License

MIT License
