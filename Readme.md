# Detect Faces and Crop

This Python script uses **MTCNN** and **OpenCV** to detect faces in team photos and crop them into either:

- 🟦 **Square face thumbnails** (`256x256`)
- 🟨 **Portrait-style profile crops** (`256x384`, includes chest area)

---

## 📂 Folder Setup

1. Place this script `bulk_crop_images.py` in your project folder.
2. In the **same folder**, create a folder named:

```
team_photos/
```

3. Add your team photos inside `team_photos/`  
   (supports `.jpg`, `.jpeg`, and `.png` images)

---

## ⚙️ Configuration

In the script `bulk_crop_images.py`, change this line to control output style:

```python
MODE = "face"         # For square face crops (256x256)
# OR
MODE = "full_profile" # For upper-body profile crops (256x384)
```

---

## 🚀 Running the Script

```bash
python bulk_crop_images.py
```

---

## 📁 Output

- Cropped images will be saved in:
  - `output_faces/` if MODE is `"face"`
  - `output_profiles/` if MODE is `"full_profile"`

Each image is saved with a unique name like `1_face_1.jpg`, `teamA_face_2.jpg`, etc.

---

## 📦 Install Dependencies

Use this to install required packages:

```bash
pip install -r requirements.txt
```

---

## ✅ Requirements

- Python 3.6+
- [MTCNN](https://github.com/ipazc/mtcnn)
- OpenCV (`opencv-python`)
- NumPy
