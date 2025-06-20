## Table of Contents

- [Resources](#resources)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Prepare run notebooks Statistical ML modeling](#prepare-run-notebooks-statistical-ml-modeling)
  - [Statistical data from raw data notebook](#statistical-data-from-raw-data-notebook)
  - [Features-Labels addition notebook](#features-labels-addition-notebook)
  - [ML Modeling notebook](#ml-modeling-notebook)
  - [Best Model notebook](#best-model-notebook)
  - [FAQs](#faqs)




## Resources

- [Slides](https://docs.google.com/presentation/d/13ZlI3FTh6VrviMzwRgV2q84-8SF6G69ucPowO5hfIeQ/edit?usp=sharing)
- [Performance Table](https://docs.google.com/spreadsheets/d/1LKn9JhQg9fdud49Y8hydikn2-QYBbj0hfzsUkexK8Dk/edit?usp=sharing)


## Getting Started

#### Clone a repository using VS Code

- Clone repository with HTTPS
- Open Terminal in VS code and copy/past following link into VS Terminal

```bash
git clone https://git.informatik.uni-rostock.de/bckrlab/theses/master/2023_musa-kaleem_martin.git
```

### Prerequisites

You can create your Conda environment using the following command in your terminal:

  - python =>3.10.6 <=3.11.1
```bash

conda env create -f environment.yml
```
After creating the environment, you can activate it using the following command:

```bash
conda activate my_env
```

If the environment is already created then just run the command of activate that environment but you should be in the clone repository directory before run the command of activate environment.

After completion of the above steps, the environment is ready to execute the code.



### Prepare run notebooks Statistical ML modeling

The environment is ready to compile the code, but you need to move to the directory where the notebook are located.

In our case to compile the run-test code 

```bash
cd notebooks
```

### Statistical data from raw data notebook

```bash
papermill 0007_Data_Extraction_Raw_Pipe.ipynb output_dataext_notebook.ipynb -p parent_dir_param "os.path.abspath(r'../data/')"
```

### Features-Labels addition notebook

```bash
papermill 0008_Data_Features_Pipe.ipynb output_features_notebook.ipynb
```


### ML Modeling notebook

```bash
papermill 0010_Data_Modeling_Pipe.ipynb output_modeling_notebook.ipynb
```

### Best Model notebook

In the tree-based model **Catboost** outperform all other models  

- All models are located at the **models** folder in gitLab repository

```bash
cd models
```
- This model performs well for all main labels/targets and outperforms all other models without any tunning. 
- According to research tree-based models perform better on tabular data than neural networks.

```bash
papermill 0009_Model_WYT_CAT.ipynb output_catmodel_notebook.ipynb -p parent_dir_param "os.path.abspath(r'../data/')"
```

  #### Best Model For **yaw_error_mean** with HP (Tree-based)

  ```bash
  papermill 0026_Model_Y_CAT_BEST_HPT.ipynb output_model_y_cat.ipynb -p parent_dir_param "os.path.abspath(r'../data/')"
  ```

  #### Best Model For **yaw_error_mean** with HP (neural based)


  ```bash
  papermill 0027_Model_Y_NN_BEST_HPT.ipynb output_model_y_nn.ipynb -p parent_dir_param "os.path.abspath(r'../data/')"
  ```










### FAQs


###### What if raw data in different directory?

 In the case of raw data located in different location, 

**For example:**
 ```bash
    parent_dir_param "os.path.abspath(r'../data/')"
 ```
 to this

 ```bash
    parent_dir_param "r'../data/'"
 ```
 


###### What if there is a buffer error while compiling Statistical data from raw data notebook?

 In the case of buffer error while compiling **read_int** method in notebook.
 Try different filetype in **read_int** method eg.

 ```bash
 filetype = np.frombuffer(f.read(4),dtype=np.uint)
 ```
 Or

```bash
filetype = np.frombuffer(f.read(4), dtype=np.uint32)
```



   


