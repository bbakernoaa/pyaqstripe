import numpy as np

aqstripes_rgb_colors = np.array(
    object=[
        [255, 255, 255],
        [164, 255, 254],
        [175, 218, 233],
        [176, 205, 237],
        [249, 224, 71],
        [241, 200, 75],
        [241, 166, 64],
        [233, 136, 37],
        [176, 69, 84],
        [134, 59, 71],
        [103, 59, 62],
        [70, 47, 48],
        [36, 36, 36],
    ]
)


def create_matplotlib_colorbar(ncolors=14, continuous=True, show=False):
    """
    Create a matplotlib colorbar with AQSTripes colors.

    Parameters
    ----------
    ncolors : int, optional
        Number of discrete colors in the colorbar if continuous=False.
        Default is 14.
    continuous : bool, optional
        If True, create a continuous colorbar. Otherwise, create a discrete
        colorbar. Default is True.
    show : bool, optional
        If True, show the colorbar. Otherwise, return the colorbar as a
        Matplotlib.colors.LinearSegmentedColormap object. Default is False.

    Returns
    -------
    cmap : Matplotlib.colors.LinearSegmentedColormap, optional
        If show=False, return the colorbar as a
        Matplotlib.colors.LinearSegmentedColormap object.
    """
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap

    if continuous:
        cmap = LinearSegmentedColormap.from_list(
            name="aqstripes", colors=aqstripes_rgb_colors / 255.0
        )
        if show:
            plt.imshow([np.linspace(0, 1, 256)], aspect="auto", cmap=cmap)
            plt.colorbar()
            plt.show()
    else:
        cmap = LinearSegmentedColormap.from_list(
            "aqstripes", aqstripes_rgb_colors / 255.0, N=ncolors
        )
        bounds = np.linspace(0, 1, ncolors + 1)
        norm = plt.Normalize(vmin=0, vmax=1)
        if show:
            plt.imshow(
                [np.linspace(0, 1, ncolors)],
                aspect="auto",
                cmap=cmap,
                norm=norm,
            )
            plt.colorbar(ticks=bounds)
            plt.show()
    if not show:
        return cmap


def create_bokeh_colorbar(continuous=True, ncolors=13, show=False):
    """
    Create a Bokeh colorbar with AQSTripes colors.

    Parameters
    ----------
    continuous : bool, optional
        If True, create a continuous colorbar. Otherwise, create a discrete
        colorbar. Default is True.
    ncolors : int, optional
        Number of discrete colors in the colorbar if continuous=False.
        Default is 13.
    show : bool, optional
        If True, show the colorbar. Otherwise, return the colorbar as a
        Bokeh.models.ColorBar object. Default is False.

    Returns
    -------
    color_bar : Bokeh.models.ColorBar, optional
        If show=False, return the colorbar as a Bokeh.models.ColorBar object.
    """
    from bokeh.io import output_notebook
    from bokeh.models import ColorBar, LinearColorMapper
    from bokeh.plotting import figure, show

    output_notebook()

    if continuous:
        mapper = LinearColorMapper(
            palette=[f"#{r:02x}{g:02x}{b:02x}" for r, g, b in aqstripes_rgb_colors],
            low=0,
            high=1,
        )
        color_bar = ColorBar(
            color_mapper=mapper, width=500, height=20, orientation="horizontal"
        )
    else:
        mapper = LinearColorMapper(
            palette=[f"#{r:02x}{g:02x}{b:02x}" for r, g, b in aqstripes_rgb_colors],
            low=0,
            high=len(aqstripes_rgb_colors),
        )
        color_bar = ColorBar(
            color_mapper=mapper,
            width=500,
            height=20,
            orientation="horizontal",
            major_label_overrides={i: str(i) for i in range(len(aqstripes_rgb_colors))},
        )

    p = figure(
        plot_width=600,
        plot_height=100,
        toolbar_location=None,
        min_border=0,
        outline_line_color=None,
    )
    p.add_layout(color_bar, "below")
    show(p)
