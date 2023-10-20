import numpy as np
from typing import List, Tuple
from mmocr.apis import MMOCRInferencer
from sklearn.cluster import DBSCAN

def square_center(polygon: List[float]) -> Tuple[float, float]:
    """
    Returns the center of the square that contains the polygon.
    """
    x_min = min(polygon[0::2])
    x_max = max(polygon[0::2])
    y_min = min(polygon[1::2])
    y_max = max(polygon[1::2])
    
    return (x_min + x_max) / 2, (y_min + y_max) / 2

class LineExtractor:
    def __init__(self, det='DBNet', rec='SAR', dbscan_eps=20, dbscan_min_samples=1):
        self.ocr_inference = MMOCRInferencer(det=det, rec=rec)
        self.dbscan_eps = dbscan_eps
        self.dbscan_min_samples = dbscan_min_samples
        
    
    def get_lines(self, img):
        dbscan = DBSCAN(eps=self.dbscan_eps, min_samples=self.dbscan_min_samples)
        result = self.ocr_inference(img, show=False)

        result = result['predictions'][0]
        txts = result['rec_texts']

        ceneters = np.array([square_center(polygon) for polygon in result['det_polygons']])

        y_clusters = dbscan.fit_predict(ceneters[:, 1].reshape(-1, 1))

        lines = {}
        for i in np.unique(y_clusters):
            if i == -1:
                continue
            lines[i] = []

        for i, idx in enumerate(y_clusters):
            lines[idx].append((txts[i], ceneters[i]))

        # Sort each cluster by x coordinate and sort corresponding txts
        for cluster in lines:
            lines[cluster] = sorted(lines[cluster], key=lambda x: x[1][0])

        # Sort clusters by y coordinate
        lines = dict(sorted(lines.items(), key=lambda x: x[1][0][1][1]))

        txt_lines = []
        for val in lines.values():
            str = ""
            for x in val:
                str += x[0] + " "

            txt_lines.append(str)
        
        return txt_lines
