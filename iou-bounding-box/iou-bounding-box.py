
def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    Format: [x1, y1, x2, y2]
    """
    # 1. Determine the coordinates of the intersection rectangle
    x_left = max(box_a[0], box_b[0])
    y_top = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    # 2. Calculate Intersection Area
    # If the boxes don't overlap, one of these differences will be negative
    # We use max(0, ...) to handle the "no overlap" case effectively.
    intersection_width = max(0, x_right - x_left)
    intersection_height = max(0, y_bottom - y_top)
    intersection_area = intersection_width * intersection_height

    # 3. Calculate Individual Box Areas
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    # 4. Calculate Union Area
    # Union = Area A + Area B - Intersection
    union_area = float(area_a + area_b - intersection_area)

    # 5. Compute IoU
    # Avoid division by zero if both boxes have zero area
    if union_area == 0:
        return 0.0

    return intersection_area / union_area