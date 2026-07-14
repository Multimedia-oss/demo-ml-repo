losses = [1.0, 0.82, 0.65, 0.51, 0.39, 0.31]
accuracies = [0.42, 0.55, 0.66, 0.74, 0.81, 0.86]

for epoch, (loss, acc) in enumerate(zip(losses, accuracies), start=1):
    print(f"Epoch {epoch} loss={loss:.4f} accuracy={acc:.4f}")

# 使用纯 Python 生成 SVG 图片，不依赖 matplotlib
width = 600
height = 360
margin = 50

max_loss = max(losses)
min_loss = min(losses)

points = []
for i, loss in enumerate(losses):
    x = margin + i * (width - 2 * margin) / (len(losses) - 1)
    y = height - margin - (loss - min_loss) / (max_loss - min_loss) * (height - 2 * margin)
    points.append((x, y))

polyline = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)

circles = "\n".join(
    f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#1f77b4" />'
    for x, y in points
)

labels = "\n".join(
    f'<text x="{x:.1f}" y="{y - 12:.1f}" font-size="12" text-anchor="middle">{loss:.2f}</text>'
    for (x, y), loss in zip(points, losses)
)

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
  <rect width="100%" height="100%" fill="white"/>
  <text x="{width / 2}" y="30" font-size="22" text-anchor="middle" font-family="Arial">Training Loss Curve</text>

  <line x1="{margin}" y1="{height - margin}" x2="{width - margin}" y2="{height - margin}" stroke="black"/>
  <line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height - margin}" stroke="black"/>

  <text x="{width / 2}" y="{height - 10}" font-size="14" text-anchor="middle" font-family="Arial">Epoch</text>
  <text x="18" y="{height / 2}" font-size="14" text-anchor="middle" font-family="Arial" transform="rotate(-90 18,{height / 2})">Loss</text>

  <polyline points="{polyline}" fill="none" stroke="#1f77b4" stroke-width="3"/>
  {circles}
  {labels}
</svg>
'''

with open("loss_curve.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("Saved figure: loss_curve.svg")
