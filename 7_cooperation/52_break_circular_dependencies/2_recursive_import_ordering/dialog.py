
import app

class Dialog(object):
    def __init__(self, save_dir):
        self.save_dir = save_dir

save_dialog = Dialog(app.prefs.get('save_dir'))

def show():
    print('Showing the dialog!')