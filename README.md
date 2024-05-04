# Computational Compositions

This project explores the capability of Long Short-Term Memory (LSTM) networks in generating MIDI music by training on diverse genres like classical and jazz. It leverages LSTM's potential to model temporal sequences to produce coherent piano melodies and chords.

## Project Structure

The project includes several Jupyter notebooks and Python scripts, each corresponding to different phases and experiments of the research:

- `final_project.ipynb`: Base model training on the MAESTRO dataset.
- `final_project-rests.ipynb`: Model training including rests and note durations.
- `final_project-rests-penalty.ipynb`: Model training with penalized rest predictions.
- `final_project-rests-penalty-jazz.ipynb`: Training on the PiJAMA jazz dataset.
- `loss_graph_gen/generate_loss_graph....py`: Scripts to extract and plot loss data from the training logs.

## Datasets
There is sample data in the directories `pijama_jazz` and `maestro_v3_2013`, but the full data is available below:
- **MAESTRO (MIDI and Audio Edited for Synchronous TRacks and Organization)**: Contains over 200 hours of virtuoso piano performances. Available [here](https://magenta.tensorflow.org/datasets/maestro).
- **PiJAMA (Piano Jazz with Automadic MIDI Annotations)**: Focuses on jazz genres and provides a different stylistic challenge. Available [here](https://transactions.ismir.net/articles/10.5334/tismir.162).

## Getting Started

To reproduce the results of this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
2. **Instal Dependencies
3. **Download and Prepare the Data
   Download the full datasets from the provided links and put them in the folders, with structure given by this repo.
4. **Run the Notebooks
   Open one of the `.ipynb` and run the cells until you get to the training cell, which calls the function `train_model`. This is the cell to run to train the model. All cells under the `predict.py` section are for prediction, and the last cell of the entire notebook will generate a MIDI file.
