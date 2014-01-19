import numpy as np
from statsmodels.graphics.dotplots import dotplot
import pandas as pd

try:
    import matplotlib.pyplot as plt
    import matplotlib
    from matplotlib.backends.backend_pdf import PdfPages
    if matplotlib.__version__ < '1':
        raise
    have_matplotlib = True
except:
    have_matplotlib = False

def test_all():

    pdf = PdfPages("test_dotplot.pdf")

    plt.clf()

    # Basic dotplot with points only
    points = range(20)
    ax = plt.axes()
    fig = dotplot(points, ax=ax)
    ax.set_title("Basic horizontal dotplot")
    pdf.savefig(facecolor="yellow")

    # Basic vertical dotplot
    plt.clf()
    points = range(20)
    ax = plt.axes()
    fig = dotplot(points, ax=ax, horizontal=False)
    ax.set_title("Basic vertical dotplot")
    pdf.savefig(facecolor="yellow")

    # Tall and skinny
    plt.figure(figsize=(4,12))
    ax = plt.axes()
    vals = np.arange(40)
    dotplot(points, ax=ax)
    ax.set_title("Tall and skinny dotplot")
    ax.set_xlabel("x axis label")
    pdf.savefig()

    # Short and wide
    plt.figure(figsize=(12,4))
    ax = plt.axes()
    vals = np.arange(40)
    dotplot(points, ax=ax, horizontal=False)
    ax.set_title("Short and wide dotplot")
    ax.set_ylabel("y axis label")
    pdf.savefig()

    # Tall and skinny striped dotplot
    plt.figure(figsize=(4,12))
    ax = plt.axes()
    points = np.arange(40)
    dotplot(points, ax=ax, striped=True)
    ax.set_title("Tall and skinny striped dotplot")
    ax.set_xlim(-10, 50)
    pdf.savefig()

    # Short and wide striped
    plt.figure(figsize=(12,4))
    ax = plt.axes()
    points = np.arange(40)
    dotplot(points, ax=ax, striped=True, horizontal=False)
    ax.set_title("Short and wide striped dotplot")
    ax.set_ylim(-10, 50)
    pdf.savefig()

    # Basic dotplot with few points
    plt.figure()
    ax = plt.axes()
    points = np.arange(4)
    dotplot(points, ax=ax)
    ax.set_title("Basic horizontal dotplot with few lines")
    pdf.savefig()

    # Basic dotplot with few points
    plt.figure()
    ax = plt.axes()
    points = np.arange(4)
    dotplot(points, ax=ax, horizontal=False)
    ax.set_title("Basic vertical dotplot with few lines")
    pdf.savefig()

    # Manually set the x axis limits
    plt.figure()
    ax = plt.axes()
    points = np.arange(20)
    dotplot(points, ax=ax)
    ax.set_xlim(-10, 30)
    ax.set_title("Dotplot with adjusted horizontal range")
    pdf.savefig()

    # Left row labels
    plt.clf()
    ax = plt.axes()
    lines = ["ABCDEFGH"[np.random.randint(0, 8)] for k in range(20)]
    points = np.random.normal(size=20)
    dotplot(points, lines=lines, ax=ax)
    ax.set_title("Dotplot with user-supplied labels in the left margin")
    pdf.savefig()

    # Left and right row labels
    plt.clf()
    ax = plt.axes()
    points = np.random.normal(size=20)
    lines = ["ABCDEFGH"[np.random.randint(0, 8)] + "::" + str(k+1)
             for k in range(20)]
    dotplot(points, lines=lines, ax=ax, split_names="::")
    ax.set_title("Dotplot with user-supplied labels in both margins")
    pdf.savefig()

    # Both sides row labels
    plt.clf()
    ax = plt.axes([0.1, 0.1, 0.88, 0.8])
    points = np.random.normal(size=20)
    lines = ["ABCDEFGH"[np.random.randint(0, 8)] + "::" + str(k+1)
             for k in range(20)]
    dotplot(points, lines=lines, ax=ax, split_names="::",
            horizontal=False)
    txt = ax.set_title("Vertical dotplot with user-supplied labels in both margins")
    txt.set_position((0.5, 1.06))
    pdf.savefig()

    # Custom colors and symbols
    plt.clf()
    ax = plt.axes([0.1, 0.07, 0.78, 0.85])
    points = np.random.normal(size=20)
    lines = np.kron(range(5), np.ones(4)).astype(np.int32)
    styles = np.kron(np.ones(5), range(4)).astype(np.int32)
    marker_props = {k: {"color": "rgbc"[k], "marker": "osvp"[k],
                        "ms": 7, "alpha": 0.6} for k in range(4)}
    dotplot(points, lines=lines, styles=styles, ax=ax,
            marker_props=marker_props)
    ax.set_title("Dotplot with custom colors and symbols")
    pdf.savefig()

    # Basic dotplot with symmetric intervals
    plt.clf()
    ax = plt.axes()
    points = range(20)
    dotplot(points, intervals=np.ones(20), ax=ax)
    ax.set_title("Dotplot with symmetric intervals")
    pdf.savefig()

    # Basic dotplot with symmetric intervals, pandas inputs.
    plt.clf()
    ax = plt.axes()
    points = pd.Series(range(20))
    intervals = pd.Series(np.ones(20))
    dotplot(points, intervals=intervals, ax=ax)
    ax.set_title("Dotplot with symmetric intervals (Pandas inputs)")
    pdf.savefig()

    # Basic dotplot with nonsymmetric intervals
    plt.clf()
    ax = plt.axes()
    points = np.arange(20)
    intervals = [(1, 3) for i in range(20)]
    dotplot(points, intervals=intervals, ax=ax)
    ax.set_title("Dotplot with nonsymmetric intervals")
    pdf.savefig()

    # Vertical dotplot with nonsymmetric intervals
    plt.clf()
    ax = plt.axes()
    points = np.arange(20)
    intervals = [(1, 3) for i in range(20)]
    dotplot(points, intervals=intervals, ax=ax, horizontal=False)
    ax.set_title("Vertical dotplot with nonsymmetric intervals")
    pdf.savefig()

    # Dotplot with nonsymmetric intervals, adjust line properties
    plt.clf()
    ax = plt.axes()
    points = np.arange(20)
    intervals = [(1, 3) for x in range(20)]
    line_props = {0: {"color": "lightgrey",
                      "solid_capstyle": "round"}}
    dotplot(points, intervals=intervals, line_props=line_props, ax=ax)
    ax.set_title("Dotplot with custom line properties")
    pdf.savefig()

    # Dotplot with two points per line and a legend
    plt.clf()
    ax = plt.axes([0.1, 0.1, 0.75, 0.8])
    points = 5*np.random.normal(size=40)
    lines = np.kron(range(20), (1,1))
    intervals = [(1,3) for k in range(40)]
    styles = np.kron(np.ones(20), (0,1)).astype(np.int32)
    styles = [["Cat", "Dog"][i] for i in styles]
    dotplot(points, intervals=intervals, lines=lines, styles=styles,
            ax=ax, stacked=True)
    handles, labels = ax.get_legend_handles_labels()
    leg = plt.figlegend(handles, labels, "center right", numpoints=1,
                        handletextpad=0.0001)
    leg.draw_frame(False)
    ax.set_title("Dotplot with two points per line")
    pdf.savefig()

    # Vertical dotplot with two points per line and a legend
    plt.clf()
    ax = plt.axes([0.1, 0.1, 0.75, 0.8])
    points = 5*np.random.normal(size=40)
    lines = np.kron(range(20), (1,1))
    intervals = [(1,3) for k in range(40)]
    styles = np.kron(np.ones(20), (0,1)).astype(np.int32)
    styles = [["Cat", "Dog"][i] for i in styles]
    dotplot(points, intervals=intervals, lines=lines, styles=styles,
            ax=ax, stacked=True, horizontal=False)
    handles, labels = ax.get_legend_handles_labels()
    leg = plt.figlegend(handles, labels, "center right", numpoints=1,
                        handletextpad=0.0001)
    leg.draw_frame(False)
    ax.set_title("Vertical dotplot with two points per line")
    pdf.savefig()

    # Vertical dotplot with two points per line and a legend
    plt.clf()
    ax = plt.axes([0.1, 0.1, 0.75, 0.8])
    points = 5*np.random.normal(size=40)
    lines = np.kron(range(20), (1,1))
    intervals = [(1,3) for k in range(40)]
    styles = np.kron(np.ones(20), (0,1)).astype(np.int32)
    styles = [["Cat", "Dog"][i] for i in styles]
    dotplot(points, intervals=intervals, lines=lines, styles=styles,
            ax=ax, stacked=True, striped=True, horizontal=False)
    handles, labels = ax.get_legend_handles_labels()
    leg = plt.figlegend(handles, labels, "center right", numpoints=1,
                        handletextpad=0.0001)
    leg.draw_frame(False)
    plt.ylim(-20, 20)
    ax.set_title("Vertical dotplot with two points per line")
    pdf.savefig()

    # Dotplot with color-matched points and intervals
    plt.clf()
    ax = plt.axes([0.1, 0.1, 0.75, 0.8])
    points = 5*np.random.normal(size=40)
    lines = np.kron(range(20), (1,1))
    intervals = [(1,3) for k in range(40)]
    styles = np.kron(np.ones(20), (0,1)).astype(np.int32)
    styles = [["Cat", "Dog"][i] for i in styles]
    marker_props = {"Cat": {"color": "orange"},
                    "Dog": {"color": "purple"}}
    line_props = {"Cat": {"color": "orange"},
                  "Dog": {"color": "purple"}}
    dotplot(points, intervals=intervals, lines=lines, styles=styles,
            ax=ax, stacked=True, marker_props=marker_props,
            line_props=line_props)
    handles, labels = ax.get_legend_handles_labels()
    leg = plt.figlegend(handles, labels, "center right", numpoints=1,
                        handletextpad=0.0001)
    leg.draw_frame(False)
    ax.set_title("Dotplot with color-matched points and intervals")
    pdf.savefig()

    # Dotplot with color-matched points and intervals
    plt.clf()
    ax = plt.axes([0.1, 0.1, 0.75, 0.8])
    points = 5*np.random.normal(size=40)
    lines = np.kron(range(20), (1,1))
    intervals = [(1,3) for k in range(40)]
    styles = np.kron(np.ones(20), (0,1)).astype(np.int32)
    styles = [["Cat", "Dog"][i] for i in styles]
    marker_props = {"Cat": {"color": "orange"},
                    "Dog": {"color": "purple"}}
    line_props = {"Cat": {"color": "orange"},
                  "Dog": {"color": "purple"}}
    dotplot(points, intervals=intervals, lines=lines, styles=styles,
            ax=ax, stacked=True, marker_props=marker_props,
            line_props=line_props, horizontal=False)
    handles, labels = ax.get_legend_handles_labels()
    leg = plt.figlegend(handles, labels, "center right", numpoints=1,
                        handletextpad=0.0001)
    leg.draw_frame(False)
    ax.set_title("Dotplot with color-matched points and intervals")
    pdf.savefig()

    # Dotplot with sections
    plt.clf()
    ax = plt.axes()
    points = range(30)
    lines = np.kron(range(15), (1,1)).astype(np.int32)
    styles = np.kron(np.ones(15), (0,1)).astype(np.int32)
    sections = np.kron((0,1,2), np.ones(10)).astype(np.int32)
    sections = [["Axx", "Byy", "Czz"][k] for k in sections]
    dotplot(points, lines=lines, styles=styles, sections=sections, ax=ax)
    ax.set_title("Dotplot with sections")
    pdf.savefig()

    # Vertical dotplot with sections
    plt.clf()
    ax = plt.axes([0.1,0.1,0.9,0.75])
    points = range(30)
    lines = np.kron(range(15), (1,1)).astype(np.int32)
    styles = np.kron(np.ones(15), (0,1)).astype(np.int32)
    sections = np.kron((0,1,2), np.ones(10)).astype(np.int32)
    sections = [["Axx", "Byy", "Czz"][k] for k in sections]
    dotplot(points, lines=lines, styles=styles, sections=sections, ax=ax,
            horizontal=False)
    txt = ax.set_title("Vertical dotplot with sections")
    txt.set_position((0.5, 1.08))
    pdf.savefig()

    # Reorder sections
    plt.clf()
    ax = plt.axes()
    points = range(30)
    lines = np.kron(range(15), (1,1)).astype(np.int32)
    styles = np.kron(np.ones(15), (0,1)).astype(np.int32)
    sections = np.kron((0,1,2), np.ones(10)).astype(np.int32)
    sections = [["Axx", "Byy", "Czz"][k] for k in sections]
    dotplot(points, lines=lines, styles=styles, sections=sections, ax=ax,
            section_order=["Byy", "Axx", "Czz"])
    ax.set_title("Dotplot with sections in specified order")
    pdf.savefig()

    # Reorder the lines.
    plt.figure()
    ax = plt.axes()
    points = np.arange(4)
    lines = ["A", "B", "C", "D"]
    line_order = ["B", "C", "A", "D"]
    dotplot(points, lines=lines, line_order=line_order, ax=ax)
    ax.set_title("Dotplot with reordered lines")
    pdf.savefig()

    # Dotplot with different numbers of points per line
    plt.clf()
    ax = plt.axes([0.1, 0.1, 0.75, 0.8])
    points = 5*np.random.normal(size=40)
    lines = []
    ii = 0
    while len(lines) < 40:
        for k in range(np.random.randint(1, 4)):
            lines.append(ii)
        ii += 1
    styles = np.kron(np.ones(20), (0,1)).astype(np.int32)
    styles = [["Cat", "Dog"][i] for i in styles]
    dotplot(points, lines=lines, styles=styles,
            ax=ax, stacked=True)
    handles, labels = ax.get_legend_handles_labels()
    leg = plt.figlegend(handles, labels, "center right", numpoints=1,
                        handletextpad=0.0001)
    leg.draw_frame(False)
    ax.set_title("Dotplot with different numbers of points per line")
    pdf.savefig()

    pdf.close()


#test_all()
