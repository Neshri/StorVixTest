import pathlib
import tensorflow as tf
from PIL import Image

class DataFetcher:
    
    def __init__(self) -> None:
        dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
        data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)
        self.data_dir = pathlib.Path(data_dir)
        
    def get_data(self, search):
        """Returns

        Args:
            search (_type_): _description_

        Returns:
            _type_: _description_
        """
        return list(self.data_dir.glob(search))



Image.open()
print(DataFetcher().get_data("roses/*"))
