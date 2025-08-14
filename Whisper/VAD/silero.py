import pathlib
import json 

import Vad



class silero(Vad):
    def __init__(self, **kwargs): 
        super.__init__(kwargs['vad_onset'])

        self.vad_onset = kwargs['vad_onset']
        self.chunk_size = kwargs['chunk_size']
        self.vad_pipeline, vad_utils = torch.hub.load(dir = '', model = 'silero_vad', force_load=False, onnx=False, trust_repo = True)

    def __call__(self, **kwargs):
        

