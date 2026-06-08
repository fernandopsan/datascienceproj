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

## Project Structure

```text
.
├── README.md               <- The top-level README for developers using this project
├── Dockerfile              <- Docker image to run environment
├── config.yml              <- Configuration file
├── .gitignore              <- Git ignore file
├── data/
│   ├── INTERVALDATA.CSV    <- The original, immutable data dump
│   ├── interim/            <- Intermediate data that has been transformed
│   └── .gitignore
├── models/                 <- Trained models
├── notebooks/              <- Jupyter notebooks for exploration analysis
└── src/
    ├── preprocess/
    │   └── prepare_data.py
    ├── model/
    │   └── model.py
    ├── evaluate/
    │   └── evaluate.py
    ├── visualization/
    │   └── visualize.py
    └── common/
        └── tools.py
```
