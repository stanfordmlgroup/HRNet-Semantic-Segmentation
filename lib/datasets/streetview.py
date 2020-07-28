import pandas as pd
from pathlib import Path

from .cityscapes import Cityscapes

class Streetview(Cityscapes):
    def __init__(self, *kargs, **kwargs):
        super(Streetview, self).__init__(*kargs, **kwargs)

    def read_files(self):
        assert 'test' in self.list_path
        img_infos = pd.read_csv(self.root + self.list_path)
        fpaths = img_infos.save_loc.tolist()
        files = [{'img': path, 'name': Path(path).stem} for path in fpaths]
        return files
