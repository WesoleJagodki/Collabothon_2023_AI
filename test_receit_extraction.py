from processing.ocr import LineExtractor
from processing.openai import ParametersExtractorOpenAI

file = "samples/receit_1.jpg"

line_extractor = LineExtractor()
lines = line_extractor.get_lines(file)

extractor = ParametersExtractorOpenAI()
parameters = extractor.get_parameters(lines)

print("Parameters:")
print(parameters)
