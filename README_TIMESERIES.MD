## Table of Contents

- [Resources](#resources)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Prepare run time series notebooks](#prepare-run-time-series-notebooks)
  - [Extraction data sample from raw data](#extraction-data-sample-from-raw-data)
  - [Prepare data for modeling notebook](#prepare-data-for-modeling-notebook)
  - [Exploratory data analysis notebook](#exploratory-data-analysis-notebook)
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

Environmental dependency is always complicated, While using the above command stumble on errors like 
  - Version not found
  - No suitable version available

In this case, install packages independently by running the following commands 

```bash
conda create -n myenv python pandas numpy matplotlib seaborn scipy scikit-learn jupyter tensorflow keras pytorch
```

```bash
conda activate myenv
```

If the environment is already created then just run the command of activate that environment.

After completion of the above steps, the environment is ready to execute the code.



### Prepare run time series notebooks

The environment is ready to compile the code, but you need to move to the directory where the notebook are located.

In our case to compile the run-test code 

```bash
cd notebooks
```

### Extraction data sample from raw data

```bash
papermill mmap-3.ipynb output_mmap-3.ipynb -p parent_dir_param "os.path.abspath(r'../data/')"
```

### Prepare data for modeling notebook

```bash
papermill mmap3-1.ipynb output_mmap3-1.ipynb -p parent_dir_param "os.path.abspath(r'../data/')"
```


### Exploratory data analysis notebook

```bash
papermill mmap-3-2.ipynb output_mmap-3-2.ipynb -p parent_dir_param "os.path.abspath(r'../data/')"
```

### ML Modeling notebook

```bash
papermill mmap-3-3.ipynb output_mmap-3-3.ipynb -p parent_dir_param "os.path.abspath(r'../data/')"
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



   


