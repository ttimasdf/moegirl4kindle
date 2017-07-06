from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes
from PIL import Image
from io import BytesIO
import hashlib


class KindleImagesPipeline(ImagesPipeline):
    """Tuned ImagePipeline for Kindle"""

    def convert_image(self, image, size=None):
        if image.mode == 'P':
            image = image.convert("RGBA")

        if size:  # make thumbnail
            image = image.copy().convert('L')
            img_x, img_y = image.size
            if img_x > img_y:  # Horizonal
                image = image.rotate(90)
            if img_x / img_y > size[0] / size[1]:
                w, h = img_y * (size[0] / size[1]), img_y
            else:
                w, h = img_x, img_x * (size[1] / size[0])

            image = image.crop((
                (img_x - w) / 2,
                (img_y - h) / 2,
                (img_x + w) / 2,
                (img_y + h) / 2))
            image = image.resize(size)

        buf = BytesIO()
        image.save(buf, 'PNG')
        return image, buf

    def file_path(self, request, response=None, info=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return 'full/%s.png' % (image_guid)
