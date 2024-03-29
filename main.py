from PromptMessage import *
from VideoTextClass import *
from GptSummary import *




path = 'video\prakash_raj.mp4'

# Creating object to get the text from the video
vidText = Videotext(path)
transcript = vidText.getText()

# Creating object of class for generating summary using gpt
gptSumm = Gptresponse(system_msg, transcript)
final_summary = gptSumm.getSummary()

# print(final_summary)