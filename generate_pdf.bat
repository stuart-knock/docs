REM This file should be used only to generate quickly PDF files while writing them. 
REM For the official release there is a Python script (doc_generator.py) which creates PDF
REM files and place them on the correct folder to be included into distribution.

cls
del *.pdf

rst2pdf -o InstallationManual.pdf InstallationManual.rst --stylesheets=styles/pdf_doc.style
rst2pdf -o UserGuide.pdf UserGuide.rst --stylesheets=styles/pdf_doc.style
rst2pdf -o UserScientificReport.pdf UserScientificReport.rst --stylesheets=styles/pdf_doc.style
rst2pdf -o DeveloperReferenceManual.pdf DeveloperReferenceManual.rst --stylesheets=styles/pdf_doc.style

