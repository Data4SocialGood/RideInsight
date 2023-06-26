# RideInsight 

## Introduction



## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a `Linux` machine.
* You have installed python 3 and mongodb.

## Necessary steps

In any situation you will have to follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/raniatze/Archimedes-OASA1-Project
```

2. Change into the project directory:

```bash
cd Archimedes-OASA1-Project
```

3. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

4. Create the starting database with all necessary data, except the AKE data.

```bash
sh makeDB.sh
```

## Running the Application

To run **RideInsight**, follow these steps, if you have the historical AKE data in your database:

1. Get the weather for the day:

```bash
python3 get_weather_today
```

2. Run the application:

```bash
cd App/
python3 app.py
```

## Preparing your AKE data for predictions

If you have your own AKE data like the file in Data/ake_sample.csv to make predictions you need to prepare it as show below:

1. If your file doesn't have headers run:

```bash
python3 addHeaders.py
```

2. Get historical weather data. Be sure to specify the correct time period in the code:

```bash
python3 get_weather.py
```

3. Process and enhance your AKE data with:

```bash
python3 process_ake.py
```

4. Insert your enhanced AKE data into your database:

```bash
python3 insertAKE.py
```

## Training the Machine Learning Model

If you wish to train the machine learning model yourself, follow these steps:

1. Prepare your AKE data as show above.

2. Prepare this data for training. You can change the number of previous stops and days by changing the **m** and **n** parameters. Also you must specify the line for which you prepeare the data by changing the **num_line_descr** value. This is done so you don't have to process it all at once.

```bash
python3 prepare_model_dataset.py
```

3. Train your model. Be sure to match **m**, **n** parameters with your data preparation. Also you can change the model, batch_size and number of epochs.

```bash
python3 train_model.py
```

## Contributing to Project Title

To contribute to **Project Title**, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin Archimedes-OASA1-Project
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact us, reach us at `archimedesai.gr/en/contact`.

## License

This project uses the following license: [license_name](<link_to_license>).
