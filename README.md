# Signal Modulation with Interactive Widgets

This project is a signal modulation visualization tool built using Python. It allows users to generate and visualize modulated signals by adjusting various parameters such as the amplitude and frequency of the carrier and modulating signals, as well as the duration of the signal.

## Features

- **Signal Generation:**
  - Generate a modulated signal based on the input parameters.
  - Visualize the modulating signal and the resulting modulated signal.

- **Interactive Widgets:**
  - Adjust the amplitude and frequency of the modulating signal.
  - Modify the duration of the signal.
  - Real-time updates of the signal plot based on the changes in the input parameters.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- NumPy
- Matplotlib
- Ipywidgets
- IPython

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/signal-modulation.git
    cd signal-modulation
    ```

2. **Install the required Python packages:**

    ```bash
    pip install numpy matplotlib ipywidgets
    ```

3. **Run the Jupyter Notebook:**

    If you don't have Jupyter installed, you can install it using:

    ```bash
    pip install jupyter
    ```

    Then, start the Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

4. **Open the notebook:**

    In the Jupyter Notebook interface, open the `signal_modulation.ipynb` file to interact with the project.

## Usage

### Interactive Signal Modulation

- The interactive widgets allow you to adjust the following parameters:
  - **Amplitude of Modulating Signal (A_m):** Adjust the amplitude of the modulating signal.
  - **Frequency of Modulating Signal (f_m):** Adjust the frequency of the modulating signal.
  - **Duration:** Set the duration of the signal.
  
- The plots will update in real-time based on the selected parameters, showing the modulating signal and the generated modulated signal.

## Project Structure

- `README.md`: This README file.
- `cos2.py`: This file programm

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
