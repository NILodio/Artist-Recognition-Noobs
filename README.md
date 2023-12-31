
<div align="center">

# 🐍 Artistic Recognition


[![GitHub release (latest by date)](https://img.shields.io/github/v/release/anujonthemove/Python-Machine-Learning-Template?style=flat-square)](

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

[![Linux](https://img.shields.io/badge/Linux-yellow?style=flat-square&logo=linux)]()
[![macOS](https://img.shields.io/badge/MacOS-inactive?style=flat-square&logo=macos)]()
[![Windows](https://img.shields.io/badge/Windows-blue?style=flat-square&logo=windows11)]()

</div>

## 🗂️ Directory Structure

```

.
├── config/                  <- 📂 Configuration files [.ini, .json, .yaml]
├── data/                    <- 📂 Images, numpy data objects, text files
├── docs/                    <- 📂 Store .md files. Used by Mkdocs for Project Documentation
├── logs/                    <- 📂 Log files generated by the project during execution
├── models/                  <- 📂 Model files [.h5, .pkl, .pt] - pre-trained weight files, snapshots, checkpoints
├── notebooks/               <- 📂 Jupyter Notebooks
├── references/              <- 📂 Data dictionaries, manuals, and all other explanatory materials
├── scripts/                 <- 📂 Utility scripts for various project-related tasks
├── src/                     <- 📂 Source code (.py files)
├── tests/                   <- 📂 Unit tests for the project
├── workspaces/              <- 📂 Multi-user workspace that can be used in the case of a single machine
├── .env-template            <- 🔧 Template for the .env file
├── .gitattributes           <- 🔧 Standard .gitattributes file
├── .gitignore               <- 📛 Standard .gitignore file
├── .pre-commit-config.yaml  <- 🔧 Config file for Git Hooks
├── LICENSE                  <- 🪧 License file [choose your appropriate license from GitHub]
├── mkdocs.yml               <- 🗞️ Base config file required for Mkdocs
├── Pipfile		              <- 🗃️ Most commonly used python packages
├── README.md                <- 📝 Project readme
├── setup.py                 <- 📦️ For installing & packaging the project
└── tox.ini                  <- 🔧 General-purpose package configuration manager

```

## 📦 Dev-Packages
All the packages to be installed are included in the Pipfile. For installing additional packages

<details> 
<summary> <h3> Base Packages </h3> </summary>

```
* numpy           <- for numerical computing and scientific computing
* scipy           <- mathematical algorithms and convenience functions built on the NumPy
* pandas          <- for data manipulation and analysis
* matplotlib      <- plotting library
* seaborn         <- data visualization library for drawing informative statistical graphics.
* scikit-learn    <- machine learning library 
* jupyter         <- web-based interactive computing platform
* jupyter-server  <- backend for Jupyter notebooks. Required when running notebooks in VS Code
* ipykernel       <- interactive Python shell. Required when running notebooks in VS Code
* ipython         <- provides a powerful interactive shell and a kernel for Jupyter
```
</details>
 
<details> 
<summary> <h3> Development Packages </h3> </summary>


```
* isort                        <- sorts imports in a python file
* python-decouple              <- Reads configuration/settings from .env, system environment variables 
* flake8                       <- Code linter (format checker)
* flake8-tabs                  <- Tab (and Spaces) Style Checker for flake8
* black                        <- Code formatter
* mypy                         <- Static type checker
* pre-commit                   <- A framework for managing and maintaining multi-language pre-commit hooks.
* pdoc3                        <- Generate API documentation for Python projects
* mkdocs                       <- Generate Project documentation for Python projects
```
</details>


## 👷 Kaggle

Due to the complexity of the problems, the models were trained using Kaggle, as it provides a more robust hardware processing environment. However, the notebooks related to these models can be found in the "notebooks" folder.
 

* 😎 Fast-App PCO

* 🤩 Streamlit App 



## 🚀 Features

* 😎 Fast-App PCO

* 🤩 Streamlit App 


## 👽️ POC

### 🧑‍💻 Steps:

Open your terminal and navigate to the project directory.

   **Setting dolowload models** 
   
   🚨 To run the application, download the required model files from this Google Drive [link](https://drive.google.com/drive/folders/18rBBjrhTNR4eqVZpVhDtlPComDtRTceR?usp=sharing) and place them in the models/ directory.

   ```
   .
   ├── models/ <- 📂 Model files [.h5, .pkl, .pt] - pre-trained weight files, snapshots, checkpoints
      ├── vgg19_001/                  <- 📂 Model [.h5]
         ├── labels.json              <-  File [.json]
         ├── model.h5                 <-  File [.h5]
   ```
   
### 🐳 Docker

   ```
    * Docker is required to run the application. Follow these steps: 
    * Install Docker if it's not already installed on your system.
    * Navigate to the /app directory in the terminal.
   ```
   **Option 1 - 🐳 Docker build local**

   ```
      docker-compose up --build
   ```

   🚨 If you encounter issues building the image, it likely indicates that you are missing some essential system packages for building.

   **Option 2 - 🐳 Pull Image from [Docker](https://hub.docker.com/r/ddiazva312/object_classification)**
   ```
      docker pull ddiazva312/object_classification
   ```
   ```
      docker-compose up
   ```

### Fast-Api
```
http://localhost:8080/docs

```

<p align="center">
  <img src="docs/fastapi.jpg" alt="Sheet" style="width:100%">
</p>

### Streamlit
```
http://localhost:5000/
```

<div class="row">
  <div class="column">
    <p align="center">
      <img src="docs/streamlit.jpg" alt="Sheet" style="width:50%">
    </p>
  </div>
</div>

