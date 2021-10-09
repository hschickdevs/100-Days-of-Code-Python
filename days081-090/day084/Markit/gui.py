import PySimpleGUI as sg
import os
import base64
from datetime import datetime
from log_client import Logger
from image_handler import ImageHandler

sg.theme('LightBlue2')
APP_ICON = base64.b64encode(open('app_icon.png', 'rb').read())


class ImagePreview(sg.Window):
    def __init__(self, image_metadata):
        self.layout = [
            [sg.Image(filename=os.path.join(os.getcwd(), 'temp_preview.png'))],
            [sg.Text(f'Watermark Location: {image_metadata["wm_location"]} | Opacity: {image_metadata["opacity"]} | Watermark Size: {image_metadata["size"]}')],
        ]
        super().__init__('Markit - Image Preview', self.layout, font=('Arial', 14, 'bold'), icon=APP_ICON)
        self.mainloop()

        # Remove the temp image after the window is closed
        os.remove(os.path.join(os.getcwd(), 'temp_preview.png'))

    def mainloop(self):
        while True:
            event, values = self.read()
            if event == sg.WIN_CLOSED:
                break


class MainWindow(sg.Window):
    def __init__(self, logger_client):
        self.logger = logger_client
        self.layout = [
            # [sg.Text("", size=(10, 1)), sg.Image(filename='fedex_logo.png', key='image')],
            [sg.Text("")],
            [sg.Text('Select an image to watermark', size=(49, 1)),
             sg.FileBrowse(key='--SINGLEIMAGE--')],
            [sg.Text("Or", font=('Arial', 14, 'normal'), size=(49, 1))],
            [sg.Text('Select a directory containing multiple images to watermark', size=(49, 2)),
             sg.FolderBrowse(key='--MULTIPLEIMAGES--')],
            [sg.Text("")],
            [sg.Text('Select the watermark image', size=(49, 2)),
             sg.FileBrowse(key='--WATERMARKIMAGE--')],
            [sg.Text("")],
            [sg.Text('Select output folder for watermarked image(s)', size=(49, 2)),
             sg.FolderBrowse(key='--DOWNLOAD--')],
            [sg.Text("")],
            [sg.Text("Watermark Opacity", size=(27, 1), justification='center'),
             sg.Text('Watermark Size (% of original)', size=(28, 1), justification='center')],
            [sg.Slider(key='--WM_OPACITY--', range=(0, 1), resolution=0.01, orientation='horizontal', default_value=1,
                       size=(25, 15), font=('Arial', 15, 'normal')),
             sg.Slider(key='--WM_SIZE--', range=(1, 100), resolution=1, orientation='horizontal', default_value=100,
                       size=(25, 15), font=('Arial', 15, 'normal'))],
            [sg.Text("")],
            [sg.Text('Watermark Location:', size=(28, 1), justification='right'),
             sg.Combo(key='--WM_LOCATION--', values=['center', 'top left', 'top right', 'bottom left', 'bottom right'],
                      default_value='center', font=('Arial', 15, 'normal'))],
            [sg.Text("")],
            [sg.Text("Please Note:\nThe interface will be unresponsive while generating the image(s).", size=(57, 2),
                     font=('Arial', 14, 'normal'))],
            # [sg.Text("Please Note:\nThis is the beta version. Please report bugs to hschickdevs@gmail.com", size=(57, 2))],
            [sg.Button('Generate Images', size=(18, 1)), sg.Button('Quit Program', size=(16, 1)),
             sg.Button('Generate Preview', size=(18, 1))]]

        super().__init__('Markit - Watermark Engine', self.layout, font=('Arial', 15, 'bold'), icon=APP_ICON)
        self.mainloop()

    def mainloop(self):
        while True:
            event, values = self.read()
            if event == "Quit Program" or event == sg.WIN_CLOSED or event == "Exit":
                break

            elif event == "Generate Preview":
                image_input_path = values['--SINGLEIMAGE--']
                image_dir_input_path = values['--MULTIPLEIMAGES--']
                watermark_image_input_path = values['--WATERMARKIMAGE--']

                if (len(image_input_path) > 0 and len(image_dir_input_path) > 0) or len(image_dir_input_path) > 0:
                    sg.PopupError("Please select a single image to generate a preview",
                                  keep_on_top=True, modal=True,
                                  font=('Arial', 15, 'normal'),
                                  title='ERROR', icon=APP_ICON)
                else:
                    img_handler = ImageHandler()
                    wm_opacity = float(values['--WM_OPACITY--'])
                    wm_size = float(values['--WM_SIZE--']) / 100
                    wm_location = values['--WM_LOCATION--'].strip().lower()
                    img_resp = img_handler.process_image(watermark_path=watermark_image_input_path,
                                                         image_path=image_input_path,
                                                         wm_opacity=wm_opacity, wm_size=wm_size,
                                                         wm_location=wm_location)
                    if img_resp == 1:
                        sg.PopupError("Could not generate preview. An error occurred when trying to process the main image.",
                                      keep_on_top=True, modal=True,
                                      font=('Arial', 15, 'normal'),
                                      title='ERROR', icon=APP_ICON)
                    elif img_resp == 2:
                        sg.PopupError("Could not generate preview.\nAn error occurred when trying to process the watermark image.",
                                      keep_on_top=True, modal=True,
                                      font=('Arial', 15, 'normal'),
                                      title='ERROR', icon=APP_ICON)
                    else:
                        ImagePreview(image_metadata={'opacity': wm_opacity, 'size': wm_size, 'wm_location': wm_location})

            elif event == "Generate Images":
                # validate and save input file
                image_input_path = values['--SINGLEIMAGE--']
                image_dir_input_path = values['--MULTIPLEIMAGES--']
                watermark_image_input_path = values['--WATERMARKIMAGE--']

                target_folder = values['--DOWNLOAD--']

                if len(target_folder) < 1:
                    sg.PopupError("Please select an output folder.", keep_on_top=True, font=('Arial', 15, 'normal'),
                                  title='ERROR', icon=APP_ICON)
                elif len(image_input_path) > 0 and len(image_dir_input_path) > 0:
                    sg.PopupError("Please select EITHER a single image, or a directory containing multiple "
                                  "images.\nTo clear the inputs, please restart the program.", keep_on_top=True,
                                  font=('Arial', 15, 'normal'),
                                  title='ERROR', icon=APP_ICON, modal=True)
                else:
                    try:
                        target_folder = os.path.join(target_folder, 'Markit Program Output')
                        if not os.path.isdir(target_folder):
                            os.makedirs(target_folder)

                        target_folder = os.path.join(target_folder,
                                                     f'{datetime.now().strftime("%Y-%m-%d_%H%M%S")}_Output')
                        if not os.path.isdir(target_folder):
                            os.makedirs(target_folder)

                    except Exception as e:
                        sg.PopupError('FATAL ERROR: Could not access target output folder.\nPlease make sure that the '
                                      f'target folder is valid.\n{e}',
                                      title='Error', keep_on_top=True, font=('Arial', 15, 'normal'), icon=APP_ICON)
                        continue

                    image_mode = "multi" if len(image_dir_input_path) > len(image_input_path) else "single"
                    wm_opacity = float(values['--WM_OPACITY--'])
                    wm_size = float(values['--WM_SIZE--']) / 100
                    wm_location = values['--WM_LOCATION--'].strip().lower()
                    if image_mode == 'single':
                        image_operations = [image_input_path]
                    else:
                        image_operations = [os.path.join(image_dir_input_path, filename) for filename in os.listdir(image_dir_input_path)]

                    print(image_operations)

                    self.logger.output_dir = target_folder
                    self.logger.update_log(event=f'Program started')
                    self.logger.update_log(event=f'Saving all files to {target_folder}')
                    self.logger.update_log(event=f'Mode: {image_mode} image')
                    self.logger.update_log(event=f'Watermark Location: {wm_location}')

                    img_handler = ImageHandler(logger=self.logger, target_folder=target_folder)
                    success_count = 0
                    for i, im_path in enumerate(image_operations):
                        resp = img_handler.process_image(watermark_path=watermark_image_input_path,
                                                         image_path=im_path,
                                                         wm_opacity=wm_opacity, wm_size=wm_size,
                                                         wm_location=wm_location)
                        if resp == 2:
                            sg.PopupError(
                                f'FATAL ERROR: Could not run operation.\nSee the program logs for more info:\n{target_folder}',
                                title='Error', keep_on_top=True, font=('Arial', 15, 'normal'), icon=APP_ICON)
                            break
                        elif resp == 0:
                            success_count += 1

                        if i + 1 == len(image_operations):
                            sg.Popup(f'Operation finished.\nAll files saved to {target_folder}',
                                     title='Operation Success', keep_on_top=True, font=('Arial', 15, 'normal'),
                                     icon=APP_ICON)

                    self.logger.update_log(event=f'Operation finished. Successfully processed {success_count} image(s).')


if __name__ == "__main__":
    logger = Logger()
    MainWindow(logger_client=logger)
