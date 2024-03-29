from tensorflow.keras import backend as K
import pandas as pd
import misc_utils.inference_utils as msu

img_height = 448
img_width = 448
confidence_threshold = 0.5
iou_threshold = 0.5
classes = ['background', 'car', 'bicyclist', 'pedestrian']
multi_model_path = "C:/Users/Administrator/Desktop/cruw_model_multi_v2.h5"
rgb_img_base_path = "C:/Users/Administrator/Desktop/datasets/CRUW/ALL/resized/CRUW_kaggle/images/"
rf_img_base_path = "C:/Users/Administrator/Desktop/datasets/CRUW/ALL/resized/CRUW_kaggle/rf_maps/"
rgb_data_path = "data/cruw_test_data_rgb.csv"
rf_data_path = "data/cruw_test_data_rf.csv"
dest_path = "C:/Users/Administrator/Desktop/my_detections/cruw/multi/lab_cv/"

# select data
rgb_df = pd.read_csv(rgb_data_path)
rf_df = pd.read_csv(rf_data_path)

rgb_list = rgb_df['image'].unique()
rf_list = rf_df['image'].unique()

# load model
K.clear_session()
multi_model = msu.load_det_model(multi_model_path)
detections = msu.do_multi_detections(rgb_list,
                                     rgb_img_base_path,
                                     rf_list,
                                     rf_img_base_path,
                                     multi_model,
                                     img_height,
                                     img_width,
                                     confidence_threshold,
                                     iou_threshold)
# print(len(detections))
# msu.print_detections(detections)

# save detections
# msu.show_detections(detections, rgb_list, rgb_img_base_path, classes, dest_path, img_height, img_width)
msu.show_detections_cv(detections, rgb_list, rgb_img_base_path, classes, dest_path, img_height, img_width, 1)
print("Done")
