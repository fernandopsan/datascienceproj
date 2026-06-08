# Interval Data Analysis

## Requirements

 - Docker
 - Docker Compose

## Starting the application

In order to start the application you need to run the following command:

```bash
$ docker compose up --build -d
```

## Stopping the application

To stop the application, run the following command:

```bash
$ docker compose down
```

File Structure

.
├── README.md               <- The top-level README for developers using this project
├── Dockerfile              <- Docker image to run environment
├── config.yml              <- Configuration file
├── .gitignore              <- Git ignore file
├── data/                   <- Folder to store the CSV files
│   ├── INTERVALDATA.CSV    <- The original, immutable data dump
│   ├── interim/            <- Intermediate data that has been transformed
│   └── .gitignore          <- Git ignore file
├── models/                 <- Trained models
├── notebooks/              <- Jupyter notebooks for exploration analysis
└── src/                    <- Source code for use in this project
    ├── preprocess/         <- Scripts to turn raw data into features for modeling
    │   └── prepare_data.py
    ├── model/              <- Scripts to train models and apply models
    │   └── model.py
    ├── evaluate/           <- Scripts to validate and apply the model to data
    │   └── evaluate.py
    ├── visualization/      <- Scripts to create exploratory and results-oriented visualizations
    │   └── visualize.py
    └── common/             <- Scripts shared among other modules
        └── tools.py
