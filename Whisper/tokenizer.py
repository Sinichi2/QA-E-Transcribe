from __future__ import annotations
import tiktoken
import string 
import os 
import base64

@dataclass
class Tokenizer: 
    encoding: tiktoken.encoding 
    num_languages: int 
    languages: Optional[str] = None 
    task: Optional[str] = 'transcribe'

    sot_sequence: tuple[int, ...] = ()
    special_tokens = Dict[int, str] = field(default_factory=dict)

    #The token tables
    def __post_init__(self) -> None: 
        #mapping every registered special string to a numeric id 
        for tok in self.encoding.special_tokens_set: 
            self.special_tokens[tok] = self.encoding.encode_single_token(tok)

        #Convenience
        sot = self.special_tokens['<|startoftranscript|>']
        transcribe = self.special_tokens['<|transcribe|>']

        #Building the SOT sequence 
        sequence = [sot]
        if self.language: 
            lang_codes = tuple(LANGUAGES.keys())[: self.num_languages]
            sequence.append(sot + 1 + lang_codes.index(self.language))
        if self.task: 
            sequence.append(transcribe if self.task == "transcribe" else None)
        self.sot_sequence = tuple(sequence)
    #encoding portion of the tokens
    def encode(self, text: str, **kw) -> List[int]:
        return self.encoding.encode(text, **kw)
    #decoding portion of the tokens
    def decode(self, tokens: List[int], **kw) ->str: 
        return self.encoding.decode(clean, **kw) 

    @cached_property
    def eot(self) -> int: 
        return self.encoding.eot_token
    