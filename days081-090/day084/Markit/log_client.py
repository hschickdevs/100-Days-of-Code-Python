import os


class Logger:
    """Custom logger class instead of using the logging module (no benefit or loss just preference)"""
    def __init__(self, output_dir=None):
        self.log = ""
        self.output_dir = output_dir

    def update_log(self, event):
        self.log += f"\n> {event}\n"
        self.save_log()
        print(event)

    def save_log(self):
        with open(os.path.join(self.output_dir, 'program_log.txt'), 'w') as log:
            log.write(self.log)
