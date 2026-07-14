import matplotlib.pyplot as plt


losses = [1.0, 0.82, 0.65, 0.51, 0.39, 0.31]
accuracies = [0.42, 0.55, 0.66, 0.74, 0.81, 0.86]

for epoch, (loss, acc) in enumerate(zip(losses, accuracies), start=1):
    print(f"Epoch {epoch} loss={loss:.4f} accuracy={acc:.4f}")

plt.figure()
plt.plot(range(1, len(losses) + 1), losses, marker="o")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Curve")
plt.savefig("loss_curve.png")

print("Saved figure: loss_curve.png")