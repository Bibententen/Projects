# Customer clustering

A coursework notebook exploring customer segmentation with pandas, KMeans and agglomerative clustering.

## Files

- [47522003.ipynb](47522003.ipynb): exploration, clustering and summaries.
- [data.csv](data.csv): input data.
- [data legend.csv](data%20legend.csv): accompanying field legend.
- `BUSINESS REPORT.docx`: accompanying report.

## Opening the notebook

Start Jupyter from this folder and open `47522003.ipynb`. The input path is `data.csv`, matching the committed layout. The notebook imports pandas, scikit-learn, seaborn and matplotlib.

The path has been corrected from `data/data.csv`. This change alone does not establish compatibility with current package versions or a successful full run. The agglomerative clustering call uses the historical `affinity` parameter; validate the intended scikit-learn environment before changing it.

## What it demonstrates

- Reading and inspecting a CSV dataset.
- Fitting KMeans and agglomerative clustering models.
- Exploring cluster proportions and grouped customer characteristics.

## Next improvements

Record a clean run with tested package versions, add input schema checks, and document feature scaling choices before presenting clustering results as validated findings.

[Back to portfolio](../README.md)
