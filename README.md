Project Name
==============================

This project is a starting Pack for MLOps projects based on the subject "movie_recommandation". It's not perfect so feel free to make some modifications on it.

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── logs               <- Logs from training and predicting
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling, to run the API and the API tests
    │   │   └── build_features.py       # by default
    │   │   └── ee_stream7.py           # UI
    │   │   └── jr_preprocessing.py     # Data Preprocessing
    │   │   └── login_predict_jr.py     # API (login, predict the attendance time)
    │   │   └── test_api4_.py           # test of the API
    │   │   └── test_api_containerd.py  # test of the API in the containerized context       
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py            # by default, not used
    │   │   └── train_model.py              # by default, not used
    │   │   └── lh_ee_xgbootmodel1_c01.py   # training and saving the the model, in containeritźed context
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py            # by default, not used.
    │   └── config         <- Describe the parameters used in train_model.py and predict_model.py
    │  
    ├── tests                <- tests scripts (preprocessing and training)
    │   └── lh_model_evaluation_test_exec.py        # execution of unit tests and retrieval of the standard output for the log file 
    │   └── lh_model_evaluation_test.py             # functions of the model test
    │   └── lh_model_evaluation.py                  # library for the test of the new model
    │   └── test_jr_preprossing.py                  # test of the preprocessing
    |── [Files used to build images (Dockerfile, and shell scripts...), to run images (YAML files for Docker Compose, and shell scripts)]       # UI
--------

Procedure make the system work


I. Setup of the system

#Build the 2 Docker images for respectively : the preprocessing and the preprocessing tests
./lh_setup_preprocessing_all.sh

#Build the Docker image for the training of the model
./lh_setup_training.sh

#Build the Docker image for the test of the model and its management according to F2-score and
#accuracy
./lh_setup_model_test.sh

#Build 3 Docker inages for respectively : the API, the Streamlit UI and the API tests
./lh_setup_api.sh


II. Run of the system

#run the data preprocessing and the tests
./lh_exec_preprocessing_all.sh

#run the training of the model with newly processed data
./lh_exec_training.sh

#run the test of the model and the handling of it, according to F2-score and accuracy.
./lh_exec_model_test.sh

#run of the API, the streamlit and the API tests
./lh_exec_api.sh



<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
