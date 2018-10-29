from operator import itemgetter
import cv2 as cv
import numpy as np
import math
import images as img

display = False
debug = False
_threshold = 0.8


def set_display(d):
    global display
    display = d


def set_debug(d):
    global debug
    debug = d


def set_threshold(d):
    global _threshold
    _threshold = d


def match_test(_template_name, _template, _source, threshold=_threshold):
    return match(_template_name, _template, cv.imread('sources/{}.png'.format(_source)), threshold)


def match_name(name, threshold=0.8):
    image = img.info(name)
    return match(image[0], image[1], img.screenshot(), threshold)


# Returns array of tuples, of matching pixel coordinates
def match(template_name, template, source, threshold=0.8):
    # The half lengths are added to the returned pixel pairs,
    # so the cursor clicks on the middle of the image instead of
    # the top left corner (as all image inputs start at)
    half_width = math.floor(template.shape[1]/2)
    half_height = math.floor(template.shape[0]/2)

    # This allows you to better evaluate the supported matchers of OpenCV
    # methods = ['cv.TM_SQDIFF_NORMED', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_CCOEFF']
    methods = ['cv.TM_CCOEFF_NORMED']

    for method in methods:
        # Use the given method to generate a sorted list of points
        # whose confidence level is above the threshold
        result_array = cv.matchTemplate(source, template, eval(method))
        match_array = np.where(result_array >= threshold)
        confidence = []
        for point in zip(match_array[1], match_array[0]):
            confidence.append([point, result_array[point[1]][point[0]]])
        confidence = sorted(confidence, key=itemgetter(1), reverse=True)

        # Filter the matching arrays, by removing points
        # that are too close to one another. Take the most confident
        # point, and remove all other values that are within a five pixel range
        filtered_points = []
        confidence = [x[0] for x in confidence]
        while len(confidence) > 0:
            baseline = confidence.pop(0)
            confidence = list(
                filter(
                    lambda cpoint: (abs(baseline[0] - cpoint[0]) > 5 or abs(baseline[1] - cpoint[1]) > 5),
                    confidence))
            baseline = ((baseline[0] + half_width), (baseline[1] + half_height))
            filtered_points.append(baseline)

        if debug:
            print("{} Threshold: {} Sorted: {}".format(
                template_name,
                np.shape(match_array)[1], len(filtered_points)))

        if display and filtered_points:
            for point in filtered_points:
                cv.rectangle(
                    source, (point[0] - half_width, point[1] - half_height),
                    (point[0] + half_width, point[1] + half_height),
                    (0, 0, 255), 2)
            cv.namedWindow(template_name, cv.WINDOW_NORMAL)
            cv.imshow(template_name, source)
            cv.waitKey(0)
            cv.destroyAllWindows()

        return filtered_points
