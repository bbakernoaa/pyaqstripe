# PyAQSTripe

This is a simple python module to recreate the colormap found at the [AQ Stripes](https://airqualitystripes.info)

![image](https://cemac.github.io/airqualitystripes-plots/plots/Guatemala%20City,%20Guatemala_North_America_aq_stripes_withline_withindicativebar.png  )


## How to use

### Create a continuous colormap

```python
import pyaqstripe

cmap = pyaqstripe.create_aqstripe_cmap() 
```

### Create discrete colormap

```python
cmap = pyaqstripe.create_aqstripe_cmap(ncolors=14)
```
