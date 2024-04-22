# base image : alpine is used for its small size 
FROM python:alpine

# Set the directory in the container
WORKDIR /app

# Copy the Python script and the text file 
COPY WordFrequencyAnalysis.py .
COPY paragraphs.txt /app/paragraphs.txt

# install nltk

RUN pip install nltk
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

# Run the Python script 
CMD ["python", "WordFrequencyAnalysis.py"]