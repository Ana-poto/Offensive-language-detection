# [Offensive-language-detection](https://www.aclweb.org/anthology/2020.trac-1.22.pdf)


##  Description
  Offensive Language Detection is a project which aims to label comments in Romanian as neutral, offensive or positive.
An elaborated explanation of the impact that online negative comments can be found in the research paper mentioned in section [Notes](#notes)

## Project File Structure and Elaboration
  The project files hierarchy is divided in multiple folders, each of them representing a step in the development of the project.
  ### Data Collection 
  - the main data source of this project was represented by web scraping news sites comments section and Reddit Roumanian threads comments
  ### Data Prepocessing
  The scraped data had been preprocessed twice :
  -  first : it was clean of any mentions/links/emoji/etc -> the obtained data was used in the annotation step
  -  second : it was divided into tokens and all kind of noise, including stopwords/words from other languages/mentions/links/emoji/etc were removed until a vocabulary was formed
  ### Data Annotation
  This part was realized based on the first preprocessing stage output with the help of the Linguistics University Department.
  The clean comments were annotated with 3 tags, based on their meaning/impact : neutral, offensive or positive.
  ### Data Vectorization
  ### Bayes Classifier
  ### UserInterface integration
## Project Structure
### Project Diagram Overview
![Imaginatorul](https://github.com/Ana-poto/Offensive-language-detection/blob/main/Diagrams/OLDetectionApp.svg)
### Project Diagram Expanded
![Imaginatorul](https://github.com/Ana-poto/Offensive-language-detection/blob/main/Diagrams/OLDetectionAppExp.svg)

## Notes
The project represents an adaptive implementation of one of the classifiers presented in the paper [Offensive Language Detection Explained](https://www.aclweb.org/anthology/2020.trac-1.22.pdf) by Julian Risch, Robin Ruff and Ralf Krestel

