import sys
from datetime import datetime
from PyPDF2 import PdfReader

path = sys.argv[1]

print('running script...') 
print('input path: ', path)
print('parsing...')
reader = PdfReader(path)
text = ''
for page in reader.pages:
    text += page.extract_text() + '\n'
print('parsed')

print('processing...')
result = text # Add processing logic
print('processed')

print('writing output...')
timestamp = datetime.now().strftime('%d-%m-%y_%H-%M')
inputFileName = path.split('/').pop().split('.')[0]
outputFileName = f'output\\{inputFileName}_{timestamp}.txt'
print('output path: ', outputFileName)
outputFile = open(outputFileName, 'x')
outputFile.write(result)
outputFile.close()
print('output complete')

print('process completet')