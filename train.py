groups = [
    {
        "name": "baseline",
        "loss": 0.82,
        "accuracy": 0.70,
    },
    {
        "name": "method_a",
        "loss": 0.51,
        "accuracy": 0.82,
    },
    {
        "name": "method_b",
        "loss": 0.31,
        "accuracy": 0.86,
    },
]


def generate_svg(filename, title, loss, accuracy):
    width = 500
    height = 300

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
  <rect width="100%" height="100%" fill="white"/>
  <text x="250" y="45" font-size="24" text-anchor="middle" font-family="Arial">{title}</text>

  <rect x="100" y="90" width="{300 * accuracy:.1f}" height="45" fill="#1f77b4"/>
  <text x="100" y="82" font-size="16" font-family="Arial">Accuracy = {accuracy:.2f}</text>

  <rect x="100" y="190" width="{300 * (1 - loss):.1f}" height="45" fill="#ff7f0e"/>
  <text x="100" y="182" font-size="16" font-family="Arial">1 - Loss = {1 - loss:.2f}</text>

  <text x="250" y="275" font-size="14" text-anchor="middle" font-family="Arial">loss={loss:.2f}, accuracy={accuracy:.2f}</text>
</svg>
'''

    with open(filename, "w", encoding="utf-8") as file:
        file.write(svg_content)


for group in groups:
    image_name = f"{group['name']}.svg"

    print(
        f"GROUP {group['name']} "
        f"loss={group['loss']:.4f} "
        f"accuracy={group['accuracy']:.4f} "
        f"image={image_name}"
    )

    generate_svg(
        filename=image_name,
        title=group["name"],
        loss=group["loss"],
        accuracy=group["accuracy"],
    )

print("All comparison results have been generated.")
