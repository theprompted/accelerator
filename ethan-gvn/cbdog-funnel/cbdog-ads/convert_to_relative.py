import re

# Read the large HTML file
with open('ad-mockups-all.html', 'r') as f:
    html = f.read()

# Track which ad we're on
batch1_count = 0
batch2_count = 0

def replace_base64(match):
    global batch1_count, batch2_count
    
    # First 20 are batch 1, next 11 are batch 2
    total = batch1_count + batch2_count
    
    if total < 20:
        batch1_count += 1
        return f'src="generated_ad_images/ad_{batch1_count:02d}.png"'
    else:
        batch2_count += 1
        return f'src="generated_ad_images_batch2/ad_{batch2_count:02d}.png"'

# Replace all base64 image sources
# Pattern matches src="data:image/png;base64,..." or src="data:image/jpeg;base64,..."
pattern = r'src="data:image/[^;]+;base64,[^"]*"'

new_html = re.sub(pattern, replace_base64, html)

# Write the new lightweight HTML
with open('ad-mockups-all-lightweight.html', 'w') as f:
    f.write(new_html)

print(f"Done! Replaced {batch1_count + batch2_count} images")
print(f"Batch 1: {batch1_count}, Batch 2: {batch2_count}")
