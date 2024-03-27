
            x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
            box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]
            colour_box_current = [int(j) for j in colours[class_numbers[i]]]
            cv2.rectangle(image_input, (x_min, y_min), (x_min + box_width, y_min + box_height),colour_box_current, 3) 
    if len(pred_scores) > 0:
        mean_avg_prec = sum(pred_scores)/len(results)
        obj_mean_avg = len(