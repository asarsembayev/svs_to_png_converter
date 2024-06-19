# Data Convert

A Python script for converting data from svs format to {png, jpg}.

## Description

The `data_convert.py` script is designed to convert data from SVS format to raster images formats {png, jpeg, jpg}. It provides a simple and flexible interface through command line.

## Features

- Supports SVS input and png, jpeg output formats
- Easy-to-use command-line interface

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/your-username/data-convert.git
    ```
2. Install python virtual environment if necessary
    
    ```shell
    python -m venv {env_name}
    source {env_name}/bin/activate
    ```
3. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

To convert data using the `data_convert.py` script, follow these steps:

1. Prepare your input images in SVS format and put into an `src/` folder

2. Run the script with the appropriate command-line arguments:

    ```shell
    python data_convert.py src/ dst/
    ```

    Replace `<src/>` with the path to your folder containing input files, `<dst/>` an empty folder with the desired output path.

3. The converted data will be saved to the specified output folder path.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
