cat > README.md <<EOF
# Detect Faces and Crop

This script uses MTCNN and OpenCV to recursively detect faces in images and crop either:

- square **face thumbnails**
- vertical **profile portraits** (with head + torso)

## Usage

Edit `MODE` in \`bulk_crop_images.py\`:
- \`face\` – for 256x256 face images
- \`full_profile\` – for 256x384 upper-body images

Place your images inside \`team_photos/\` and run:

\`\`\`bash
python bulk_crop_images.py
\`\`\`

Outputs are saved in either:
- \`output_faces/\`
- \`output_profiles/\`

## Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`
EOF
