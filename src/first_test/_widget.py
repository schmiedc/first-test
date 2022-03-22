from magicgui import magic_factory
import napari
import imageio

@magic_factory
def flood_magic_factory(
        img_layer: napari.layers.Image, threshold: float = 0
) -> napari.types.LayerDataTuple:

    label_image = img_layer.data <= threshold  # # get numpy array from image layer, threshold image return binary
    label_image = label_image.astype(int) * 13  # label 13 is blue in napari

    # create DataTuple
    label_seg = (label_image, {'name': 'seg'})
    return label_seg


# for quickly testing the widget
if __name__ == "__main__":
    # create a Viewer and add an image here
    viewer = napari.Viewer()

    # reads in png with imageio as np array
    test_image = imageio.imread("/home/christopher.schmied/HT_Docs/Projects/2022-03_Hackaton/test_data/island.png")

    # adds numpy array to viewer as image with a name
    viewer.add_image(test_image, name='Images')

    # adds a widget to the viewer
    viewer.window.add_dock_widget(flood_magic_factory())

    napari.run()
