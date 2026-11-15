# Melbourne Airbnb price prediction

A team coursework project exploring Airbnb listing prices in Melbourne through data preparation and predictive modelling.

## My contribution

The [original notebook](BUSA8001-Group-Project-Final.ipynb) lists **Duy Pham — Task 2**. This section focuses on cleaning, categorical encoding and feature engineering. The wider notebook includes team contributions to initial analysis and modelling; those are not presented as my individual implementation.

## Repository contents

- `BUSA8001-Group-Project-Final.ipynb`: assignment context, data preparation and modelling code.
- `train.csv` and `test.csv`: committed input tables.
- `metaData.csv`: accompanying metadata.
- `submissionSVC.csv`: committed prediction output.
- `Project summary.docx`: accompanying report.

## Data preparation evidence

The notebook reads the train and test CSVs, adds a dataset-type flag, concatenates the tables and performs missing-value handling and categorical transformations. This provides a concrete example of Python data preparation within an analytical workflow.

## Reproducibility and limitations

Open the notebook with this folder as the working directory. It also references `sample_submission.csv`, which is not included. Retrieve the original authorized file or review whether that dependency can be removed; do not assume the committed prediction output is an equivalent input.

A clean end-to-end run and package versions have not been verified. Before reporting model metrics, review how preprocessing uses the combined train/test data and ensure fitted transformations do not leak evaluation information.

## Smallest useful engineering extension

Extract one cleaning step into a function with explicit inputs and outputs. Add schema and missing-value checks, test it with a small fixture, and document a reproducible command before expanding the project.

[Back to portfolio](../README.md)
