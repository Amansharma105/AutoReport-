import matplotlib.pyplot as plt

def bar_chart(df, x, y):
    plt.bar(df[x], df[y])
    plt.show()

def line_chart(df, x, y):
    plt.plot(df[x], df[y])
    plt.show()

def pie_chart(df, column):
    df[column].value_counts().plot.pie()
    plt.show()

def scatter_chart(df, x, y):
    plt.scatter(df[x], df[y])
    plt.show()
