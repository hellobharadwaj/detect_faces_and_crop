from mtcnn import MTCNN
import cv2
import os
import numpy as np

# CONFIGURATION
MODE = "full_profile"  # Options: "face" or "full_profile"
INPUT_FOLDER = "team_photos"
OUTPUT_FOLDER = "output_faces" if MODE == "face" else "output_profiles"

# Detection and resizing settings
PADDING_RATIO = 0.3
OUTPUT_FACE_SIZE = 256
OUTPUT_PROFILE_SIZE = (256, 384)  # width x height for full profile

# Initialize face detector
detector = MTCNN()
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Start processing
for root, dirs, files in os.walk(INPUT_FOLDER):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(root, file)
            img = cv2.imread(input_path)

            if img is None:
                print(f"⚠️ Failed to read image: {input_path}")
                continue

            results = detector.detect_faces(img)
            base_name = os.path.splitext(file)[0]

            for i, face in enumerate(results):
                x, y, width, height = face['box']

                # Face padding
                pad_w = int(width * PADDING_RATIO)
                pad_h = int(height * PADDING_RATIO)

                if MODE == "face":
                    # Classic square face crop
                    x1 = max(x - pad_w, 0)
                    y1 = max(y - pad_h, 0)
                    x2 = min(x + width + pad_w, img.shape[1])
                    y2 = min(y + height + pad_h, img.shape[0])
                    cropped = img[y1:y2, x1:x2]

                    # Square padding
                    h, w = cropped.shape[:2]
                    size = max(h, w)
                    square = np.zeros((size, size, 3), dtype=np.uint8)
                    y_offset = (size - h) // 2
                    x_offset = (size - w) // 2
                    square[y_offset:y_offset + h, x_offset:x_offset + w] = cropped
                    resized = cv2.resize(square, (OUTPUT_FACE_SIZE, OUTPUT_FACE_SIZE))

                elif MODE == "full_profile":
                    # Extend downward for chest area
                    x1 = max(x - pad_w, 0)
                    y1 = max(y - pad_h, 0)
                    x2 = min(x + width + pad_w, img.shape[1])
                    y2 = min(y + int(2.5 * height), img.shape[0])  # Extend below face
                    cropped = img[y1:y2, x1:x2]

                    # Pad to portrait ratio (256x384)
                    h, w = cropped.shape[:2]
                    new_w, new_h = OUTPUT_PROFILE_SIZE
                    result = np.zeros((new_h, new_w, 3), dtype=np.uint8)
                    result[:] = (0, 0, 0)

                    # Resize while maintaining aspect ratio
                    scale = min(new_w / w, new_h / h)
                    resized_w = int(w * scale)
                    resized_h = int(h * scale)
                    resized_cropped = cv2.resize(cropped, (resized_w, resized_h))

                    x_offset = (new_w - resized_w) // 2
                    y_offset = (new_h - resized_h) // 2
                    result[y_offset:y_offset + resized_h, x_offset:x_offset + resized_w] = resized_cropped
                    resized = result

                # Save output
                output_filename = f"{base_name}_face_{i+1}.jpg"
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)
                cv2.imwrite(output_path, resized)

            print(f"✅ Processed {file} — {len(results)} faces detected.")
