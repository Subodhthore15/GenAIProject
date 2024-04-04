from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PromptMessage import *
from VideoTextClass import *
from GptSummary import *
# from ClassLab45API import *
from GptSummary import *
import pytube
from extract_information import *

app = Flask(__name__)

# Define the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to process uploaded video and return summary
def process_video(video_path):
    # Creating object to get the text from the video
    vidText = Videotext(video_path)
    transcript = vidText.getText()
    return transcript

def process_youtube_link(url):
    youtube=pytube.YouTube(url)
    stream=youtube.streams.get_audio_only()
    stream.download(output_path=r'youtube_path', filename='youtube_video.mp4') # store in the localhost
    path = r'youtube_path\youtube_video.mp4'
    vidText = LinkVideoTimelyText(path)
    transcript = vidText.getText()
    return transcript


def get_final_summary(system_msg, transcript):
    # Creating object of class for generating summary using gpt.
    gptSumm = Gptresponse(system_msg, transcript)
    final_summary = gptSumm.getSummary()
    return final_summary

# create function to download the transcript
def download_transcript(trascript):
    text_file = open(r'transcript_path\transcript.doc', 'w')
    trascript = trascript
    text_file.write(trascript)
    text_file.close()
    return

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    # if 'file' not in request.files:
    #     return 'No file part'
    file = request.files['file']
    # if file.filename == '':
    #     return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        transcript = process_video(video_path)
        download_transcript(transcript)
        print(transcript)
        final_summary = get_final_summary(system_msg, transcript)

        return render_template('result.html', summary=final_summary)

    else:
        youtube_path = request.form.get("youtube")
        transcript = process_youtube_link(youtube_path)
        download_transcript(transcript)
        print(transcript)
        final_summary = get_final_summary(system_msg, transcript)
        print(final_summary)
        
        # Call the function
        topic, sentiment, conclusion, summary = extract_information(final_summary)
        
        # Displaying the variables
        print("Topic:", topic)
        print()
        print("Sentiment:", sentiment)
        print()
        print("Conclusion:", conclusion)
        print()
        print("Summary:", summary)
        
        return render_template('result.html', final_summary = final_summary, topic = topic, sentiment= sentiment, conclusion = conclusion, summary=summary)

    # else:
    #     return 'File type not allowed'

if __name__ == "__main__":
    app.run(debug=True)
