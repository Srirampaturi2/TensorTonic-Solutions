def nms(boxes, scores, iou_threshold):
    if not boxes:
        return []
    
    # 1. Sort indices by score descending
    indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    
    keep = []
    while indices:
        # 2. Pick best box
        best = indices[0]
        keep.append(best)
        indices = indices[1:]
        
        # 3. Compare best against all remaining  boxes
        
        remaining = []
        for i in indices:
            box_a = boxes[best]
            box_b = boxes[i]
            
            # IoU calculation
            x_left   = max(box_a[0], box_b[0])
            y_top    = max(box_a[1], box_b[1])
            x_right  = min(box_a[2], box_b[2])
            y_bottom = min(box_a[3], box_b[3])
            
            intersection = max(0, x_right - x_left) * max(0, y_bottom - y_top)
            area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
            area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
            union = float(area_a + area_b - intersection)
            
            iou = 0.0 if union == 0 else intersection / union
            
            if iou < iou_threshold:
                remaining.append(i)  # keep it
        
        indices = remaining
    
    return keep
    