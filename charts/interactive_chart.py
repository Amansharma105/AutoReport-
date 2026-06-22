import plotly.express as px

def interactive_bar_chart():
    departments = ["IT", "HR", "Finance"]
    employees = [2, 2, 1]

    fig = px.bar(
        x=departments,
        y=employees,
        labels={"x": "Department", "y": "Employees"},
        title="Employee Distribution"
    )

    fig.write_html("reports/interactive_chart.html")
