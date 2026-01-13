import json
try:
        with open("dulieu.json", "r", encoding="utf-8") as f:
            ds = json.load(f)
except FileNotFoundError:
    ds = []
    with open("dulieu.json", "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=4)

for i in range(1, 101):
    sv = {
        "msv": f"{i:03d}",     # 001 → 100
        "ten": f"Sinh viên {i}",
        "m1": i % 10,
        "m2": (i + 1) % 10,
        "m3": (i + 2) % 10,
        "m4": (i + 3) % 10
    }
    ds.append(sv)

with open("dulieu.json", "w", encoding="utf-8") as f:
    json.dump(ds, f, ensure_ascii=False, indent=4)