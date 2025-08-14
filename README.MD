# Audio to Transcription AI model 

This AI model is **PRIMARILY** for Transcriptions that aid towards to: 

- Interviews
- Court Hearings / depositions
- Focus groups / workshops
- Lectures / panels / podcasts
- Customer support calls / sales calls
- Medical Dictations
- Town halls / public council sessions

This model will convert video/audio (.wav, .mp3, .mp4) files to text transcription. In the text, the transcription will have 3 different categories: 

1. [QUESTION]
2. [ANSWER]
3. [EMPHASIS] - Notable words/phrases detected via prosodic cues, typography, repetition, or cue words (e.g., "important", "note", "to be clear")

This pipeline alsos upports speaker diarzitation to map turns to "Interviewer/Judge/Lawyer" vs. "Respondent/Witness/Interviewee," improving the QUESTION/ANSWER label. 
    
## Steps
1. Run requirements.txt file through:
```
    pip install -r requirements.txt    
```

## Output Format 
```
	[QUESTION] (Speaker S0 @00:01.2–00:05.8)
	Could you state your full name for the record?
	
	[ANSWER] (Speaker S1 @00:06.0–00:07.9)
	John Michael Reyes.
	
	[EMPHASIS] (Speaker S1 @00:25.1–00:28.2)
	I was **NOT** informed ahead of time.
```
