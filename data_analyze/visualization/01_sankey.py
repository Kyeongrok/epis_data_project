import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["서울", "대전", "대구", "B2", "C1"],
      color = "blue"
    ),
    link = dict(
      source = [0, 0, 1], # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = [1, 2, 0],
      value = [1, 4, 5]
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()