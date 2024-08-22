# Multidimensional Wilcoxon Mann Whitney U Test

This test aims to give a score that represents how well two sets of multidimensional points are separated. For each point $x$ of a given set, create the distance rankings to all other points and compute the statistic:

$$   U_x= \frac{\max(R_{1}-{n_{1}(n_{1}+1) \over 2}, R_{2}-{n_{2}(n_{2}+1) \over 2})}{n_1 n_2}$$

where $R_1$ is the sum of the rankings for the $n_1$ points of the same set as $x$, and $R_2$ is the sum of the rankings for the $n_2$ points of a different set than $x$. This statistic increases when the points of the same set as $x$ are closer to $x$ than the points the other set. Finally, we compute the mean of $U_x$ for all the points $x$, which we will call $AvgU$. This statistic lies in the range $0.5 - 1$, and the univariate WMW is equivalent to the AUC. The computation of the presented statistic is a variant of the multivariate statistic presented in [1].

[1] Liu, J., Ma, S., Xu, W., & Zhu, L. (2022). A generalized Wilcoxon–Mann–Whitney type test for multivariate data through pairwise distance. Journal of Multivariate Analysis, 190, 104946.

## Demo
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/habla-liaa/multidimensional-wilcoxon-mann-whitney/blob/main/example/Demo.ipynb)


## Install
```bash
pip install multidimensional-wilcoxon-mann-whitney
```

## Usage
```python
from multidimensional_wilcoxon_mann_whitney import multidimensional_ranksum

## Cite

```
@inproceedings{riera2023phone,
  title={Phone and speaker spatial organization in self-supervised speech representations},
  author={Riera, Pablo and Cerdeiro, Manuela and Pepino, Leonardo and Ferrer, Luciana},
  booktitle={2023 IEEE International Conference on Acoustics, Speech, and Signal Processing Workshops (ICASSPW)},
  pages={1--5},
  year={2023},
  organization={IEEE}
}
```

U = multidimensional_ranksum(X,y)
```
