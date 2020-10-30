import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')


def one_dim_scatterplot(data, ax, jitter=0.2, **options):

    """
    Creates a 1D scatter plot with jitter. Useful to explore
    distribution of research funding per relationship. Largely based on
    example from Galvanize Data Science Immersive lecture:

    Parameters
    ----------
    data : array like (1D)
    ax : Axes
    jitter : float
    **options
        other options for plotting from matplotlib

    Returns
    -------
    plot
    """

    if jitter:
        jitter = np.random.uniform(-jitter, jitter, size=data.shape)
    else:
        jitter = np.repeat(0.0, len(data))
    ax.scatter(data, jitter, **options)
    ax.yaxis.set_ticklabels([])
    ax.set_ylim([-1, 1])
    ax.tick_params(axis='both', which='major', labelsize=15)


def stacked_bars(df, ax):

    """
    Creates a stacked barchart for product funding. Useful to explore
    dependnce in product focused research funding. Largely based on
    example on The Python Graph Gallery written by Oliver Gaudard
    availabled at:
    https://python-graph-gallery.com/12-stacked-barplot-with-matplotlib/

    Parameters
    ----------
    df : DataFrame
        what data you want to observe dependencies in 

    Returns
    -------
    plot
    """
    
    # Values of each part of the stack
    biobar = [
        df.loc[(df.Biological_Related == True)
        & (df.Drug_Related == False)
        & (df.Device_Related == False)
        ].Total_Amount_of_Payment_USDollars.sum(),
        df.loc[(df.Biological_Related == True)
        & (df.Drug_Related == True)
        & (df.Device_Related == False)
        ].Total_Amount_of_Payment_USDollars.sum(),
        df.loc[(df.Biological_Related == True)
        & (df.Drug_Related == False)
        & (df.Device_Related == True)
        ].Total_Amount_of_Payment_USDollars.sum()
    ]
    drugbar = [
        df.loc[(df.Biological_Related == True)
        & (df.Drug_Related == True)
        & (df.Device_Related == False)
        ].Total_Amount_of_Payment_USDollars.sum(),
        df.loc[(df.Biological_Related == False)
        & (df.Drug_Related == True)
        & (df.Device_Related == False)
        ].Total_Amount_of_Payment_USDollars.sum(),
        df.loc[(df.Biological_Related == False)
        & (df.Drug_Related == True)
        & (df.Device_Related == True)
        ].Total_Amount_of_Payment_USDollars.sum()
    ]
    devicebar = [
        df.loc[(df.Biological_Related == True)
        & (df.Drug_Related == False)
        & (df.Device_Related == True)
        ].Total_Amount_of_Payment_USDollars.sum(),
        df.loc[(df.Biological_Related == False)
        & (df.Drug_Related == True)
        & (df.Device_Related == True)
        ].Total_Amount_of_Payment_USDollars.sum(),
        df.loc[(df.Biological_Related == False)
        & (df.Drug_Related == False)
        & (df.Device_Related == True)
        ].Total_Amount_of_Payment_USDollars.sum()
    ]
    
    # set bottom for devices
    bars = np.add(biobar, drugbar).tolist()
    position = [0,1,2]
    names = ['Biological Related', 'Drug Related', 'Device Related']
    barWidth = .8
    
    # stack 'em
    bb = plt.bar(position, biobar, color='#735f7f', edgecolor='white',
        width=barWidth)
    drb = plt.bar(position, drugbar, bottom=biobar, color='#402294',
        edgecolor='white', width=barWidth)
    deb = plt.bar(position, devicebar, bottom=bars, color='#206b80',
        edgecolor='white', width=barWidth)

    # complete formatting, show
    plt.xticks(position, names, fontweight='bold')
    plt.xlabel("Product Research Category")
    plt.ylabel("Funding Recieved Billions USD")
    plt.title("Overlap in Funding", fontsize=16, fontweight='bold')
    ax.legend([bb, drb, deb], ['Biological', 'Drug', 'Device'])
    plt.show()
