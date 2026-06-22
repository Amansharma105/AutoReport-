import matplotlib.pyplot as plt

def bar_chart(labels, values):
    plt.bar(labels, values)
    plt.xlabel("Department")
    plt.ylabel("Count")
    plt.title("Department Chart")
    plt.savefig("charts/bar_chart.png")
    plt.close()

def pie_chart(labels, values):
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Department Distribution")
    plt.savefig("charts/pie_chart.png")
    plt.close()
