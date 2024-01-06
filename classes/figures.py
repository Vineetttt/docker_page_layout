import layoutparser as lp
from classes.utilities import process_blocks_to_bboxes

def load_figure_model():
    model = lp.Detectron2LayoutModel(
        config_path="https://www.dropbox.com/s/yc92x97k50abynt/config.yaml?dl=1",  # In model catalog
        label_map={
            1: "Text",
            2: "Image",
            3: "Table",
            4: "Maths",
            5: "Separator",
            6: "Other",
        },  # In model`label_map`
        extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.4],  # Optional
    )
    return model

def get_figure_detection(image):
    # Layout
    model = load_figure_model()
    layout = model.detect(image)
    lp.draw_box(image, layout, show_element_type=True)
    figure_blocks = lp.Layout([b for b in layout if b.type == 'Image'])
    figure_bboxes = process_blocks_to_bboxes(figure_blocks)
    return figure_bboxes