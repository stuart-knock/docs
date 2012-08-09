#!/bin/bash

# This script should be used only to generate PDF documents during development.
# For final distribution, there is a Python script that creates PDFs and  put them
# in the correct place
rst2pdf -o InstallationManual.pdf --stylesheets=./styles/pdf_doc.style InstallationManual.rst
rst2pdf -o UserGuide.pdf --stylesheets=./styles/pdf_doc.style UserGuide.rst
rst2pdf -o DeveloperReferenceManual.pdf --stylesheets=./styles/pdf_doc.style DeveloperReferenceManual.rst
rst2pdf -o UserScientificReport.pdf --stylesheets=./styles/pdf_doc.style UserScientificReport.rst
