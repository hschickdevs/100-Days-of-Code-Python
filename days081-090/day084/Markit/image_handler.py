from PIL import Image
import os, sys


class ImageHandler:
    def __init__(self, target_folder=None, logger=None):
        self.logger = logger
        self.target_folder = target_folder
        self.watermark_img = None
        with open('valid_filetypes.txt') as infile:
            self.acceptable_filetypes = [f".{filetype.strip().lower()}" for filetype in infile.readlines()]
        print('Acceptable Filetypes:', self.acceptable_filetypes)

    def process_image(self, watermark_path: str, image_path: str, wm_opacity: float, wm_size: float, wm_location):
        """Attempts to process the images.
        wm_opacity and wm_size must be a float between 0 and 1
        A return code of 2 means a critical error occured and the program has failed.
        A return code of 1 means that soft error occured (ie. the image could not be opened)
        Otherwise, the program returns 0 success code."""
        try:
            if self.watermark_img is None:
                self.watermark_img = Image.open(watermark_path).convert('RGBA')

                # Resize the watermark image according to the specified size:
                if wm_size != 1:
                    self.watermark_img = self.resize_image(self.watermark_img, wm_size)

                # Set the opacity of the watermark image:
                if wm_opacity != 1:
                    self.set_opacity(self.watermark_img, wm_opacity)

                if self.logger is not None:
                    self.logger.update_log(event=f'Watermark Image Size: {self.watermark_img.size}')

        except Exception as e:
            if self.logger is not None:
                self.logger.update_log(event=f'CRITICAL ERROR: Could not process watermark image ({watermark_path}) - {e}')
            return 2

        image_ext = os.path.splitext(image_path)[1].lower()
        if image_ext not in self.acceptable_filetypes:
            if self.logger is not None:
                self.logger.update_log(event=f'ERROR: Could not open {image_path} image for processing - "{image_ext}" is an invalid filetype')
            return 1
        else:
            try:
                main_image = Image.open(image_path).convert('RGBA')
            except Exception as e:
                if self.logger is not None:
                    self.logger.update_log(event=f'ERROR: Could not open {image_path} image for processing - {e}')
                return 1

        wm_width, wm_height = self.watermark_img.size
        main_width, main_height = main_image.size

        if wm_width > main_width or wm_height > main_height:
            if self.logger is not None:
                self.logger.update_log(
                    event=f'Could not watermark {image_path} image. Watermark {self.watermark_img.size} larger than background image {main_image.size}. Try setting the watermark image size to a smaller percentage.')
            return 1

        self.append_watermark(background_im=main_image, watermark_im=self.watermark_img, wm_location=wm_location)

        if self.target_folder is not None:
            im_dir = os.path.join(self.target_folder, 'Watermarked Images')
            if not os.path.isdir(im_dir):
                os.mkdir(im_dir)

            filename = image_path.split("/")[-1].split(".")[0] + ".png"
            main_image.save(os.path.join(im_dir, filename), quality=95)
        else:
            main_image.save(os.path.join(os.getcwd(), 'temp_preview.png'), quality=95)

        if self.logger is not None:
            self.logger.update_log(event=f'Successfully processed image: {image_path}')

        return 0

    def resize_image(self, image: Image, multiple):
        return image.resize((round(image.size[0] * multiple), round(image.size[1] * multiple)))

    def set_opacity(self, image: Image, multiple):
        im2 = image.copy()
        im2.putalpha(int(255 * multiple))
        image.paste(im2, image)
        return image

    def append_watermark(self, wm_location, background_im: Image, watermark_im: Image):
        bg_w, bg_h = background_im.size
        wm_w, wm_h = watermark_im.size
        if wm_location == 'top left':
            background_im.paste(watermark_im, (0, 0), watermark_im)
        elif wm_location == 'top right':
            background_im.paste(watermark_im, (bg_w - wm_w, 0), watermark_im)
        elif wm_location == 'bottom left':
            background_im.paste(watermark_im, (0, bg_h - wm_h), watermark_im)
        elif wm_location == 'bottom right':
            background_im.paste(watermark_im, (bg_w - wm_w, bg_h - wm_h), watermark_im)
        else:
            # If the location is 'center' or anything else (instead of just throwing an error)
            background_im.paste(watermark_im, (int((bg_w - wm_w) / 2), int((bg_h - wm_h) / 2)), watermark_im)
