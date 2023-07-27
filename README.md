<p align="center">
  <img align="center" alt="DroneXtract logo" width="600" src="https://github.com/ANG13T/ClimaCast/blob/main/assets/ClimaCast.png">
</p>

## About
ClimaCast is a command-line tool written with Python that provides meteorology reports and forecasts, satellite pass predictions, communications decoding, and imagery analysis for NOAA satellites.

## Preview

<img alt="ClimaCast preview" width="400" src="https://github.com/ANG13T/ClimaCast/blob/main/assets/preview.png">

## Features
ClimaCast features four main features for NOAA satellite reconnaissance. They include the following:

### 🌦  Weather Forecasts and Alerts
Get up-to-date weather forecasts, data, and alerts from NOAA satellites. You can choose to get information via GPS coordinates, station ID, or area code. The retrieved data will be visualized and formatted in a table outline. 
The image below includes an example of a parsed forecasting report provided using an inputted GPS coordinate.

<img alt="Display" width="800" src="https://github.com/ANG13T/ClimaCast/blob/main/assets/display-3.png">

###  🛰  Pass Predictor
Predict radio or visual satellite passes of all NOAA satellites by inputting your GPS coordinates, altitude, and visibility.
Pass prediction data will be visualized and displayed in a table outline as shown below.

<img alt="Display" width="800" src="https://github.com/ANG13T/ClimaCast/blob/main/assets/display-4.png">

### 📡  APT Image Decoder
Decode NOAA satellite images by inputting audio MP3 files of satellite transmissions.
There is also a resampling feature to resample the file before decoding.
The output of the decoding is saved as a PNG file. An example output is displayed below.

<img alt="Display" height="300" src="https://github.com/ANG13T/ClimaCast/blob/main/assets/display-5.png">

### 🌎  Meteorological Image Analysis
Retrieve meterological images from the Sentinel-2 data collection for remote sensing analysis.
Thumbnail satellite images can be saved in the JPG format.
Remote raster data files (one per optical band, as acquired by the multi-spectral instrument) can be saved as a TIF file.

<img alt="Display" height="300" src="https://github.com/ANG13T/ClimaCast/blob/main/assets/display-1.png"> <img alt="Display" height="300" src="https://github.com/ANG13T/ClimaCast/blob/main/assets/display-2.png">

## Usage
The CLI will prompt for N2YO credentials if none are present in your environmental variables. Ensure to configure it as an environment variable.

Create an account at [**N2YO**](https://n2yo.com) and save the API key.

Ensure the N2YO API Key is configured in the `.env` file
```
N2YO_API=API_KEY_HERE
```

To run ClimaCast, you will need Python3 and Pip installed.

```bash
$ pip install -r requirements.txt
$ python3 climacast.py
```

### APIs Used
- [NOAA Weather Services](https://api.weather.gov): Retrieve Forecasts and Weather Details
- [N2YO](https://n2yo.com/api): Retrieve Satellite Pass Predictions
- [AWS Sentinel-2 Dataset](https://registry.opendata.aws/sentinel-2-l2a-cogs/): Retrieve Sentinel-2 Satellite Imagery

## Configuration
There are a set of environment variables utilized in ClimaCast. In order to set up the API and tailor the values for your specific meteorological research purposes, you can go to the `.env` file and adjust the following values:

`N2YO_API` N2YO API Key

`RESAMPLE_RATE` resampling number for satellite APT decoder

## Learning and Resources
To learn more about DJI drone digital forensics and the features of DroneXtract, refer to [this article](https://medium.com/@angelinatsuboi/a-comprehensive-guide-to-digital-forensics-with-dji-drones-fd7ef5af2891).

## Contributing
DroneXtract is open to any contributions. Please fork the repository and make a pull request with the features or fixes you want to be implemented.

## Upcoming
- DUML parser for firmware integrity checking
- DJI Flight Log TXT parsing for the parsing suite
- GEOJSON parsing output for SRT files in the steganography suite

## Support
If you enjoyed DroneXtract, please consider [becoming a sponsor](https://github.com/sponsors/ANG13T) in order to fund my future projects. 

To check out my other works, visit my [GitHub profile](https://github.com/ANG13T).

https://carpentries-incubator.github.io/geospatial-python/05-access-data/

- explain STAC and GEOTIFFs and TIFFs file format
